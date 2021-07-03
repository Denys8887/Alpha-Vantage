from logging_func import logging_csv
from alpha_vantage.techindicators import TechIndicators

key = open('alphavantageAPI').read()


@logging_csv
def tech_indicators_sma():
    ti = TechIndicators(key, output_format='pandas')
    data, meta = ti.get_sma(symbol='MSFT', interval='daily', time_period='200', series_type='close')

    return data


if __name__ == '__main__':
    print(tech_indicators_sma())
