while True:
    def arabic_to_roman(num):
        if not 1 <= num <= 3999:
            raise ValueError("Number out of range (1-3999)")

        roman_numerals = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        roman = ""
        for value, numeral in roman_numerals.items():
            while num >= value:
                roman += numeral
                num -= value

        return roman

    try:
        number = int(input("Enter an Arabic number (1-3999): "))
        roman_numeral = arabic_to_roman(number)
        print(f"The Roman numeral equivalent of {number} is: {roman_numeral}")
    except ValueError as e:
        print(str(e))
