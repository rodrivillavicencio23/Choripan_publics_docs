import matplotlib.pyplot as plt # también un alias ampliamente usado
import pandas as pd
datos_peliculas = {
    'Título': ['Frozen', 'Toy Story', 'The Lion King', 'Moana', 'Coco'],
    'Año': [2013, 1995, 1994, 2016, 2017],
    'Género': ['Animación', 'Animación', 'Animación', 'Animación', 'Animación'],
    'Duración': [102, 81, 88, 107, 105],
    'Calificación': [7.4, 8.3, 8.5, 7.6, 8.4]
}

df_peliculas = pd.DataFrame(datos_peliculas)


plt.figure(figsize=(10,5))
plt.bar(df_peliculas['Título'], df_peliculas['Calificación'], color='skyblue')
plt.title('Calificaciones de Películas de Disney')
plt.xlabel('Películas')
plt.ylabel('Calificación IMDb')
plt.show()