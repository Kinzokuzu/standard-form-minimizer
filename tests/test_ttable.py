import unittest
from lib import ttable as tt

class TestTTableFunctions(unittest.TestCase):
    def test_generate_table_easy(self):
        test_inputs = ['A','B']
        test_outputs = ['F']

        expected_table = [['A','B','|','F'],
                          ['0','0','|','0'],
                          ['0','1','|','0'],
                          ['1','0','|','0'],
                          ['1','1','|','0'],]

        generated_table = tt.generate_table(test_inputs, test_outputs)

        self.assertEqual(generated_table, expected_table)

if __name__ == '__main__':
    main()
