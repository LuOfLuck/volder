# Volder Online

Volder Online es un sitio web desarrollado para unificar las tareas escolares de manera dinamica, sin la necesidad de requerir aplicaciones externas, modalando el sistema escolar en jerarquiaz


![foto-perfil-2](https://user-images.githubusercontent.com/77320589/116850027-438b2980-abc6-11eb-850a-bce413902d08.jpg)

### **_¿porqué creamos Volder_** 
Durante la pandemia nos dimos cuenta que la forma en que corria la informacion dentro de una escuela, era muy lenta, mala, conflictiva y nadie estaba haciendo nada de
manera directa para resolver el problema


### **_¿Como lo hicimos?_**
Decidimos imitar el modelo de una escuela secundaria dividiendo a los usuarios en una jerarquía especifica. Estas son:
- Estudiante
- Profesor
- Preceptor
- Secretario


Para evitar que alguien ajeno a la escuela tenga acceso, evitamos el uso de un formulario de registro publico, dando lugar a un formulario de registro manual basado en jerarquías.
![diagrama-de-fludo-de-datos-registro](https://user-images.githubusercontent.com/77320589/116844074-5b5bb100-abb8-11eb-9382-475d1692d017.png)
De esta manera dividimos el trabajo de agregar a todos entre secretarias y preceptor, asegurando que todos los miembros de la escuela estén dentro de Volder.

Una vez hecho esto, se pueden utilizar las verdades funciones de Volder. Como la clásica enviar y recibir trabajos principalmente entre profesor y estudiante. 
![dfd-trabajos](https://user-images.githubusercontent.com/77320589/116849633-7d0f6500-abc5-11eb-93b4-cb9d6a363227.png)
Nota: 
Para mas información de todas las funciones de Volder (desarrolladas hasta el momento) puede visitar [volder explicacion](http://luofluck.epizy.com/volder-explicacion/)

### **_¿Que tiene de especial Volder ante cualquier software similar?_**
Volder fue pensado exclusivamente para las escuelas segundarias. Así que ataca los problemas de maneras directas, no pretende quedarse en un simple ClassRoom que solo se utiliza para enviar y recibir trabajos sino que también la escuela tenga control de manera autónoma y directa de todo lo que pasa en la plataforma, creando un sistema para poder cumplir con cada necesidad que se requiera.

### **_¿Como es la comunicación_**
- De uno a uno mandando mensajes directos
- De uno a mucho creando publicaciones 

# **_Parte técnica_**

### **_Frontend:_**

- **HTML:** Como lenguaje de  *HyperText* para dar la estructura a todo el sitio
- **CSS:** Para dar estilo y una buena vista al usuario
- **JavaScript:** A fin de utilizarlo para hacer *AJAX* y animaciones
- **Bootstrap:** responsable de la mayoria del responsive 

### **_Backend:_**
- **Python:** Lenguaje de programación realizado para las consultar y la lógica de la pagina con el Framework *Django*
- **Django:** como Framework de backend

> Las tecnologías fueron elegidas debido a que queríamos crear un software escalable y mantenible a largo plazo. Al tomar la decisión de que seria un sitio web se eligió HTML, CSS y JS de manera intuitiva pero Django fue elegido debido a su forma de dividirse en aplicaciones y su fácil uso de manejo de datos
### **_Desarrolladores_**
- [Alvarado Matias](https://github.com/m-alvarado) - Frontend developer
- [Guerrero Lucas](https://github.com/LuOfLuck/) - FullStack Developer

### **Requerimientos e instalacion_**
>Nota: al descargar el repositorio entre y borre los pycache

- Python 3.8
``` cmd
pip install Django==2.2.3
pip install Pillow
python manage.py makemigrations
python manage.py migrate
python runserver
```

### **_Modelos entidad relacion_**
![8  base de datos (volder)](https://user-images.githubusercontent.com/77320589/119431946-da409700-bce9-11eb-9fd2-e5c1f8fa0e30.jpg)
> click a la imagen para ver en maxima calidad

##### Algunas aclaraciones
- Se utilizo una tabla *noticia* independiente para los 3 roles superiores ya que cada una de estas tienen cualidades y alcanze de manera diferente, y a largo plazo se
van a agregar muchas cosas que sera mas sencillo y eficaz tener 3 tablas diferente
- Cada tabla de rol tiene un nombre, apellido, dni de manera repetitiva por una mala toma de desiciones, ya se esta trabajando para arreglar eso.
- La tabla *proyecto* es para crear trabajos grupales aunque este no esta en funcionamiento debido a que esta en desarrollo


[Imágenes/documentos/modelos del desarrollo](https://drive.google.com/drive/folders/1ZFJ_6E2z0HjK1FPmN_XBpFfXelqbUTtl?usp=sharing)

