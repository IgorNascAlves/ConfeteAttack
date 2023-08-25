# Importe as bibliotecas necessárias
import mouse  # Para controlar o mouse
import sys    # Para obter argumentos da linha de comando
import time   # Para adicionar atrasos (delays) entre ações

# Itera pelo número de vezes especificado na linha de comando
for i in range(int(sys.argv[1])):
    # Arrasta o mouse de uma posição para outra com confete
    mouse.drag(1000, 500, 1200, 700, absolute=True, duration=0.001)
    
    # Move o cursor do mouse para uma posição específica (onde começará a próxima ação)
    mouse.move(1000, 500, absolute=True)
    
    # Adiciona um pequeno atraso entre as ações (10 milissegundos)
    time.sleep(0.01)
