#Este é o jogo da Forca
#Neste jogo o objetivo é acertar todas as letras sem ser enforcado


print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")

palavra_secreta = "mulher"
letras_acertadas = ["_", "_", "_", "_", "_", "_"]

enforcou = False
acertou = False

print(letras_acertadas)

while(not enforcou and not acertou):

    chute = input("Qual letra? ")
    chute = chute.strip()

    index = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index = index + 1

    print("jogando ...")

print("Fim do jogo")

 
