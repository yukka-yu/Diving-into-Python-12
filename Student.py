import random

from home12.Name import Name
import csv

file = 'home12.csv'


class Student:
    file = 'home12.csv'
    first_name = Name()
    last_name = Name()
    patronymic = Name()

    def __init__(self, first_name: str, last_name: str, patronymic: str):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.list_lessons = []
        self.file = file
        with open(self.file, 'r', encoding='utf-8') as f:
            self.list_lessons.extend(f.readline().split(','))

        self.dict_ball = {}
        self.dict_tests = {}
        for i in self.list_lessons:
            count_ball = random.randint(4, 10)
            list_ = []
            list_2 = []
            for j in range(count_ball):
                list_.append(random.randint(2, 5))
                list_2.append(random.randint(0, 100))
            self.dict_ball[i] = list_
            self.dict_tests[i] = list_2

    def __str__(self):
        return f'Фамилия: {self.last_name}, Имя: {self.first_name}, Отчество: {self.patronymic}, ' \
               f'Средняя оценка по всем предметам = {round(self.medium_balls(), 2)}, ' \
               f'Средние оценки по тестам: {self.medium_tests()}'

    def medium_balls(self) -> float:
        result = 0
        for value in self.dict_ball.values():
            result += sum(value) / len(value)
        result /= len(self.dict_ball)
        return result

    def medium_tests(self) -> dict:
        my_dict = {}
        for key, value in self.dict_tests.items():
            my_dict[key] = round(sum(value) / len(value), 2)
        return my_dict


if __name__ == '__main__':
    a = Student('Иван', 'Иванов', 'Иванович')
    print(a)


