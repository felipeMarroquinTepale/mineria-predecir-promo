import mysql.connector as connection
from prophet import Prophet
import pandas as pd

mydb = connection.connect(
                     host="db-apibeekepeer.cdqxvmj3d7xx.us-east-1.rds.amazonaws.com",    # your host, usually localhost
                     user="admin",         # your username
                     passwd="datamin3",  # your password
                     db="Tienda"
                     )        # name of the data base

query = "Select ds,y from Tienda.price"
df = pd.read_sql(query,mydb)
df.head()

# print(df.info())

p = Prophet(interval_width=0.92, daily_seasonality=True)
model = p.fit(df)

future = p.make_future_dataframe(periods=365, freq='D')
future.tail()

forecast_prediction = p.predict(future)
forecast_prediction.tail()

plot1 = p.plot(forecast_prediction)

plot2 = p.plot_components(forecast_prediction)