from functions import *

sma4 = SMA_INTERVAL_4HRS(4, 'ADABUSD')
sma9 = SMA_INTERVAL_4HRS(9, 'ADABUSD')
sma18 = SMA_INTERVAL_4HRS(18, 'ADABUSD')

if sma4 > sma9 and sma4 > sma18:
    print("Se está cumpliendo la estrategia Triple Cruce SMA 4 9 18")


ema10 = EMA_INTERVAL_4HRS(10, 'LTCBUSD')
ema20 = EMA_INTERVAL_4HRS(20, 'LTCBUSD')
ema30 = EMA_INTERVAL_4HRS(30, 'LTCBUSD')

if ema10 > ema20 and ema10 > ema30:
    print("Se está cumpliendo la estrategia Triple Cruce EMA 10 20 30")