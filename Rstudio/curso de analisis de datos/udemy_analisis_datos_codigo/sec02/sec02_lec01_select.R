# Curso de manipulación de datos en R

# lección - verbo select() dplyr

# ------------------------------------------------
# Objetivo: seleccionar datos
# ------------------------------------------------
# En este ejercicio vamos a:
# 1. seleccionar una o más columnas
# 2. seleccionar rangos y "eliminar" columnas
# 3. starts_with(), ends_with(), contains()

# cargar paquete de datos
library(gapminder)

# cargar paquete de analisis
library(tidyverse)

# cargar datos
data("gapminder")

# ver encabezado de datos
head(gapminder)

# ------------------------------------------------
# 1. seleccionar una o más columnas
# ------------------------------------------------

# ver columnas de datos




# seleccionar varias columnas
# opcion 1


# opcion 2


# utilidad por si las columnas están en variables


# ------------------------------------------------
# 2. seleccionar rangos y "eliminar" columnas
# ------------------------------------------------

# escoger rango de columnas


# "eliminar" columnas


# ------------------------------------------------
# 3. starts_with(), ends_with(), contains()
# ------------------------------------------------
gapminder %>% 
  select(starts_with('c'))

# ejemplo con iris dataset
data_iris <- iris

# starts_with()


# ends_with()


# contains()

