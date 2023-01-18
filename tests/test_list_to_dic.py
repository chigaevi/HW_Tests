from main import list_to_dic
from unittest import TestCase, main


class list_to_dic_test(TestCase):
    def test_equal_1(self):
        self.assertEqual(list_to_dic(['2018-01-01', 'yandex', 'cpc', 100]),{'2018-01-01': {'yandex': {'cpc': 100}}})

    def test_equal_2(self):
        self.assertEqual(list_to_dic(['1', '2', '3', '4']),{'1': {'2': {'3': '4'}}})

    def test_wrong_type_1(self):
        with self.assertRaises(TypeError) as e:
            list_to_dic(1, 10, 10)
            # list_to_dic([1, 10, 10])
        # print(e.exception.args)

    def test_wrong_type_2(self):
        with self.assertRaises(TypeError) as e:
            list_to_dic(1)
            # list_to_dic([10, '10', 10])
        # print(e.exception.args)


if __name__ == '__main__':
    main()

