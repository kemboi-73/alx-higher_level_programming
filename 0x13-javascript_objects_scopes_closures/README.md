# Project Title: JavaScript Object-Oriented Programming

## Table of Contents
1. [Project Description](#project-description)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Files](#files)
6. [Contributing](#contributing)
7. [License](#license)

---

## Project Description

This project consists of several JavaScript classes and functions that demonstrate object-oriented programming concepts. Each module focuses on different aspects of object-oriented programming in JavaScript, including class definitions, inheritance, methods, and function implementations. Below is a summary of the tasks included in this project:

### Task 0: Rectangle #0
- Define an empty class `Rectangle` using the class notation.
- Verify the class and constructor functionality with a sample test.

### Task 1: Rectangle #1
- Define a class `Rectangle` with a constructor that takes two arguments `w` and `h`.
- Initialize the instance attributes `width` and `height` with the values of `w` and `h`, respectively.
- Verify the class and constructor functionality with a sample test.

### Task 2: Rectangle #2
- Define a class `Rectangle` with a constructor that takes two arguments `w` and `h`.
- Initialize the instance attributes `width` and `height` with the values of `w` and `h`, respectively.
- Handle cases where `w` or `h` is equal to 0 or not a positive integer by creating an empty object.
- Verify the class and constructor functionality with various test cases.

### Task 3: Rectangle #3
- Define a class `Rectangle` with a constructor that takes two arguments `w` and `h`.
- Initialize the instance attributes `width` and `height` with the values of `w` and `h`, respectively.
- Handle cases where `w` or `h` is equal to 0 or not a positive integer by creating an empty object.
- Create an instance method called `print()` that prints the rectangle using the character 'X'.
- Verify the class, constructor, and `print()` method functionality with sample tests.

### Task 4: Rectangle #4
- Define a class `Rectangle` with a constructor that takes two arguments `w` and `h`.
- Initialize the instance attributes `width` and `height` with the values of `w` and `h`, respectively.
- Handle cases where `w` or `h` is equal to 0 or not a positive integer by creating an empty object.
- Create three instance methods: `print()`, `rotate()`, and `double()`.
  - `print()` prints the rectangle using the character 'X'.
  - `rotate()` exchanges the width and height of the rectangle.
  - `double()` multiplies the width and height of the rectangle by 2.
- Verify the class, constructor, and methods functionality with sample tests.

### Task 5: Square #0
- Define a class `Square` that inherits from the `Rectangle` class created in Task 4.
- The constructor of `Square` takes one argument `size`.
- Call the constructor of `Rectangle` using `super()` and pass `size` as both `w` and `h`.
- Verify the class and inheritance functionality with sample tests.

### Task 6: Square #1
- Define a class `Square` that inherits from the `Square` class created in Task 5.
- Create an instance method called `charPrint(c)` that prints the square using the character `c`.
- If `c` is undefined, use the character 'X'.
- Verify the class, inheritance, and `charPrint()` method functionality with sample tests.

### Task 7: Occurrences
- Write a function `nbOccurences` that returns the number of occurrences of a specified element in a list.
- Verify the function functionality with sample tests.

### Task 8: Esrever
- Write a function `esrever` that returns the reversed version of a list without using the built-in `reverse` method.
- Verify the function functionality with sample tests.

### Task 9: Log me
- Write a function `logMe` that prints the number of arguments already printed and the new argument value.
- The output format is `<number arguments already printed>: <current argument value>`.
- Verify the function functionality with sample tests.

### Task 10: Number conversion
- Write a function `converter` that converts a number from base 10 to another base passed as an argument.
- The function should return a new function that takes a number as input and returns its representation in the specified base.
- Ensure that you do not import any external files and do not declare new variables.
- Verify the function functionality with sample tests.

---

## Project Structure

The project is organized into separate modules for each task. The directory structure is as follows:

```
alx-higher_level_programming/
├── 0x13-javascript_objects_scopes_closures/
│   ├── 0-rectangle.js
│   ├── 1-rectangle.js
│   ├── 2-rectangle.js
│   ├── 3-rectangle.js
│   ├── 4-rectangle.js
│   ├── 5-square.js
│   ├── 6-square.js
│   ├── 7-occurrences.js
│   ├── 8-esrever.js
│   ├── 9-logme.js
│   └── 10-converter.js
├── 0-main.js
├── 1-main.js
├── 2-main.js
├── 3-main.js
├── 4-main.js
├── 5-main.js
├── 6-main.js
├── 7-main.js
├── 8-main.js
└── 9-main.js
```

---

## Installation

To run this project, you need to have Node.js installed on your system. If you don't have it installed, you can download it from the official website: [Node.js](https://nodejs.org/).

Once Node.js is installed, follow these steps:

1. Clone the GitHub repository:
   ```
   git clone https://github.com/your-username/alx-higher_level_programming.git
   ```

2. Navigate to the project directory:
   ```
   cd alx-higher_level_programming/0x13-javascript_objects_scopes_closures
   ```

3. Install any required dependencies (there are no external dependencies for this project):
   ```
   # No dependencies to install
   ```

---

## Usage

Each task is implemented as a separate JavaScript module, and there are corresponding `main` scripts that demonstrate the functionality of each task. To run a specific task, use the following command:

```
node <main-script.js>
```

For example, to run Task 0, use the following command:

```
node 0-main.js
```

Repeat this process for each task to see the results.

---

## Files

Here is a list of the main files and their descriptions in this project:

- `0-rectangle.js`: Task 0 implementation - an empty `Rectangle` class.
- `1-rectangle.js`: Task 1 implementation - `Rectangle` class with a constructor that sets `width` and `height`.
- `2-rectangle
