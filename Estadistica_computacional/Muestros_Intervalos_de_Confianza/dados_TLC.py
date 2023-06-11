import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Configuración de estilo de Seaborn
sns.set(style='darkgrid')

# Lanzamiento de dados
num_dados = 3  # Número de dados a lanzar en cada experimento
num_lanzamientos = 1000  # Número de experimentos a realizar

# Realizar los lanzamientos de los dados
dados_lanzados = np.random.randint(1, 7, size=(num_lanzamientos, num_dados))
suma_resultados = np.sum(dados_lanzados, axis=1)  # Suma de los resultados de los dados en cada experimento

# Calcular la media de las sumas
medias = np.mean(suma_resultados)

# Calcular la desviación estándar de las sumas
desviacion_estandar = np.std(suma_resultados)

# Crear un histograma de las sumas
sns.histplot(data=suma_resultados, kde=True, color='skyblue', bins=range(num_dados, 7*num_dados+2))

# Agregar líneas verticales para mostrar la media y el intervalo de confianza
plt.axvline(x=medias, color='red', linestyle='--', label='Media')
plt.axvline(x=medias + desviacion_estandar, color='green', linestyle='--', label='Media + Desviación Estándar')
plt.axvline(x=medias - desviacion_estandar, color='green', linestyle='--', label='Media - Desviación Estándar')

# Configuración de la leyenda y etiquetas del gráfico
plt.legend()
plt.xlabel('Suma de los resultados')
plt.ylabel('Frecuencia')
plt.title('Distribución de la suma de los resultados de lanzamientos de dados')

# Guardar el gráfico como imagen
plt.savefig('distribucion_dados.png')

# Mostrar el gráfico
plt.show()

