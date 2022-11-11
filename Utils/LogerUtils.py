import logging


class Logger:
    fn_log = 'Resource/test.log'
    _logger = logging.getLogger("Logger")
    logging.basicConfig(level=logging.INFO, filemode='w', filename=fn_log,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S')

    @staticmethod
    def info(message):
        Logger._logger.info(msg=message)

    @staticmethod
    def debug(message):
        Logger._logger.debug(msg=message)

    @staticmethod
    def warning(message):
        Logger._logger.warning(msg=message)

    @staticmethod
    def error(message):
        Logger._logger.error(msg=message)

    @staticmethod
    def fatal(message):
        Logger._logger.fatal(msg=message)
