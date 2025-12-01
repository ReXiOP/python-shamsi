from shamsi import JulianDay, SOLAR_DAYS_NAME, SOLAR_MONTHS_NAME

def test_manual():
    print("--- Manual Test of Shamsi Calendar Package ---")
    
    # Test Date: December 1, 2025
    year, month, day = 2025, 12, 1
    print(f"\n1. Converting Gregorian Date: {year}-{month}-{day}")
    
    # Convert to Julian
    jd = JulianDay.to_julian([year, month, day])
    print(f"   Julian Day: {jd}")
    
    # Convert back to Solar Date
    solar_date = JulianDay.get_solar_date(jd)
    print(f"   Solar Date (Day, Month Index, Year): {solar_date}")
    
    # Interpret Solar Date
    s_day, s_month_idx, s_year = solar_date
    s_month_name = SOLAR_MONTHS_NAME[s_month_idx]
    print(f"   Formatted Solar Date: {s_day} {s_month_name} {s_year}")
    
    # Test Day of Week
    dow_index = JulianDay.get_day_of_week_index(s_day, s_month_idx, s_year)
    dow_name = SOLAR_DAYS_NAME[dow_index]
    print(f"   Day of Week: {dow_name}")

    print("\n--- Test Complete ---")

if __name__ == "__main__":
    test_manual()
