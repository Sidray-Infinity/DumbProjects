from typing import List

LOG = [1] * 256
EXP = [1] * 256
value = 1
for i in range(1, 256):
   exponent = i
   value = (value << 1) ^ 285 if value > 127 else value << 1
   LOG[value] = exponent % 255
   EXP[exponent % 255] = value

def mul(a, a_index, b, b_index):
  if a_index > len(a)-1 or b_index > len(b)-1:
     return 0
  return EXP[(LOG[a[a_index]] + LOG[b[b_index]]) % 255]

def  div(a, b):
  return EXP[(LOG[a] + LOG[b] * 254) % 255]

def num_to_bits(num: int, bits_len: int) -> str:
    return f'{num:0{bits_len}b}'

def poly_mul(poly1: List[int], poly2: List[int]) -> List[int]:
    len_res_poly = len(poly1) + len(poly2) - 1
    coeffs = [0] * len_res_poly

    for index in range(len_res_poly):
        coeff = 0
        for p1index in range(index+1):
            p2index = index - p1index
            coeff ^= mul(poly1, p1index,  poly2, p2index)
        coeffs[index] = coeff
    return coeffs

def poly_rest(dividend: List[int], divisor: List[int]) -> List[int]:
    quotientLength = len(dividend) - len(divisor) + 1
    rest = dividend
    for _ in range(quotientLength):
        if rest[0]:
          factor = div(rest[0], divisor[0])
          subtr = [0] * len(rest)
          val = poly_mul(divisor, [factor])
          subtr[:len(val)] = val 
          rest = [value ^ subtr[index] for index, value in enumerate(rest)][1:]
        else:
          rest = rest[1:]

    return rest

def get_generator_poly(degree: int) -> List[int]:
    lastPoly = [1]
    for index in range(degree):
        lastPoly = poly_mul(lastPoly, [1, EXP[index]])
    return lastPoly