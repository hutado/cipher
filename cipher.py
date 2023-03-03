# -*- coding: utf-8 -*-

"""
Основной модуль для работы с утилитой
"""

import argparse

from core.encrypt import Encrypt
from core.decrypt import Decrypt


class Cipher:
    encrypt = Encrypt
    decrypt = Decrypt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Cipher',
        description='Консольная утилита для шифрования/дешифрования текста',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Шифрование/Дешифрование')
    parser.add_argument('func', choices=['caesar', 'vigenere', 'atbash'], help='Функция')
    parser.add_argument('text', help='Текст для шифрования')

    parser.add_argument(
        '-s', '--shift',
        required=False,
        type=int,
        default=1,
        help='Сдвиг для шифра Цезаря (default: 1)'
    )
    parser.add_argument(
        '-k', '--key',
        required=False,
        type=str,
        default='b',
        help='Ключ для шифра Виженера (default: B)'
    )

    args = parser.parse_args()

    mode_: str = args.mode
    func_: str = args.func
    text_: str = args.text

    params = {
        'caesar': args.shift,
        'vigenere': args.key
    }

    cipher = Cipher()
    type_ = getattr(cipher, mode_)
    function_ = getattr(type_, func_)

    print(function_(*[_ for _ in [text_, params.get(func_)] if _]))
