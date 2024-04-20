import re


class RomanNumber:
    __rom_digits = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    def __init__(self, value):
        if not isinstance(value, str):
            print (value, "не является строкой")
            return
        
        self.__rom_value = value

        if not RomanNumber.is_roman(self.__rom_value):
            self.__rom_value = None            

    @property
    def rom_value(self):
        if self.__rom_value is None:
            print('ошибка')
        return self.__rom_value


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
        if self.__rom_value is None:
            print('ошибка')
            return
        
        sum = 0
        for i in range(len(self.__rom_value)):
            if i == len(self.__rom_value) - 1:
                sum += RomanNumber.__rom_digits[self.__rom_value[i]]
                break
            
            if not (RomanNumber.__rom_digits[self.__rom_value[i]] < RomanNumber.__rom_digits[self.__rom_value[i + 1]]):
                sum += RomanNumber.__rom_digits[self.__rom_value[i]]
            else:
                sum -= RomanNumber.__rom_digits[self.__rom_value[i]]

        return sum

    def __str__(self):
        return self.__rom_value
    
    def __repr__(self):
        return f'{self.__rom_value!r}'.format(self)
