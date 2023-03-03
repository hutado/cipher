import unittest

from core.encrypt import Encrypt
from core.decrypt import Decrypt


class TestEncrypt(unittest.TestCase):

    def test_caesar(self):
        """
        Тест шифра Цезаря
        """

        self.assertEqual(Encrypt.caesar(None, 1), None)
        self.assertEqual(Encrypt.caesar('A', None), 'A')
        self.assertEqual(Encrypt.caesar(None, None), None)
        # Тест английского текста
        self.assertEqual(Encrypt.caesar('A', 1), 'B')
        self.assertEqual(Encrypt.caesar('a', 1), 'b')
        self.assertEqual(Encrypt.caesar('Z', 1), 'A')
        self.assertEqual(Encrypt.caesar('z', 1), 'a')
        self.assertEqual(Encrypt.caesar('A', 2), 'C')
        self.assertEqual(Encrypt.caesar('a', 25), 'z')
        self.assertEqual(Encrypt.caesar('a', 26), 'a')
        self.assertEqual(Encrypt.caesar('Python', 1), 'Qzuipo')
        self.assertEqual(Encrypt.caesar('Python3.6', 1), 'Qzuipo4.7')
        self.assertEqual(Encrypt.caesar('Python the best language', 1), 'Qzuipo uif cftu mbohvbhf')
        # Тест цифр и числел
        self.assertEqual(Encrypt.caesar('1', 1), '2')
        self.assertEqual(Encrypt.caesar('9', 1), '0')
        self.assertEqual(Encrypt.caesar('1', 9), '0')
        self.assertEqual(Encrypt.caesar('19', 1), '20')
        self.assertEqual(Encrypt.caesar('91', 1), '02')
        # Тест русского текста
        self.assertEqual(Encrypt.caesar('А', 1), 'Б')
        self.assertEqual(Encrypt.caesar('а', 1), 'б')
        self.assertEqual(Encrypt.caesar('Я', 1), 'А')
        self.assertEqual(Encrypt.caesar('я', 1), 'а')
        self.assertEqual(Encrypt.caesar('А', 32), 'Я')
        self.assertEqual(Encrypt.caesar('А', 33), 'А')
        self.assertEqual(Encrypt.caesar('Ё', 1), 'Ж')
        self.assertEqual(Encrypt.caesar('ё', 1), 'ж')
        self.assertEqual(Encrypt.caesar('Пайтон', 1), 'Рбкупо')
        self.assertEqual(Encrypt.caesar('Пайтон3.6', 1), 'Рбкупо4.7')
        # Тест отрицательного сдвига
        self.assertEqual(Encrypt.caesar('a', -1), 'z')
        self.assertEqual(Encrypt.caesar('A', -1), 'Z')
        self.assertEqual(Encrypt.caesar('а', -1), 'я')
        self.assertEqual(Encrypt.caesar('А', -1), 'Я')
        # Тест пустой строки, пробелов и знаков препинания
        self.assertEqual(Encrypt.caesar('', 1), '')
        self.assertEqual(Encrypt.caesar('', -1), '')
        self.assertEqual(Encrypt.caesar(' ', 1), ' ')
        self.assertEqual(Encrypt.caesar(' ', -1), ' ')
        self.assertEqual(Encrypt.caesar('.,!@#$%^&*()\\|/', 1), '.,!@#$%^&*()\\|/')
        # Тест обоих языков в строке
        self.assertEqual(Encrypt.caesar('AА', 1), 'BБ')
        self.assertEqual(Encrypt.caesar('aа', -1), 'zя')

    def test_vigenere(self):
        """
        Тест шифра Виженера
        """

        self.assertEqual(Encrypt.vigenere(None, 'A'), None)
        self.assertEqual(Encrypt.vigenere('A', None), 'A')
        self.assertEqual(Encrypt.vigenere(None, None), None)
        self.assertEqual(Encrypt.vigenere('test', '.'), 'sdrs')
        # Тест английского языка
        self.assertEqual(Encrypt.vigenere('A', 'a'), 'A')
        self.assertEqual(Encrypt.vigenere('A', 'b'), 'B')
        self.assertEqual(Encrypt.vigenere('Z', 'b'), 'A')
        self.assertEqual(Encrypt.vigenere('Python', 'Key'), 'Zcrrsl')
        self.assertEqual(Encrypt.vigenere('Python3.6', 'Key'), 'Zcrrsl3.0')
        # Тест русского языка
        self.assertEqual(Encrypt.vigenere('А', 'а'), 'А')
        self.assertEqual(Encrypt.vigenere('А', 'б'), 'Б')
        self.assertEqual(Encrypt.vigenere('Пайтон', 'ключ'), 'Ълзйщщ')
        self.assertEqual(Encrypt.vigenere('Пайтон3.6', 'ключ'), 'Ълзйщщ4.7')
        # Тест пустой строки, пробелов и знаков препинания
        self.assertEqual(Encrypt.vigenere('', ''), '')
        self.assertEqual(Encrypt.vigenere('', 'key'), '')
        self.assertEqual(Encrypt.vigenere('', 'ключ'), '')
        self.assertEqual(Encrypt.vigenere(' ', 'key'), ' ')
        self.assertEqual(Encrypt.vigenere('.,!@#$%^&*()\\|/', 'key'), '.,!@#$%^&*()\\|/')
        # Тест разных языков в тексте и ключе
        self.assertEqual(Encrypt.vigenere('Python3.6', 'ключ'), 'Akyfzz4.7')
        self.assertEqual(Encrypt.vigenere('Пайтон3.6', 'key'), 'Щдбьте3.0')
        self.assertEqual(Encrypt.vigenere('Pайтон3.6', 'kлюч'), 'Zлзйшщ4.6')


