import threading

matriz = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

class SomaLinha(threading.Thread):
    def __init__(self, linha):
        threading.Thread.__init__(self)
        self.linha = linha
        
    def run(self):
        soma = sum(self.linha)
        print(f"Soma da linha {matriz.index(self.linha) + 1}: {soma}")
        
threads = []

for linha in matriz:
    thread = SomaLinha(linha)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()