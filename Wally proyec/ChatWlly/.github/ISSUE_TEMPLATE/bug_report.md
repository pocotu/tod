# Eso es un plantilla de informe de errores que se puede utilizar para informar de un problema o fallo en un software. El informe 
# incluye una serie de secciones que proporcionan información detallada sobre el problema, lo que facilita la identificación y 
# solución del problema.
# 
# La sección "Describe the bug" proporciona una descripción clara y concisa del problema o fallo que se está experimentando. La
# sección "To Reproduce" proporciona los pasos para reproducir el problema, lo que puede ser útil para comprender mejor el problema 
# y cómo se produce. La sección "Expected behavior" proporciona una descripción clara y concisa del comportamiento que se esperaba y 
# que no se ha producido. La sección "Output" proporciona instrucciones para ejecutar el software con opciones de depuración que 
# pueden ser útiles para identificar el problema.
# 
# La sección "Environment" proporciona información sobre el sistema operativo y la versión de Python que se está utilizando, así 
# como la versión del software en el que se ha detectado el problema. Esta información es importante para poder comprender el 
# contexto en el que se ha producido el problema y puede ser útil para solucionarlo.
# 
# La sección "Additional context" proporciona cualquier otra información relevante sobre el problema que pueda ser útil para 
# comprenderlo y solucionarlo.

---
name: Bug report
about: Create a report to help us improve
title: "[BUG]"
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Output**
In the correct directory, run `python3 -m revChatGPT --debug`

**Environment (please complete the following information):**

Please update your packages before reporting! `pip3 install --upgrade OpenAIAuth revChatGPT`
 - OS: [e.g. Linux, MacOS, Windows]
 - Python version: `python -V`
 - ChatGPT Version: `pip3 show revChatGPT`
 - OpenAI Version: `pip3 show OpenAIAuth`

**Additional context**
Add any other context about the problem here.
