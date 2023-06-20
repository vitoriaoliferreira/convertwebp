from PIL import Image
import os

def convert_images_to_webp(input_folder, output_folder):
    # Verifica se a pasta de saída existe, caso contrário, cria-a
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Percorre todos os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        # Verifica se o arquivo é uma imagem
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # Cria o caminho completo para o arquivo de entrada
            input_path = os.path.join(input_folder, filename)

            # Abre a imagem usando a biblioteca Pillow
            image = Image.open(input_path)

            
  # Redimensiona a imagem para a largura e altura especificadas pelo usuário
            image = image.resize((width, height))


            # Define a qualidade da compactação da imagem (0 é o valor mínimo e 100 é o máximo)
            quality = 50

            # Define o caminho completo para o arquivo de saída
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".webp")

            # Converte a imagem para o formato WebP e salva no arquivo de saída
            image.save(output_path, "webp", quality=quality)

            # Imprime a conversão concluída
            print(f"Imagem convertida: {output_path}")

            # Fecha a imagem
            image.close()

# Pasta de entrada com as imagens a serem convertidas
input_folder = "./input"

# Pasta de saída para salvar as imagens convertidas
output_folder = "./output"

# Solicita ao usuário a largura desejada para a imagem
width = int(input("Informe a largura desejada para a imagem: "))

# Solicita ao usuário a altura desejada para a imagem
height = int(input("Informe a altura desejada para a imagem: "))

# Chama a função para converter as imagens
convert_images_to_webp(input_folder, output_folder)
