import threading

def contador_crescente():
    for i in range(1, 501):
        print(i)

def contador_decrescente():
    for i in range(500, 0, -1):
        print(i)

t1 = threading.Thread(target=contador_crescente)
t2 = threading.Thread(target=contador_decrescente)

t1.start()
t2.start()

t1.join()
t2.join()


#As funções contador_crescente e contador_decrescente são responsáveis por contar e exibir os números em ordem crescente e decrescente, respectivamente.
#As variáveis t1 e t2 representam as duas threads que serão criadas.
#Os métodos start são responsáveis por iniciar as threads.
#O método join é utilizado para garantir que as threads sejam executadas em paralelo e finalizem antes do término do programa.
#Ao executar esse programa, serão exibidos na tela os números de 1 a 500 em ordem crescente e de 500 a 1 em ordem decrescente, de forma intercalada e simultânea, conforme as threads são executadas em paralelo.
