import io
import unittest
import unittest.mock
import functions


class TestApp(unittest.TestCase):

    def setUp(self):
        self.contact_number = '10'
        self.test_operator_names = ['Op_A', 'Op_B', 'Op_C']
        self.operator_a = {
            2: 0.9,
            3684: 4.2,
            76: 1.17,
            9620: 0.0,
            568: 0.15,
            4631: 0.15,
            4673: 0.9,
            46732: 1.1
        }
        self.operator_b = {
            1: 0.92,
            44: 0.0,
            46: 0.2,
            467: 1.0,
            48: 1.2
        }
        self.operators = [self.operator_a, self.operator_b]

    def test_get_contact_input(self):
        with unittest.mock.patch('builtins.input', return_value=self.contact_number):
            assert functions.get_contact_input() == self.contact_number
        with unittest.mock.patch('builtins.input', return_value=''):
            assert functions.get_contact_input() == -1

    def test_get_operator_name(self):
        self.assertEqual(functions.get_operator_name(1, self.test_operator_names), "Op_B")
        self.assertRaises(TypeError, functions.get_operator_name, 'sdg', self.test_operator_names)
        self.assertRaises(TypeError, functions.get_operator_name, 0.0, self.test_operator_names)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, contact_number, service_operators, service_operator_names, expected_output, mock_stdout):
        functions.find_cheapest(contact_number, service_operators, service_operator_names)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_find_cheapest(self):
        self.assert_stdout(-1, self.operators, self.test_operator_names,
                           'Please enter your contact number!\n')
        self.assert_stdout(-2, self.operators, self.test_operator_names,
                           'Please enter only numbers!\n')
        self.assert_stdout(' 88 8 ', self.operators, self.test_operator_names,
                           'There is no operator who provide services to the area code you dialed\n')
        self.assert_stdout('467325', self.operators, self.test_operator_names,
                           'The lowest cost for your call would be $ 1.0/min from "Op_B"\n')
        self.assert_stdout('9620', self.operators, self.test_operator_names,
                           'The lowest cost for your call would be $ 0.0/min from "Op_A"\n')


if __name__ == '__main__':
    unittest.main()
