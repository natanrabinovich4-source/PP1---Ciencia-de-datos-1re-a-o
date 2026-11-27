#  Diagnóstico de la Brecha Digital e Inclusión Tecnológica en Argentina

**Práctica Profesional I**

**Carrera:** *Técnico Superior en Ciencia de Datos e Inteligencia Artificial*

**Alumno:** *Natan Levi Rabinovich*

**Año:** *2026*


---------------

## Descripción del proyecto

Este proyecto busca analizar la brecha digital en Argentina y ver cómo distintas condiciones de los hogares pueden influenciar el acceso a la tecnológia. Comparando factores como los ingresos, el nivel educativo y la región donde se encuentra el hogar para determinar si tienen relación con la posibilidad de contar con una computadora y conexión a Internet.

Para este trabajo se utilizará Python para generar,preparar y limpiar los datos, realizar analisis estadisticos y generar graficos que permitan interpretar mejor los resultados.

------------------------------

## Objetivos

* Analizar la influencias de las condiciones social - economicas sobre el acceso a las tegnológias.

* Identificar posibles diferencias en el acceso a computadoras e Internet y determinar qué factores tienen una mayor relación con la brecha digital.

-------------------

## Hipotesis

### Hipótesis 1: Ingresos y computadora
Los hogares que se encuentran en los deciles de mayores ingresos tendrán una mayor presencia de computadoras o laptops.

### Hipótesis 2: Educación e Internet
Los hogares donde el jefe/a de hogar tiene un mayor nivel educativo tendrán un mayor acceso a Internet.

### Hipótesis 3: Ingresos e Internet
Los hogares con mayores ingresos tendrán un mayor acceso a Internet que los hogares de menores ingresos.

-------------------------------------------------

## Data Set

Para realizar el proyecto se utiliza un data set con 1000 hogares generado aleatoriamente con Python para este proyecto en particular.

**Son datos generados para fines academicos, bajo ningun concepto se utilizaran para otros fines.**

Las variables utilizadas toman como referencia la nomenclatura de la Encuesta Permanente de Hogares (EPH) y permiten analizar información económica, educativa, geográfica y tecnológica de los hogares.

El archivo inicial utilizado es:

Datasetinicial.cvs

------------------------------

## Variables

**Variable	Descripción**

CODUSU	Identificador del hogar

REGION	Región donde se encuentra el hogar

IX_TOT	Cantidad de integrantes del hogar

NIVEL_ED	Nivel educativo del jefe/a de hogar

ITF	Ingreso Total Familiar

DECIFR	Decil de ingreso familiar

IV12_3	Indica si el hogar posee computadora o laptop

II7	Indica si el hogar tiene acceso a Internet

**Regiones**

1 = GBA

40 = NOA

41 = NEA

42 = Cuyo

43 = Pampeana

44 = Patagonia

**Nivel educativo**

1 = Primaria incompleta

2 = Primaria completa

3 = Secundaria incompleta

4 = Secundaria completa

5 = Superior/Universitaria completa

9 = Sin respuesta

**Tenencia de computadora e Internet**

1 = Sí

2 = No

9 = Sin respuesta

----------------

## Herramientas utilizadas

* Python
* Visual Studio Code
* Excel
* librerias : Panda, Numpy , Matplotlib, Github.

----------------

## Metodologia de trabajo

* Generación y carga del dataset.
* Exploración inicial de los datos.
* Identificación de valores faltantes y datos que necesitan ser tratados.
* Limpieza y preparación de los datos.
* Generación de un dataset limpio.
* Análisis estadístico de las principales variables.
* Cruce de variables económicas, educativas y tecnológicas.
* Generación de gráficos.
* Análisis de los resultados.
* Evaluación de las hipótesis planteadas.
* Elaboración de conclusiones y posibles recomendaciones.

  -------------------
  ## Paso a Paso
  **Exploracion de los datos:**

Los códigos 9 presentes en las variables NIVEL_ED, IV12_3 e II7 fueron considerados como "Sin respuesta" y se transformaron en valores nulos (NaN) para evitar que fueran interpretados como valores válidos durante los análisis estadísticos.

Los registros con información faltante no fueron eliminados completamente, ya que pueden contener datos útiles para otros análisis. En cada análisis se utilizarán únicamente los registros que tengan información válida para las variables estudiadas.
Luego de la limpieza se generó el archivo df_clean.csv, manteniendo el dataset original sin modificaciones.

**Analisis Estadisticos de las principales variables**

Luego de realizar la limpieza se comenzó con un análisis exploratorio para conocer mejor el comportamiento de las principales variables.

Ingreso Total Familiar
El Ingreso Total Familiar (ITF) presenta los siguientes resultados:

Media: $773.680

Mediana: $604.132

Mínimo: $67.039

Máximo: $5.884.802

Desvío estándar: $576.672

Primer cuartil (25%): $403.629

Tercer cuartil (75%): $977.464

Al comparar la media con la mediana se observa que la media es mayor. En el histograma también se puede ver una concentración de hogares en los ingresos más bajos y una cola hacia los ingresos más altos. (grafica Asimetrica positiva)

