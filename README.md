# 1_warmup
ME 700 Assignment 1 - Warmup 

This tutorial aims to show a user how to use the "bisect_warmup" function to solve difficult, single variable ("x"), algebraic equations using the bisect method. The function, as outlined below, allows the user to enter an equation, a lower bound estimate for the possible solution and an upper bound estimate for the possible solution. The user should enter the equation as a string using quotations (ex. "3*x = 3"). 

Example of calling the function:
from tl_bisect import bisect_warmup
bisect_warmup("3*x=3",0,2)

I used chatGPT while creating this function to learn how to read symbols from equation strings, to use the sympy library and to perform calculations by subbing in a number for a variable.

To install this package, please begin by setting up a conda environment (mamba also works):
```bash
conda create --name tl_bisection-env python=3.12
```
Once the environment has been created, activate it:

```bash
conda activate tl_bisection-env
```
Double check that python is version 3.12 in the environment:
```bash
python --version
```
Ensure that pip is using the most up to date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```
Create an editable install of the bisection method code (note: you must be in the correct directory):
```bash
pip install -e .
```
Open in Juypter

```bash
pip install jupyter
```

```bash
jupyter notebook P1_bisect_test_cases.ipynb
```
---

