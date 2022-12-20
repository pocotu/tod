# Este código es la documentación del módulo revChatGPT, que es parte de la biblioteca ChatGPT. La documentación proporciona 
# información detallada sobre las clases, métodos y funciones disponibles en el módulo revChatGPT y cómo utilizarlos.
# 
# El módulo revChatGPT proporciona una clase principal llamada Chatbot, que permite interactuar con un chatbot utilizando OpenAI's 
# ChatGPT. La clase Chatbot tiene una serie de métodos disponibles para enviar mensajes al chatbot y obtener respuestas, reiniciar 
# la conversación, retroceder la conversación, actualizar la sesión de autenticación del chatbot y obtener la configuración actual 
# del chatbot.
# 
# El módulo también proporciona una clase secundaria llamada AsyncChatbot, que es una versión asincrónica de la clase Chatbot. La 
# clase AsyncChatbot tiene la mayoría de los mismos métodos que la clase Chatbot, pero son implementados de manera asincrónica y 
# utilizan el módulo "aiohttp" para realizar solicitudes de red de manera asincrónica.
# 
# La documentación también incluye información sobre una clase de utilidad llamada CaptchaSolver, que se utiliza para resolver 
# captcha utilizados por el chatbot de OpenAI. La clase CaptchaSolver tiene un único método estático llamado solve_captcha, que toma 
# una cadena SVG raw como entrada y devuelve la solución del captcha como una cadena.
# 
# La documentación también incluye información sobre las excepciones que pueden ser lanzadas por el módulo revChatGPT y cómo 
# manejarlas.

<a id="revChatGPT"></a>

# revChatGPT

<a id="revChatGPT.Exceptions"></a>

# revChatGPT.Exceptions

<a id="revChatGPT.__main__"></a>

# revChatGPT.\_\_main\_\_

<a id="revChatGPT.__main__.CaptchaSolver"></a>

## CaptchaSolver Objects

```python
class CaptchaSolver()
```

Captcha solver

<a id="revChatGPT.__main__.CaptchaSolver.solve_captcha"></a>

#### solve\_captcha

```python
@staticmethod
def solve_captcha(raw_svg)
```

Solves the captcha

**Arguments**:

- `raw_svg` (`:obj:`str``): The raw SVG

**Returns**:

`:obj:`str``: The solution

<a id="revChatGPT.revChatGPT"></a>

# revChatGPT.revChatGPT

<a id="revChatGPT.revChatGPT.generate_uuid"></a>

#### generate\_uuid

```python
def generate_uuid() -> str
```

Generate a UUID for the session -- Internal use only

**Returns**:

`:obj:`str``: a random UUID

<a id="revChatGPT.revChatGPT.AsyncChatbot"></a>

## AsyncChatbot Objects

```python
class AsyncChatbot()
```

Initialize the AsyncChatbot.

See wiki for the configuration json:
https://github.com/acheong08/ChatGPT/wiki/Setup

**Arguments**:

- `config` (`:obj:`json``): The configuration json
- `conversation_id` (`:obj:`str`, optional`): The conversation ID
- `parent_id` (`:obj:`str`, optional`): The parent ID
- `debug` (`:obj:`bool`, optional`): Whether to enable debug mode
- `refresh` (`:obj:`bool`, optional`): Whether to refresh the session
- `request_timeout` (`:obj:`int`, optional`): The network request timeout seconds
- `base_url` (`:obj:`str`, optional`): The base url to chat.openai.com backend server,
useful when set up a reverse proxy to avoid network issue.

**Returns**:

`:obj:`Chatbot``: The Chatbot object

<a id="revChatGPT.revChatGPT.AsyncChatbot.reset_chat"></a>

#### reset\_chat

```python
def reset_chat() -> None
```

Reset the conversation ID and parent ID.

**Returns**:

None

<a id="revChatGPT.revChatGPT.AsyncChatbot.get_chat_response"></a>

#### get\_chat\_response

```python
async def get_chat_response(prompt: str,
                            output="text",
                            conversation_id=None,
                            parent_id=None) -> dict or None
```

Get the chat response.

**Arguments**:

- `prompt` (`:obj:`str``): The message sent to the chatbot
- `output` (`:obj:`str`, optional`): The output type `text` or `stream`

**Returns**:

`:obj:`dict` or :obj:`None``: The chat response `{"message": "Returned messages", "conversation_id": "conversation ID", "parent_id": "parent ID"}` or None

<a id="revChatGPT.revChatGPT.AsyncChatbot.rollback_conversation"></a>

#### rollback\_conversation

```python
def rollback_conversation() -> None
```

Rollback the conversation.

**Returns**:

None

<a id="revChatGPT.revChatGPT.AsyncChatbot.refresh_session"></a>

#### refresh\_session

```python
def refresh_session() -> None
```

Refresh the session.

**Returns**:

None

<a id="revChatGPT.revChatGPT.AsyncChatbot.login"></a>

#### login

```python
def login(email: str, password: str) -> None
```

Log in to OpenAI.

**Arguments**:

- `email` (`:obj:`str``): The email
- `password` (`:obj:`str``): The password

**Returns**:

None

<a id="revChatGPT.revChatGPT.Chatbot"></a>

## Chatbot Objects

```python
class Chatbot(AsyncChatbot)
```

Initialize the AsyncChatbot.

See wiki for the configuration json:
https://github.com/acheong08/ChatGPT/wiki/Setup

**Arguments**:

- `config` (`:obj:`json``): The configuration json
- `conversation_id` (`:obj:`str`, optional`): The conversation ID
- `parent_id` (`:obj:`str`, optional`): The parent ID
- `debug` (`:obj:`bool`, optional`): Whether to enable debug mode
- `refresh` (`:obj:`bool`, optional`): Whether to refresh the session
- `request_timeout` (`:obj:`int`, optional`): The network request timeout seconds
- `base_url` (`:obj:`str`, optional`): The base url to chat.openai.com backend server,
useful when set up a reverse proxy to avoid network issue.

**Returns**:

`:obj:`Chatbot``: The Chatbot object

<a id="revChatGPT.revChatGPT.Chatbot.get_chat_response"></a>

#### get\_chat\_response

```python
def get_chat_response(prompt: str,
                      output="text",
                      conversation_id=None,
                      parent_id=None) -> dict or None
```

Get the chat response.

**Arguments**:

- `prompt` (`:obj:`str``): The message sent to the chatbot
- `output` (`:obj:`str`, optional`): The output type `text` or `stream`

**Returns**:

`:obj:`dict` or :obj:`None``: The chat response `{"message": "Returned messages", "conversation_id": "conversation ID", "parent_id": "parent ID"}` or None

