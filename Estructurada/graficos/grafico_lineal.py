import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ejemplo con pedos
# aca se abre el csv
df = pd.read_csv("graficos\\pedos.csv")

# aca se crean los graficos
sns.lineplot(x="fecha",y="pedos",data=df)

# aca se puede colocar un punto en un sitio especifico
plt.plot("01-09",17,"o")

# aca se muestra el grafico
plt.show()


