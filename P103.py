import pandas as pd
import plotly.express as ex

df =pd.read_csv("Projects\P103\Copy+of+data+-+data.csv")

fig = ex.scatter(df, x = "date", y = "cases", color = "country")
fig.show()