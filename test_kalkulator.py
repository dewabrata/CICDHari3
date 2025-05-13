import unittest
import kalkulator

class TestKalkulator(unittest.TestCase):

    def test_tambah(self):
        self.assertEqual(kalkulator.tambah(1, 2), 3)
        self.assertEqual(kalkulator.tambah(-1, 1), 0)
        self.assertEqual(kalkulator.tambah(-1, -1), -2)
        self.assertEqual(kalkulator.tambah(0, 0), 0)
        self.assertEqual(kalkulator.tambah(1.5, 2.5), 4.0)

    def test_kurang(self):
        self.assertEqual(kalkulator.kurang(2, 1), 1)
        self.assertEqual(kalkulator.kurang(-1, 1), -2)
        self.assertEqual(kalkulator.kurang(-1, -1), 0)
        self.assertEqual(kalkulator.kurang(0, 0), 0)
        self.assertEqual(kalkulator.kurang(2.5, 1.5), 1.0)

    def test_kali(self):
        self.assertEqual(kalkulator.kali(2, 3), 6)
        self.assertEqual(kalkulator.kali(-1, 1), -1)
        self.assertEqual(kalkulator.kali(-1, -1), 1)
        self.assertEqual(kalkulator.kali(0, 5), 0)
        self.assertEqual(kalkulator.kali(1.5, 2), 3.0)

    def test_bagi(self):
        self.assertEqual(kalkulator.bagi(6, 3), 2)
        self.assertEqual(kalkulator.bagi(-6, 3), -2)
        self.assertEqual(kalkulator.bagi(-6, -3), 2)
        self.assertEqual(kalkulator.bagi(0, 5), 0)
        self.assertEqual(kalkulator.bagi(5, 2), 2.5)
        with self.assertRaises(ValueError):
            kalkulator.bagi(10, 0)

if __name__ == '__main__':
    unittest.main()
