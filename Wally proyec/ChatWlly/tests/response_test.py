# Este código crea una instancia de una clase llamada Chatbot y luego llama a un método de esa clase llamado get_chat_response para obtener una respuesta del chatbot a un mensaje de entrada dado. El mensaje de entrada en este caso es "Hello".
# 
# El Chatbot se inicializa con un diccionario de configuración que incluye un correo electrónico y una contraseña. Estos se usan para autenticar la conexión del Chatbot a un servicio de chatbot.
# 
# El método refresh_session se llama antes de llamar a get_chat_response y se utiliza para actualizar la sesión del Chatbot con el servicio de chatbot.
# 
# El método get_chat_response toma un mensaje de entrada y devuelve un diccionario que incluye un campo "message" con la respuesta del chatbot al mensaje de entrada. Si el mensaje de respuesta es None, se imprime un mensaje de error y la función test_response devuelve False. De lo contrario, se imprime la respuesta del chatbot y la función test_response devuelve True.

from os import environ

from revChatGPT.revChatGPT import Chatbot

import base64

EMAIL = environ["OPENAI_EMAIL"]
PASSWORD = base64.b64decode(environ["OPENAI_PASSWORD"]).decode("utf-8")

config = {
    "email": EMAIL,
    "password": PASSWORD, }


def test_response():
    try:
        bot = Chatbot(config=config, debug=True)

        bot.refresh_session()

        response = bot.get_chat_response("Hello")

        if response['message'] is None:
            print("Error: response['message'] is None")
            assert False
        else:
            print(f"response['message']: {response['message']}")

        print("Success!")
    except Exception as exc:
        print(f"Error: {exc}")
        assert False
    assert True
