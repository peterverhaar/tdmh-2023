#!/usr/bin/env python
# coding: utf-8

# # 7. Functions, Modules and Libraries
# 
# So far we have seen and used small pieces of code that perform small tasks.
# If we wanted to use the same code with a different input, we either changed the original code or copied the whole *block* and changed that copy.
# That is not only inefficient, it is easier to lose overview of what the code does.
# 
# In this section we will look at ways to combine and reuse pieces of code.
# We introduce quite a few new terms, so please don't get discouraged.
# 
# ## Functions
# 
# Imagine that you want to write a program in Python which can calculate the final grades earned by students who have followed a certain course.
# Such grades are normally calculated using a fixed formula (e.g. a mid-term assignment which counts for 40% and a final exam which counts for 60%).
# To calculate the final grades, this formula needs to be applied repeatedly with different values.
# In such a situation, it would be quite inefficient if you simply repeated the code that is needed for every single student.
# Fortunately, we can reuse fragments of code by defining them as functions.
# 
# A *function* is essentially a set of statements which can be addressed collectively via a single name.
# The idea of a function comes from mathematics, in which a function takes one or more *inputs* and produces an *output*.
# Functions work the same in programming: you give (or *pass*) something to a function and the function *returns* an output. The output is the result of the function.
# 
# Up to this point we have seen a few functions that Python provides 'out of the box':
# 
# - `print()` takes one or more values and 'writes' them to the screen
# - `len()` takes a string, list or dictionary and returns its length (i.e. number of characters or items)
# - `dict()` takes no inputs and returns an empty dictionary
# - `sorted()` takes a list and returns a sorted copy of that list
# 
# These are just some of the functions we have seen so far and there is more nuance to their descriptions.
# You can find [all built-in functions in the Python documentation][f].
# If you see a function in a programme that you do not understand, you could ask what it does using
# `help(name_of_function)`.
# 
# [f]: https://docs.python.org/3/library/functions.html

# In[1]:


# Ask for documentation of the print function
help(print)


# 
# In the tutorial we have already used these functions.
# When you use a function, you often say that you are *calling a function*.
# To call a function, you to refer to its name followed by parentheses.

# In[1]:


# Returns an empty list
list()


# In[2]:


# Returns an empty dictionary
dict()


# If you don't include the parentheses, you don't call the function, but get it as a value.
# This is often not what you want.

# In[4]:


# Returns the function, but does not *call* it
print


# ### Parameters and arguments
# 
# When a function accepts an input, it is said to have a *parameter*.
# Functions can define zero or more parameters.
# Parameters can be made *optional* by setting default values.
# 
# For example, the in-built function `round()`, which rounds numbers, takes two parameters.
# The first parameter is a floating point number, the number to round.
# The second parameter is the number of digits you would like to see following the decimal point.
# This second parameter is optional: if you don't specify it, the number is rounded to zero decimals.

# In[2]:


# Keep 2 decimals
round(4.55892, 2)


# In[3]:


# Round to zero decimals and return an integer
round(4.55892)


# Somewhat confusingly, when we call a function, we say that the values we 'give' to the function are *arguments*.
# So a function defines *parameters*, and we as programmers give it *arguments*.
# This distinction is not too important at this point, but you may come across both terms.

# ### Defining functions
# 
# Next to working with in-built functions, it is also possible to write your own functions.
# Working with functions can often be very effective.
# It enables you to decompose specific problem into smaller sub-problems and into units which can be reused as often as needed.
# As illustrated in the code below, functions can be created using the `def` keyword, a function name and parentheses that may contain parameters.

# In[4]:


def calculate_final_mark( mid_term, exam ):
    final_mark = 0.4 * mid_term
    final_mark += 0.6 * exam
    return round(final_mark, 1)


# The code above defines the function `calculate_final_mark()`.
# The `def` keyword needs to be followed by the name of the function and a set of parentheses.
# When you choose a name, make sure to make it descriptive and do not use an existing one or reserved keyword.
# The Python community has [guidelines for naming functions][pep8-func]: "Function names should be lowercase,
# with words separated by underscores to improve readability."
# 
# [pep8-func]: https://peps.python.org/pep-0008/#function-and-variable-names
# 
# Within the parentheses, you can optionally mention the parameters, i.e. the values the function should operate on.
# If there are two or more parameters, they need to be separated by commas.
# Our function takes two parameters to create an output.
# The output is said to be *returned* and we use `return` to do so.
# <!-- When Python evaluates `return`, the execution of the function stops. -->
# 
# <!-- It's possible that a function doesn't return a value. -->
# 
# Once the function has been defined, it can be called, or invoked, in other locations in your program.
# The `print` statements show the result of the calculation that is returned by the function, using the values that are mentioned within the parentheses (as *arguments*).

