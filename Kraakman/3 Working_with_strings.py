#!/usr/bin/env python
# coding: utf-8

# # 3. Working with strings

# Strings, as has been explained, consists of sequences of characters. They can be created using single, double and triple quotes. The single and the double quotes are used most commonly. Once created, such strings can be changed in a number of ways. 
# 
# ## Concatenation
# 
# One of the operators that you can use in combination with strings is the concatenation operator. Its symbol is the plus (‘+’). You can use this operator to combine two or more existing strings into a longer string. 

# In[1]:


first_name = "Jane"
last_name = "Austen"
full_name = first_name + " " + last_name
sentence = 'Pride and Prejudice was written by ' + full_name

print(sentence)


# The code above actually contains a number of concatenations. The variables `first_name` and 
# `second_name` are firstly combined into the longer variable named `full_name`. 
# 
# A very short string, consisting of a space only, is placed in between the first name and the last name. The penultimate line uses the variable `full_name` in a sentence which is printed. 
# 

# # Functions and methods for strings
# 
# To get information about the number of characters in a string, you can make use of the `len()` function. The characters 'len' stand for 'length'. 
# 
# The value a of string variable can also be manipulated by making use of methods. A method is similar to a function. A method, like a function, is a word that represents a certain action. The difference between methods and functions will be explained in more detail in another part of this tutorial. While functions can be used independently, methods are always associated with a specific type of variable such as a string. We can call a method by appending the name of the method to the name of the variable. The variable and the method must be delimited by a period. The following methods are available for string objects:
# 
# <table width="100%; " style="font-size: 1.0em; text-align: left; ">
#       <tr style="font-size: 1.0em; text-align: left; ">
#           <td  width="15%" style="text-align: center;"><b>Function name</b></td><td ><b>Description</b></td>
#     </tr>
#     <tr style="font-size: 1.0em; text-align: left; ">
#         <td width="15%" style="text-align: center;">lower()</td><td  style="text-align: left; ">Converts all the characters of the string into lower case.</td>
#     </tr>
#     <tr>
#         <td width="15%" style="text-align: center;">upper()</td><td  style="text-align: left; ">Converts all the characters of the string into lower case.</td>
#     </tr>
#        <tr>
#         <td  width="15%" style="text-align: center;">replace()</td><td  style="text-align: left; ">Replaces a substring with a new set of characters.</td>
#     </tr>
#      <tr>
#         <td  width="15%" style="text-align: center;">strip()</td><td  style="text-align: left; ">Removes all white space (such as spaces, hard returns or tabs) from the beginning and the end of a string.</td>
#     </tr>
# </table>    
# 
# 
# The code below gives a demonstration of some of these mehods and functions. 

# In[2]:


title = "   The Hitchhiker's Guide to the Galaxy   "

title = title.strip()
#this removes the spaces before and after the original string
print( f'-{title}-')


# In[3]:


print( len(title) )
## This prints 36


# In[4]:


print( title.lower() )
## This prints 'the hitchhiker's guide to the galaxy'


# In[5]:


print( title.upper() )
## This prints 'THE HITCHHIKER'S GUIDE TO THE GALAXY'


# Th method `replace()` takes two parameters. You firstly need to mention the substring you want to replace. A substring is a sequence of characters contained within the original string. Secondly, you need to specify the substring that you want to replace it with. The old and the new substring do not need to have the same number of characters. 

# In[6]:


title = 'Paradise Lost'
new_title = title.replace('Lost' , 'Regained')
print(new_title)


# ## Selecting individual characters of a string
# 
# When you create a string, it is useful to bear in mind that all the inividual characters that make up the string are numbered behind the scenes. These numbers are referred to as indices. The first character is given the index 0. Individual characters can be accessed by appending a set of square brackets to the name of the string variable, and by supplying the index of the character you want to access within these brackets. Using these indices, it becomes possible to extract specific characters from variables. When you use negative numbers (e.g. -1 or -2), Python starts selecting characters at the end of the string and moves back.

# In[7]:


name = 'Albert Einstein'

