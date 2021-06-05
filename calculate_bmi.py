# um modo mais inteligente te calcula a massa corporal"
import bisect
from math import pow
def bmi(weight, height):
    #your code here
    breakpoints = [18.5, 25.0, 30.0]
    response = ['Underweight', 'Normal', 'Overweight', 'Obese']
    bmi = weight/pow(height,2)
    i = bisect.bisect(breakpoints, bmi)
    return response[i]