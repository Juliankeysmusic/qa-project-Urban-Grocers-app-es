# Proyecto Urban Grocers Julian Jimenez Sprint 7 Grupo 26 (Introduccion a automatización de pruebas)
# Descripcion del proyecto:
# Este proyecto tiene como finalidad testear el nombre del proceso de creacion de kits mediante solicitudes POST siguiendo el protocolo HTTP.
# El proyecto ya tiene unos casos de prueba escritos por otro QA Engineer, el propósito es automatizar las 9 pruebas escritas mediante programacion en Python.
# Instalacion de librerias:
# Requerimos de las librerias requests y pytest para poder desarrollar correctamente nuestro proyecto.
# Para instalar la libreria requests, buscamos en IDE Pycharm, la opción Python Packages localizado en la esquina inferior izquierda, luego en la barra de busqueda
# buscamos requests e instalamos la versión mas reciente.
# Para instalar la libreria pytest, buscamos en IDE Pycharm, la opción Python Packages localizado en la esquina inferior izquierda, luego en la barra de busqueda
# buscamos pytest e instalamos la versión mas reciente.
# Organizacion del proyecto y observaciones:
# Al crear los archivos se debe tener en cuenta organizar las urls y endpoints en el archivo configuracion.py
# Las solicitudes POST se realizar en el sender_stand_request.py 
# los datos genericos se crean en data.gy para poder generar copias despues y poder ejecutar los casos de prueba correctamente
# en el archivo create kit_name_kit_test.py se crean las funciones possitive y negative assert, y una que modifica el json del kit_body
# para poder ejecutar las distintas pruebas, tambien se guarda el authToken en el header como valor de la clave authorization
# se escriben las respecivas pruebas usando la funcion correspondiente (si es negativa o positiva)
# al final 5 tests pasaron las pruebas y otros 4 permitian crear los kits asi no fueran validos, y el test 8 dio un error 500 no 400.
# Ejecucion de las pruebas mediante la herramienta pytest:
# Se abre la ventana terminal en el IDE PyCharm, haciendo click en la esquina inferior izquierda, en el icono de una ventana con un signo mayor y una barra al piso
# Luego aparece la direccion donde esta guardado el proyecto, se procede a ejecutar el comando pytest seguido del nombre del archivo del proyecto
# Es importante que el nombre del archivo de los pruebas contenga la palabra test en el. En el caso de este proyecto el archivo se llama create_kit_name_kit_test.py
# por lo que se escribe en el shell: pytest create_kit_name_kit_test.py y se ejecutaran todas las funciones que tengas test dentro de su nombre.

