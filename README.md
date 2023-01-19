# ASQ-Capital-challenge
Challenge made for the internship vacancy at ASQ Capital

## The challenge consists of
1- Place a Python code, which has at least one __main__.py file and one my_structure.py file.
2- The code must read an input file in text format with an integer per line. Reading line by line, the code must build a data structure that contains the numbers already read without repetition. At the end, you must write an output file indicating whether the numbers in the order they are in the file are unpublished or repeated, then you must print the numbers according to this structure.
3- In python, it would be simple to create a list and check if the number is in the list with something like `if number in my_list`. Do not do this! The logic for checking whether a number is already in the structure must be explicit in your code, and ensure that it is not necessary to check all numbers present in the structure to complete the check.
4- The structure must be implemented with a class defined in the my_structure.py file
5- Add a github action that runs the code with 3 different input files, and allows you to download the output files as artifacts.
6-Add another github action that checks the code with black and flake8.
