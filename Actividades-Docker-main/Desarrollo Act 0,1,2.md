# Desarrollo Actividad 0!

`$ docker container run rancher/cowsay Hello`

![image.png](https://i.postimg.cc/Twj3dzkG/image.png)


**Probando minikube y kubectl**

![image.png](https://i.postimg.cc/QxJYQ0zt/image.png)

![image.png](https://i.postimg.cc/yd60zyPf/image.png)

![image.png](https://i.postimg.cc/yx43vqdS/image.png)

## Preguntas

1.  Un contenedor es como una caja de herramientas portátil que contiene todo lo que una aplicación necesita para funcionar, permitiéndole trabajar de la misma manera, sin importar dónde se lleve.
    
2.  Los contenedores cambian el juego al proporcionar portabilidad, eficiencia en el uso de recursos, aislamiento y rapidez de despliegue.
    
3.  La afirmación de que "si un contenedor funciona en un lugar, funciona en cualquier lugar" se basa en la consistencia de ejecución y en la independencia de la infraestructura que proporcionan los contenedores.
    
4.  Falso. Los contenedores Docker son útiles tanto para aplicaciones heredadas como nuevas, ya que facilitan la gestión de dependencias y mejoran la portabilidad y la consistencia.
    
5.  Un administrador de paquetes es crucial para instalar y gestionar software de manera eficiente y para mantener la consistencia entre diferentes entornos de desarrollo y producción.
    
6.  Sí, Docker Desktop permite desarrollar y ejecutar contenedores de Linux en diferentes sistemas operativos, incluyendo Windows y Mac.
    
7.  Buenas habilidades de programación son esenciales para automatizar y gestionar contenedores y servicios, para la resolución de problemas y la personalización de entornos.
    
8.  Docker está certificado para ejecutarse en Ubuntu, CentOS, RHEL y SLES.
    
9.  Minikube se utiliza para pruebas, desarrollo y aprendizaje de Kubernetes en un entorno local simulando un clúster de Kubernetes.


## DESARROLLO ACTIVIDAD 2!

**Aplicaciones docker**

![image.png](https://i.postimg.cc/P5p43HfS/image.png)

![image.png](https://i.postimg.cc/Hxpbg1HD/image.png)

**CREACION IMAGENES DOCKER**

![image.png](https://i.postimg.cc/8PJGHFv9/image.png)

![image.png](https://i.postimg.cc/7PpHjMqw/image.png)

![image.png](https://i.postimg.cc/FKb69Sdf/image.png)


## EJERCICIO

Parte 1: Exploración y Ejecución Loca

![image.png](https://i.postimg.cc/jSxG1LnR/image.png)

Parte 2: Introducción a Docker

`FROM ubuntu:20.04 
RUN apt-get update &&  
\apt-get install  
-y python COPY hola.py 
.ENTRYPOINT ["python", "hola.py"]´`


Parte 3:  Construcción de la Imagen Docker:

![image.png](https://i.postimg.cc/c1mR1H5K/image.png)

![image.png](https://i.postimg.cc/pTnjtf18/image.png)


Parte  4: Manipulación de la  red Docker

![image.png](https://i.postimg.cc/3RcdWdzh/image.png)

![image.png](https://i.postimg.cc/g0KM9PQ8/image.png)

![image.png](https://i.postimg.cc/j239prWZ/image.png)

[![image.png](https://i.postimg.cc/Dw1hX84h/image.png)

![image.png](https://i.postimg.cc/x8NhV4KQ/image.png)

## Ejercicios1. 

 **Ejecute CouchDB como contenedor Docker y publique su puerto de la siguiente manera: Puede usar el comando de búsqueda de Docker para encontrar la imagen de CouchDB.**

![image.png](https://i.postimg.cc/HWtBVHkN/image.png)


![image.png](https://i.postimg.cc/6pV3NH0C/image.png)

![image.png](https://i.postimg.cc/Vs3nfVjh/image.png)

![image.png](https://i.postimg.cc/nc4jHcVs/image.png)

**Cree una imagen de Docker con un  servicio REST, respondiendo Hola Mundo alocalhost:8080/hello. Utilice cualquier lenguaje y frameworks que prefiera.**

![image.png](https://i.postimg.cc/mrwyhybH/image.png)
![image.png](https://i.postimg.cc/Bn5xwBPV/image.png)


**ALPINE**

![image.png](https://i.postimg.cc/020YVCwH/image.png)

![image.png](https://i.postimg.cc/Gtc2tvmH/image.png)

![image.png](https://i.postimg.cc/MG2zX1sq/image.png)

**Cree un Dockerfile que utilice varios pasos para crear una imagen de una aplicación de algoritmos (el que desees de tamaño mínimo), escrita en C, Go, Java, C++.**

![image.png](https://i.postimg.cc/26y9DK46/image.png)

**NUEVO DOCKERFILE**

![image.png](https://i.postimg.cc/yNm3N1yp/image.png)

![image.png](https://i.postimg.cc/xTXkzyPz/image.png)

![image.png](https://i.postimg.cc/XJyjvQWj/image.png)

![image.png](https://i.postimg.cc/jd3F8KN1/image.png)

![image.png](https://i.postimg.cc/FzWDngfS/image.png)

