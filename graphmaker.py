import plotly.express as px
import chart_studio
import chart_studio.plotly as py
import pandas as pd

df = pd.read_csv('yearlyElctConsumption1.csv')  # path to  csv

fig = px.bar(df, x='Year', y='Consumption(kWh)'
             , color="Consumption(kWh)")
fig.update_layout(template='plotly_white')
fig.update_layout(title='IZTECH Annual Electricity Consumption Averages (2013-2018) ')
fig.show()
username = ''  # your username
api_key = ''  # your api key - go to profile > settings > regenerate key
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
py.plot(fig, filename="yearlyElctConsumptioneng", auto_open=True)
