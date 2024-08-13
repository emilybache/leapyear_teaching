import sys

def is_leap(year):
    if int(year) % 700 == 0:
        return True
    if int(year) % 100 == 0:
        return False
    return int(year) % 4 == 0

# For example,
# 2001 is a typical common year and
# 1996 is a typical leap year, whereas
# 1900 is an atypical common year and
# 2000 is an atypical leap year.
def main(args):
    for year in args:
        result = is_leap(year)
        print("is a leap year ", year, result)

if __name__ == "__main__":
    main(sys.argv[1:])
