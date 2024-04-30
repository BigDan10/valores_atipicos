import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('gastos_costos_20_23.xlsx', sheet_name='2022')

#tratar nulos en columnas seleccionadas
df["Importe"] = df["Importe"].fillna(df["Importe"].mean())
df["TOTAL MX"] = df["TOTAL MX"].fillna(df["TOTAL MX"].mean())
df["TOTAL SAT"] = df["TOTAL SAT"].fillna(df["TOTAL SAT"].mean())


#Primera columna
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["Importe"], color='red', rwidth=0.50)
plt.title('Histograma de IMPORTE con outliers')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["Importe"]) 
plt.title("Outliers de IMPORTE")
plt.show()

y=df["Importe"]
#print(y)

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr= percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido", Limite_Superior_iqr)
#print("Limite inferior permitido", Limite_Inferior_iqr)

data_clean_iqr= df[ (y< Limite_Superior_iqr) & (y > Limite_Inferior_iqr) ]
#print(data_clean_iqr)

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["Importe"]) 
plt.title("Outliers de IMPORTE")
plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["Importe"], color='blue', rwidth=0.50)
plt.title('Histograma de IMPORTE sin outliers')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
plt.show()

#Segunda columna
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["TOTAL MX"], color='red', rwidth=0.50)
plt.title('Histograma de TOTAL MX con outliers')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["TOTAL MX"]) 
plt.title("Outliers de TOTAL MX")
plt.show()

y=df["TOTAL MX"]
#print(y)

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr= percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido", Limite_Superior_iqr)
#print("Limite inferior permitido", Limite_Inferior_iqr)

data_clean_iqr= df[ (y< Limite_Superior_iqr) & (y > Limite_Inferior_iqr) ]
#print(data_clean_iqr)

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["TOTAL MX"]) 
plt.title("Outliers de TOTAL MX")
plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["TOTAL MX"], color='blue', rwidth=0.50)
plt.title('Histograma de TOTAL MX sin outliers')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
plt.show()

#Tercera columna
fig = plt.figure(figsize =(7, 3)) 
plt.hist(x=df["TOTAL SAT"], color='red', rwidth=0.50)
plt.title('Histograma de TOTAL SAT con outliers')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["TOTAL SAT"]) 
plt.title("Outliers de TOTAL SAT")
plt.show()

y=df["TOTAL SAT"]
#print(y)

percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr= percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido", Limite_Superior_iqr)
#print("Limite inferior permitido", Limite_Inferior_iqr)

data_clean_iqr= df[ (y< Limite_Superior_iqr) & (y > Limite_Inferior_iqr) ]
#print(data_clean_iqr)

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr["TOTAL SAT"]) 
plt.title("Outliers de TOTAL SAT")
plt.show()

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr["TOTAL SAT"], color='blue', rwidth=0.50)
plt.title('Histograma de TOTAL SAT sin outliers')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
plt.show()

data_clean_iqr.to_csv("2022.csv")

