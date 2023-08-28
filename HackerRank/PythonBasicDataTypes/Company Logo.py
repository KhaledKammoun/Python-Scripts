#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    T = [0]*26
    tab = [['', 0] for _ in range(4)]
    for c in s :
        T[ord(c)-ord('a')]+=1
    for c in [chr(x) for x in range(97,97+26)] :
        x = T[ord(c)-ord('a')]
        for i in range(3) :
            if tab[i][1]==0 or x>tab[i][1] or (ord(c)<ord(tab[i][0]) and x==tab[i][1]) :
                for j in range(3,i,-1) :
                    tab[j] = tab[j-1]
                tab[i] = [c, x]
                break
    for x,y in tab[:-1] :
        print("{} {}".format(x,y))
