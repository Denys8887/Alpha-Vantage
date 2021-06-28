import logging


def logging_csv(func):
    def wrap(*args, **kwargs):
        logging.basicConfig(level=logging.DEBUG,
                            format="{asctime},{levelname:<6} {processName}  {message} ",
                            style='{',
                            filename='mylog.csv ')
        result = func(*args, **kwargs)
        return result

    return wrap
