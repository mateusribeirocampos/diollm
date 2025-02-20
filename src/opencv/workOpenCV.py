import cv2  # Importa a biblioteca OpenCV para manipulação de imagens
from matplotlib import pyplot as plt  # Importa a biblioteca Matplotlib para plotagem de gráficos
import numpy as np  # Importa a biblioteca NumPy para manipulação de arrays

import requests  # Importa a biblioteca Requests para fazer requisições HTTP
url = 'https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg'  # URL da imagem
r = requests.get(url, allow_redirects=True)  # Faz uma requisição GET para baixar a imagem
with open('lena.jpg', 'wb') as f:  # Abre um arquivo para salvar a imagem
    f.write(r.content)  # Escreve o conteúdo da imagem no arquivo

img = cv2.imread('lena.jpg')  # Lê a imagem usando OpenCV
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converte a imagem para escala de cinza
img = cv2.GaussianBlur(gray, (5, 5), 0)  # Aplica um filtro Gaussiano para suavizar a imagem

sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # Aplica o filtro Sobel no eixo X
sobely = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)  # Aplica o filtro Sobel no eixo Y
sobelxy = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)  # Aplica o filtro Sobel nos eixos X e Y

plt.figure(figsize=(18, 19))  # Cria uma figura com tamanho especificado

plt.subplot(221)  # Adiciona um subplot na posição 2x2, 1
plt.imshow(img, cmap='gray')  # Exibe a imagem original em escala de cinza
plt.title('Original')  # Define o título do subplot
plt.axis('off')  # Remove os eixos

plt.subplot(222)  # Adiciona um subplot na posição 2x2, 2
plt.imshow(sobelxy, cmap='gray')  # Exibe a imagem com os filtros Sobel X e Y combinados
plt.title('Sobel X Y')  # Define o título do subplot
plt.axis('off')  # Remove os eixos

plt.subplot(223)  # Adiciona um subplot na posição 2x2, 3
plt.imshow(sobelx, cmap='gray')  # Exibe a imagem com o filtro Sobel X
plt.title('Sobel X')  # Define o título do subplot
plt.axis('off')  # Remove os eixos

plt.subplot(224)  # Adiciona um subplot na posição 2x2, 4
plt.imshow(sobely, cmap='gray')  # Exibe a imagem com o filtro Sobel Y
plt.title('Sobel Y')  # Define o título do subplot
plt.axis('off')  # Remove os eixos

plt.show()  # Exibe a figura com todos os subplots