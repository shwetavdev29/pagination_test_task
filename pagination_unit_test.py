import unittest
from pagination_test_task_solution import get_footer_pagination


class TestFooterPagination(unittest.TestCase):

    def test_raises_value_error_if_variable_is_not_integer(self):
        random_float = 1.5
        random_string = 'hello'
        boolean = True
        string_number = '7'
        self.assertRaises(TypeError, get_footer_pagination, current_page=random_float,
                          total_pages=random_string, around=boolean, boundaries=string_number)

    def test_raises_error_if_variables_are_negative_numbers(self):
        negative_number = -1
        self.assertRaises(ValueError, get_footer_pagination, current_page=negative_number,
                          total_pages=negative_number, around=negative_number, boundaries=negative_number)

    def test_raises_error_if_current_or_total_pages_is_equal_to_zero(self):
        self.assertRaises(ValueError, get_footer_pagination, current_page=0, total_pages=0,
                          around=0, boundaries=0)

    def test_raises_error_if_current_page_is_larger_than_total_pages(self):
        self.assertRaises(ValueError, get_footer_pagination, current_page=5, total_pages=4,
                          around=0, boundaries=0)

    def test_raises_error_if_all_arguments_are_not_provided(self):
        self.assertRaises(TypeError, get_footer_pagination)
        self.assertRaises(TypeError, get_footer_pagination, current_page=5)
        self.assertRaises(TypeError, get_footer_pagination, total_pages=10)
        self.assertRaises(TypeError, get_footer_pagination, around=1)
        self.assertRaises(TypeError, get_footer_pagination, boundaries=2)
        self.assertRaises(TypeError, get_footer_pagination, current_page=5, total_pages=10)
        self.assertRaises(TypeError, get_footer_pagination, around=1, boundaries=2)
        self.assertRaises(TypeError, get_footer_pagination, current_page=5, boundaries=2)
        self.assertRaises(TypeError, get_footer_pagination, total_pages=10, around=1)
        self.assertRaises(TypeError, get_footer_pagination, current_page=5, total_pages=10, around=2)
        self.assertRaises(TypeError, get_footer_pagination, total_pages=10, around=2, boundaries=1)

    def test_result_is_correct_for_edge_cases(self):
        self.assertEqual(get_footer_pagination(1, 1, 0, 0), [1])
        self.assertEqual(get_footer_pagination(2, 1, 0, 0), [1, '...'])
        self.assertEqual(get_footer_pagination(1000, 1, 2, 0), [1, 2, 3, '...'])
        self.assertEqual(get_footer_pagination(1000, 1, 1, 3), [1, 2, 3, '...', 998, 999, 1000])
        self.assertEqual(get_footer_pagination(1000, 1000, 1, 3), [1, 2, 3, '...', 998, 999, 1000])
        self.assertEqual(get_footer_pagination(100, 100, 0, 0), ['...', 100])
        self.assertEqual(get_footer_pagination(100, 100, 0, 1), [1, '...', 100])
        self.assertEqual(get_footer_pagination(100, 50, 0, 1), [1, '...', 50, '...', 100])
        self.assertEqual(get_footer_pagination(100, 100, 1, 0), ['...', 99, 100])
        self.assertEqual(get_footer_pagination(100, 100, 4, 5), [1, 2, 3, 4, 5, '...', 96, 97, 98, 99, 100])
        self.assertEqual(get_footer_pagination(10, 5, 3, 2), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(get_footer_pagination(10, 5, 20, 12), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(get_footer_pagination(10, 5, 9, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(get_footer_pagination(10, 5, 1, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(get_footer_pagination(10, 5, 9, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(get_footer_pagination(1000, 500, 3, 2), [1, 2, '...', 497, 498, 499, 500, 501, 502, 503, '...', 999, 1000])
        self.assertEqual(get_footer_pagination(10, 4, 2, 2), [1, 2, 3, 4, 5, 6, '...', 9, 10])
        self.assertEqual(get_footer_pagination(15, 6, 3, 3), [1, 2, 3, 4, 5, 6, 7, 8, 9, '...', 13, 14, 15])
        self.assertEqual(get_footer_pagination(15, 7, 1, 3), [1, 2, 3, '...', 6, 7, 8, '...', 13, 14, 15])
        self.assertEqual(get_footer_pagination(10, 4, 10, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(get_footer_pagination(10, 10, 10, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(get_footer_pagination(20, 10, 1, 5), [1, 2, 3, 4, 5, '...', 9, 10, 11, '...', 16, 17, 18, 19, 20])
        self.assertEqual(get_footer_pagination(20, 10, 4, 1), [1, '...', 6, 7, 8, 9, 10, 11, 12, 13, 14, '...', 20])
        self.assertEqual(get_footer_pagination(600, 566, 0, 0), ['...', 566, '...'])
        self.assertEqual(get_footer_pagination(10, 5, 1, 1), [1, '...', 4, 5, 6, '...', 10])


if __name__ == '__main__':
    unittest.main()
