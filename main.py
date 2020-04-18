import datetime

class TimeManager:
    def __enter__(self):
        self.start_time = datetime.datetime.utcnow()
        print(f'Время запуска кода в менеджере контекста: {self.start_time}')


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = datetime.datetime.utcnow()
        print(f'Время время окончания работы кода в менеджере контекста: {self.end_time}')
        print(f'На выполнение кода было потрачено: {self.end_time - self.start_time}')

with TimeManager() as log:
    nonsense = range(99999999)
    for value in nonsense:
        value = value/10