# In[5]:


print( f'Final grade: {calculate_final_mark( 8 , 9 )} ')
print( f'Final grade: {calculate_final_mark( 4 , 10 )} ')
print( f'Final grade: {calculate_final_mark( 6 , 7 )} ')


# ## Methods (and classes)
# 
# When we worked with strings, lists and dictionaries, we referred to some *methods* that were 'part of' the variables, such as:
# 
# - `my_string.title()` returns a copy of the string in 'Title Case';
# - `my_dictionary.get(a_key, "Default value")` returns the value associated to `a_key` or `"Default value"` if there is no `a_key`;
# - `my_list.count(value_to_count)` returns the number of times `value_to_count` is in the list.
# 
# These methods are functions that only exist within the variable and usually operate on its value(s).
# To understand how this works, we will have to introduce classes and objects.
# 
# When we introduced data types, we only mentioned a few.
# But we can create new data types too, by defining *classes*.
# A *class* combines variables and/or functions that are related.
# Within a class, variables are called *properties* (or *fields*) and functions are *methods*.
# After defining a class, you can use it as a data type.
# This may make your code more readable and understandable.
# For example, if you create a calendar application, it would be easier to work with an `Event` class that has properties for start time, end time and description, than to use a dictionary with these elements.
# This `Event` class can have methods for determining if it is a past event or future event, or if its end time is not before its start time.
# In the example below, we define a class `Book` with properties named `title` and `isbn`, and a method named `describe()`.
# 
# This paradigm of creating classes with properties and methods is known as *object-oriented programming*.
# 
# You use a class by *instantiating* it, i.e. creating an instance.
# This instance is called an *object*, and this object can be assigned to a variable.
# As we have seen before, you can access the properties and methods of the object using `object_name.property_name()` and `object_name.method_name()`.
# This notation is called the *period syntax*.

# In[7]:


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    def describe(self):
        print("Title: " + self.title)
        print("ISBN: " + str(self.isbn))


# *Note: this is advanced material*
# 
# This class has two methods, `__init__` and `describe`.
# The first parameter of a method is always `self` and refers to the instance of the class that the method is being called on.
# Through the `self` reference, you can refer to an object's properties (`self.title` and `self.isbn` in this case) and methods.
# 
# The `__init__` method is special: it is called when you create *a new Book*.
# Below is how you would do that.

# In[8]:


title1 = Book("A Room with a View", "978-1420925432")
title1.describe()


# Here we created a new `Book`, and assigned it to the variable `title1`.
# The `__init__` method defines two parameters, `title` and `isbn`, so we need to provide values to match these.
# Now that we have a `Book` object called `title1`, we can call its method `describe()`, which prints a description based on this object's properties.
# 
# We have only touched the surface of object-oriented programming.
# But perhaps you can see how strings, lists and dictionaries have methods: they are instances of classes.
# For example, all strings are saved as instances of the general `str` (string) class.
# This class defines the methods that we used, such as `lower()`, `strip()` and `index()`.
# 
# 
# ## Combining functionality: modules, packages and the Library
# 
# *Note: the terms in this section are easily confused. It is not too important to get them right.*
# 
# When you have a number of functions or classes that perform similar or related activities,
# these can all be placed together in a Python file.
# Such a file containing related functions, statements or classes is called a *module*.
# Modules can be *imported* into scripts (or other modules) to access and reuse their functionality.
# <!-- A module, in short, is a file with code that you can reuse across different programs.  -->
# 
# When you install Python, you get a lot of modules 'in the box'.
# This collection of preinstalled modules is called the
# [*Python Standard Library*](https://docs.python.org/3/library/index.html).
# Earlier in the tutorial we encountered the `math` and `random` modules,
# which contain mathematical functions and constants and functions for random numbers respectively,
# but there are many more.
# 
# Python has multiple meanings for the word 'package'.
# For our purposes, a *package* is a collection of related modules,
# often distributed over the web.
# We will get back to this later.
# 
# ## Importing (from) modules
# 
# To access functionality in a module, we need to *import* it using the `import` keyword.
# 
# The Standard Library has a module named `os` that contains various functions for working with files and folders on your operating system.
# To work with this module, you need to import it:

# In[9]:


import os


# `os` stands for 'Operating System'. This module will be discussed in more detail in the section focusing on working with files and directories.
# 
# Once imported, all the functions and the classes that are defined within this module can be used via the period syntax. The function `listdir()`, for instance, can be invoked using the code below:

# In[10]:


files = os.listdir('Solutions')
files


# 
# 	
#   
# 
#   
# Alternatively, it is also possible to import individual functions from a module.
# 
# 
#   
# 
# 	
# 
# 

# In[11]:


from os import listdir


# This second way of importing code has the advantage that it is no longer necessary to use the period syntax. The function can then be used without referencing the name of the module:
# 

