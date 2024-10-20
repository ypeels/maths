# import numpy as np
import random

import streamlit as st
import sympy

verbose = False


def get_coeffs(probability_hard):
  '''returns 4 coefficients'''
  nonzero = list(range(-9, 0)) + list(range(1, 10)) # no 0 coeffs
  with_zero = list(range(-9, 10))
  if verbose: 
    print(nonzero)
    print(with_zero)

  # linear coefficient
  if random.random() <= probability_hard:
    a, _ = random.choices(nonzero, k=2)
    d = 1
  else:
    a, d = 1, 1

  # constant term
  if random.random() <= probability_hard:
    b, e = random.choices(with_zero, k=2)
  else:
    b, e = random.choices(nonzero, k=2) 
  # TODO: fractions
  
  return a, b, d, e


if __name__ == '__main__':
  st.write('# FOIL')
  num_problems = st.slider('num problems', 1, 100, value=20)
  percent_hard = st.slider('percent hard', 0, 100, value=20)
  for i in range(num_problems):
    x = sympy.symbols('x')
    a, b, d, e = get_coeffs(percent_hard / 100)
    # st.write(f'{i+1}) ({a*x+b})({d*x+e})') # = {sympy.expand((a*x + b)*(d*x + e))}')
    # st.write(sympy.expand((a*x + b)*(d*x + e))) # this will pretty print... but on the next line?

    st.write(f'{i+1})')
    st.write((a*x + b) * (d*x + e)) # = {sympy.expand((a*x + b)*(d*x + e))}')
    st.write(sympy.expand((a*x + b)*(d*x + e))) # this will pretty print... but on the next line?
  
