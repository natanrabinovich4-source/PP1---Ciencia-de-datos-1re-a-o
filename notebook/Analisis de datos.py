# Inicio del proceso ETL - Exploracion de la data; 
# antes de empezar a trabajar con el proyecto en sí, necesito conocer con que valores estoy trabajando
# para ello primero voy a hacer una lectura de los datos

# llamo al modulo de Pandas
import pandas as pd

# Cargar el dataset original

df = pd.read_csv("eph_tecnologia_microdatos.csv")

# Mostrar dimensiones -  solo para saber cuantas filas y columnas tiene el dataset.
print("\nDIMENSIONES DEL DATASET:")
print(df.shape)


# Ver las primeras filas - para saber con que tipos de
#  datos me voy a encontrar, solo llame a 3 filas para ver la estructura
print("PRIMERAS FILAS:")
print(df.head(3))


# Mostrar información de las columnas - me muestra la cantidad 
# de dato que tengo por columnas
print("\nINFORMACIÓN DEL DATASET:")
df.info()

# Cuento cuantos valores nulos (NaN) existen en cada columna
print("\nVALORES NULOS:")
print(df.isnull().sum())

# Mostrar valores posibles de las variables categóricas
print("\nVALORES DE REGION:")
print(df["REGION"].value_counts().sort_index())

print("\nVALORES DE NIVEL EDUCATIVO:")
print(df["NIVEL_ED"].value_counts().sort_index())

print("\nVALORES DE TENENCIA DE COMPUTADORA:")
print(df["IV12_3"].value_counts(dropna=False).sort_index())

print("\nVALORES DE INTERNET:")
print(df["II7"].value_counts(dropna=False).sort_index())

# Con estos comandos ya puedo conocer como esta compuesto el dataset.
# Se encontraron 142 celdas con valores nulos y, ademas, existen respuestas
# codificadas con 9 que significan "Sin respuesta".
# Estos codigos tambien deben tratarse como datos faltantes


# Limpieza de datos


import numpy as np

# Crear una copia para conservar el dataset original
df_clean = df.copy()

# Reemplazar codigos "Sin respuesta" (9) por valores nulos
df_clean["NIVEL_ED"] = df_clean["NIVEL_ED"].replace(9, np.nan)
df_clean["IV12_3"] = df_clean["IV12_3"].replace(9, np.nan)
df_clean["II7"] = df_clean["II7"].replace(9, np.nan)

# Visualizamos el total real de valores faltantes
print("\nVALORES NULOS REALES DESPUÉS DEL REEMPLAZO:")
print(df_clean.isnull().sum())

# realizamos una comprobacion de los datos para descartar algun error en la 
# recodificacion de datos
print("\nVALORES DE NIVEL EDUCATIVO DESPUÉS DE LIMPIAR:")
print(df_clean["NIVEL_ED"].value_counts(dropna=False).sort_index())

print("\nVALORES DE COMPUTADORA DESPUÉS DE LIMPIAR:")
print(df_clean["IV12_3"].value_counts(dropna=False).sort_index())

print("\nVALORES DE INTERNET DESPUÉS DE LIMPIAR:")
print(df_clean["II7"].value_counts(dropna=False).sort_index())

#creamos un dataset nuevo (limpio ) con la recodificacion de los valores 9

df_clean.to_csv("df_clean.csv", index=False)

print("\nDataset limpio generado correctamente.")
print("Dimensiones:", df_clean.shape)

#Comienzo del analisis estadistico

#Estadistica descriptiva
#Calculo estadisticas descriptivas de las principales variables numericas.
# Se incluyen media y mediana como medidas de tendencia central,
# minimo y maximo para conocer los extremos y desvio estandar
# para analizar la dispersion de los datos.
# No utilizo la moda porque en estas variables numericas
# no aporta informacion relevante para el objetivo del analisis.

print("\nESTADÍSTICAS DESCRIPTIVAS")

variables_numericas = ["IX_TOT", "ITF", "DECIFR"]

for variable in variables_numericas:
    print(f"\nVariable: {variable}")
    print(f"Media: {df_clean[variable].mean():.2f}")
    print(f"Mediana: {df_clean[variable].median():.2f}")
    print(f"Mínimo: {df_clean[variable].min():.2f}")
    print(f"Máximo: {df_clean[variable].max():.2f}")
    print(f"Desvío estándar: {df_clean[variable].std():.2f}")

