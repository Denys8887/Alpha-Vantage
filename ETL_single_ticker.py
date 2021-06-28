from logging_func import logging_csv
from alpha_vantage.techindicators import TechIndicators

key = open('alphavantageAPI').read()


@logging_csv
def tech_indicators_sma():
    try:
        ti = TechIndicators(key, output_format='pandas')
        data, meta = ti.get_sma(symbol='MSFT', interval='daily', time_period='200', series_type='close')

        return data

    except Exception as ex:

        f = open("mylog.csv", "a")

        f.write(str(ex))

        f.close()


if __name__ == '__main__':
    print(tech_indicators_sma())
