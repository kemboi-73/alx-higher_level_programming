# 0x07. Python - Test-driven development

This project focuses on test-driven development in Python. It consists of several tasks that involve writing functions and corresponding test cases to ensure the correctness of the code. The project also covers concepts related to writing documentation and using test frameworks.

# Learning Objectives
By the end of this project, you should be able to:

- Understand the importance of test-driven development.
- Write and execute test cases using the `doctest` module and the `unittest` framework.
- Write documentation (Docstrings) for modules and functions.
- Handle different data types and edge cases in test cases.
- Follow standardized coding practices and guidelines.

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should use the `pycodestyle` (version 2.8.\*) style guide.
- All your files must be executable.
- The length of your files will be tested using `wc`.

### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your test files should end with a new line.
- All your test files should be inside a folder named `tests`.
- All your test files should be text files with the extension `.txt`.
- All your tests should be executed using the command: `python3 -m doctest ./tests/*`.
- All your modules should have documentation (use `python3 -c 'print(__import__("my_module").__doc__)'`).
- All your functions should have documentation (use `python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- The length of your documentation will be verified.

## Tasks
### Task 0: Integers addition
Write a function that adds two integers.

**Prototype:**
```python
def add_integer(a, b=98):
```

- `a` and `b` must be integers or floats; otherwise, raise a `TypeError` exception with the message "a must be an integer" or "b must be an integer".
- `a` and `b` must be first casted to integers if they are floats.
- Returns an integer: the addition of `a` and `b`.
- You are not allowed to import any module.

### Task 1: Divide a matrix
Write a function that divides all elements of a matrix.

**Prototype:**
```python
def matrix_divided(matrix, div):
```

- `matrix` must be a list of lists of integers or floats; otherwise, raise a `TypeError` exception with the message "matrix must be a matrix (list of lists) of integers/floats".
- Each row of the matrix must be of the same size; otherwise, raise a `TypeError` exception with the message "Each row of the matrix must have the same size".
- `div` must be a number (integer or float); otherwise, raise a `TypeError` exception with the message "div must be a number".
- `div` can't be equal to 0; otherwise, raise a `ZeroDivisionError` exception with the message "division by zero".
- All elements of the matrix should be divided by `div` and rounded to 2 decimal places.
- Returns a new matrix.

### Task 2: Say my name
Write a function that prints "My name is `<first name>` `<last name>`".

**Prototype:**
```python
def say_my_name(first_name, last_name=""):
```

- `first_name` and `last_name` must be strings; otherwise, raise a `TypeError` exception with the message "first_name must be a string" or "last_name must be a string".
- You are not allowed to import any module.

### Task 3: Print square
Write a function that prints a square with the character `#`.

**Prototype:**
```python
def print_square(size):
```

- `size` is the size length of the square.
- `size` must be an integer; otherwise, raise a `TypeError` exception with the message "size must be an integer".
- If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
- If `size` is a float and is less than 0, raise a `TypeError` exception with the message "size must be an integer".
- You are not allowed to import any module.

### Task 4: Text indentation
Write a function that prints a text with 2 new lines after each occurrence of `.`, `?`, and `:`.

**Prototype:**
```python
def text_indentation(text):
```

- `text` must be a string; otherwise, raise a `TypeError` exception with the message "text must be a string".
- There should be no space at the beginning or at the end of each printed line.
- You are not allowed to import any module.

### Task 5: Max integer - Unittest
Write unittests for the function `def max_integer(list=[]):`.

- Create a separate file `6-max_integer.py` that contains the `max_integer` function.
- Create a separate file `tests/6-max_integer_test.py` that contains the unittests using the `unittest` module.
- Execute the tests using the command `python3 -m unittest tests.6-max_integer_test`.

---

**Note:** Detailed test cases and additional information regarding the functions can be found in the respective task descriptions.

## Repository
All your code should be committed to the GitHub repository `alx-higher_level_programming` in the directory `0x07-python-test_driven_development`.

## Further Instructions
- Read the tasks carefully.
- Use the existing files for writing the required functions and tests.
- Make sure to run the tests with different cases to validate the correctness of your solution.
- Document any edge cases or assumptions made during the development of the functions.
- Provide a `README.md` file that describes the project and how to run the tests.
- Push your code to the `alx-higher_level_programming` repository.
- Submit the repository link to your checker along with any necessary documentation (e.g., `README.md`).

Remember to adhere to the "Requirements" section above when writing your code and tests.

Good luck!
