from main import get_unique_num
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


if __name__ == '__main__':
    main()
