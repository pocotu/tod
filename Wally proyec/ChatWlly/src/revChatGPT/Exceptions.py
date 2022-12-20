# Estas clases parecen ser excepciones personalizadas para manejar errores específicos en una aplicación de chat utilizando GPT (Generative Pre-trained Transformer, un modelo de lenguaje utilizado en procesamiento del lenguaje natural).
# 
# La clase base ChatGPTException es una clase de excepción personalizada que toma un mensaje como argumento y lo almacena en una propiedad message. También proporciona un método __str__ para devolver el mensaje de la excepción como una cadena de caracteres cuando se imprima o se muestre de otra manera.
# 
# Las clases AuthError, ExpiredAccessToken, InvalidAccessToken, y InvalidCredentials son subclases de AuthError que se utilizan para manejar errores de autenticación específicos. AuthError es a su vez una subclase de ChatGPTException.
# 
# Las clases APIError y NetworkError son subclases de ChatGPTException que se utilizan para manejar errores de la API y errores de red, respectivamente. HTTPError es una subclase de NetworkError que se utiliza para manejar errores HTTP específicos. HTTPStatusError es una subclase de HTTPError que agrega una propiedad status_code para almacenar el código de estado HTTP.

class ChatGPTException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class AuthError(ChatGPTException):
    pass


class ExpiredAccessToken(AuthError):
    pass


class InvalidAccessToken(AuthError):
    pass


class InvalidCredentials(AuthError):
    pass


class APIError(ChatGPTException):
    pass


class NetworkError(ChatGPTException):
    pass


class HTTPError(NetworkError):
    pass


class HTTPStatusError(HTTPError):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code