El boxplot muestra varios valores extremos en la parte superior de la distribución. Estos valores se conservaron para el análisis, ya que no necesariamente representan errores en los datos.

## Analisis multivariable

**Hipotesis 1: Ingresos y computadora**

Se estudio la relacion que existe entre la variable ingreso vs la tenencia de computadora. para ello se creo una tabla de contingencia comparando las variables y se grafico lineal.

En el decil 1, el 40,66% de los hogares cuenta con computadora o laptop, mientras que en el decil 10 este porcentaje aumenta al 91,30%.

Se observa una tendencia general a que los hogares ubicados en los deciles más altos (hogares con mayor ingreso) presentan un mayor acceso a computadoras.

Por este motivo, los resultados respaldan la hipótesis planteada.

**Hipotesis 2 : Nivel educativo e internet**

Se estudio la relacion que existe entre la variable nivel de ingreso vs acceso a internet. para ello se creo una tabla de contingencia comparando las variables y se grafico con un grafico de barra.

Los resultados muestran una relación clara entre el nivel educativo y el acceso a Internet.

En los hogares con nivel educativo de primaria incompleta, el 43,90% cuenta con acceso a Internet. Este porcentaje aumenta a medida que sube el nivel educativo, llegando al 97,71% en el nivel superior/universitario completo.

Los resultados muestran una tendencia creciente en todos los niveles analizados, por lo que respaldan la hipótesis planteada.

**Hipotesis 3 : Ingresos e internet**

Se estudio la relacion que existe entre la variable Ingresos vs acceso a internet. para ello se creo una tabla de contingencia comparando las variables y se grafico con un grafico lineal.

Los resultados muestran una relación entre el nivel de ingreso y el acceso a Internet.

En el decil 1, el 57,14% de los hogares cuenta con acceso a Internet, mientras que en el decil 10 el porcentaje alcanza el 95,70%.

Si bien existen algunas variaciones entre deciles, se observa una tendencia general donde los hogares de mayores ingresos presentan un mayor acceso a Internet.

Los resultados respaldan la hipótesis planteada.

**Analisis complementario : Acceso a internet y tenencia de computadora por region**

Se comparo la influencia de la variable Region respecto al acceso a internet y tenencia de computadora.
Para ello se creo dos tablas de comparacion para tomar cada variable por separado, pero no se demuestra que la region puede influenciar en el acceso a internet o la tenencia de computadora.

**Analisis complementario : Matriz de correlacion**

Se realizo una matriz de correlacion entre las principales variables para determinar la correlacion que existe entre las principales variables, arrojando la siguiente comparacion:

Nivel educativo e ingreso familiar: 0,66.

Nivel educativo y decil de ingreso: 0,72.

Nivel educativo y acceso a Internet: 0,33.

Decil de ingreso y tenencia de computadora: 0,30.

Decil de ingreso y acceso a Internet: 0,32.

## Principales hallazgos

A partir de los análisis realizados se encontraron tres resultados principales:

* El nivel de ingreso está relacionado con la tenencia de computadora. Los hogares de los deciles más altos presentan un mayor acceso a este tipo de equipamiento.

* El nivel educativo presenta una relación clara con el acceso a Internet. El porcentaje de hogares conectados aumenta a medida que aumenta el nivel educativo.

* Los ingresos también están relacionados con el acceso a Internet. Los hogares pertenecientes a los deciles más altos muestran mayores porcentajes de conectividad.

En cambio, las diferencias encontradas entre las regiones fueron relativamente pequeñas dentro de este dataset.

En conjunto, los resultados muestran que las diferencias económicas y educativas tienen una relación más marcada con el acceso tecnológico que la región geográfica.

## Limitaciones del estudio
El dataset utilizado fue generado de forma sintética con fines académicos, tomando como referencia variables y codificaciones utilizadas en la Encuesta Permanente de Hogares (EPH).

Por este motivo, los resultados obtenidos sirven para practicar y demostrar el proceso de análisis de datos, pero no deben interpretarse como estimaciones reales de la situación de la población argentina.

El objetivo del proyecto es aplicar un proceso completo de ciencia de datos que incluya generación, limpieza, exploración, análisis, visualización e interpretación de la información.

## Conclusion

El análisis permitió identificar una relación entre las condiciones socioeconómicas y educativas de los hogares y su acceso a la tecnología.

Las tres hipótesis planteadas fueron respaldadas por los resultados del dataset. Los hogares con mayores ingresos mostraron un mayor acceso a computadoras e Internet, mientras que los hogares con mayores niveles educativos también presentaron mayores porcentajes de conectividad.

Dentro de los datos analizados, las diferencias relacionadas con ingresos y educación fueron más marcadas que las diferencias encontradas entre regiones.

Estos resultados permiten observar cómo el análisis de datos puede utilizarse para identificar grupos con diferentes niveles de acceso tecnológico y ayudar a orientar posibles medidas de inclusión digital.


