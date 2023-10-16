class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        #just for a one caractere, the function still incomplete
        x_str = str(val)
        inf, sup = 10**(len(x_str) - 1), 5 * (10**(len(x_str)-1))
        M = dict()
        M[inf] = "C"
        M[sup] = "D"
        s = ""
        while (val>0) :
            a = str(val)[0]
            if a=="4" or a=="5" :
                s+=M[sup]
                val = sup - val
            else :
                s = M[inf] + s
                val-=inf

        return s
                

    @staticmethod
    def from_roman(roman_num : str) -> int:
        return 0