from unittest import TestCase
from unittest.mock import patch
import calc

class TestCalculator(TestCase):
    def test_should_raise_exception_if_input_is_not_a_number(self):
        calculator=calc.Calculator()
        first='a'
        second=15
        self.assertRaises(calc.NotANumber(),calculator.Add(first,second))
        self.assertRaises(calc.NotANumber(), calculator.Add(second,first))
        self.assertRaises(calc.NotANumber(), calculator.Add(first, first))
        self.assertRaises(calc.NotANumber(), calculator.Sub(first, second))
        self.assertRaises(calc.NotANumber(), calculator.Sub(second, first))
        self.assertRaises(calc.NotANumber(), calculator.Sub(first, first))
        self.assertRaises(calc.NotANumber(), calculator.Multiply(first, second))
        self.assertRaises(calc.NotANumber(), calculator.Multiply(second, first))
        self.assertRaises(calc.NotANumber(), calculator.Multiply(first, first))
        self.assertRaises(calc.NotANumber(), calculator.Div(first, second))
        self.assertRaises(calc.NotANumber(), calculator.Div(second, first))
        self.assertRaises(calc.NotANumber(), calculator.Div(first, first))
        self.assertRaises(calc.NotANumber(), calculator.Derivative(first, first))
    def test_should_raise_exception_if_input_for_derivate_is_not_a_string(self):
        calculator=calc.Calculator()
        func = 15
        order = 2
        self.assertRaises(calc.NotAString(), calculator.Derivative(func,order))
    def test_should_raise_exception_if_denominator_for_Div_is_zero(self):
        calculator=calc.Calculator()
        first = 0
        self.assertRaises(calc.DenominatorIsZero(),calculator.Div(first,first))
    @patch('numpy.derivative',return_value='a')
    def test_should_derivative_return_correct_result_for_integer_and_string_as_input(self):
        expected_output='a'
        calculator=calc.Calculator()
        assertEqual(calculator.Derivative(),expected_output)
    def test_should_add_return_correct_sum_for_integer_values_as_input(self):
        calculator=calc.Calculator()
        first=10
        second=2
        expected_sum=12
        self.assertEqual(calculator.Add(first,second),expected_sum)
    def test_should_add_return_correct_sum_for_float_values_as_input(self):
        calculator=calc.Calculator()
        first=10.1
        second=2.1
        expected_sum=12.2
        self.assertAlmostEqual(calculator.Add(first,second),expected_sum)
    def test_should_sub_return_correct_result_for_integer_values_as_input(self):
        calculator=calc.Calculator()
        first=10
        second=2
        expected_sum=8
        self.assertEqual(calculator.Sub(first,second),expected_sum)
    def test_should_sub_return_correct_result_for_float_values_as_input(self):
        calculator=calc.Calculator()
        first=10.1
        second=2.1
        expected_sum=8.0
        self.assertAlmostEqual(calculator.Sub(first,second),expected_sum)
    def test_should_multiply_return_correct_result_for_integer_values_as_input(self):
        calculator=calc.Calculator()
        first=10
        second=2
        expected_sum=20
        self.assertEqual(calculator.Sub(first,second),expected_sum)
    def test_should_multiply_return_correct_result_for_float_values_as_input(self):
        calculator=calc.Calculator()
        first=10.0
        second=2.0
        expected_sum=20.0
        self.assertAlmostEqual(calculator.Sub(first,second),expected_sum)
    def test_should_div_return_correct_result_for_integer_values_as_input(self):
        calculator=calc.Calculator()
        first=10
        second=2
        expected_sum=5
        self.assertEqual(calculator.Sub(first,second),expected_sum)
    def test_should_div_return_correct_result_for_float_values_as_input(self):
        calculator=calc.Calculator()
        first=10.0
        second=2.0
        expected_sum=5.0
        self.assertAlmostEqual(calculator.Sub(first,second),expected_sum)


if __name__ == '__main__':
    TestCase.main()
