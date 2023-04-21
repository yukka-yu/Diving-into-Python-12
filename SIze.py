class Size:
    # def __init__(self, number: int = 0):
    #     self.number = number

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f'Значение {value} должно быть больше {0}')
        setattr(instance, self.param_name, value)




