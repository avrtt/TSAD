import logging


class Logger(object):
    def __init__(self):
        super()

    @staticmethod
    def get_logger():
        logging.basicConfig(level=logging.INFO)
        return logging


if __name__ == "__main__":
    pass
