#EJER 1
#THREADING ID 

import threading
import time
import random

def thread_function(thread_id):
  print(f'Hilo {thread_id} iniciado')
  sleep_time = random.randint(1, 5)
  time.sleep(sleep_time)
  print(f'Hilo {thread_id} a finalizado de {sleep_time} segundos')

threads = []

for i in range(5):
  thread= threading.Thread(target=thread_function, args=(i,))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()

print(f'Todos los hilos se han ejecutado')
