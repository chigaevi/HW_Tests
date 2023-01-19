from main import get_unique_num
from main import get_visits
from main import list_to_dic
from unittest import TestCase, main


class get_unique_num_test(TestCase):

    def test_equal(self):
        self.assertEqual(get_unique_num({'u1': [10, 1, 3],
                                         'u2': [3, 7, 11001]
                                         }
                                        ),
                         [1,3,7,10,11001])

    def test_wrong_type(self):
        with self.assertRaises(TypeError) as e:
            get_unique_num(1, 10, 10)
            # get_unique_num({'u1': [10, 1],'u2': [3, 7]})
        print(e.exception.args)


class vists_get_test(TestCase):

    def test_equal_1(self):
        self.assertEqual(get_visits(
            [   {'visit1': ['Москва', 'Россия']},
                {'visit2': ['Дели', 'Индия']}
            ],
            'Россия'), ['visit1'])

    def test_equal_2(self):
        self.assertEqual(get_visits(
            [
                {'visit4': ['Лиссабон', 'Португалия']},
                {'visit5': ['Париж', 'Франция']}
            ],
            'Россия'), [])

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            get_visits(1, 'Португалия')
            # get_visits([{'visit4': ['Лиссабон', 'Португалия']}, {'visit1': ['Москва', 'Россия']}],'Россия')
            # get_visits([{'visit4': ['Лиссабон', 'Португалия']}], 1)

    def test_wrong_Attribute(self):
        with self.assertRaises(AttributeError):
            get_visits('1', 'Португалия')
            # get_visits([{'visit4': ['Лиссабон', 'Португалия']}],'Россия')


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
