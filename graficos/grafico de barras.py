import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  cofla
df = pd.read_csv("graficos\\cofla_ingresos.csv")

# creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

# obteniendo el total de ingresos
total_ingreso = df['ingresos'].sum()

# mostrando el total de ingresos
print(f"el total de ingreso es ${total_ingreso} USD ")

# mostrando el grafico
plt.show()


