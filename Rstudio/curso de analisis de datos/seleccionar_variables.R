#manipulacion de datos en R
#leccion verbo selec()dplyr

#cargar paquete de datos
library(gapminder)

#cargar paquete de analisis
library(tidyverse)

#cargar datos
data("gapminder")

#ver encabezado de datos
head(gapminder)


####################################
# 1 seleccionar una o mas columnas
####################################

#ver columnas de datos
colnames(gapminder)

#seleccionar varias columnas
#opcion 1
gapminder %>%
  select(country, pop)

#opcion 2
gapminder %>%
  select(c('country', 'pop'))

#utilizar por si las columnas estan en variables
columnas_de_interes <- c('country', 'pop')
gapminder %>%
  select(columnas_de_interes)

# 2 seleccionar rangos y 'eliminar' columnas

#escoger rango de columnas
gapminder %>%
  select(2:4)

gapminder %>%
  select(1:3, 6)

#"eliminar" columnas
gapminder %>%
  select(-continent)

gapminder %>%
  select(-continent, -gdpPercap)

gapminder%>%
  select(-c('continent', 'gdpPercap'))
