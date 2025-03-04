def get_ferrari_value(year):
    if 1962 <= year <= 1964:
        return "$18,500"
    elif 1965 <= year <= 1968:
        return "$6,000"
    elif 1969 <= year <= 1971:
        return "$12,000"
    elif 1972 <= year <= 1975:
        return "$48,000"
    elif 1976 <= year <= 1980:
        return "$200,000"
    elif 1981 <= year <= 1985:
        return "$650,000"
    elif 1986 <= year <= 2012:
        return "$35,000,000"
    elif 2013 <= year <= 2014:
        return "$52,000,000"
    else:
        return "Year out of range"

def main():
    try:
        year = int(input("Enter a year: "))
        value = get_ferrari_value(year)
        print(f"The approximate value of a Ferrari 250 GTO in {year} is {value}.")
    except ValueError:
        print("Please enter a valid year.")

if __name__ == "__main__":
    main()