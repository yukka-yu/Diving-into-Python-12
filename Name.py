class Name:
    """Десткриптор для имени, фамилии и отчества на проверку isalpha() и istitle()"""

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value.isalpha() and value.istitle():
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Строка {value} должны содержать только буквы и начинаться с большой буквы')
