# primera clase

# instalar paquete de datos (requiere internet)
# install.packages('gapminder')
# install.packages('tidyverse')

# cargar paquete de datos
library(gapminder)

# cargar paquete de analisis
library(tidyverse)

# cargar datos
data("gapminder")

# ver encabezado de datos
head(gapminder)

# generando preguntas

# para que años está la información
distinct(gapminder, year)

# para que paises está la información
distinct(gapminder, country)
# mostrar todas las columnas
print(distinct(gapminder, country), n=142)

# como se ve la esperanza de vida por año para Portugal
gapminder %>% 
  filter(country == 'Portugal',
         year == 2007)

# pregunta: esperanza de vida españa 2007

# ahora una grafica
gapminder %>% 
  filter(continent == 'Americas',
         year == 2007) %>% 
  ggplot(aes(x = lifeExp, y = country)) +
  geom_point()

# Pregunta: qué pais tiene MINIMA EDV en 2007 en Europa


# ejercicio como es la esperanza de vida en tu pais
gapminder %>% 
  filter(country == 'Venezuela') %>% 
  ggplot(aes(x = year, y = lifeExp)) +
  geom_point()

