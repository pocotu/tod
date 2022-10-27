# Curso de manipulación de datos en R

# lección - dependencia y correlacion

# ------------------------------------------------
# Objetivo: explorar correlacion entre datos
# ------------------------------------------------
# En este ejercicio vamos a:
# 1. buscar correlaciones en datos
# 2. formas de graficar la matriz de correlacion
# 3. graficar correlacion encontrada

# cargar paquete de datos
library(gapminder)

# cargar paquete de analisis
library(tidyverse)

# cargar datos
data("gapminder")

# ver encabezado de datos
head(gapminder)

# ------------------------------------------------
# 1. buscar correlaciones en datos
# ------------------------------------------------
# mirando todas las graficas de puntos a la vez


# cambiando a escala logaritmica

# ------------------------------------------------
# 2. formas de graficar la matriz de correlacion
# ------------------------------------------------

# graficar la matriz de correlacion
# install.packages('corrplot')
library(corrplot)


# otra forma de estudiar correlacion
# install.packages("PerformanceAnalytics")
library(PerformanceAnalytics)


# ------------------------------------------------
# 3. graficar correlacion encontrada
# ------------------------------------------------
# grafica para gapcor


# viendo tendencia a lo largo de los años

