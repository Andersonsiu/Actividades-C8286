**PROCESOS DE PLANIFICACIÓN**


**Simulación Básica con FIFO**

Ejecuta una simulación con tres trabajos A, B y C, donde A dura 10 unidades de tiempo, B dura 5 unidades de tiempo y C dura 2 unidades de tiempo, todos llegando al mismo tiempo.

- python3 process-run.py -l 10:100,5:100,2:100 --policy FIFO -c -p

![image.png](https://i.postimg.cc/D0RVdKyJ/image.png)



**Simulación Básica con SJF**

Pregunta: Ejecuta una simulación con tres trabajos A, B y C, donde A dura 10 unidades de tiempo, B dura 5 unidades de tiempo y C dura 2 unidades de tiempo, todos llegando al mismo tiempo.

- python3 process-run.py -l 10:100,5:100,2:100 --policy SJF -c -p

![image.png](https://i.postimg.cc/nhbbXZPN/image.png)


**Simulación Básica con STCF**

Simula un escenario donde A realiza una E/S cada 10 unidades de tiempo y dura 50 unidades de tiempo en total, mientras que B simplemente usa la CPU durante 50 unidades de tiempo.

- python3 process-run.py -l 5:20,50:100 --policy STCF -c -p

![image.png](https://i.postimg.cc/zf8sk75j/image.png)


**Quantum Variado con RR**

Simula un escenario donde A, B y C duran 10 unidades de tiempo cada uno, probando diferentes valores de quantum (1, 2 y 5 unidades de tiempo).

**Comando con quantum de 1,2,5 unidad de tiempo:**
 - python3 process-run.py -l 10:100,10:100,10:100 --policy RR --quantum 1 -c -p
 - python3 process-run.py -l 10:100,10:100,10:100 --policy RR --quantum 2 -c -p
 - python3 process-run.py -l 10:100,10:100,10:100 --policy RR --quantum 5 -c -p


![image.png](https://i.postimg.cc/KYfdpT8y/image.png)


**Simulación con SQMS**

Pregunta: Ejecuta una simulación con cinco trabajos A, B, C, D y E en un sistema con 4 CPUs, utilizando una cola única.

- python3 process-run.py -l 10:100,5:100,7:100,3:100,2:100 --policy SQMS -c -p

![image.png](https://i.postimg.cc/tJZwgmtX/image.png)


**Simulación con MQMS**

Pregunta: Ejecuta una simulación similar a la anterior pero utilizando múltiples colas, una por CPU.

- python3 process-run.py -l 10:100,5:100,7:100,3:100,2:100 --policy MQMS -c -p

