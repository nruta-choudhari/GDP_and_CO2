# importing packages
import pandas as pd
import numpy as np

# reading the data
df = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)
columns = [
    "Mortality rate, under-5 (per 1,000 live births)",
    "GDP per capita (constant 2010 US$)",
    "Country Name",
]
df = df[columns]

df["Log GDP Per Capita"] = np.log(df["GDP per capita (constant 2010 US$)"])

# importing more packages
import seaborn.objects as so
import seaborn as sns
from matplotlib import style

# plotting the graph
my_chart = (
    so.Plot(
        df, x="Log GDP Per Capita", y="Mortality rate, under-5 (per 1,000 live births)"
    )
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="Log GDP and Under-5 Mortality")
)

sns.set_theme(style="whitegrid")

my_chart.show()
