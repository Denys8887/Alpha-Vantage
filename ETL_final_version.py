import time
from alpha_vantage.async_support.techindicators import TechIndicators
from logging_func import logging_csv
import asyncio

symbols = ['ADI', 'ADMA', 'ADMP', 'ADMS', 'TEST_TICKER'], ['ADP', 'ADRA', 'ADRD', 'ADRE', 'ADRU'], ['ADSK', 'ADTN',
                                                                                                    'ADUS',
                                                                                                    'ADVS',
                                                                                                    'ADXS'], [
              'ADXSW', 'AEGN', 'AEGR', 'AEHR', 'AEIS'], ['AEPI', 'AERI', 'AETI', 'AEY', 'AEZS']
# you can use ticker_search.py to find more tickers and implement them hear.

key = open('alphavantageAPI').read()


@logging_csv
async def get_data(symbol):
    try:
        ti = TechIndicators(key, output_format='pandas')
        data, _ = await ti.get_sma(symbol=symbol, interval='daily', series_type='close')
        await ti.close()
        return data
    except:
        pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task1 = [get_data(symbol) for symbol in symbols[0]]
    group1 = asyncio.gather(*task1)
    result1 = loop.run_until_complete(group1)
    print(result1)
    time.sleep(60)
    task2 = [get_data(symbol) for symbol in symbols[1]]
    group2 = asyncio.gather(*task2)
    result2 = loop.run_until_complete(group2)
    print(result2)
    time.sleep(60)
    task3 = [get_data(symbol) for symbol in symbols[2]]
    group3 = asyncio.gather(*task3)
    result3 = loop.run_until_complete(group3)
    print(result3)
    time.sleep(60)
    task4 = [get_data(symbol) for symbol in symbols[3]]
    group4 = asyncio.gather(*task4)
    result4 = loop.run_until_complete(group4)
    print(result4)
    time.sleep(60)
    task5 = [get_data(symbol) for symbol in symbols[4]]
    group5 = asyncio.gather(*task5)
    result5 = loop.run_until_complete(group5)
    print(result5)

'''If you have Premium Alpha Vantage you can use this code'''

# loop = asyncio.get_event_loop()
#     tasks = [get_data(symbol) for symbol in symbols]
#     group1 = asyncio.gather(*tasks)
#     results = loop.run_until_complete(group1)
#
#     print(results)