#se agrupa por percentiles el ingreso familiar para una mejor apreciacion.

print("\nPERCENTILES DE INGRESO FAMILIAR")

print(df_clean["ITF"].quantile([0.25, 0.50, 0.75]))    

#vamos a graficar para visualizar la informacion
import matplotlib.pyplot as plt


#primero vamos a realizar un grafico tipo histograma para visualizar 
# la distribucion de los hogares
plt.figure(figsize=(10, 6))

plt.hist(
    df_clean["ITF"].dropna(),
    bins=30,
    edgecolor="black"
)

plt.title("Distribución del Ingreso Familiar")
plt.xlabel("Ingreso Total Familiar")
plt.ylabel("Cantidad de hogares")

plt.tight_layout()
plt.savefig("graficos/histograma_ingresos.png", dpi=300, bbox_inches="tight")

plt.show()

plt.figure(figsize=(10, 4))

# Ademas se realiza un grafico de Caja para analizar desde otra 
# pespectiva la distribucion de los datos
plt.boxplot(
    df_clean["ITF"].dropna(),
    vert=False
)

plt.title("Distribución del Ingreso Total Familiar")
plt.xlabel("Ingreso Total Familiar")

plt.tight_layout()
plt.savefig("graficos/boxplot_ingresos.png", dpi=300, bbox_inches="tight")
plt.show()

# Los graficos muestran una distribucion con asimetria positiva:
# existe una mayor concentracion de hogares en ingresos bajos y medios,
# con una cola que se extiende hacia los ingresos mas altos.


# ANÁLISIS BIVARIADO
# HIPÓTESIS 1: INGRESO VS COMPUTADORA


# Selecciono solamente los registros que tienen valores validos
# tanto en DECIFR como en IV12_3
df_h1 = df_clean.dropna(subset=["DECIFR", "IV12_3"]).copy()

# Se creo una matriz de contingencia
tabla_pc = pd.crosstab(
    df_h1["DECIFR"],
    df_h1["IV12_3"]
)

print("\nDECIL DE INGRESO VS TENENCIA DE COMPUTADORA")
print(tabla_pc)

# Porcentajes por decil
porcentaje_pc = pd.crosstab(
    df_h1["DECIFR"],
    df_h1["IV12_3"],
    normalize="index"
) * 100

print("\nPORCENTAJES POR DECIL")
print(porcentaje_pc.round(2))

# GRÁFICO HIPÓTESIS 1


# Obtener porcentaje de hogares con computadora
pc_por_decil = porcentaje_pc[1.0]

plt.figure(figsize=(10, 6))

plt.plot(
    pc_por_decil.index,
    pc_por_decil.values,
    marker="o"
)

plt.title("Tenencia de computadora según decil de ingreso")
plt.xlabel("Decil de ingreso")
plt.ylabel("Hogares con computadora (%)")

plt.xticks(range(1, 11))
plt.ylim(0, 100)
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "graficos/computadora_por_decil.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# HIPÓTESIS 2: NIVEL EDUCATIVO VS INTERNET

#se extraen solamente las columnas a comparar
df_h2 = df_clean.dropna(subset=["NIVEL_ED", "II7"]).copy()

# Matriz de contingencia
tabla_internet_educacion = pd.crosstab(
    df_h2["NIVEL_ED"],
    df_h2["II7"]
)

print("\nNIVEL EDUCATIVO VS ACCESO A INTERNET")
print(tabla_internet_educacion)

# Porcentajes por nivel educativo
porcentaje_internet_educacion = pd.crosstab(
    df_h2["NIVEL_ED"],
    df_h2["II7"],
    normalize="index"
) * 100

print("\nPORCENTAJES DE INTERNET POR NIVEL EDUCATIVO")
print(porcentaje_internet_educacion.round(2))

#Grafico de la hipotesis 2

internet_por_educacion = porcentaje_internet_educacion[1.0]

niveles = [
    "Primaria\nincompleta",
    "Primaria\ncompleta",
    "Secundaria\nincompleta",
    "Secundaria\ncompleta",
    "Superior/\nUniversitaria"
]

plt.figure(figsize=(10, 6))

plt.bar(
    niveles,
    internet_por_educacion.values
)

