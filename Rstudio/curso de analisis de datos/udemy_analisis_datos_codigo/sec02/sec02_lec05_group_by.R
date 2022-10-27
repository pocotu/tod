# Curso de manipulación de datos en

# lección - verbo summarise() y group_by() dplyr

# ------------------------------------------------
# Objetivo: agrupar y resumir tablas
# ------------------------------------------------
# En este ejercicio vamos a:
# 1. sumarizar toda una tabla
# 2. agrupar por una variable y sumarizar
# 3. agrupar por varias variable y sumarizar

# cargar paquete de datos
library(gapminder)

# cargar paquete de analisis
library(tidyverse)

# cargar datos
data("gapminder")

# ver encabezado de datos
head(gapminder)

# ------------------------------------------------
# 1. sumarizar toda una tabla
# ------------------------------------------------

# máximo de esperanza de vida


# podemos buscar el pais con filter


# calcular suma total de poblacion e 2007


# otras funciones para usar en summarise
# sum()
# mean()
# median()
# min()
# max()
# n()

# ------------------------------------------------
# 2. agrupar por una variable y sumarizar
# ------------------------------------------------

# EDP por año


# poblacion y conteos por continente para 2007

  
# ------------------------------------------------
# 3. agrupar por varias variable y sumarizar
# ------------------------------------------------

# suma de poblacion por año por continente


# suma de poblacion por continente y por año


# los resultados son los mismo, pero no el orden

# para terminar vamos con un gráfico




