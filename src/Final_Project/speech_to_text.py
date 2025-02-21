import pyaudio
import speech_recognition as sr
import webbrowser
import wikipedia
from datetime import datetime
from speech_utils import text_to_speech

def speech_to_text():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Diga algo...")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
    except sr.WaitTimeoutError:
        print("Nenhuma fala detectada. Tentando novamente...")
        audio = None

    try:
        text = recognizer.recognize_google(audio, language='pt-BR')
        return text.lower()
    except sr.UnknownValueError:
        print("Não consegui entender o áudio.")
        return None
    except sr.RequestError:
        print("Erro na requisição ao serviço de reconhecimento de fala.")
        return None

def executar_comando(comando):
    if 'wikipédia' in comando or 'pesquisar wikipédia' in comando:
        palavras = comando.split()
        try:
            index = palavras.index('wikipédia')
            termo = " ".join(palavras[index+1:])
            if termo:
                wikipedia.set_lang("pt")
                resumo = wikipedia.summary(termo, sentences=2)
                print(resumo)
                text_to_speech(resumo)
            else:
                print("Termo não encontrado.")
                text_to_speech("Por favor, diga o que deseja pesquisar na Wikipédia.")
        except ValueError:
            print("Erro ao processar o comando.")
            text_to_speech("Não consegui entender o que pesquisar na Wikipédia.")
    
    elif 'abrir o youtube' in comando:
        webbrowser.open("https://www.youtube.com")
        text_to_speech("Abrindo o YouTube.") 
    
    elif 'localizar farmácia' in comando:
        text_to_speech("Desculpe, esta funcionalidade requer configuração da API do Google Maps.")
    
    elif 'horas' in comando:
        hora = datetime.now().strftime("%H:%M")
        text_to_speech(f"Agora são {hora}.")
    
    elif 'parar' in comando:
        text_to_speech("Encerrando assistente.")
        exit()

    else:
        text_to_speech("Comando não reconhecido.")

# Loop principal
while True:
    comando = speech_to_text()
    if comando:
        print(f"Comando reconhecido: {comando}")
        text_to_speech(f"Você disse: {comando}") 
        executar_comando(comando)
    else:
        text_to_speech("Não entendi, pode repetir?")