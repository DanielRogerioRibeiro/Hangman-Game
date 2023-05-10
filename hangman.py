#Este é o jogo da Forca
#Neste jogo o objetivo é acertar todas as letras sem ser enforcado


print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")

palavra_secreta = "mulher".upper()
letras_acertadas = ["_" for letra in palavra_secreta]

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
            if(chute == letra):
                    letras_acertadas[index] = letra
            index += 1
    else:
        erros += 1 
        
    enforcou = erros == 5
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

if(acertou):
    print("Você ganhou!!")
else:
    print("Você perdeu!!")
    
print("Fim do jogo")


