import unittest
import datetime

from birthday import berechnung_alter

class Testbirthday(unittest.TestCase):
   
    def test_calculated_age_day(self):
        birthday = datetime.datetime.strptime("22.01.2000","%d.%m.%Y")
        today = datetime.datetime.strptime("22.02.2022", "%d.%m.%Y")
        result = berechnung_alter(birthday,today)
        self.assertEqual(result,22)
    def test_calculated_age_day2(self):
        birthday = datetime.datetime.strptime("22.05.2000","%d.%m.%Y")
        today = datetime.datetime.strptime("22.02.2022", "%d.%m.%Y")
        result = berechnung_alter(birthday,today)
        self.assertEqual(result,21)
    

if __name__ == '__main__':
    unittest.main()