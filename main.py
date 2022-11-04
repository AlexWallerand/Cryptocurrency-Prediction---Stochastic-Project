from get_data import *
from formula import *
from ar import *
import matplotlib.pyplot as plt

# ================== Récupération Données ==================

symbol = input("Symbol : ").upper()
comparative_symbol = input("Comparative Symbol : ").upper()
hourly = input("Daily or hourly historical (d/h) : ")
details = input("Frames details of the AR model (y/n) : ")
time_delta = 1
df = hourly_price_historical(
    symbol, comparative_symbol, 2000, time_delta, hourly)
title = f"{symbol}/{comparative_symbol}-{hourly}"
df.to_csv(f"{symbol}-{comparative_symbol}-{hourly}")


# ================== Moyenne Mobile simple ==================

MoyMobil10 = moyenneMobile(df, 10)
print("MA 10 OK")
MoyMobil50 = moyenneMobile(df, 50)
print("MA 50 OK")
MoyMobil100 = moyenneMobile(df, 100)
print("MA 100 OK")

plt.plot(df.timestamp, df.close)
plt.plot(df.timestamp, MoyMobil10, color='red', linewidth=0.8, alpha=0.8)
plt.plot(df.timestamp, MoyMobil50, color='green', linewidth=0.8, alpha=0.8)
plt.plot(df.timestamp, MoyMobil100, color='purple', linewidth=0.8, alpha=0.8)

plt.title(title)
plt.xlabel("Timestamp")
plt.ylabel(comparative_symbol)
plt.legend([symbol, 'MA 10', 'MA 50', 'MA 100'])
plt.xticks(rotation=60)
plt.show()

# ================== Moyenne Mobile Exponantielle ==================

MoyMobilEXP10 = MoyenneMobileExp(df, 10)
print("MA EXP 10 OK")
MoyMobilEXP50 = MoyenneMobileExp(df, 50)
print("MA EXP 50 OK")
MoyMobilEXP100 = MoyenneMobileExp(df, 100)
print("MA EXP 100 OK")

plt.plot(df.timestamp, df.close)
plt.plot(df.timestamp, MoyMobilEXP10, color='red', linewidth=0.8, alpha=0.8)
plt.plot(df.timestamp, MoyMobilEXP50, color='green', linewidth=0.8, alpha=0.8)
plt.plot(df.timestamp, MoyMobilEXP100,
         color='purple', linewidth=0.8, alpha=0.8)

plt.title(title)
plt.xlabel("Timestamp")
plt.ylabel(comparative_symbol)
plt.legend([symbol, 'Exponential MA 10',
           'Exponential MA 50', 'Exponential MA 100'])
plt.xticks(rotation=60)
plt.show()

# ================== Indice Stochastique ==================

k = stochastic(df)
k = k[100:]
d = moyenneMobileSimple(k, 14)
df1 = df.iloc[100:]
print("Stochastic indice OK")
plt.plot(df1.timestamp, k)
plt.plot(df1.timestamp, d)
plt.axhline(y=80, color='black', linestyle='--')
plt.axhline(y=20, color='black', linestyle='--')
plt.title(f"Stochastic Indice {symbol}/{comparative_symbol}")
plt.legend(['K indice', 'D indice'])
plt.xticks(rotation=60)
plt.show()

# ================== Modèle Auto-Régressif ==================

AR_model(df, details, symbol, comparative_symbol)
