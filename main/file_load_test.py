import unittest
import file_load as p

class test_data_load(unittest.TestCase):
    def setUp(self):
        self.file_count = 12
        self.array = self.array_setup(self.file_count)

    def test_pandas_module_check(self):
        import numpy
        import matplotlib

    def array_setup(self,file_count):
        f = p.file_load(file_count)
        return f.total_data

    def test_data_population(self):
        if len(self.array) == 0:
            assert False

    def test_array_shape(self):
        x=40
        y=60*self.file_count
        expected_shape = (y,x)
        actual_shape = self.array.shape
        self.assertEqual( expected_shape, actual_shape)

if __name__ == '__main__':
    unittest.main()

