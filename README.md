# Aplicación con información de ciudades

### Se trata de una aplicación sencilla que demuestra cómo, mediante la utilización del framework Django, es posible crear un sitio web con algunas funcionalidades.

--------
--------

1. Descripción del trabajo:

* Creación del entorno virtual `python3 -m venv venv-Django_bas`
* Activación del entorno `source venv-Django_bas/bin/activate`
* Instalación de la librería Django `pip install django`
* Instalación de la librería Pillow (para las imágenes) `python -m pip install Pillow`
* Creación del proyecto `django-admin startproject ale_travel .`
* Se generan archivos de importancia:
  * 'manage.py' es como un CLI interno para nuestro proyecto y se lo llama al correr el runserver
  * 'asgi.py’ y ‘wsgi.py’ para montar el servidor (crear la aplicación, definir el puerto, etc)
  * 'urls.py' donde se agregan los path a los que acceder en la aplicacione, ya viene con ‘admin/’ y su ruta
  * 'settings.py’ archivo de configuracion con algunas constantes (BASE_DIR, SECRET_KEY, DEBUG, ALLOWED_HOSTS, etc)
* A partir de aquí se comienza a crear código para dar forma al proyecto
* Una vez creada la estructura, también se puede hacer uso del Panel de Administración de Django:
  
  * Panel de ingreso con validación de credenciales:

    ![Captura de pantalla 2023-06-22 a las 10 18 05](https://github.com/alebusquet/Django-Cities_of_the_World/assets/110254796/9deb885f-4109-44bf-ad86-d86a2f2c0e68)

  * Posibilidad de trabajar con los usuarios o con las aplicaciones de nuestro proyecto:

    ![Captura de pantalla 2023-06-22 a las 10 22 42](https://github.com/alebusquet/Django-Cities_of_the_World/assets/110254796/3ad1ccc1-0e34-4169-82d2-5bd2485ac24d)

  * Opciones para definir o modificar perfiles de usuarios:

    ![Captura de pantalla 2023-06-22 a las 10 23 58](https://github.com/alebusquet/Django-Cities_of_the_World/assets/110254796/5a9e5c70-16a0-40eb-b896-e16b1d033675)

  * Se va generando la estructura de las aplicaciones:

    ![Captura de pantalla 2023-06-22 a las 10 24 56](https://github.com/alebusquet/Django-Cities_of_the_World/assets/110254796/d25081f4-407c-4a54-871f-8a5a84913243)

  * Y el contenido de sus componentes:

    ![Captura de pantalla 2023-06-22 a las 10 26 55](https://github.com/alebusquet/Django-Cities_of_the_World/assets/110254796/53b05d61-042b-4fbb-9a1d-fc1f569f137c)









2. Cómo implementarlo:



3. Imágenes de la aplicación:



#### Es todo. Muchas gracias!


-------

### Autor:

--> Alejandro Busquet

* Linkedin: [Acá](https://www.linkedin.com/in/alejandro-busquet/ "Acá")

* Mail: <a href="mailto:algabu00@gmail.com" target="_blank">algabu00@gmail.com</a>
