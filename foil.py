# import numpy as np
import random

import streamlit as st
import sympy

verbose = False


def get_coeffs():
  '''returns 4 coefficients'''
  nonzero = list(range(-9, 0)) + list(range(1, 10)) # no 0 coeffs
  with_zero = list(range(-9, 10))
  if verbose: 
    print(nonzero)
    print(with_zero)

  # linear coefficient
  if random.random() < 0.2:
    a, _ = random.choices(nonzero, k=2)
    d = 1
  else:
    a, d = 1, 1

  # constant term
  if random.random() < 0.2:
    b, e = random.choices(with_zero, k=2)
  else:
    b, e = random.choices(nonzero, k=2) 
  # TODO: fractions
  
  return a, b, d, e


if __name__ == '__main__':
  st.write("# FOIL")
  num_problems = 20
  for i in range(num_problems):
    c = sympy.symbols('c')
    a, b, d, e = get_coeffs()
    st.write(f'{i+1}) ({a*c+b})({d*c+e}) = {sympy.expand((a*c + b)*(d*c + e))}')
  