plt.title("Acceso a Internet según nivel educativo")
plt.xlabel("Nivel educativo")
plt.ylabel("Hogares con Internet (%)")

plt.ylim(0, 100)

plt.tight_layout()

plt.savefig(
    "graficos/internet_por_educacion.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# HIPÓTESIS 3: INGRESO VS INTERNET

# Se extraen los valores a comparar
df_h3 = df_clean.dropna(subset=["DECIFR", "II7"]).copy()
#se crea una matriz de contingencia

tabla_internet_ingreso = pd.crosstab(
    df_h3["DECIFR"],
    df_h3["II7"]
)

print("\nDECIL DE INGRESO VS ACCESO A INTERNET")
print(tabla_internet_ingreso)

porcentaje_internet_ingreso = pd.crosstab(
    df_h3["DECIFR"],
    df_h3["II7"],
    normalize="index"
) * 100

print("\nPORCENTAJES DE INTERNET POR DECIL")
print(porcentaje_internet_ingreso.round(2))

# GRÁFICO HIPÓTESIS 3


internet_por_decil = porcentaje_internet_ingreso[1.0]

plt.figure(figsize=(10, 6))

plt.plot(
    internet_por_decil.index,
    internet_por_decil.values,
    marker="o"
)

plt.title("Acceso a Internet según decil de ingreso")
plt.xlabel("Decil de ingreso")
plt.ylabel("Hogares con Internet (%)")

plt.xticks(range(1, 11))
plt.ylim(0, 100)
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "graficos/internet_por_decil.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ANÁLISIS POR REGIÓN : complementario
# Se creo un diccionario para relacionar los nombres con su codigo

regiones = {
    1: "GBA",
    40: "NOA",
    41: "NEA",
    42: "Cuyo",
    43: "Pampeana",
    44: "Patagonia"
}

df_region = df_clean.copy()
df_region["REGION_NOMBRE"] = df_region["REGION"].map(regiones)

# INTERNET POR REGIÓN: matriz de contingencia
internet_region = pd.crosstab(
    df_region["REGION_NOMBRE"],
    df_region["II7"],
    normalize="index"
) * 100

print("\nACCESO A INTERNET POR REGIÓN")
print(internet_region.round(2))

# COMPUTADORA POR REGIÓN: matriz de contingencia
pc_region = pd.crosstab(
    df_region["REGION_NOMBRE"],
    df_region["IV12_3"],
    normalize="index"
) * 100

print("\nTENENCIA DE COMPUTADORA POR REGIÓN")
print(pc_region.round(2))

# ANALISIS DE CORRELACION
# Creo una copia del dataset para preparar las variables
# que voy a utilizar en la matriz
# Recodifico las variables tecnologicas para facilitar
# la interpretacion de la matriz:
# 1 = tiene acceso
# 0 = no tiene acceso

df_corr = df_clean.copy()

# Recodificar variables tecnológicas:
# 1 = tiene acceso
# 0 = no tiene acceso
df_corr["TIENE_PC"] = df_corr["IV12_3"].map({
    1: 1,
    2: 0
})

df_corr["TIENE_INTERNET"] = df_corr["II7"].map({
    1: 1,
    2: 0
})

variables_correlacion = [
    "IX_TOT",
    "NIVEL_ED",
    "ITF",
    "DECIFR",
    "TIENE_PC",
    "TIENE_INTERNET"
]

matriz_correlacion = df_corr[variables_correlacion].corr()

print("\nMATRIZ DE CORRELACIÓN")
print(matriz_correlacion.round(2))


# GRÁFICO MATRIZ DE CORRELACIÓN


plt.figure(figsize=(9, 7))

plt.imshow(
    matriz_correlacion,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.colorbar(label="Correlación")

plt.xticks(
    range(len(variables_correlacion)),
    variables_correlacion,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(variables_correlacion)),
    variables_correlacion
)

# Mostrar los valores dentro del gráfico
for i in range(len(variables_correlacion)):
    for j in range(len(variables_correlacion)):
        plt.text(
            j,
            i,
            f"{matriz_correlacion.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Matriz de correlación")

plt.tight_layout()

plt.savefig(
    "graficos/matriz_correlacion.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

import os

# Creo la carpeta donde voy a guardar los graficos
# si ya existe no realiza ningun cambio
os.makedirs("graficos", exist_ok=True)