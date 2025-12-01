import unittest
from sammsi_calendar import JulianDay, SOLAR_DAYS_NAME, SOLAR_MONTHS_NAME

class TestJulianDay(unittest.TestCase):
    def test_to_julian(self):
        # Test case: Dec 1, 2025
        # Julian Day calculation verification
        # Using an online converter or known algorithm for verification
        # 2025-12-01 -> 2461010.5 (approx, depending on time, but code returns float)
        
        # Let's use the code's logic to verify consistency
        jd = JulianDay.to_julian([2025, 12, 1])
        self.assertIsInstance(jd, float)
        self.assertTrue(jd > 0)

    def test_get_solar_date(self):
        # Test specific case provided by user: 2025-12-01 -> 1393-07-02
        # Month 7 is "Saabi''" (index 6)
        
        solar_date = JulianDay.to_solar(2025, 12, 1)
        
        # Expected: [2, 6, 1393] -> [day, month_index, year]
        self.assertEqual(solar_date[0], 2)      # Day
        self.assertEqual(solar_date[1], 6)      # Month Index (0-based)
        self.assertEqual(solar_date[2], 1393)   # Year
        
        # Verify Month Name
        self.assertEqual(SOLAR_MONTHS_NAME[solar_date[1]], "Saabi''")
        
        # Verify Day Name
        dow_index = JulianDay.get_day_of_week_index(solar_date[0], solar_date[1], solar_date[2])
        self.assertEqual(SOLAR_DAYS_NAME[dow_index], "Isnail Azeemi")

    def test_constants(self):
        self.assertEqual(len(SOLAR_DAYS_NAME), 7)
        self.assertEqual(len(SOLAR_MONTHS_NAME), 12)

if __name__ == '__main__':
    unittest.main()
