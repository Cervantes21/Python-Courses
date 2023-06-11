import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generar datos de ejemplo
np.random.seed(0)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100)

# Crear un DataFrame con los datos
data = pd.DataFrame({'X': x, 'Y': y})

# Crear un gráfico de dispersión con línea de regresión
sns.lmplot(x='X', y='Y', data=data)

# Guardar la imagen en un archivo
plt.savefig('regresion_lineal.png')

# Mostrar el gráfico
plt.show()

