import os
import requests
import hashlib
import time
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

# Configurações
API_KEY = os.getenv("GOOGLE_API_KEY")
CSE_ID = os.getenv("GOOGLE_CSE_ID")
QUERY = "tomatoes red -tomatillo"
SAVE_DIR = "red_tomatoes_images"
NUM_IMAGES = 100
MAX_RETRIES = 3
DELAY_BETWEEN_PAGES = 2

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Referer": "https://www.google.com/",
}

def download_images():
    os.makedirs(SAVE_DIR, exist_ok=True)
    downloaded = 0
    start_index = 1
    hashes = set()

    while downloaded < NUM_IMAGES:
        try:
            url = f"https://customsearch.googleapis.com/customsearch/v1?q={QUERY}&key={API_KEY}&cx={CSE_ID}&searchType=image&start={start_index}"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            results = response.json().get("items", [])
            
            if not results:
                print("Não há mais resultados disponíveis.")
                break

            for item in results:
                if downloaded >= NUM_IMAGES:
                    break

                image_url = item.get("link")
                if not image_url:
                    continue

                for attempt in range(MAX_RETRIES):
                    try:
                        response_img = requests.get(image_url, headers=headers, timeout=15)
                        response_img.raise_for_status()
                        
                        # Verificação do tipo de conteúdo
                        content_type = response_img.headers.get('Content-Type', '')
                        if 'image' not in content_type:
                            print(f"URL não é imagem: {content_type}")
                            continue
                            
                        image_data = response_img.content
                        image_hash = hashlib.md5(image_data).hexdigest()
                        
                        if image_hash in hashes:
                            continue
                            
                        # Verificação da imagem
                        img = Image.open(BytesIO(image_data))
                        img.verify()
                        img = Image.open(BytesIO(image_data))  # Reabrir após verificação
                        
                        # Salvar imagem
                        file_path = os.path.join(SAVE_DIR, f"tomato_{downloaded+1}.jpg")
                        img.save(file_path)
                        
                        hashes.add(image_hash)
                        downloaded += 1
                        print(f"Imagem {downloaded} salva: {file_path}")
                        break
                        
                    except Exception as e:
                        print(f"Erro (tentativa {attempt+1}): {str(e)}")
                        time.sleep(1)
                        continue

            start_index += 10
            time.sleep(DELAY_BETWEEN_PAGES)

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                print("Limite de cota atingido ou acesso bloqueado")
                break
            raise

if __name__ == "__main__":
    download_images()
    print("Processo concluído!")