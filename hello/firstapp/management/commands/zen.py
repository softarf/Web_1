import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'The Zen of Python'

    def add_arguments(self, parser):
        # Объявляет ключи для вывода короткого сообщения приветствия.
        parser.add_argument(
            '-s',
            '--short',
            action='store_true',
            default=False,
            help='Вывод короткого сообщения'
        )
        # Получает имя файла с данными для чтения. По умолчанию - 'text1.txt'.
        parser.add_argument(
            'file_name',
            action='store',
            nargs='?',
            default='text1.txt',
            help='Название файла для считывания данных'
        )
        pass

    def handle(self, *args, **options):
        # Показывает работу ключа для вывода короткого сообщения.
        if options['short']:
            import __hello__    # Почему-то не работает.
        else:
            import this         # Вывод полного сообщения работает.

        # Выводит название главной папки проекта.
        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(os.path.abspath(__file__)))))
        self.stdout.write(f"\n    Каталог: {base_dir}")
        file_name = options['file_name']
        file_path = os.path.join(base_dir, file_name)
        self.stdout.write(file_name)  # Для проверки.
        self.stdout.write(f"    Файл:    {file_path}")

        # Проверяет существование переданного файла.
        if os.path.exists(file_path):
            self.stdout.write("Файл существует.")
        else:
            self.stdout.write(f"Файл не найден\n{file_path}")

        # Печатает все имеющиеся аргументы функции handle().
        for arg in args:
            self.stdout.write(arg)
        self.stdout.write()
        for opt in options:
            self.stdout.write(opt)
        self.stdout.write()

        # Демонстрирует чтение из переданного файла.
        with open(file_path, 'rt', encoding="utf-8") as file:
            lines = file.readlines()
        for arg in args:
            self.stdout.write(arg)
        self.stdout.write()
        for line in lines:
            self.stdout.write(line)
        self.stdout.write()

        # with open('phones.csv', 'r') as file:
        #     phones = list(csv.DictReader(file, delimiter=';'))

        # for phone in phones:
        #     # TODO: Добавьте сохранение модели
        #     pass
