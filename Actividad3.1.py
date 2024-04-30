import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventastotalessinnulos.csv",index_col = 0)

# Eliminar la columna "indice_tiempo"
df.drop(columns=["indice_tiempo"], inplace=True)

# Eliminar las columnas sin valores
columns_to_drop = ["almacen", "panaderia", "lacteos", "carnes", "verduleria_fruteria",
                   "alimentos_preparados_rotiseria", "articulos_limpieza_perfumeria",
                   "indumentaria_calzado_textiles_hogar", "electronicos_articulos_hogar", "otros"]
df.drop(columns=columns_to_drop, inplace=True)

# Ahora df contiene los datos limpios

# Visualización de outliers mediante un gráfico de caja
plt.figure(figsize=(10, 6))
df.boxplot(column=["ventas_precios_corrientes", "ventas_precios_constantes", "ventas_totales_canal_venta"])
plt.title("Gráfico de caja para identificar outliers")
plt.ylabel("Valores")
plt.show()

# Eliminación de outliers utilizando Desviación Estándar
threshold = 2  # Puedes ajustar este valor según tus necesidades

# Columna 1: ventas_precios_corrientes
mean1 = df["ventas_precios_corrientes"].mean()
std1 = df["ventas_precios_corrientes"].std()
df_cleaned1 = df[(df["ventas_precios_corrientes"] > mean1 - threshold * std1) & (df["ventas_precios_corrientes"] < mean1 + threshold * std1)]

# Columna 2: ventas_precios_constantes
mean2 = df["ventas_precios_constantes"].mean()
std2 = df["ventas_precios_constantes"].std()
df_cleaned2 = df[(df["ventas_precios_constantes"] > mean2 - threshold * std2) & (df["ventas_precios_constantes"] < mean2 + threshold * std2)]

# Columna 3: ventas_totales_canal_venta
mean3 = df["ventas_totales_canal_venta"].mean()
std3 = df["ventas_totales_canal_venta"].std()
df_cleaned3 = df[(df["ventas_totales_canal_venta"] > mean3 - threshold * std3) & (df["ventas_totales_canal_venta"] < mean3 + threshold * std3)]


# Ahora df_cleaned1, df_cleaned2 y df_cleaned3 contienen los datos sin outliers en las columnas específicas

# Reemplaza 'df_cleaned1', 'df_cleaned2' y 'df_cleaned3' con los DataFrames que contienen los datos limpios para cada columna
df_cleaned1.to_csv("ventas_precios_corrientes_cleaned.csv")
df_cleaned2.to_csv("ventas_precios_constantes_cleaned.csv")
df_cleaned3.to_csv("ventas_totales_canal_venta_cleaned.csv")
