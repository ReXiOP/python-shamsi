from sammsi_calendar import JulianDay, SOLAR_DAYS_NAME, SOLAR_MONTHS_NAME

def debug_conversion():
    print("--- Debugging Conversion for 2025-12-01 ---")
    
    g_year, g_month, g_day = 2025, 12, 1
    
    # 1. Get Julian Day
    jd = JulianDay.to_julian([g_year, g_month, g_day])
    print(f"Julian Day: {jd}")
    
    # 2. Get Total Days (Epoch Days)
    # This is what get_solar_date likely expects
    epoch_days = JulianDay.get_total_day_upto_curr_date(g_year, g_month, g_day)
    print(f"Epoch Days (JD - 1952043.0): {epoch_days}")
    
    # 3. Convert to Solar Date using Epoch Days
    solar_date = JulianDay.get_solar_date(epoch_days)
    print(f"Solar Date (from Epoch Days): {solar_date}")
    
    s_day, s_month_idx, s_year = solar_date
    print(f"Parsed: Year {s_year}, Month {s_month_idx + 1} ({SOLAR_MONTHS_NAME[s_month_idx]}), Day {s_day}")
    
    # 4. Check Day of Week
    # User expects "Isnail Azeemi" (Index 0)
    # Note: get_day_of_week_index takes (real_day, real_month, real_year)
    # real_month is 0-based index
    dow_idx = JulianDay.get_day_of_week_index(s_day, s_month_idx, s_year)
    print(f"Day of Week Index: {dow_idx} ({SOLAR_DAYS_NAME[dow_idx]})")

if __name__ == "__main__":
    debug_conversion()
