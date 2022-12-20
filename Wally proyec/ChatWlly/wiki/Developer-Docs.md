# Este código muestra un ejemplo de cómo utilizar la clase Chatbot del módulo revChatGPT para interactuar con un chatbot utilizando 
# OpenAI's ChatGPT.
# 
# Para utilizar la clase Chatbot, primero se importa desde el módulo revChatGPT. Luego, se crea una instancia de Chatbot 
# proporcionando un diccionario de configuración, que puede estar vacío pero debe incluirse en la llamada al constructor de la clase.
# 
# Una vez que se ha creado una instancia de Chatbot, se puede llamar al método get_chat_response para obtener una respuesta del 
# chatbot a un mensaje de entrada dado. El mensaje de entrada se proporciona como un argumento "prompt" y el método 
# get_chat_response devuelve la respuesta del chatbot como una cadena de texto. Si se proporciona el argumento opcional "output" con 
# el valor "stream", get_chat_response devolverá un generador asincrónico en lugar de una cadena de texto.
# 
# El código proporciona un enlace a un archivo en el repositorio de ChatGPT que muestra un ejemplo de cómo utilizar la clase Chatbot 
# en un programa.

# TODO

```py
from revChatGPT.revChatGPT import Chatbot

# Do some config
...


chatbot = Chatbot({
   # This could be blank but the dict should be here
})

chatbot.get_chat_response(prompt, output="text") #output=stream uses async generator
```

Example: https://github.com/acheong08/ChatGPT/blob/main/src/revChatGPT/__main__.py