# Este código es una guía de configuración para el módulo revChatGPT, que es parte de la biblioteca ChatGPT. La guía describe cómo 
# instalar y configurar el módulo revChatGPT para interactuar con un chatbot utilizando OpenAI's ChatGPT.
# 
# Para instalar el módulo revChatGPT, se debe ejecutar el comando pip3 install --upgrade revChatGPT. Además, se deben instalar las 
# dependencias del módulo ejecutando el comando python3 -m playwright install después de instalar el módulo.
# 
# Para utilizar el módulo revChatGPT en entornos de escritorio, se debe iniciar sesión en OpenAI a través de una ventana del 
# navegador y esperar a que la ventana se cierre automáticamente.
# 
# Para utilizar el módulo revChatGPT en servidores, se debe proporcionar un token de sesión en el archivo de configuración. El token 
# de sesión se puede obtener manualmente a través del navegador o utilizando Xvfb para emular un entorno de escritorio.
# 
# La guía también proporciona un ejemplo de archivo de configuración con opciones adicionales para configurar un proxy y un idioma 
# de aceptación.

# Setup
`pip3 install --upgrade revChatGPT`

## Dependencies
Run `python3 -m playwright install` after installing `revChatGPT`

## Desktop environments:
A Chrome/Chromium/Firefox window will show up.
1. Wait for the Cloudflare checks to pass
2. Log into OpenAI via the open browser (Google/Email-Password/Etc)
3. It should automatically redirect you to `https://chat.openai.com/chat` after logging in. If it doesn't, go to this link manually after logging in.
4. The window should close automatically
5. You are good to go

## Servers:
You must define the session token in the config:

You can find the session token manually from your browser:
1. Go to `https://chat.openai.com/api/auth/session`
2. Press `F12` to open console
3. Go to `Application` > `Cookies`
4. Copy the session token value in `__Secure-next-auth.session-token`
5. Paste it into `config.json` in the current working directory
```json
{"session_token":"<YOUR_TOKEN>"}
```

You can use `Xvfb` to emulate a desktop environment. It should automatically get the `cf_clearance` given no captcha.

Search it up if you don't know. Ask ChatGPT.


# Config options
```json
{
  "session_token": "<token>",
  "proxy":"<proxy>",
  "accept_language": "en-US,en"
}
```