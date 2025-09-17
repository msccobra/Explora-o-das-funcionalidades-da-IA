#Programa básico de predição análise de valor de criptomoedas

import ccxt
import pandas as pd
import matplotlib.pyplot as plt

def cripto(
    symbol='BTC/USDT',
    window1=10,
    window2=50,
    limit=90,
    exchange_name='binance'
):
    exchange = getattr(ccxt, exchange_name)()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1d', limit=limit+window2)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df['MA10'] = df['close'].rolling(window=window1).mean()
    df['MA50'] = df['close'].rolling(window=window2).mean()

    plt.figure(figsize=(12,6))
    plt.plot(df.index[-limit:], df['close'][-limit:], label='Preço de Fechamento')
    plt.plot(df.index[-limit:], df['MA10'][-limit:], label='Média Móvel 10 dias')
    plt.plot(df.index[-limit:], df['MA50'][-limit:], label='Média Móvel 50 dias')
    plt.title('Médias Móveis de 10 e 50 dias')
    plt.xlabel('Data')
    plt.ylabel('Preço (USDT)')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    cripto('BTC/USDT')

if __name__ == "__main__":
    main()
