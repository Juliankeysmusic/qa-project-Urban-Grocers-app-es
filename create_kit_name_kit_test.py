import sender_stand_request
import data

# Función para cambiar el valor del parámetro Name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    current_body = data.kit_body.copy()
    # Se cambia el valor del parámetro Name
    current_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor Name requerido
    return current_body
# Función de prueba positiva
def positive_assert(name):
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    user_body = get_kit_body(name)
    current_header = data.header_kit.copy()
    # El resultado de la solicitud para crear un kit se guarda en la variable response
    user_account = sender_stand_request.post_new_user()
    assert user_account.status_code == 201
    current_header["Authorization"] = 'Bearer '+ user_account.json()["authToken"]
    print(current_header)
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    kit_response = sender_stand_request.post_new_kit(current_header,user_body)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    # Comprueba si el nombre se guardo correctamente
    assert kit_response.json()["name"] == name
    # Comprueba si los demas valores existen
    assert kit_response.json()["productsList"] == None
    assert kit_response.json()["id"] != ""
    assert kit_response.json()["productsCount"] == 0


def negative_assert(name):
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    user_body = get_kit_body(name)
    current_header = data.header_kit.copy()
    # El resultado de la solicitud para crear un kit se guarda en la variable response
    user_account = sender_stand_request.post_new_user()
    assert user_account.status_code == 201
    current_header["Authorization"] = 'Bearer '+ user_account.json()["authToken"]
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    kit_response = sender_stand_request.post_new_kit(current_header, user_body)

    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400
    # Comprueba si devuelve el json un codigo de error 400 y que haya un mensaje como lo indica el api
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] != ""

def test_1_one_character():
    positive_assert("a")
def test_2_511_characters():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
def test_3_none_character():
    negative_assert("")
def test_4_512_characters():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
def test_5_special_characters():
    positive_assert('"№%@",')
def test_6_has_spaces():
    positive_assert( " A Aaa ")
def test_7_has_numbers():
    positive_assert("123")
def test_8_no_params():
    kit_body = data.kit_body.copy()
    current_header = data.header_kit.copy()
    # El parámetro "Name" se elimina de la solicitud
    kit_body.pop("name")
    user_account = sender_stand_request.post_new_user()

    assert user_account.status_code == 201
    current_header["Authorization"] = 'Bearer ' + user_account.json()["authToken"]
    kit_response = sender_stand_request.post_new_kit(current_header, kit_body)
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400
    # Comprueba si devuelve el json un codigo de error 400 y que haya el mensaje correspondiente como lo indica el api
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


def test_9_none_character():
    # El cuerpo actualizado de la solicitud se guarda en la variable user_body
    kit_body = get_kit_body(123)
    current_header = data.header_kit.copy()
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    user_account = sender_stand_request.post_new_user()
    # se creo exitosamente el usuario
    assert user_account.status_code == 201
    # pasamos el numero de autorizacion como parametro del encabezado
    current_header["Authorization"] = 'Bearer ' + user_account.json()["authToken"]
    # enviamos una solicitud post con el header y body solicitados en la prueba
    kit_response = sender_stand_request.post_new_kit(current_header, kit_body)
    # Comprueba si el código de estado es 400
    assert kit_response.status_code == 400
    # Comprueba si devuelve el json un codigo de error 400 y que haya el mensaje correspondiente como lo indica el api
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"
