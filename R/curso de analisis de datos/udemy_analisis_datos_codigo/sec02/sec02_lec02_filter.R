# Curso de manipulación de datos en R

# lección - verbo filter() dplyr

# ------------------------------------------------
# Objetivo: filtrar observaciones
# ------------------------------------------------
# En este ejercicio vamos a:
# 1. filtrar por una condicion
# 2. filtrar por varias condiciones
# 3. otras condiciones logicas |, &, - (negar)

# cargar paquete de datos
library(gapminder)

# cargar paquete de analisis
library(tidyverse)

# cargar datos
data("gapminder")

# ver encabezado de datos
head(gapminder)

# ------------------------------------------------
# 1. filtrar por un valor
# ------------------------------------------------
# ver columnas de datos
colnames(gapminder)

# filtrar un pais (caracter)


# filtrar por edad exactamente 40 (numérica)


# filtrar por edad mayor a 40 (peor no igual)


# otras posibilidades
  # >= mayor o igual
  # >  mayor pero no igual
  # <= menor o igual
  # <  menor pero no igual
  # != distinto

# ------------------------------------------------
# 2. filtrar por más de un valor
# ------------------------------------------------

# filtrar dos (o mas) paises


# filtrar por rango de edades


# combinando filtros caracter y numérico



# ------------------------------------------------
# 3. filtrar con operadores lógicos
# ------------------------------------------------

# operadores lógicos
  # ! representa la negación
  # & representa la "y", AND en inglés
  # | representa la "o", OR en inglés

# combinando condiciones con & (y, AND)


# combinando condiciones con | (o, OR)


# combinando condiciones con ! o negacion


