### calcular determinante de una matriz 3x3 

#funcion_determinante <- function(matriz){
#    det <- 0
#    det <- det + (matriz[1,1] * matriz[2,2] * matriz[3,3])
#    det <- det + (matriz[1,2] * matriz[2,3] * matriz[3,1])
#    det <- det + (matriz[1,3] * matriz[2,1] * matriz[3,2])
#    det <- det - (matriz[1,3] * matriz[2,2] * matriz[3,1])
#    det <- det - (matriz[1,2] * matriz[2,1] * matriz[3,3])
#    det <- det - (matriz[1,1] * matriz[2,3] * matriz[3,2])
#    return(det)
#}

#det <- funcion_determinante(matriz)

v=c(1, 2, 3, 4, 5, 6, 7, 8, 9)

determinate <- function(matriz){
    for (i in 1:3){
        for (j in 1:3){
            if (i == j){
                det <- det + (matriz[i,j] * matriz[i+1,j+1] * matriz[i+2,j+2])
                det <- det + (matriz[i,j+1] * matriz[i+1,j+2] * matriz[i+2,j])
                det <- det + (matriz[i,j+2] * matriz[i+1,j] * matriz[i+2,j+1])
                det <- det - (matriz[i,j+2] * matriz[i+1,j+1] * matriz[i+2,j])
                det <- det - (matriz[i,j+1] * matriz[i+1,j] * matriz[i+2,j+2])
                det <- det - (matriz[i,j] * matriz[i+1,j+2] * matriz[i+2,j+1])
            }
        }
    }
}

# llamar a la funcion determinante
det <- determinate(matriz)