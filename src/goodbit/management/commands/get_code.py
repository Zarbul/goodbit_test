from django.core.management.base import BaseCommand

from src.goodbit.services import generate_promo_code


class Command(BaseCommand):
    help = "Генерирует новые промо коды и сохраняет их в указанный файл."

    def add_arguments(self, parser):
        parser.add_argument("-a",
                            "--amount",
                            type=int,
                            help="Количество новых кодов")
        parser.add_argument("-g",
                            "--group",
                            type=str,
                            help="Название группы, для которой будут созданы промокоды")

    def handle(self, *args, **kwargs):
        amount = kwargs["amount"]
        group = kwargs["group"]

        if amount is None:
            self.stdout.write("Укажите количество кодов: -a <количество>")
            return
        if group is None or group == "":
            self.stdout.write("Укажите группу: -g <группа>")
            return

        try:
            codes = generate_promo_code(amount=amount,
                                        group=group)
        except AssertionError:
            self.stdout.write("Неверно указаны параметры команды")
            return
        self.stdout.write(f"Новые коды: {codes}")
