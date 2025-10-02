import os
import pyautogui as auto 

# PEGA O CAMINHO QUE O PYTHON ESTÁ EXECUTANDO O PROGRAMA.
CAMINHO_PASTA = os.getcwd()
print("Caminho da pasta:",CAMINHO_PASTA)


CAMINHO_PASTA_IMAGENS = os.path.join(CAMINHO_PASTA,".\\Automacao\\img")
print("Caminho da pasta imagens:",CAMINHO_PASTA_IMAGENS)


lista_fotos = os.listdir(CAMINHO_PASTA_IMAGENS)
print("Conteúdos da lista de fotos:",lista_fotos)
caminho_dino = os.path.join (CAMINHO_PASTA,".\\Automacao\\dino.png")

while True:
    for foto in lista_fotos:
        caminho_da_foto = os.path.join(CAMINHO_PASTA_IMAGENS,foto)
      
        #verificar se a imagem esta na tela
        try:
            posicao_cacto = auto.locateOnScreen(caminho_da_foto, confidence= 0.7 ) 
            posicao_dino = auto.locateOnScreen (caminho_dino, confidence= 0.6 )
        except:
            posicao_cacto = None
            posicao_dino = None

        else:
            print ("posicao do cacto:" , posicao_cacto.left)
            if posicao_cacto.left <= 850:
                auto.press ("space")
                auto.keyDown ("space")
