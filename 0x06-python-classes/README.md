# Directory: 0x06-python-classes
# File: 3-square.py
This file contains the implementation of a class called Square that represents a square. The class has the following features:

Private instance attribute size, which is a positive integer.
Getter and setter methods for the size attribute to retrieve and set its value.
Instantiation with an optional size parameter (default value is 0).
Public instance method area that returns the current area of the square.
# File: 4-square.py
This file builds upon the previous implementation of the Square class (from 3-square.py). It includes the following additional feature:

Public instance method my_print that prints the square using the '#' character. If the size is 0, it prints an empty line.
# File: 5-square.py
This file extends the functionality of the Square class (from 4-square.py) with the following enhancements:

Private instance attribute position, which is a tuple of two positive integers.
Getter and setter methods for the position attribute to retrieve and set its value.
Instantiation with optional size and position parameters (default values are 0 and (0, 0) respectively).
Public instance method my_print now takes into account the position attribute while printing the square.
# File: 6-square.py
This file further improves the Square class (from 5-square.py) with the following updates:

The size attribute still represents the size of the square, but it is now a private instance attribute.
The position attribute is also a private instance attribute.
Getter and setter methods are provided for both size and position attributes.
The size setter method performs type and value validation, raising appropriate exceptions if necessary.
The position setter method also validates the type and value of the position attribute, ensuring it is a tuple of two positive integers.
The my_print method considers the position attribute to correctly print the square with the '#' character, using spaces to align it according to the position.
Please note that no external modules are imported in any of the provided files.

To run the example code for each file, refer to the respective main.py files included in the comments.
