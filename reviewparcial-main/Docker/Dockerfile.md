Componentes básicos de un Dockerfile

- FROM: Establece la imagen base para las instrucciones siguientes.
- Por ejemplo, FROM ubuntu:20.04 comienza la construcción utilizando la imagen base de Ubuntu 20.04.
  
- RUN: Ejecuta comandos en una nueva capa encima de la imagen actual y la usa para la siguiente
instrucción en el Dockerfile. Por ejemplo, RUN apt-get update && apt-get install -y git.

- CMD: Proporciona comandos por defecto para la ejecución de un contenedor. Solo puede existir
un CMD; si se especifican varios, solo el último surtirá efecto.

- EXPOSE: Indica los puertos en los que un contenedor escuchará conexiones. Por ejemplo,
EXPOSE 80 sugiere que el contenedor estará escuchando en el puerto 80.

- ENV: Establece variables de entorno dentro del contenedor. Por ejemplo, ENV LANG C.UTF-8.
  
- COPY y ADD: Copian archivos y directorios desde el sistema de archivos local al contenedor.
  
- ENTRYPOINT: Permite configurar un contenedor que se ejecutará como un ejecutable.
  
**-CREA EL DOCKERFILE, ASÍ:**

FROM ubuntu:20.04

RUN apt-get update && \ 

apt-get install -y python

COPY hola.py . 

ENTRYPOINT ["python", "hola.py"]


**- Construyendo la imagen**

Ahora, podemos construir la imagen exactamente de la misma manera que lo hicimos antes, de la siguiente manera: 

- $ docker build -t hola-python .

**- Ejecutando la aplicación Ejecutamos la aplicación ejecutando el contenedor, así:** 

- $ docker run hola-python

**- Este comando inició el contenedor de Ubuntu pero no le adjuntó la consola. Podemos ver que se está ejecutando usando el siguiente comando:** 

- $ docker ps

**- Este comando imprime todos los contenedores que se encuentran en estado de ejecución. ¿Qué pasa con nuestros contenedores viejos, ya salidos? Podemos encontrarlos imprimiendo todos los contenedores, así:**

- $ docker ps -a 

**- Por ejemplo, podemos dejar de ejecutar el contenedor de Ubuntu, como se muestra aquí:** 

- $docker stop 13181f811922 

**- Necesitamos iniciar el contenedor, especificando la asignación de puertos con el indicador p (--publish), de la siguiente manera: - p, --publish**
**- Entonces, primero detengamos el contenedor en ejecución y comencemos uno nuevo, así:**

- $ docker stop 9b92be34d101
- $ docker run -d -p 8080:8080 tomcat

**Usar en otra consola el comando "docker exec -it <container_id> curl http://localhost:5000"**

Esto debe permitir probar la conectividad dentro del contenedor sin problemas.
