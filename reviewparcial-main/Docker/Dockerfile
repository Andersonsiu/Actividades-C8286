FROM ubuntu:20.04

# Evitar que se soliciten entradas de usuario durante la instalación de paquetes
ARG DEBIAN_FRONTEND=noninteractive

# Actualizar los paquetes e instalar Python 3 y pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Establecer el directorio de trabajo en el contenedor
WORKDIR /ejemplo-codigo

# Copiar los scripts del cliente, servidor y el script de inicio al contenedor
COPY cliente.py servidor.py start.sh /ejemplo-codigo/

# Dar permisos de ejecución al script start.sh
RUN chmod +x start.sh

# Ejecutar start.sh al iniciar el contenedor
CMD ["./start.sh"]

