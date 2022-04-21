import json
import os
import random
from typing import Union
from pathlib import Path
from config.settings import BASE_DIR


def main():
    generate_promo_code(5, 'banks')


file_path = BASE_DIR / 'src/goodbit/promo_codes.json'


def generate_promo_code(amount: int = 1, group: Union[int, str] = "default"):
    """
    Генерирует рандомные промо коды.
    """
    symbols = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
    codes = []

    for num in range(0, amount):

        new_code = ''.join(random.choices(symbols, k=random.randint(5, 10)))
        codes.append(new_code)

    data = {group: codes}
    if check_group_in_file(group):
        change_json(group, codes)
    else:
        write_json(group, codes)
    return data


def check_group_in_file(group):
    if not os.path.exists(file_path):
        Path(file_path).touch()
        return False

    with open(file_path, 'r') as file:
        data = json.load(file)
        if str(group) in data['promo_codes']:
            return True
        return False


def check_code_in_file(code):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for key, value in data['promo_codes'].items():
            if str(code) not in value:
                print(f'код {code} не существует в группе = {key}')
            else:
                print(f'код {code} существует в группе = {key}')


def change_json(group, codes):
    with open(file_path, 'r') as read_file:
        data = json.load(read_file)
        data['promo_codes'][str(group)].extend(codes)
        with open(file_path, 'w') as write_file:
            json.dump(data, write_file, ensure_ascii=False, indent=4)


def write_json(group, codes):
    with open(file_path, 'r') as read_file:
        try:
            data = json.load(read_file)
            data['promo_codes'][group] = codes
            with open(file_path, 'w') as write_file:
                json.dump(data, write_file, ensure_ascii=False, indent=4)
        except json.decoder.JSONDecodeError:
            data = {'promo_codes': {group: codes}}
            with open(file_path, 'w') as write_file:
                json.dump(data, write_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # main()
    check_code_in_file('VKXz45naWe')
