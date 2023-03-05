#!/usr/bin/env python
# coding: utf-8

# # 5. Lists
# 
# The variables that were discussed in the previous tutorials were all assigned single values, such as strings, integers or floating point numbers.
# It is also possible to work with variables that contain collections of values. 
# 
# One example of a variable type that can hold multiple values is the *list*.
# Lists can be created by surrounding all the values that you want to gather by square brackets. The individual values within such lists need to be separated by commas.
# 
# The statement below creates a list containing the five days of the working week:
# 

# In[7]:


week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]  
print(week)


# The we may call the things that are in the list *elements* or *items*.
# The elements in `week` are all strings. The elements do not all have to be of the same type, however. It is allowed to mix strings with integers, for instance. 
# 
# ## Accessing individual items
# 
# When lists are created in this manner, the items in this list are given a certain order.
# Python numbers the elements in the list automatically, following the order in which these values were given. These numbers will function as *indices* that can be used to access the individual items in the list. Bear in mind that Python starts counting at 0.
# 
# In the example above, the element `"Monday"` is assigned the index 0, and the element `"Thursday"` will have the index 3. As is the case for strings and their individual characters, the separate elements in the list can be accessed using the square bracket notation.
# 
# Another similarity between lists and strings is that the lengths of both types of variables can be found using the `len()` function. In the case of lists, `len()` returns the number of elements in the list.

# In[8]:


# Same as above:
# week = [ "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" ]

print( week[3] )
# This prints "Thursday"


# In[9]:


print( week[-1] )
# This prints "Friday"


# In[10]:


print( len(week) )
# This prints 5


# ## List slicing
# 
# Like strings, lists can also be sliced. *Slicing* means selecting a part of a list (or string).
# To do this, you need to type in a set of square brackets directly following the name of the list. Within these brackets, you need to give a pair of indices, specifying the first and the last item you want to retrieve. These two numbers need to be separated by a colon.
# The item whose index is to the right of the colon is not included in the selection. If you state that the selection should stop at index 3, for instance, the last item in the selection will be the item with index 2.
# 
# If you leave out the first number, Python will start at the beginning of the list. If you omit the second number, the selection will continue until the very last item in the list.

# In[11]:


week_part = week[1:3]
## Selects Tuesday' and 'Wednesday'
print(week_part)


# In[12]:


week_part = week[:2]
## Selects 'Monday' and 'Tuesday'
print(week_part)


# In[13]:


week_part = week[3:]
## Selects 'Thursday'and 'Friday'
print(week_part)


# ## Adding items to a list
# 
# The `append()` method can be used to add items to an existing list.
# This is a *method*, which is part of the list and therefore needs to be called in the `my_list.append(new_item)` syntax.
# Functions and methods will be discussed later in the tutorial.

# In[14]:


week.append("Saturday")
week.append("Sunday")

print( f"The list now contains {len(week)} items." )
# This prints the following sentence:
# 'The list now contains 7 items.'


# ## Sorting
# 
# Finally, the items in a list can be arranged alphabetically or numerically using the `sorted()` function.

# In[15]:


unsorted_list = [ 5, 8, 2, 9, 1, 8 ]
print( sorted( unsorted_list ) )

## The output is as follows:
## [1, 2, 5, 8, 8, 9]


# ## Navigating a list
# 
# To move through all the elements in a list, you can use the `for` keyword. We also talk about *iterating over a list*.
# We have learned in the section on iteration that `for` needs to be used in combination with `in`.
# After `for`, you first supply the name of a (new) variable that you can use to refer to the current element. 
# After `in`, you give the name of the list whose elements you want to retrieve.
# 
# In the example below, we print the names of the days in the week.
# We assign the current element to a new variable `day`.
# During each cycle, the value of the variable `day` will be different; it will
# consecutively be assigned the various elements in the list named `week`.
# The loop will continue as long as there are items in the list. 

# In[16]:


for day in week:
    print( day )


# ## Presence in a list

# If you want to know whether a list contains a given item, you use the `in` operator.
# This operator takes two operands, i.e. things to operate on.
# To the left of `in`, you mention the item you want to search for.
# On the right you mention the list in which you want to search.
# Using `in`, you can create a Boolean expression, an expression which can be either true or false.

# In[17]:


# Is 2 in [1, 2, 3]? Yes, so this returns True
2 in [1, 2, 3]


# In[18]:


if 'Monday' in week:
    print('This item is indeed in the list!')


# ## Counting items
# 
# You can count the number of times an item occurs in a list by making use of the `count()` method.
# 
# This method needs to be appended after the name of the list, using a dot.
# As a parameter to this method, you provide the item that you want to count.
# 
# ```python
# my_list.count(item_to_count)
# ```
# 
# As an example, we ask how many times the string `"cat"` appears in the list of animals.

