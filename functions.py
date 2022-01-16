from operator import le
from binance.client import Client
from binance.enums import *
from connection import client

def GET_ALL_TICKERS():

    list_tickers = client.GET_ALL_TICKERS()

    for ticker in list_tickers:
        symbol = ticker['symbol']
        price = ticker['price']

        print("Símbolo: " + symbol + " Precio: " + price)



# Medias móviles simples
def SMA_INTERVAL_4HRS(period, ticker):
    closing_price_list = []

    data_historical = client.get_historical_klines(ticker, Client.KLINE_INTERVAL_4HOUR, '800 hour ago UTC')

    #print("Candles: ", len(data_historical))

    sum = 0

    if len(data_historical) == 200:
        print("Se obtuvieron todas las velas satisfactoriamente")

        for i in range((200 - period), 200):
            #print(data_historical[i])

            sum += float(data_historical[i][4])

        sma = sum / period

        print("SMA: " +  ticker + " Periodo " + str(period) + ": " + str(sma))

        return(sma)

    else:
        print("No se pudo obtener el historial de velas")

# Medias móviles exponenciales
def EMA_INTERVAL_4HRS(period, ticker):
    closing_price_list = []
    ema = []

    data_historical = client.get_historical_klines(ticker, Client.KLINE_INTERVAL_4HOUR, '1000 hour ago UTC')

    #print("Velas: ", len(data_historical))

    sma = SMA_INTERVAL_4HRS(period, ticker)
    ema.append(sma)

    if len(data_historical) == 250:
        print("Se obtuvieron todas las velas satisfactoriamente")

        for i in range(len(data_historical)):
            closing_price_list.append(float(data_historical[i][4]))

        for price in closing_price_list[period:]:
            ema.append( (price * (2/(period + 1))) + ema[-1] * (1 - (2/(period + 1))) )

            #print("Cantidad de elementos: ", len(ema))

            #for i in ema:
            #    print(i)

            ema_value = round(ema.pop(), 1)

            print("EMA: " + ticker + " Periodo: " + str(period) + " : " + str(ema_value))

            return(ema_value)

    else:
        print("No se pudo obtener el historial de velas")