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

    def test_raises_error_if_all_arguments_are_not_provided_1(self):
        self.assertRaises(TypeError, get_footer_pagination)
    def test_raises_error_if_all_arguments_are_not_provided_2(self):
        self.assertRaises(TypeError, get_footer_pagination, current_page=5)
    def test_raises_error_if_all_arguments_are_not_provided_3(self):
        self.assertRaises(TypeError, get_footer_pagination, total_pages=10)
    def test_raises_error_if_all_arguments_are_not_provided_4(self):
        self.assertRaises(TypeError, get_footer_pagination, around=1)
    def test_raises_error_if_all_arguments_are_not_provided_5(self):
        self.assertRaises(TypeError, get_footer_pagination, boundaries=2)
    def test_raises_error_if_all_arguments_are_not_provided_6(self):
        self.assertRaises(TypeError, get_footer_pagination, current_page=5, total_pages=10)
    def test_raises_error_if_all_arguments_are_not_provided_7(self):
        self.assertRaises(TypeError, get_footer_pagination, around=1, boundaries=2)
    def test_raises_error_if_all_arguments_are_not_provided_8(self):
        self.assertRaises(TypeError, get_footer_pagination, current_page=5, boundaries=2)
    def test_raises_error_if_all_arguments_are_not_provided_9(self):
        self.assertRaises(TypeError, get_footer_pagination, total_pages=10, around=1)
    def test_raises_error_if_all_arguments_are_not_provided_10(self):
        self.assertRaises(TypeError, get_footer_pagination, current_page=5, total_pages=10, around=2)
    def test_raises_error_if_all_arguments_are_not_provided_11(self):
        self.assertRaises(TypeError, get_footer_pagination, total_pages=10, around=2, boundaries=1)

    def test_result_is_correct_for_edge_cases_1(self):
        self.assertEqual(get_footer_pagination(1, 1, 0, 0), [1])
    def test_result_is_correct_for_edge_cases_2(self):
        self.assertEqual(get_footer_pagination(2, 1, 0, 0), [1, '...'])
    def test_result_is_correct_for_edge_cases_3(self):
        self.assertEqual(get_footer_pagination(1000, 1, 2, 0), [1, 2, 3, '...'])
    def test_result_is_correct_for_edge_cases_4(self):
        self.assertEqual(get_footer_pagination(1000, 1, 1, 3), [1, 2, 3, '...', 998, 999, 1000])
    def test_result_is_correct_for_edge_cases_5(self):
        self.assertEqual(get_footer_pagination(1000, 1000, 1, 3), [1, 2, 3, '...', 998, 999, 1000])
    def test_result_is_correct_for_edge_cases_6(self):
        self.assertEqual(get_footer_pagination(100, 100, 0, 0), ['...', 100])
    def test_result_is_correct_for_edge_cases_7(self):
        self.assertEqual(get_footer_pagination(100, 100, 0, 1), [1, '...', 100])
    def test_result_is_correct_for_edge_cases_8(self):
        self.assertEqual(get_footer_pagination(100, 50, 0, 1), [1, '...', 50, '...', 100])
    def test_result_is_correct_for_edge_cases_9(self):
        self.assertEqual(get_footer_pagination(100, 100, 1, 0), ['...', 99, 100])
    def test_result_is_correct_for_edge_cases_10(self):
        self.assertEqual(get_footer_pagination(100, 100, 4, 5), [1, 2, 3, 4, 5, '...', 96, 97, 98, 99, 100])
    def test_result_is_correct_for_edge_cases_11(self):
        self.assertEqual(get_footer_pagination(10, 5, 3, 2), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_12(self):
        self.assertEqual(get_footer_pagination(10, 5, 20, 12), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_13(self):
        self.assertEqual(get_footer_pagination(10, 5, 9, 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_14(self):
        self.assertEqual(get_footer_pagination(10, 5, 1, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_15(self):
        self.assertEqual(get_footer_pagination(10, 5, 9, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_16(self):
        self.assertEqual(get_footer_pagination(1000, 500, 3, 2), [1, 2, '...', 497, 498, 499, 500, 501, 502, 503, '...', 999, 1000])
    def test_result_is_correct_for_edge_cases_17(self):
        self.assertEqual(get_footer_pagination(10, 4, 2, 2), [1, 2, 3, 4, 5, 6, '...', 9, 10])
    def test_result_is_correct_for_edge_cases_18(self):
        self.assertEqual(get_footer_pagination(15, 6, 3, 3), [1, 2, 3, 4, 5, 6, 7, 8, 9, '...', 13, 14, 15])
    def test_result_is_correct_for_edge_cases_19(self):
        self.assertEqual(get_footer_pagination(15, 7, 1, 3), [1, 2, 3, '...', 6, 7, 8, '...', 13, 14, 15])
    def test_result_is_correct_for_edge_cases_20(self):
        self.assertEqual(get_footer_pagination(10, 4, 10, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_21(self):
        self.assertEqual(get_footer_pagination(10, 10, 10, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_22(self):
        self.assertEqual(get_footer_pagination(20, 10, 1, 5), [1, 2, 3, 4, 5, '...', 9, 10, 11, '...', 16, 17, 18, 19, 20])
    def test_result_is_correct_for_edge_cases_23(self):
        self.assertEqual(get_footer_pagination(20, 10, 4, 1), [1, '...', 6, 7, 8, 9, 10, 11, 12, 13, 14, '...', 20])
    def test_result_is_correct_for_edge_cases_24(self):
        self.assertEqual(get_footer_pagination(600, 566, 0, 0), ['...', 566, '...'])
    def test_result_is_correct_for_edge_cases_25(self):
        self.assertEqual(get_footer_pagination(10, 5, 1, 1), [1, '...', 4, 5, 6, '...', 10])
    def test_result_is_correct_for_edge_cases_26(self):
        self.assertEqual(get_footer_pagination(10, 10, 0, 0), ['...', 10])
    def test_result_is_correct_for_edge_cases_27(self):
        self.assertEqual(get_footer_pagination(10, 10, 1, 0), ['...', 9, 10])
    def test_result_is_correct_for_edge_cases_28(self):
        self.assertEqual(get_footer_pagination(10, 10, 2, 0), ['...', 8, 9, 10])
    def test_result_is_correct_for_edge_cases_29(self):
        self.assertEqual(get_footer_pagination(10, 10, 5, 0), ['...', 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_30(self):
        self.assertEqual(get_footer_pagination(10, 10, 8, 0), ['...', 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_31(self):
        self.assertEqual(get_footer_pagination(10, 10, 9, 0), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_32(self):
        self.assertEqual(get_footer_pagination(10, 10, 10, 0), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_33(self):
        self.assertEqual(get_footer_pagination(10, 10, 0, 1), [1, '...', 10])
    def test_result_is_correct_for_edge_cases_34(self):
        self.assertEqual(get_footer_pagination(10, 10, 0, 2), [1, 2, '...', 9, 10])
    def test_result_is_correct_for_edge_cases_35(self):
        self.assertEqual(get_footer_pagination(10, 10, 0, 4), [1, 2, 3, 4, '...', 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_36(self):
        self.assertEqual(get_footer_pagination(10, 10, 0, 5), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_37(self):
        self.assertEqual(get_footer_pagination(10, 10, 0, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_38(self):
        self.assertEqual(get_footer_pagination(10, 10, 0, 8), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_39(self):
        self.assertEqual(get_footer_pagination(10, 10, 0, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_40(self):
        self.assertEqual(get_footer_pagination(10, 10, 0, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_41(self):
        self.assertEqual(get_footer_pagination(10, 10, 0, 15), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_42(self):
        self.assertEqual(get_footer_pagination(10, 10, 1, 1), [1, '...', 9, 10])
    def test_result_is_correct_for_edge_cases_43(self):
        self.assertEqual(get_footer_pagination(10, 10, 1, 2), [1, 2, '...', 9, 10])
    def test_result_is_correct_for_edge_cases_44(self):
        self.assertEqual(get_footer_pagination(10, 10, 1, 4), [1, 2, 3, 4, '...', 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_45(self):
        self.assertEqual(get_footer_pagination(10, 10, 1, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_46(self):
        self.assertEqual(get_footer_pagination(10, 10, 1, 8), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_47(self):
        self.assertEqual(get_footer_pagination(10, 10, 1, 9), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_48(self):
        self.assertEqual(get_footer_pagination(10, 10, 1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_49(self):
        self.assertEqual(get_footer_pagination(10, 10, 2, 1), [1, '...', 8, 9, 10])
    def test_result_is_correct_for_edge_cases_50(self):
        self.assertEqual(get_footer_pagination(10, 10, 5, 1), [1, '...', 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_51(self):
        self.assertEqual(get_footer_pagination(10, 10, 5, 2), [1, 2, '...', 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_52(self):
        self.assertEqual(get_footer_pagination(10, 10, 5, 3), [1, 2, 3, '...', 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_53(self):
        self.assertEqual(get_footer_pagination(10, 8, 4, 2), [1, 2, '...', 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_54(self):
        self.assertEqual(get_footer_pagination(10, 3, 4, 2), [1, 2, 3, 4, 5, 6, 7, '...', 9, 10])
    def test_result_is_correct_for_edge_cases_55(self):
        self.assertEqual(get_footer_pagination(10, 2, 4, 2), [1, 2, 3, 4, 5, 6, '...', 9, 10])
    def test_result_is_correct_for_edge_cases_56(self):
        self.assertEqual(get_footer_pagination(10, 1, 4, 2), [1, 2, 3, 4, 5, '...', 9, 10])
    def test_result_is_correct_for_edge_cases_57(self):
        self.assertEqual(get_footer_pagination(10, 1, 0, 0), [1, '...'])
    def test_result_is_correct_for_edge_cases_58(self):
        self.assertEqual(get_footer_pagination(10, 1, 1, 0), [1, 2, '...'])
    def test_result_is_correct_for_edge_cases_59(self):
        self.assertEqual(get_footer_pagination(10, 1, 4, 0), [1, 2, 3, 4, 5, '...'])
    def test_result_is_correct_for_edge_cases_60(self):
        self.assertEqual(get_footer_pagination(10, 1, 8, 0), [1, 2, 3, 4, 5, 6, 7, 8, 9, '...'])
    def test_result_is_correct_for_edge_cases_61(self):
        self.assertEqual(get_footer_pagination(10, 1, 9, 0), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_62(self):
        self.assertEqual(get_footer_pagination(10, 1, 0, 1), [1, '...', 10])
    def test_result_is_correct_for_edge_cases_63(self):
        self.assertEqual(get_footer_pagination(10, 1, 1, 6), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_result_is_correct_for_edge_cases_64(self):
        self.assertEqual(get_footer_pagination(10, 2, 0, 1), [1, 2, '...', 10])


if __name__ == '__main__':
    unittest.main()
