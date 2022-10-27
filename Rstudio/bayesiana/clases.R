x = NULL
x[1]=rnorm(1,mean=0,sd=1)
for (i in 2:2000) x[i]=0.3*x[(i-1)]+rnorm(1,0.1)

#Grafica de cadena
plot(ts(x),col="red", xlab="Iteraciones o estados", ylab="Valor del estado", main="Cadena de Markov")

#Forma empirica de verificar la convergencia
#1 promedio Ergodico
mergod=cumsum(x)/(1:length(x))
plot(1:2000,mergod,col="red",cex=0.7,type="l",ylab="Promedio de la cadena", xlab="t", main="Media ergodica")

#2 no correlacion serial
acf(x,main="Funcion de autocorrelacion", xlab="Periodos (LAG)", ylab="Grado de asociacion (ACF")

#Histograma de los datos simulados
hist(x,breaks=50, prob=T)
grid=seq(-8,8,0.01)
var.x=1/(1-0.3^2)
lines(grid,dnorm(grid,0,sqrt(var.x)),col="hotpink",lwd=3)