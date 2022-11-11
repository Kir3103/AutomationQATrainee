class MetaClassSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaClassSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def clear(cls):
        return cls._instances.pop(cls, None)
