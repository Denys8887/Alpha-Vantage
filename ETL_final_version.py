from alpha_vantage.async_support.techindicators import TechIndicators
from logging_func import logging_csv
import asyncio

symbols = ['AAPL', 'ABAC', 'ABAX', 'MSFT',
           'IBM']  # you can use ticker_search.py to find more tickers and implement them hear.For more use of
# tickers,you must have a premium version.

key = open('alphavantageAPI').read()


@logging_csv
async def get_data(symbol):
    try:
        ti = TechIndicators(key, output_format='pandas')
        data, _ = await ti.get_sma(symbol=symbol, interval='daily', series_type='close')
        await ti.close()
        return data
    except Exception as ex:

        f = open("mylog.csv", "a")

        f.write(str(ex))

        f.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [get_data(symbol) for symbol in symbols]
    group1 = asyncio.gather(*tasks)
    results = loop.run_until_complete(group1)

    print(results)
