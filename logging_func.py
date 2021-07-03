import logging


def logging_csv(func):
    def wrap(*args, **kwargs):
        try:
            logging.basicConfig(level=logging.DEBUG,
                                format="{asctime},{levelname:<6} {processName}  {message} ",
                                style='{',
                                filename='mylog.csv ')
            result = func(*args, **kwargs)
            return result
        except Exception as ex:

            f = open("mylog.csv", "a")

            f.write(str(ex))

            f.close()

    return wrap
