from HW_task_1 import get_unique_num, get_visits, list_to_dic, max_sales, per_of_search_queries
from HW_task_2 import ya_disk, get_token_ya_ru
from unittest import TestCase, main


#
# class get_unique_num_test(TestCase):
#
#     def test_equal(self):
#         self.assertEqual(get_unique_num({'u1': [10, 1, 3],
#                                          'u2': [3, 7, 11001]
#                                          }
#                                         ),
#                          [1,3,7,10,11001])
#
#     def test_wrong_type(self):
#         with self.assertRaises(TypeError) as e:
#             get_unique_num(1, 10, 10)
#             # get_unique_num({'u1': [10, 1],'u2': [3, 7]})
#         print(e.exception.args)
#
#
# class vists_get_test(TestCase):
#
#     def test_equal_1(self):
#         self.assertEqual(get_visits(
#             [   {'visit1': ['Москва', 'Россия']},
#                 {'visit2': ['Дели', 'Индия']}
#             ],
#             'Россия'), ['visit1'])
#
#     def test_equal_2(self):
#         self.assertEqual(get_visits(
#             [
#                 {'visit4': ['Лиссабон', 'Португалия']},
#                 {'visit5': ['Париж', 'Франция']}
#             ],
#             'Россия'), [])
#
#     def test_wrong_type(self):
#         with self.assertRaises(TypeError):
#             get_visits(1, 'Португалия')
#             # get_visits([{'visit4': ['Лиссабон', 'Португалия']}, {'visit1': ['Москва', 'Россия']}],'Россия')
#             # get_visits([{'visit4': ['Лиссабон', 'Португалия']}], 1)
#
#     def test_wrong_Attribute(self):
#         with self.assertRaises(AttributeError):
#             get_visits('1', 'Португалия')
#             # get_visits([{'visit4': ['Лиссабон', 'Португалия']}],'Россия')
#
#
# class list_to_dic_test(TestCase):
#     def test_equal_1(self):
#         self.assertEqual(list_to_dic(['2018-01-01', 'yandex', 'cpc', 100]),{'2018-01-01': {'yandex': {'cpc': 100}}})
#
#     def test_equal_2(self):
#         self.assertEqual(list_to_dic(['1', '2', '3', '4']),{'1': {'2': {'3': '4'}}})
#
#     def test_wrong_type_1(self):
#         with self.assertRaises(TypeError) as e:
#             list_to_dic(1, 10, 10)
#             # list_to_dic([1, 10, 10])
#         # print(e.exception.args)
#
#     def test_wrong_type_2(self):
#         with self.assertRaises(TypeError) as e:
#             list_to_dic(1)
#             # list_to_dic([10, '10', 10])
#         # print(e.exception.args)
#
#
# class max_sales_test(TestCase):
#
#     def test_equal(self):
#         stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
#         self.assertEqual(max_sales(stats), 'yandex')
#
#     def test_wrong_type(self):
#         with self.assertRaises(TypeError) as e:
#             max_sales(1, 1)
#         # print(f'test_wrong_type def max_sales --> {e.exception.args[0]}')
#
#     def test_wrong_type_2(self):
#         with self.assertRaises(TypeError) as e:
#             max_sales([],[])
#         # print(f'test_wrong_type_2 def max_sales --> {e.exception.args[0]}')
#
#     def test_wrong_Attribute(self):
#         with self.assertRaises(AttributeError) as e:
#             max_sales(1)
#         # print(f'test_wrong_Attribute def max_sales --> {e.exception.args[0]}')
#
#     def test_args_not_none(self):
#         stats = {None: 55}
#         self.assertIsNone(max_sales(stats))
#
#
# class per_of_search_queries_test(TestCase):
#     def test_equal(self):
#         stats = ['слово', 'слово', 'слово']
#         self.assertEqual(per_of_search_queries(stats), {1:100})
#
#     def test_equal_(self):
#         stats = ['слово', 'два слова', 'это три слова']
#         self.assertEqual(per_of_search_queries(stats), {1: 33,2:33,3:33})
#
#     def test_wrong_type(self):
#         for arg in (1, 10, 1000):
#             with self.assertRaises(TypeError) as e:
#                 per_of_search_queries(arg)
#             # print(f'test_wrong_type def per_of_search_queries --> {e.exception.args[0]}')

class ya_disk_test(TestCase):

    def test_existed_folder(self):
        path = 'new_folder'
        self.assertEqual(ya_disk(get_token_ya_ru()).getInfo(path), 200)
        self.assertNotEqual(ya_disk(get_token_ya_ru()).create_folder(path), 201)

    def test_created_folder(self):
        path = 'new_folder'
        # ya_disk(get_token_ya_ru()).del_folder(path)
        self.assertEqual(ya_disk(get_token_ya_ru()).create_folder(path), 201)



if __name__ == '__main__':
    main()
