from PIL import Image
import os

def convert_images_to_png_jpeg(input_folder, output_folder):
    # Verifica se a pasta de saída existe, caso contrário, cria-a
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Percorre todos os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        # Verifica se o arquivo é uma imagem WebP
        if filename.endswith('.webp'):
            # Cria o caminho completo para o arquivo de entrada
            input_path = os.path.join(input_folder, filename)

            # Abre a imagem usando a biblioteca Pillow
            image = Image.open(input_path)

            # Define o caminho completo para o arquivo de saída, convertendo a extensão para PNG ou JPEG
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpeg")

            # Converte a imagem para o formato PNG ou JPEG e salva no arquivo de saída
            image.save(output_path, "JPEG")

            # Imprime a conversão concluída
            print(f"Imagem convertida: {output_path}")

            # Fecha a imagem
            image.close()

# Pasta de entrada com as imagens a serem convertidas
input_folder = "./input"

# Pasta de saída para salvar as imagens convertidas
output_folder = "./output"

# Chama a função para converter as imagens
convert_images_to_png_jpeg(input_folder, output_folder)