class TestDecrypt(unittest.TestCase):

    def test_caesar(self):
        """
        Тест шифра Цезаря
        """

        self.assertEqual(Decrypt.caesar(None, 1), None)
        self.assertEqual(Decrypt.caesar('A', None), 'A')
        self.assertEqual(Decrypt.caesar(None, None), None)
        # Тест английского текста
        self.assertEqual(Decrypt.caesar('B', 1), 'A')
        self.assertEqual(Decrypt.caesar('b', 1), 'a')
        self.assertEqual(Decrypt.caesar('A', 1), 'Z')
        self.assertEqual(Decrypt.caesar('a', 1), 'z')
        self.assertEqual(Decrypt.caesar('C', 2), 'A')
        self.assertEqual(Decrypt.caesar('z', 25), 'a')
        self.assertEqual(Decrypt.caesar('a', 26), 'a')
        self.assertEqual(Decrypt.caesar('Qzuipo', 1), 'Python')
        self.assertEqual(Decrypt.caesar('Qzuipo4.7', 1), 'Python3.6')
        self.assertEqual(Decrypt.caesar('Qzuipo uif cftu mbohvbhf', 1), 'Python the best language')
        # Тест цифр и числел
        self.assertEqual(Decrypt.caesar('2', 1), '1')
        self.assertEqual(Decrypt.caesar('0', 1), '9')
        self.assertEqual(Decrypt.caesar('0', 9), '1')
        self.assertEqual(Decrypt.caesar('20', 1), '19')
        self.assertEqual(Decrypt.caesar('02', 1), '91')
        # Тест русского текста
        self.assertEqual(Decrypt.caesar('Б', 1), 'А')
        self.assertEqual(Decrypt.caesar('б', 1), 'а')
        self.assertEqual(Decrypt.caesar('А', 1), 'Я')
        self.assertEqual(Decrypt.caesar('а', 1), 'я')
        self.assertEqual(Decrypt.caesar('Я', 32), 'А')
        self.assertEqual(Decrypt.caesar('А', 33), 'А')
        self.assertEqual(Decrypt.caesar('Ж', 1), 'Ё')
        self.assertEqual(Decrypt.caesar('ж', 1), 'ё')
        self.assertEqual(Decrypt.caesar('Рбкупо', 1), 'Пайтон')
        self.assertEqual(Decrypt.caesar('Рбкупо4.7', 1), 'Пайтон3.6')
        # Тест отрицательного сдвига
        self.assertEqual(Decrypt.caesar('z', -1), 'a')
        self.assertEqual(Decrypt.caesar('Z', -1), 'A')
        self.assertEqual(Decrypt.caesar('я', -1), 'а')
        self.assertEqual(Decrypt.caesar('Я', -1), 'А')
        # Тест пустой строки, пробелов и знаков препинания
        self.assertEqual(Decrypt.caesar('', 1), '')
        self.assertEqual(Decrypt.caesar('', -1), '')
        self.assertEqual(Decrypt.caesar(' ', 1), ' ')
        self.assertEqual(Decrypt.caesar(' ', -1), ' ')
        self.assertEqual(Decrypt.caesar('.,!@#$%^&*()\\|/', 1), '.,!@#$%^&*()\\|/')
        # Тест обоих языков в строке
        self.assertEqual(Decrypt.caesar('BБ', 1), 'AА')
        self.assertEqual(Decrypt.caesar('zя', -1), 'aа')

    def test_vigenere(self):
        """
        Тест шифра Виженера
        """

        self.assertEqual(Decrypt.vigenere(None, 'A'), None)
        self.assertEqual(Decrypt.vigenere('A', None), 'A')
        self.assertEqual(Decrypt.vigenere(None, None), None)
        self.assertEqual(Encrypt.vigenere('test', '.'), 'sdrs')
        # Тест английского языка
        self.assertEqual(Decrypt.vigenere('A', 'a'), 'A')
        self.assertEqual(Decrypt.vigenere('B', 'b'), 'A')
        self.assertEqual(Decrypt.vigenere('A', 'b'), 'Z')
        self.assertEqual(Decrypt.vigenere('Zcrrsl', 'Key'), 'Python')
        self.assertEqual(Decrypt.vigenere('Zcrrsl3.0', 'Key'), 'Python3.6')
        # Тест русского языка
        self.assertEqual(Decrypt.vigenere('А', 'а'), 'А')
        self.assertEqual(Decrypt.vigenere('Б', 'б'), 'А')
        self.assertEqual(Decrypt.vigenere('Ълзйщщ', 'ключ'), 'Пайтон')
        self.assertEqual(Decrypt.vigenere('Ълзйщщ4.7', 'ключ'), 'Пайтон3.6')
        # Тест пустой строки, пробелов и знаков препинания
        self.assertEqual(Decrypt.vigenere('', ''), '')
        self.assertEqual(Decrypt.vigenere('', 'key'), '')
        self.assertEqual(Decrypt.vigenere('', 'ключ'), '')
        self.assertEqual(Decrypt.vigenere(' ', 'key'), ' ')
        self.assertEqual(Decrypt.vigenere('.,!@#$%^&*()\\|/', 'key'), '.,!@#$%^&*()\\|/')
        # Тест разных языков в тексте и ключе
        self.assertEqual(Decrypt.vigenere('Akyfzz4.7', 'ключ'), 'Python3.6')
        self.assertEqual(Decrypt.vigenere('Щдбьте3.0', 'key'), 'Пайтон3.6')
        self.assertEqual(Decrypt.vigenere('Zлзйшщ4.6', 'kлюч'), 'Pайтон3.6')


if __name__ == '__main__':
    unittest.main()
