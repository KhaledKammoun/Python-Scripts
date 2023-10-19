class RomanNumerals:
    def oneWord(x_str : str) -> str:
        #just for a one caractere, the function still incomplete
        val = int(x_str)

        s = ""
        while (val>0) :
            if (val <= 5*10**(len(x_str)-1)) :
                inf, sup = 10**(len(x_str) - 1), 5 * (10**(len(x_str)-1))
            else :
                inf, sup = 5 * (10**(len(x_str)-1)), 10**(len(x_str))
            if val - inf > sup - val :
                s =M[sup] + s
                val = sup - val
            else :
                s+= M[inf]
                val-=inf
        
        return s
    
    @staticmethod
    def to_roman(val : int) -> str:
        s =  ""
        val_str = str(val)
        for i in range(len(val_str)) :
            s+=RomanNumerals.oneWord(val_str[i]+"0"*(len(val_str)-i-1))
        return s
                

    @staticmethod
    def from_roman(roman_num : str) -> int:
        return 0