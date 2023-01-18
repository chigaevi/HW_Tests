from main import get_visits
from unittest import TestCase, main


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

if __name__ == '__main__':
    main()
