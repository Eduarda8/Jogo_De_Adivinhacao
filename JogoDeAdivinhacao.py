#JOGO DE ADIVINHAÇÃO :

#Um jogador deverar escolher ente o numero 1 até 100 e o outro devera tentar adivinhar.
#Se o palpite for mais alto exiba uma mensagem que o numero sorteado é menor.
#Se o palpite for muito baixo exiba uma mensagem sujerindo deverá ser maior.
#Um jogador só terá 3 chamces de acertar o numero e o Jogo deverá ser finalizado quando o jogador informar sair.

import random
resp = "Yes"
x = 0
jogo = []
while x < 100:
    jogo.append(x)
    x+=1
while resp == "Yes" :
    num = random.choice(jogo)
    A = int(input("Digite um número:"))
    aux = 1
    while A!= num and aux < 3 :
        if A > num:
            dif = A - num
            if dif <= 2 :
                print("O número chegou quase perto")
            else:
                print("Tente um número menor")
        if A < num :
            dif = num - A
            if dif <= 2 :
                print("O número chegou quase perto")
            else:
                print("Tente um número maior")
        if A == num :
            print("Muito bem, você acertou !!")
        aux+=1
        A = int(input("Digite um número :"))
    if A!= num :
        print("Fim de Jogo, o número era:", num)
    if A == num :
        print("Muito bem, você acertou !!")
    print("Vai continuar jogando ?")
    resp = str(input())
print("fim de jogo")
