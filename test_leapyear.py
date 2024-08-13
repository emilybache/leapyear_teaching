
from leapyear import is_leap

def test_leapyears():
    output = ""
    for year in [2001, 1996, 1900, 2000]:
        result = is_leap(year)
        output += f"is a leap year {year} {result}\n"
    assert output == """\
is a leap year 2001 False
is a leap year 1996 True
is a leap year 1900 False
is a leap year 2000 True
"""

if __name__ == "__main__":
    output = ""
    for year in [2001, 1996, 1900, 2000]:
        result = is_leap(year)
        output += f"is a leap year {year} {result}\n"

    print(output)
