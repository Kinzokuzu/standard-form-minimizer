import unittest
from lib import boolfunc as bf
from lib import cbuilder as cb 

class TestCBuilderFunctions(unittest.TestCase):
    def test_write_description(self):
        test_string = "AB\'"

        expected_string = "// implementation of AB\'\n"

        result_string = cb.write_description(test_string)

        self.assertEqual(result_string, expected_string)


    def test_write_inputs(self):
        test_inputs = ['A','B']

        expected_string = """// inputs\n
                             input A;\n
                             input B;\n"""

        result_string = cb.write_inputs(test_inputs)

        self.assertEqual(result_string, expected_string)

    def test_write_outputs(self):
        test_outputs = ['F']

        expected_string = """// outputs\n
                             output F;\n"""

        result_string = cb.write_outputs(test_outputs)

        self.assertEqual(result_string, expected_string)


if __name__ == '__main__':
    pass
