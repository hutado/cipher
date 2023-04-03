# -*- coding: utf-8 -*-

"""
Модуль дешифрования
"""

# internal
from core.encrypt import Encrypt


class Decrypt:
    """
    Класс дешифрования
    """

    @staticmethod
    def caesar(text: str, shift: int) -> str:
        """
        Шифр Цезаря

        Parameters
        ----------
        text : str
            Строка для дешифрования
        shift : int
            Сдвиг шифрования

        Returns
        -------
        result : str
            Расшифрованная строка
        """

        if not (text and shift):
            return text

        return Encrypt.caesar(text, -shift)

    @staticmethod
    def vigenere(text: str, key: str) -> str:
        """
        Шифр Виженера

        Parameters
        ----------
        text : str
            Строка для дешифрования
        key : int
            Ключ шифрования

        Returns
        -------
        result : str
            Расшифрованная строка
        """

        if not (text and key):
            return text

        return Encrypt.vigenere(text, key, True)

    @staticmethod
    def atbash(text: str) -> str:
        """
        Шифр Атбаш

        Parameters
        ----------
        text : str
            Строка для дешифрования

        Returns
        -------
        result : str
            Расшифрованная строка
        """

        if not text:
            return text

        return Encrypt.atbash(text)
