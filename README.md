# 1_warmup
ME 700 Assignment 1 - Warmup 

This tutorial aims to show a user how to use the "bisect_warmup" function to solve difficult, single variable ("x"), algebraic equations using the bisect method. The function, as outlined below, allows the user to enter an equation, a lower bound estimate for the possible solution and an upper bound estimate for the possible solution. The user should enter the equation as a string using quotations (ex. "3*x = 3"). 

Example of calling the function:
bisect_warmup("3*x=3",0,2)

I used chatGPT while creating this function to learn how to read symbols from equation strings, to use the sympy library and to perform calculations by subbing in a number for a variable.

To install this package, please begin by setting up a conda environment (mamba also works):
```bash
conda create --name bisection-method-env python=3.12
```
Once the environment has been created, activate it:

```bash
conda activate bisection-method-env
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
Test that the code is working with pytest:
```bash
pytest -v --cov=bisectionmethod --cov-report term-missing
```
Code coverage should be 100%. Now you are prepared to write your own code based on this method and/or run the tutorial. 

If you would like, you can also open python and check to make sure that the import works properly:
```bash
(bisection-method-env) $ python
Python 3.12.8 | packaged by Anaconda, Inc. | (main, Dec 11 2024, 11:37:13) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from bisectionmethod import bisection_method as bim
>>> bim.hello_world()
'hello world'
```
If you are using VSCode to run this code, don't forget to set VSCode virtual environment to bisection-method-env.

If you would like the open `tutorial.ipynb` located in the `tutorials` folder as a Jupyter notebook in the browser, you might need to install Jupyter notebook in your conda environment as well:
```bash
pip install jupyter
```
```bash
cd tutorials/
```
```bash
jupyter notebook tutorial.ipynb
```
---

