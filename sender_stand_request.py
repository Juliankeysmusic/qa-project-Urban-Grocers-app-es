import configuration
import requests
import data

def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=data.user_body,  # inserta el cuerpo de solicitud
                         headers=data.header_user)  # inserta los encabezados
def post_new_kit(current_header, body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         headers = current_header)