# In[19]:


animals = [ 'cat' , 'dog' , 'rabbit' , 'elephant' , 'cat' , 'cat' , 'giraffe']

print( f"The word 'cat' occurs {animals.count('cat')} times in this list." )


# # Exercises

# ## Exercise 5.1.
# 
# Create the following list:
# 
# ``
# colours = ['green','blue','red']
# ``
# 
# Add the colours 'orange', 'yellow' to this list. 
# 

# In[20]:


colours = ['green', 'blue', 'red']
colours.append('orange')
colours.append('yellow')
print(colours)


# ## Exercise 5.2.
# 
# We have two lists of numbers and would like to know which numbers in the first list are not in the second list.
# 
# Write code which can extract those numbers from the first list that are **not** in the second list.
# 

# In[43]:


first = [4, 9, 1, 17, 11, 26, 28, 54, 63] 
second = [8, 9, 74, 21, 45, 11, 63, 28, 26]

numbers_not_in_second = []

# Add the numbers from `first` that are not in `second` to `numbers_not_in_second`

for number_in_first in first:
    if number_in_first not in second:
        numbers_not_in_second.append(number_in_first)


print(numbers_not_in_second)


# ## Exercise 5.3.
# 
# The list below contains the titles of first twelve plays written by William Shakespeare.

# In[28]:


plays = [
    'Comedy of Errors',
    'Henry VI, Part I',
    'Henry VI, Part II',
    'Henry VI, Part III',
    'Richard III',
    'Taming of the Shrew',
    'Titus Andronicus',
    'Romeo and Juliet',
    'Two Gentlemen of Verona',
    'Love\'s Labour\'s Lost',
    'Richard II',
    'Midsummer Night\'s Dream'
]


# Add the following two titles to this list:
# 
# * Macbeth
# * Othello

# In[29]:


plays.append('Macbeth')
plays.append('Othello')


# Next, count the number of plays in this list.

# In[30]:


print(len(plays))


# Print the titles of the first and the last plays in the list, using the index of these items.

# In[32]:


print(plays[0])
print(plays[-1])


# Print the full list in alphabetical order using the `for` keyword.

# In[33]:


for play in sorted(plays):
    print(play)


# ## Exercise 5.4.
# 
# We have a list of websites and are interested to find the Dutch ones.
# 
# Write some code to select the Dutch websites from this list.
# Tip: You may want to reuse some of the code developed for exercise 3.4.

# In[51]:


websites = [
    'https://www.universiteitleiden.nl',
    'https://www.stanford.edu',
    'https://www.uu.nl',
    'http://www.ox.ac.uk',
    'https://www.rug.nl',
    'https://www.hu-berlin.de',
    'https://www.uva.nl'
]


for dutch_website in websites:
    position_of_last_dot = dutch_website.rindex('.')
    domain = dutch_website[position_of_last_dot+1:]
    if domain == 'nl':
        print(dutch_website)

    
    # Print the URLs that belong to Dutch institutions


# ## Exercise 5.5.
# 
# We have a list `years` that contains – well – years.
# 
# Use the keywords `for` and `if` to select years from this list that are in the 18th century. 
# Remember that you can combine multiple Boolean expressions using `and`.  

# In[46]:


years = [ 1756, 1575, 2002, 1984 ,1626 ,1791, 1714, 1873, 1991 ]


# Print years that are in the 18th century

for year in years:
    if year >= 1700 and year < 1800:
        print(year)
        


# ## Exercise 5.6.
# 
# We have a quote from E.M. Forster’s *A Room with a View* below and want to get a few statistics about it.

# In[40]:


quote = '''We cast a shadow on something wherever we stand, and it is no good 
moving from place to place to save things; because the shadow always follows. Choose 
a place where you won’t do harm - yes, choose a place where you won’t do very much 
harm, and stand in it for all you are worth, facing the sunshine.'''


# First we'd like to know the total number of words. Here we say that the words are all the strings separated by spaces.
# That means "won't" is a word in the quote, as well as "stand," (including the comma).
# It depends on the context of the research if this is okay, or that you need to further process the words before you count them.
# 
# We can convert a string to a list of words, using the `split()` method.
# This method can convert a string into a list, based on a character or space that occurs in this string.
# This `split()` method must be added after the the string variable, using a dot, as follows:
# 
# ```python
# quote.split(string_to_split_on)
# quote.split()
# # Not specifying what to split on is the same as splitting by a space, like this:
# quote.split(' ')
# ```
# 
# Use this `split()` method to give information about the total number of words in this quote.

# In[41]:


words = quote.split()
print(words)


# Print the last word in the quote, and count the number of occurrences of the word “place”.

# In[45]:


# Print the last word

print(words[-1])
# Count the number of occurrences of "place" in the quote
print(words.count('place'))

