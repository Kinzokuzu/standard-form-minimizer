import unittest
from lib import shuntingyard as sy

class TestShuntingYardFunctions(unittest.TestCase):
    def test_shunting_yard_easy(self):
        test_string = "F = AB'"
        
        expected_rpn = ["F","A","!B","and"]

        rpn = sy.shunting_yard(test_string)

        self.assertEqual(rpn, expected_rpn)


    def test_shunting_yard_hard(self):
        test_string = "F = AB' + A'B"
        
        expected_rpn = ["F","A","!B","!A","B","and","and","or"]

        rpn = sy.shunting_yard(test_string)

        self.assertEqual(rpn, expected_rpn)


    def test_get_inputs_outputs(self):
        test_string = "F(A,B,C)"

        expected_inputs = ['A','B','C']
        expected_outputs = ['F']

        inputs, outputs = sy.get_inputs_outputs(test_string)

        self.assertEqual(inputs, expected_inputs)
        self.assertEqual(outputs, expected_outputs)

if __name__ == '__main__':
    main()
