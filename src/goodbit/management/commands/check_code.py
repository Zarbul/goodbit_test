from django.core.management.base import BaseCommand

from src.goodbit.services import check_code_in_file


class Command(BaseCommand):
    help = "Проверяет код на существование."

    def add_arguments(self, parser):
        parser.add_argument("-c",
                            "--check",
                            type=str,
                            help="Код для проверки")

    def handle(self, *args, **kwargs):
        code = kwargs["check"]

        if code is None:
            self.stdout.write("Укажите код: -c")
            return

        try:
            codes = check_code_in_file(code=code)
        except AssertionError:
            self.stdout.write("Неверно указаны параметры команды")
            return
        # self.stdout.write(f"{codes}")
