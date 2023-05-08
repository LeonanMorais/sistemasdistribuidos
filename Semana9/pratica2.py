import threading

vetor = [i for i in range(1, 1001)]
escalar = 2

class Multiplica(threading.Thread):
    def __init__(self, inicio, fim):
        threading.Thread.__init__(self)
        self.inicio = inicio
        self.fim = fim
        
    def run(self):
        for i in range(self.inicio, self.fim):
            vetor[i] *= escalar
        
threads = []

for i in range(0, 1000, 100):
    thread = Multiplica(i, i+100)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    
print(vetor)