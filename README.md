# Proyecto Urban Grocers 
# Al crear los archivos se debe tener en cuenta organizar las urls y endpoints en el archivo configuracion.py
# Las solicitudes POST se realizar en el sender_stand_request.py 
# los datos genericos se crean en data.gy para poder generar copias despues y poder ejecutar los casos de prueba correctamente
# en el archivo create kit_name_kit_test.py se crean las funciones possitive y negative assert, y una que modifica el json del kit_body
# para poder ejectuar las distintas pruebas, tambien se guarda el authToken en el header como valor de la clave authorization
# se escriben las respecivas pruebas usando la funcion correspondiente (si es negativa o positiva)
# al final 5 tests pasaron las pruebas y otros 4 permitian crear los kits asi no fueran validos, y el test 8 dio un error 500 no 400
