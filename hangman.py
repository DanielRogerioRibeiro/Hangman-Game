#Este é o jogo da Forca
#Neste jogo o objetivo é acertar todas as letras sem ser enforcado

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "mulher".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou  = False
    erros    = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1 
        
        enforcou = erros == 10
        print(letras_acertadas)

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()


#modulo 5 - Palavra secreta e chute sempre em caixa alta