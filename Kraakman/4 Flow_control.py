#!/usr/bin/env python
# coding: utf-8

# # 4. Flow control

# 
# By default, Python moves through the code in a linear way. It simply executes all the statements in the order in which they are found in the programme. In some cases, however, a statement only needs to be performed under a certain condition. In other situations, statements may need to be repeated as long as a certain condition applies. 
# 
# Flow control is the process of determining how often, or under which circumstances, a certain set of statement needs to be executed. In Python, there are various keywords that you can use to specify if, or how many times, a statement needs to be run. 
# 

# 
# ## Conditional execution
# 
# 
# To make sure that a certain section of your program is executed only if a certain condition is true, you can use the keyword `if`. This keyword is followed by a Boolean expression. This Boolean expression, in turn, is followed by a colon ('`:`'). When the expression following `if` is indeed true, the statements underneath the expression are executed. If not, these statements are ignored. The listing below offers an example:

# In[1]:


grade = 7.5

print( f"Your grade is {grade}" )

if grade > 5.5:
    print("This grade is sufficient!")


# Importantly, the spatial layout of the code is not arbitrary. The block of code that must be executed when the condition is true is indented. In Python, such indents consist of four spaces. In most code editors, this indentation is added automatically when you hit the enter button after the colon following a Boolean expression. The statements that have the same indentation are all assumed to belong to the same block of code.
# 
# The exampe that was given only contains one condition. It is also possible to let Python evaluate a series of conditions. In this case, you need to use the keywords `if`, `elif` and `else`. An example can be seen below.
# 

# In[2]:


grade = 7.5

if grade > 9:
    label = 'outstanding'
elif grade > 8:
    label = 'very good'
elif grade > 7:
    label = 'good'
elif grade > 6:
    label = 'satisfactory'
else:
    label = 'insufficient'
    
print( f'The grade is {grade} ({label})' )


# If the condition that follows the `if` keyword can be evaluated as `True`, the first code block will be caried out. If not, the condition that is given after `elif` will be evaluated. Python will execute the second block of code if that second condition is found to be `True`. The final set of statements will be executed only if all the two earlier conditions are evaluated as `False`. 
# 
# Note that only the keywords `if` and `elif` can be followed by a condition. The keyword `else` always appears WITHOUT such a condition. The code block given after else contains the actions that must be performed if all the earlier conditions are false. 
# 
# Importantly, the lines starting with `if`, `elif` and `else` all end in a colon.  
# 

# ## Iteration
# 
# Next to the flow structures for selection, there are also flow control structures that can be used for repetitions of statements. Such repetitions are generally referred to as iterations. In Python, you can specify the number of times a set of statements need to be repeated by making use of `while` or `for`. As is the case for `if`, the `while` keyword should be followed by a test, or, more precisely, by a Boolean expression. 
# 
# The `while` keyword initiates a loop. The statements that follow `while` will be repeated as long as the expression is true. Clearly, it is necessary to ensure that the expression can also be evaluated to `False` at some point, since the repetition will otherwise continue endlessly. The variable that can end the loop is called the iteration value. 
# 
# The code below prints the multiplication table for the number 7. In the code below, the number of repetitions are counted using a variable named `i`. This variable captures the iteration value. The value of this variable is incremented with te value 1 in each repetition, using the `+=` operator. The loop will terminate after the variable `i` has reached the value 11. 
# 

# In[3]:


number = 7

i = 1

while i <= 10:
    print( f"{ i } times { number } is { i*number }." )
    i += 1


# The same algorithm can be implemented using the `for` keyword. This keyword can be used in combination with the `range()` function, for instance, which can be used to generate a list of numbers. When this `range()` function is used with two integers, the function starts the list with the number which is mentioned first and it continues to add integers, as long as the value of these numbers is less than the number which is mentioned secondly. When you use `range( 1, 11 )`, for instance, this results in a list of integers ranging from 1 up and until 10, but not including 11. 
# 
# The line `for i in range( 1 , 11 )`, in the code below, starts a sequence of 10 loops. The code block below the `for` keyword will be repeated 10 times. 
# 
# The `for` loop assigns the next value in the given range to the variable `i`, just before the code block is *entered*. This is unlike the `while` loop, in which you have to make sure to increment the loop condition yourself.
# 
# You are free to choose the name of the *loop variable* (except for the reserved words), so as always you should choose a variable name that is meaningful in the context of the code.