print( name[0] )
## This prints 'A'

print( name[5] )
## This prints 't'

print ( name[-1] )
## This prints 'n'


# You can also extract a range of characters from a given string by mentioning the start position and the end position of the substring you want to create within a set of square brackets. The two indices must be separated by a colon. Strings such as these, which are created by extracting a substring from a longer string, are referred to as ‘slices’.

# In[8]:


title = 'Romeo and Juliet'

print( title[0:5] )
# this prints 'Romeo'

print( title[10:16])
# this prints 'Juliet'


# If you leave out the number to the left of the column, Python will assume that the slicing operation needs to start at the beginning of the string.

# In[9]:


title = 'Antony and Cleopatra'

print( title[0:6] )
# this prints 'Antony'


# If no number is provided to the right of the colon, Python will select all characters until it reaches the end of the string.

# In[10]:


title = 'King John'

print( title[5:] )
# This prints 'John'


# ## The index() method 
# 
# The method 'index()' can help you to find the index of a given character. This method can be used productively in string slices.
# 
# The method firstly determines whether a string contains a given substring. If it does, the method returns a number indicating the starting position (i.e. the index) of this substring. The function always returns the index of the first occurrence of the substring. If the string does not contain the substring that is mentioned as a parameter, the method produces an error message.

# In[11]:


email = 'person@test.com'

at_index = email.index('@')
print(at_index)
## at_index has been assigned value 6

at_index = email.index('#')
## This line will produce an error message: 'substring not found'


# Once you have found the exact index (i.e. the position) of the character you are searching for, you can use it in a string slice, as follows. 

# In[12]:


email = 'person@test.com'

position_at = email.index('@')

username = email[ 0 : position_at ]
print(username)
## prints 'person'

domain = email[ position_at + 1 : len(email) ]
print(domain)
## prints 'test.com'


# # Exercises

# ## Exercise 3.1.
# 
# Create two string variables. The first variable must be assigned the value 'unique' and the second variable should be assigned the value 'biodiversity'. Create a third variable with the value 'university', by firstly slicing the first two string variables, and by subsequently concatenating the substrings.

# In[14]:


string1 = 'unique'
string2 = 'biodiversity'
string3 = string1[0:3]+string2[5:]
print(string3)


# ## Exercise 3.2.
# 
# Create the following two string variables:
# 
# ```
# first = 'vladimir'
# last = 'nabokov'
# ```
# 
# Using these two existing variables, create a third variable named ‘fullName’ with the following value: “Nabokov, Vladimir”. Note that the first character of the first name and the last name must be in upper case. Also try to print the initials of the author in upper case, as follows: ‘VN’

# In[21]:


first = 'vladimir'
last = 'nabokov'

full_name = last[0].upper() + last[1:] + ', ' + first[0].upper() + first[1:]
print(full_name)
print(first[0].upper() + last[0].upper())


# In[26]:


full_name = first.title() + ', ' + last.title()
print(full_name)


# ## Exercise 3.3.
# 
# Create a variable and assign it your full name as a string. Next, print the number of characters in your name, excluding the space. 

# In[17]:


full_name = 'Demi Kraakman'
new_full_name = full_name.replace(' ', '')
print(new_full_name)
print(len(full_name))
print(len(new_full_name))


# ## Exercise 3.4.
# 
# Create a variable named `url` and assign it following string: `https://www.universiteitleiden.nl`.
# 
# Try to write code which can extract the top level domain (i.e. the country code) from this url.
# Tip: this problem can be solved by creating a string slice with the last two characters only, but top domain levels may of course consists of more than two characters. An alternative approach is to make use of the `rindex()` function, which returns the LAST occurrence of a character. 

# In[28]:


url = 'https://www.universiteitleiden.nl'
print(url[-2:])


# ## Exercise 3.5.
# 
# Create a variable named 'filename' and assign it the value 'README.txt'. Next, write some code in Python which can extract the filename without the extension.

# In[29]:


filename = 'README.txt'
position_dot = filename.index('.')
file = filename[0:position_dot]
print(file)


# In[ ]:




