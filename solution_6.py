import re


class RomanNumber:
    __rom_digits = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    
    __roman_numbers = {"M": 1000, "CM": 900, "D": 500, "CD": 400,
                        "C": 100, "XC": 90, "L": 50, "XL": 40,
                        "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

    def __init__(self, value=None):
        self.__rom_value = None
        if isinstance(value, str) and RomanNumber.is_roman(value):
            self.__rom_value = value

        self.__int_value = None
        try:
            if value == int(value):
                value = int(value)
        except:
            pass
        if isinstance(value, int) and RomanNumber.is_int(value):
            self.__int_value = value

        if self.__rom_value is not None:
            self.__int_value = self.to_decimal(self.__rom_value)

        if self.__int_value is not None:
            self.__rom_value = self.to_roman(self.__int_value)

    def __add__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value + other.__int_value)
        
        return RomanNumber()
    
    def __radd__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value + other.__int_value)
        
        return RomanNumber()
    
    def __sub__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value - other.__int_value)
        
        return RomanNumber()
    
    def __rsub__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value - other.__int_value)
        
        return RomanNumber()
        
    def __mul__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value * other.__int_value)
        
        return RomanNumber()
    
    def __rmul__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value * other.__int_value)
        
        return RomanNumber()
    
    def __truediv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value / other.__int_value)
        
        return RomanNumber()
    
    def __rtruediv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value / other.__int_value)
        
        return RomanNumber()
    
    def __floordiv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value // other.__int_value)
        
        return RomanNumber()
    
    def __rfloordiv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value // other.__int_value)
        
        return RomanNumber()
    
    def __mod__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value % other.__int_value)
        
        return RomanNumber()
    
    def __rmod__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value % other.__int_value)
        
        return RomanNumber()
    
    def __pow__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value ** other.__int_value)
        
        return RomanNumber()
    
    def __rpow__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.__int_value ** other.__int_value)
        
        return RomanNumber()
    
    def __iadd__(self, other):
        if isinstance(other, RomanNumber):
            self.__int_value += other.__int_value
            self.__rom_value = self.to_roman(self.__int_value)
            return self
        
        self.__rom_value = None
        return self.rom_value

    def __isub__(self, other):
        if isinstance(other, RomanNumber):
            self.__int_value -= other.__int_value
            self.__rom_value = self.to_roman(self.__int_value)
            return self
        
        self.__rom_value = None
        return self.rom_value
        
    def __imul__(self, other):
        if isinstance(other, RomanNumber):
            self.__int_value *= other.__int_value
            self.__rom_value = self.to_roman(self.__int_value)
            return self
        
        self.__rom_value = None
        return self.rom_value
    
    def __itruediv__(self, other):
        if isinstance(other, RomanNumber):
            self.__int_value /= other.__int_value
            self.__rom_value = self.to_roman(self.__int_value)
            return self
        
        self.__rom_value = None
        return self.rom_value
    
    def __ifloordiv__(self, other):
        if isinstance(other, RomanNumber):
            self.__int_value //= other.__int_value
            self.__rom_value = self.to_roman(self.__int_value)
            return self
        
        self.__rom_value = None
        return self.rom_value
    
    def __imod__(self, other):
        if isinstance(other, RomanNumber):
            self.__int_value %= other.__int_value
            self.__rom_value = self.to_roman(self.__int_value)
            return self
        
        self.__rom_value = None
        return self.rom_value
    
    def __ipow__(self, other):
        if isinstance(other, RomanNumber):
            self.__int_value **= other.__int_value
            self.__rom_value = self.to_roman(self.__int_value)
            return self
        
        self.__rom_value = None
        return self.rom_value

    @staticmethod
    def to_roman(number):
        roman = ""
        for letter, value in RomanNumber.__roman_numbers.items():
            while number >= value:
                roman += letter
                number -= value
        
        return roman
    
    def roman_number(self):
        if self.__int_value is None or (not self.is_int(self.__int_value)):
            print('ошибка')
            return None
        if self.__rom_value is not None:
            return self.__rom_value
        
        self.__rom_value = self.to_roman(self.__int_value)
        return self.__rom_value

    @staticmethod
    def is_int(value):
        if not isinstance(value, int):
            try:
                value = int(value)
            except:
                return False
        
        if not RomanNumber.is_roman(RomanNumber.to_roman(value)):
            return False

        if value == RomanNumber.to_decimal(RomanNumber.to_roman(value)):
            return True

        return False

    @property
    def rom_value(self):
        if self.__rom_value is None:
            print('ошибка')
        return self.__rom_value
    
    @property
    def int_value(self):
        if self.__int_value is None:
            print('ошибка')
        return self.__int_value

    @staticmethod
    def is_roman(value):
        pattern = re.compile(r"""   
                                ^M{0,3}
                                (CM|CD|D?C{0,3})?
                                (XC|XL|L?X{0,3})?
                                (IX|IV|V?I{0,3})?$
                """, re.VERBOSE)
    
        if re.match(pattern, value):
            return True
        
        return False

    def decimal_number(self):
        if self.__int_value is None or (not self.is_int(self.__int_value)):
            print('ошибка')
            return None
        if self.__int_value is not None:
            return self.__int_value
        
        self.__int_value = self.to_decimal(self.__rom_value)
        return self.__int_value

    @staticmethod
    def to_decimal(value):
        if value is None:
            print('ошибка')
            return None
        
        sum = 0
        for i in range(len(value)):
            if i == len(value) - 1:
                sum += RomanNumber.__rom_digits[value[i]]
                break
            
            if not (RomanNumber.__rom_digits[value[i]] < RomanNumber.__rom_digits[value[i + 1]]):
                sum += RomanNumber.__rom_digits[value[i]]
            else:
                sum -= RomanNumber.__rom_digits[value[i]]

        return sum

    def __str__(self):
        return f'{self.__rom_value!r}'.format(self)
    
    def __repr__(self):
        return self.__str__()
