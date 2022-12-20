# Este código muestra la salida de un programa que se ejecuta desde la línea 
# de comandos y que proporciona una interfaz de usuario para interactuar con 
# un chatbot utilizando OpenAI's ChatGPT. La interfaz de usuario se inicia 
# mostrando un mensaje de bienvenida y una lista de comandos disponibles.
# 
# Los comandos disponibles son:
# 
# !help: muestra un mensaje de ayuda con una lista de todos los comandos 
# disponibles.
# !reset: olvida la conversación actual y comienza una nueva.
# !refresh: actualiza la sesión de autenticación del chatbot.
# !rollback: retrocede la conversación un mensaje.
# !config: muestra la configuración actual del chatbot.
# !exit: sale del programa.
# Para enviar un mensaje al chatbot, el usuario debe escribir el mensaje y 
# presionar Enter dos veces. El chatbot responderá con un mensaje generado por 
# el modelo ChatGPT de OpenAI.

```
 $ python3 -m revChatGPT --debug

        ChatGPT - A command-line interface to OpenAI's ChatGPT (https://chat.openai.com/chat)
        Repo: github.com/acheong08/ChatGPT
        Run with --debug to enable debugging
        
Type '!help' to show commands
Press enter twice to submit your question.

Logging in...

You:
!help


                !help - Show this message
                !reset - Forget the current conversation
                !refresh - Refresh the session authentication
                !rollback - Rollback the conversation by 1 message
                !config - Show the current configuration
                !exit - Exit the program
```