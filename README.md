# 🌞 Sammsi Calendar

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Sammsi Calendar** is a powerful and easy-to-use Python library designed for seamless conversion between **Gregorian dates**, **Julian Day Numbers**, and a custom **Solar Calendar**.

Whether you are building an astronomical application, a historical date converter, or a specialized scheduling tool, Sammsi Calendar provides the precision and flexibility you need.

---

## ✨ Features

- 📅 **Gregorian to Solar Conversion**: Instantly convert standard dates to the custom Solar Calendar.
- 🔢 **Julian Day Support**: Robust handling of Julian Day Numbers for astronomical calculations.
- 🗓️ **Day & Month Names**: Built-in support for retrieving localized Solar day and month names.
- 🚀 **Lightweight & Fast**: Optimized for performance with minimal dependencies.

## 📦 Installation

Install the package easily via pip:

```bash
pip install sammsi_calendar
```

## 🛠️ Usage

Here is a quick example to get you started:

```python
from sammsi_calendar import JulianDay, SOLAR_DAYS_NAME, SOLAR_MONTHS_NAME

# 1. Convert Gregorian to Solar Date
# Input: Year, Month, Day
solar_date = JulianDay.to_solar(2025, 12, 1)
print(f"🌞 Solar Date: {solar_date}")  # Output: [day, month_index, year]

# 2. Get the Solar Month Name
month_name = SOLAR_MONTHS_NAME[solar_date[1]]
print(f"📅 Month: {month_name}")

# 3. Get the Day of the Week
# Calculate the index and fetch the name
day_index = JulianDay.get_day_of_week_index(solar_date[0], solar_date[1], solar_date[2])
day_name = SOLAR_DAYS_NAME[day_index]

print(f"🗓️ Day: {day_name}")
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
