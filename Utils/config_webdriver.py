from browser_factory import BrowserFactory


class MetaClassSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaClassSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]

    def clear(cls):
        _ = cls._instances.pop(cls, None)


class WebDriver(metaclass=MetaClassSingleton):
    connection = None

    def get_browser(self):
        if self.connection is None:
            self.connection = BrowserFactory().get_driver_factory('chrome')

        return self.connection

    @staticmethod
    def destroy():
        return WebDriver.clear()

    @staticmethod
    def get_driver():
        return WebDriver()
