# Desarrollo Evaluacion 0!


`pwd`: Imprime el directorio de trabajo actual. Te dice en qué carpeta estás en ese momento.
`ls`: Lista los archivos y directorios en el directorio actual.
`cd`: Cambia el directorio actual al que se especifica como argumento.
`cd /usr/bin`: Este es el comando para "change directory" (cambiar directorio).

![image.png](https://i.postimg.cc/nh04jDCj/image.png)


`cd ..`: Este es el comando para salir del directoria de donde te encuentras.

![image.png](https://i.postimg.cc/mggPz6xR/image.png)


`mv filename1 filename2`: Renombra `filename1` a `filename2` o lo mueve a la ubicación `filename2`.
    
`cp file1 file2`: Copia `file1` a `file2`.
    
`cp file1 ..` o `cp file1 directory`: Copia `file1` al directorio superior o a `directory`.


![image.png](https://i.postimg.cc/Kzzf05gy/image.png)
![image.png](https://i.postimg.cc/xjkDCvp7/image.png)
![image.png](https://i.postimg.cc/MTNLRL3L/image.png)


 `rm file...`: Elimina el archivo o archivos especificados. Los puntos suspensivos indican que hay más en el nombre del archivo o hay varios archivos, pero no están completamente mostrados en la imagen.
    
`rm -r directory`: Elimina el directorio llamado `directory` y todo su contenido de forma recursiva.
    
`mkdir directory...`: Crea un nuevo directorio con el nombre `directory`. 

![image.png](https://i.postimg.cc/ZqVt9VSk/image.png)


`type type`: Indica que `type` es un comando integrado en el shell.
    
`type ls`: Informa que `ls` es un alias para `ls --color=auto`, que lista los archivos en color.
    
`type cp`: Muestra que `cp` es un comando externo y se encuentra en `/usr/bin/cp`.
    
`which ls`: Da la ubicación del comando `ls`, `/usr/bin/ls`, que es la versión del comando que se ejecutaría en el sistema.

![image.png](https://i.postimg.cc/3JBPftkk/image.png)


El comando `cd` cambia el directorio activo en la terminal. `-L` sigue enlaces simbólicos, y `-P` evita seguirlos, accediendo al directorio real. Sin argumentos, `cd` lleva al directorio `HOME`. `CDPATH` puede definir directorios de búsqueda adicionales para el comando.

![image.png](https://i.postimg.cc/0yS72B7Q/image.png)


El comando `mkdir` se utiliza para crear directorios. Las opciones incluyen `-m` o `--mode` para definir permisos, `-p` o `--parents` para crear directorios padre si no existen, `-v` o `--verbose` para mostrar un mensaje por cada directorio creado, y `-Z` para configurar el contexto de seguridad cuando se usa SELinux.

![image.png](https://i.postimg.cc/zGpHBYVq/image.png)

 
El comando `ls -l | less` en la terminal lista los archivos y directorios en el formato largo, incluyendo permisos, número de enlaces, propietario, grupo, tamaño, fecha de última modificación y nombre. El resultado se canaliza (`|`) a `less`, lo que permite navegar por la lista de manera paginada si es muy larga. En la imagen, el proceso está detenido, posiblemente porque el usuario ha ingresado a `less` y puede moverse arriba o abajo por la lista.

![image.png](https://i.postimg.cc/TP8FpFSH/image.png)


1.  `echo *`: Imprime todos los archivos y directorios en el directorio actual.
    
2.  `echo D*`: Muestra todos los archivos y directorios que comienzan con "D".
    
3.  `echo [[:upper:]]*`: Muestra todos los archivos y directorios que comienzan con una letra mayúscula.
    
4.  `echo /usr/*share`: Expande la ruta para mostrar directorios que terminan en "share" bajo "/usr/".
    
5.  `echo ~`: Muestra el directorio home del usuario actual.
    
6.  `echo ~foo`: Intenta expandir la ruta del home de un usuario llamado 'foo', pero parece que no existe, por lo que devuelve "~foo".
    
7.  `echo $((2 + 2))`: Realiza una operación aritmética y muestra el resultado "4".
    
8.  `echo $((5/2))`: Muestra el resultado de la división entera de 5 entre 2, que es "2".
    
9.  `echo Number_{1..5}`: Utiliza brace expansion para generar una secuencia de "Number_1" a "Number_5".
    
10.  `echo $USER`: Muestra el nombre del usuario actual.
    
11.  `echo $(ls)`: Ejecuta el comando `ls` y muestra su salida (nombres de archivos y directorios).
    
12.  `ls -l $(which cp)`: Muestra información detallada del archivo ejecutable `cp`.
    
13.  `echo this is a test`: Imprime la cadena de texto "this is a test".

![image.png](https://i.postimg.cc/K8hDLbGL/image.png)



`echo -e "Inserting several blank lines\n\n\n"`: Utiliza el comando `echo` con la opción `-e` para interpretar las secuencias de escape, e imprime el texto seguido de tres nuevas líneas, lo que resulta en tres líneas en blanco tras el texto.
`ls -l /bin/bash`: Muestra los detalles del archivo ejecutable para el shell bash, incluyendo permisos, número de enlaces, propietario, grupo, tamaño, y fecha de la última modificación.

![image.png](https://i.postimg.cc/Tw263B5v/image.png)


El comando `su` se ha utilizado para cambiar al usuario root, lo que requiere ingresar la contraseña de root. Después de obtener acceso como root, el comando `exit` se usa para salir de la sesión del usuario root y volver al usuario original.

![image.png](https://i.postimg.cc/8c5fMy3q/image.png)


El comando `chmod 600 some_file` cambia los permisos del archivo llamado `some_file` para que solo el propietario tenga permiso de lectura y escritura. Nadie más puede leer, escribir o ejecutar ese archivo. El comando `xload` lanza una aplicación gráfica que muestra la carga del sistema en tiempo real.

![image.png](https://i.postimg.cc/Sx0jxNS0/image.png)


El comando `xload &` ejecuta la aplicación `xload` en segundo plano, lo que permite seguir utilizando la terminal mientras `xload` sigue ejecutándose. El signo `&` al final del comando es el que permite esta funcionalidad. El número `[2] 11465` indica que `xload` es el segundo trabajo en segundo plano y muestra su ID de proceso (PID), que es 11465.

![image.png](https://i.postimg.cc/W3Qtq2GJ/image.png)


El comando `jobs` muestra los trabajos en segundo plano y detenidos: `ls --color=auto -l | less` está detenido y `xload` ha terminado. `ps` lista los procesos actuales: `bash` es la shell, `less` está detenido y `ps` muestra su propia ejecución.

![image.png](https://i.postimg.cc/cHY0jf3r/image.png)


El usuario ejecutó `ps x | grep bad_program` para buscar procesos que coincidan con "bad_program". `grep` filtra y muestra las líneas que coinciden. Luego, con `kill -SIGTERM 11517`, envía la señal SIGTERM al proceso con PID 11517, solicitando su terminación de forma segura.

![image.png](https://i.postimg.cc/fTQvSdf5/image.png)
