import face_recognition as fr
import os

def reconhece_face(url_photo):
    foto = fr.load_image_file(url_photo)
    rostos = fr.face_encodings(foto)

    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    drigo = reconhece_face("./img/rodrigo/drigo2.jpg")
    if(drigo[0]):
        rostos_conhecidos.append(drigo[1][0])
        nomes_dos_rostos.append("Rodrigo")

    # romulo1 = reconhece_face("./img/romulo1.jpg")
    # if(romulo1[0]):
    #     rostos_conhecidos.append(romulo1[1][0])
    #     nomes_dos_rostos.append("Romulo")
    
    return rostos_conhecidos, nomes_dos_rostos

def get_list_faces(list_src, nome_pessoa):
    rostos_conhecidos = []
    nomes_dos_rostos = []
    for src in list_src:
        face = reconhece_face(src)
        if(face[0]):
            rostos_conhecidos.append(face[1][0])
            nomes_dos_rostos.append(nome_pessoa)
    
    return rostos_conhecidos, nomes_dos_rostos

def load_data_faces():
    lista_conhecidos = []
    nomes_dos_rostos = []
    nomes_das_pastas = nome_das_pastas()

    for nome in nomes_das_pastas:
        lista_fotos = get_list_faces(listar_imagens_em_pasta('./img/' + nome), nome)
        rostos_conhecidos, nomes_rostos_individuais = lista_fotos
        lista_conhecidos += rostos_conhecidos
        nomes_dos_rostos += nomes_rostos_individuais

    return lista_conhecidos, nomes_dos_rostos


def listar_imagens_em_pasta(caminho_da_pasta):
    # Lista para armazenar os nomes dos arquivos de imagem
    imagens = []

    # Verifica se o caminho é válido
    if os.path.exists(caminho_da_pasta) and os.path.isdir(caminho_da_pasta):
        # Percorre todos os arquivos na pasta
        for nome_arquivo in os.listdir(caminho_da_pasta):
            # Verifica se o arquivo tem uma extensão de imagem comum (você pode personalizar isso)
            if nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Adiciona o caminho completo do arquivo à lista de imagens
                caminho_completo = os.path.join(caminho_da_pasta, nome_arquivo)
                imagens.append(caminho_completo)

    return imagens

def nome_das_pastas():
    return [nome for nome in os.listdir('./img/') if os.path.isdir(os.path.join('./img/', nome))]

# Exemplo de uso:
# pasta_rodrigo = './img/rodrigo'
# pasta_daniel = './img/daniel'
# lista_fotos_rodrigo = listar_imagens_em_pasta(pasta_rodrigo)
# lista_fotos_daniel = listar_imagens_em_pasta(pasta_daniel)