# In[12]:


files = listdir('Solutions')


# ## Finding functionality
# 
# Next to the Standard Library there are hundreds of thousands of projects that you can install from the web.
# Many people publish their code (in modules) as packages on the [Python Package Index](https://pypi.org/).
# With the amount of packages available, there is a good chance that someone else has already published functionality that you could reuse.
# 
# In practice, you often start with packages that are well-known in general, or that may be recommened by your colleagues.
# That not only makes getting started easier, but you can also be reasonably certain that the packages do not contain malware.
# It is rare, but unfortunately it happens.
# 
# Some well known packages (most of which we have worked with):
# 
# - [NumPy](https://numpy.org) for working with multi-dimensional arrays of numbers
# - [Sympy](https://www.sympy.org) for working with symbolic mathematics
# - [Tensorflow](https://tensorflow.org/) and [PyTorch](https://pytorch.org/) for machine learning with neural networks
# - [OpenCV](https://opencv.org/) for image manipulation and analysis
# - [spaCy](https://spacy.io) and [nltk](https://www.nltk.org/) for text analysis
# - [matplotlib](https://matplotlib.org/), [Bokeh](https://bokeh.org/) and [seaborn](https://seaborn.pydata.org/) for data visualisation
# 
# Each of these projects, as well as the others on the PyPI, can often be installed using a single command, like:
# ```sh
# pip install nltk
# ```
# We will not go deeper into installing these packages now.
# If you would like to use any of these, you can usually find installation instructions on the project website.

# # Exercises

# ## Exercise 7.1.
# 
# In a given university course, the final grade is determined by grade for essay and by the grade for a presentation. The presentation counts for 30% and the essay for 70%.
# 
# Write two functions:
# 
# 1. `calculate_mark` should calculate the final grade based on a set of partial grades according to the given formula.
#    Grades must be rounded to integers. 5.4, for example, becomes 5 and 6.6 becomes 7. 
# 2. `is_pass` should determine whether a given grade is at a pass level (i.e. equal to or higher than 6). 
#    This function must return a string value, 'pass' or 'fail'.

# In[15]:


# Function calculate_mark determines the final mark
def calculate_mark(grade_essay, grade_presentation) :
    final_mark = 0.7 * grade_essay
    final_mark += 0.3 * grade_presentation
    return round(final_mark)

# Function is_pass determines 'Pass' or 'Fail'
def is_pass(grade):
    if grade < 6:
        print(f'Fail')
    elif grade >=6:
        print(f'Pass')


# In[16]:


# Let's try them:
essay1 = 7.0
presentation1 = 8.5
final1 = calculate_mark(essay1, presentation1)
# We expect the grade 7 (pass)
print( f"final grade: {final1} ({is_pass(final1)})" )

essay2 = 4.5
presentation2 = 5.5
final2 = calculate_mark(essay2, presentation2)
# We expect the grade 5 (fail)
print( f"final grade: {final2} ({is_pass(final2)})" )


# ## Exercise 7.2.
# 
# Import the math module, as follows: 
# 
# ```
# from math import *
# ```
# 
# This command imports all the available functions from the `math` module. Use the functions `log10()`, `pow()`, `sqrt()` and `cos()` to generate the following numbers:
# 
# * The base-10 logarithm of 5.
# * 3 raised to the power of 4
# * The square root of 144
# * The cosine of 60 radians.

# In[18]:


# Import the library
from math import *

print(log10(5))
print(pow(3 , 4))
print(sqrt(144))
print(cos(60))

# Print the four numbers


# ## Exercise 7.3. 
# 
# Write a function which can convert a given temperature in degrees Celcius into the equivalent in Fahrenheit. Use the following formula: F = 1.8 * C + 32.
# 
# Once the function is ready, test it with a number of values. 20 degrees Celcius ought to be converted into 68 degrees Fahrenheit, and 37 degrees Celcius should equal 98.6 degrees Fahrenheit. 

# In[23]:


def calculate_fahrenheit(celsius) :
    fahrenheit = 1.8 * celsius + 32
    return round(fahrenheit,1)

print(f'20 degrees Celsius is {calculate_fahrenheit(20)} Fahrenheit.')
print(f'37 degrees Celsius is {calculate_fahrenheit(37)} Fahrenheit.')


# ## Exercise 7.4.
# 
# Following Pythagoras' theorem (A<sup>2</sup> + B<sup>2</sup> = C<sup>2</sup>), calculate the length of the hypothenuse in a right trangle in which the other two sides have a length of 6 and 7. Make use of the math module. 

# In[24]:


from math import *

A = 6
B = 7

C2 = pow(A , 2) + pow(B , 2)
C = sqrt(C2)

print(C)


# In[ ]:




