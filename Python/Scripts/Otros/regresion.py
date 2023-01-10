import numpy as np

# Supongamos que tenemos un conjunto de datos con tres variables independientes y una variable dependiente
# llamadas x1, x2, x3 y y, respectivamente.
x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([2, 3, 4, 5, 6])
x3 = np.array([3, 4, 5, 6, 7])
y = np.array([1, 3, 5, 7, 9])

# Ahora, vamos a añadir una columna de unos a nuestros datos de entrada para tener un término independiente
# en nuestro modelo de regresión.
X = np.column_stack((np.ones(len(x1)), x1, x2, x3))

# A continuación, podemos usar la función `lstsq` de numpy para ajustar nuestro modelo de regresión.
beta, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)

# Los coeficientes del modelo se almacenan en el vector beta
print(beta)

# Si queremos hacer predicciones con el modelo, podemos usar el siguiente código:
x_test = np.array([[1, 6, 7, 8]]) # Añade una columna de unos
y_pred = np.dot(x_test, beta) # Multiplica x_test por beta
print(y_pred)
