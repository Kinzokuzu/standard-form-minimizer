import unittest
from lib import shuntingyard as sy

class TestShuntingYardFunctions(unittest.TestCase):
    def test_get_inputs_outputs(self):
        test_string = "F(A,B,C)"

        expected_inputs = ['A','B','C']
        expected_outputs = ['F']

        inputs, outputs = sy.get_inputs_outputs(test_string)

        self.assertEqual(inputs, expected_inputs)
        self.assertEqual(outputs, expected_outputs)

if __name__ == '__main__':
    main()
