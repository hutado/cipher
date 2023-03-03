# -*- coding: utf-8 -*-

"""
Модуль шифрования
"""

EN_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
RU_ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
EN_LEN = len(EN_ALPHABET)
RU_LEN = len(RU_ALPHABET)


class Encrypt:
    """
    Класс шифрования
    """

    @staticmethod
    def caesar(text: str, shift: int) -> str:
        """
        Шифр Цезаря

        Parameters
        ----------
        text : str
            Строка для шифрования
        shift : int
            Сдвиг шифрования

        Returns
        -------
        result : str
            Зашифрованная строка
        """

        if not (text and shift):
            return text

        result = ''

        for letter in text:
            if letter.isdigit():
                result += str((int(letter) + shift) % 10)

            elif letter.isalpha():
                en = letter.upper() in EN_ALPHABET
                len_ = EN_LEN if en else RU_LEN
                alphabet = EN_ALPHABET if en else RU_ALPHABET

                if (letter.isupper()):
                    result += alphabet[(alphabet.find(letter) + shift) % len_]

                else:
                    alphabet = alphabet.lower()
                    result += alphabet[(alphabet.find(letter) + shift) % len_]

            else:
                result += letter

        return result

    @staticmethod
    def vigenere(text: str, key: str, decrypt: bool=False) -> str:
        """
        Шифр Виженера

        Parameters
        ----------
        text : str
            Строка для шифрования
        key : str
            Ключ для шифрования

        Returns
        -------
        result : str
            Зашифрованная строка
        """

        if not (text and key):
            return text

        result = ''
        key = key.upper()

        for i, letter in enumerate(text):
            key_letter = key[i % len(key)]
            shift = EN_ALPHABET.find(key_letter) if key_letter in EN_ALPHABET else RU_ALPHABET.find(key_letter)
            shift = -shift if decrypt else shift
            result += Encrypt.caesar(letter, shift)

        return result

    @staticmethod
    def atbash(text:str) -> str:
        """
        Шифр Атбаш

        Parameters
        ----------
        text : str
            Строка для шифрования

        Returns
        -------
        result : str
            Зашифрованная строка
        """

        if not text:
            return text

        result = ''

        for letter in text:
            if letter.isalpha():
                en = letter.upper() in EN_ALPHABET
                len_ = EN_LEN if en else RU_LEN
                alphabet = EN_ALPHABET if en else RU_ALPHABET

                if (letter.isupper()):
                    result += alphabet[len_ - alphabet.find(letter) - 1]

                else:
                    alphabet = alphabet.lower()
                    result += alphabet[len_ - alphabet.find(letter) - 1]

            else:
                result += letter

        return result
