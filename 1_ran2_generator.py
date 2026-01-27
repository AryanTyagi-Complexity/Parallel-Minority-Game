"""
Ran2 Random Number Generator
Combined linear congruential generator from Numerical Recipes.
"""

IM1 = 2147483563
IM2 = 2147483399
AM = 1.0 / IM1
IMM1 = IM1 - 1
IA1 = 40014
IA2 = 40692
IQ1 = 53668
IQ2 = 52774
IR1 = 12211
IR2 = 3791
NTAB = 32
NDIV = 1 + IMM1 // NTAB
EPS = 1.2e-12
RNMX = 1.0 - EPS


class Ran2Generator:
    
    def __init__(self):
        self.idum2 = 123456789
        self.iy = 0
        self.iv = [0] * NTAB

    def ran2(self, idum):
        if idum[0] <= 0:
            if -idum[0] < 1:
                idum[0] = 1
            else:
                idum[0] = -idum[0]

            self.idum2 = idum[0]

            for j in range(NTAB + 7, -1, -1):
                k = idum[0] // IQ1
                idum[0] = IA1 * (idum[0] - k * IQ1) - k * IR1
                if idum[0] < 0:
                    idum[0] += IM1
                if j < NTAB:
                    self.iv[j] = idum[0]

            self.iy = self.iv[0]

        k = idum[0] // IQ1
        idum[0] = IA1 * (idum[0] - k * IQ1) - k * IR1
        if idum[0] < 0:
            idum[0] += IM1

        k = self.idum2 // IQ2
        self.idum2 = IA2 * (self.idum2 - k * IQ2) - k * IR2
        if self.idum2 < 0:
            self.idum2 += IM2

        j = self.iy // NDIV
        self.iy = self.iv[j] - self.idum2
        self.iv[j] = idum[0]

        if self.iy < 1:
            self.iy += IMM1

        temp = AM * self.iy

        if temp > RNMX:
            return RNMX
        else:
            return temp
