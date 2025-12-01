SOLAR_DAYS_NAME = [
    "Isnail Azeemi", "Sulasaie", "Arbiaye", "Khamis", "Jumuati", "Sabti", "Ahadi"
]

SOLAR_MONTHS_NAME = [
    "Awal", "Saanee", "Saalis", "Rwaabi''", "Khawaamis", "Saadis", "Saabi''", 
    "Saamin", "Taasi''", "'Aashir", "Hadi 'Ashir", "Saanee 'Ashir"
]

import math

class JulianDay:
    HALFSECOND = 0.5
    JGREG = 588829
    uptoFstDate = 1952043.0

    @staticmethod
    def to_julian(i_arr):
        """
        Converts a Gregorian date [year, month, day] to Julian Day Number.
        """
        i = i_arr[0] # year
        i2 = i_arr[1] # month
        i3 = i_arr[2] # day
        
        if i2 == 1 or i2 == 2:
            i -= 1
            i2 += 12
        
        i4 = i // 100
        i5 = (2 - i4) + (i4 // 4)
        
        # Dart: ((i5 + i3) + ((i + 4716) * 365.25).floorToDouble()) + ((i2 + 1) * 30.6001).floorToDouble() - 1524.0
        term1 = i5 + i3
        term2 = math.floor((i + 4716) * 365.25)
        term3 = math.floor((i2 + 1) * 30.6001)
        
        return float(term1 + term2 + term3 - 1524.0)

    @staticmethod
    def get_solar_date(d):
        """
        Converts a value (derived from Julian Day) to [day, month_index, year].
        """
        i = 0
        i2 = int(d) - 365
        i3 = i2 - ((i2 - 13140) // 1461)
        
        # Dart: int i4 = (d - ((i3 / 1460) - (i3 / 46720))).toInt();
        val = (i3 / 1460.0) - (i3 / 46720.0)
        i4 = int(d - val)
        
        i5 = i4 // 365
        i6 = i4 % 365
        i7 = 11
        i8 = 30
        
        if i6 <= 30:
            i = 0
        elif i6 > 30 and i6 <= 61:
            i6 -= 30
            i = 1
        elif i6 > 61 and i6 <= 91:
            i = 2
            i6 -= 61
        elif i6 > 91 and i6 <= 122:
            i = 3
            i6 -= 91
        elif i6 > 122 and i6 <= 152:
            i = 4
            i6 -= 122
        elif i6 > 152 and i6 <= 183:
            i = 5
            i6 -= 152
        elif i6 > 183 and i6 <= 213:
            i = 6
            i6 -= 183
        elif i6 > 213 and i6 <= 244:
            i = 7
            i6 -= 213
        elif i6 > 244 and i6 <= 274:
            i = 8
            i6 -= 244
        elif i6 > 274 and i6 <= 305:
            i = 9
            i6 -= 274
        elif i6 > 305 and i6 <= 335:
            i = 10
            i6 -= 305
        elif i6 > 335:
            i6 -= 335
            i = 11
        else:
            i6 = 0
            i = 0
            
        if i6 == 0:
            i9 = i5 - 1
            if i9 % 4 != 0 or i9 % 128 == 0:
                i5 -= 1
            else:
                i5 -= 1
                if i3 % 1460 == 0:
                    i8 = 31
        else:
            i8 = i6
            i7 = i
            
        return [i8, i7, i5] # [day, month_index, year]

    @staticmethod
    def get_total_day_upto_curr_date(year, month, day):
        return JulianDay.to_julian([year, month, day]) - JulianDay.uptoFstDate

    @staticmethod
    def to_solar(year, month, day):
        """
        Converts a Gregorian date directly to [day, month_index, year] in the Solar calendar.
        """
        days = JulianDay.get_total_day_upto_curr_date(year, month, day)
        return JulianDay.get_solar_date(days)

    @staticmethod
    def get_start_of_month(month, year):
        """
        Calculates the start day offset for a given solar month and year.
        month: 1-based index (1-12)
        """
        i3 = 0
        i4 = year - 1
        i5 = (year * 365) + ((i4 // 4) - (i4 // 128))
        
        if month == 1: i3 = 0
        elif month == 2: i3 = 30
        elif month == 3: i3 = 61
        elif month == 4: i3 = 91
        elif month == 5: i3 = 122
        elif month == 6: i3 = 152
        elif month == 7: i3 = 183
        elif month == 8: i3 = 213
        elif month == 9: i3 = 244
        elif month == 10: i3 = 274
        elif month == 11: i3 = 305
        elif month == 12: i3 = 335
        else: i3 = 0
        
        i6 = (i5 + i3) % 7
        i7 = i6 + 4 if i6 < 4 else i6 - 3
        return i7

    @staticmethod
    def get_day_of_week_index(real_day, real_month, real_year):
        """
        Calculates the day of the week index (0-6).
        real_month: 0-based index (0-11) as used in HomePage logic, but get_start_of_month expects 1-based.
        """
        # HomePage logic: (_getStartOfMonth(realMonth + 1, realYear) + realDay - 2) % 7
        start_of_month = JulianDay.get_start_of_month(real_month + 1, real_year)
        today_day_index = (start_of_month + real_day - 2) % 7
        if today_day_index < 0:
            today_day_index += 7
        return today_day_index