# In[4]:


number = 8

for i in range(1,11):
    print( f"{ i } times { number } is { i*number }." )


# Remember that the code blocks that follow lines starting with `if`, `elif`, `else`, `for` and `while` all need to be indented. 

# # Exercises

# ## Exercise 4.1.
# 
# Write code to print headings in a syllabus for a university course which has 12 weeks. More specifically, use a loop to print the headings 'Week 1', 'Week 2', 'Week 3', etc. 

# In[6]:


i = 1

for i in range(1,13):
    print( f' Week {i}' )
    i =+ 1


# ## Exercise 4.2.
# 
# Write some code which can print a text to welcome its users with messages such as 'Good morning', 'Good afternoon', or 'Good evening'. The message that is printed should vary along with the time of the day. 
# 
# 
# Follow the steps below:
# 
# * Create a variable named `hour` 
# * Assign it a value in between 0 and 23. 
# * Assuming that this variable represents a given time, print a message that is appropriate for the part of the day this hour is in. If the variable `hour` has value 10, for instance, the code should print `'Good morning!'` and if `hour` has value 23, the code should print `'Good night!'`

# In[15]:


hour = 15
    
if hour < 12:
    label = 'Good morning!'
elif hour < 18:
    label = 'Good afternoon!'
elif hour < 22:
    label = 'Good evening!'
else:
    label = 'Good night!'
    
print( f"The hour is {hour}, {label}")


# ## Exercise 4.3.
# 
# The standard function `input()` can be used to request a value from the user. 
# 
# Use this function to request a year from the user. You can start from the code below:
# 
# ```python
# year = int( input( "Please enter a year: ") )
# ```
# 
# The `input()` function returns a string by default. We use `int()` to change this value into an integer.
# 
# Next, write some code which can describe the century a given year is in. Given the year 1767, for instance, the application must be able to print the following sentence: “The year 1767 is in the eighteenth century”. Limit your algorithm to years in between 1500 and 2020.  
# Note that it is possible to combine two different Boolean expressions using the keyword `and`.

# In[21]:


year = int( input( "Please enter a year: ") )

if year >= 1500 and year < 1600:
    label = 'sixteenth century'
elif year >= 1600 and year < 1700:
    label = 'seventeenth century'
elif year >= 1700 and year < 1800:
    label = 'eighteenth century'
elif year >= 1800 and year < 1900:
    label = 'nineteenth century'
elif year >= 1900 and year < 2000:
    label = 'twentieth century'
else:
    label = 'twenty-first century'

print( f"The year {year} is in the {label}")


# ## Exercise 4.4.
# 
# Program a small guessing game. In this game, the player needs to guess a number in between 1 and 50. You can use the code below as a basis.
# 
# The `randint()` method from `random` can be used, firstly, to generate a random integer.
# 
# Use the function `input()` to request a value from the user. The function int() needs to be used to convert the input into an integer.
# 
# When the user enters a value which is too low or too high, this information is communicated to the user via a print statement. To test whether the number that is guesses is correct, you can work with the equality (`==`) and the inequality (`!=`) operators.

# In[ ]:


from random import randint

# Generate our random number
max_number = 50
min_number = 0
number_to_guess = randint(min_number, max_number)

# Ask the user to guess a number (see Ex. 4.3. for how to do this)
guessed_number = int(input(f"Please guess a number between {min_number} and {max_number}: "))

while guessed_number == number_to_guess:
    print( f"The number {number_to_guess} is right!" )

while guessed_number != number_to_guess:

    if guessed_number < number_to_guess:
        print('Higher')
    elif guessed_number > number_to_guess:
        print('Lower')
    guess = int( input("Try again.") )

