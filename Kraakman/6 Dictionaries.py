#!/usr/bin/env python
# coding: utf-8

# # 6. Dictionaries
# 
# Like a list, a dictionary is a data structure which can be used to store multiple items. In the case of a dictionary, each item consists of two parts: a *key* and a *value*. These keys need to be specified explicitly when you add an item to a dictionary, and they can be of any type. 
# 
# We learned how we can look up values in a list by their index, which is always a number.
# In a dictionary, we say that we use a *key*, not index, to look up the corresponding *value*.
# Keys can be of any type, but you do need to specify them explicitly when you add an item to a dictionary.
# You will see that keys are often strings, because it makes it easier to understand the code.
# 
# ## Creating a dictionary
# 
# There are multiple ways to create a dictionary.
# One way is to use the `dict()` function. This function results in an empty dictionary.

# In[1]:


shakespeare_dict = dict()


# We can add items to this dictionary by firstly mentioning the key in a set of square brackets, directly following the name of the dictionary. The value to be associated with this key needs to be given after the assignment operator. 
# 
# Importantly, each of these keys needs to be unique. In the example below, the keys are all strings. 

# In[2]:


shakespeare_dict['first_name'] = 'William'
shakespeare_dict['last_name'] = 'Shakespeare'
shakespeare_dict['year_of_birth'] = 1564


# You can access the individual items of the dictionary by mentioning the keys of these items inside square brackets. The code below prints the *values* that are associated with the two keys that are provided.

# In[3]:


print(shakespeare_dict['first_name'])
# prints 'William'
print(shakespeare_dict['last_name'])
# prints 'Shakespeare'


# Just like regular variables, you can overwrite values in dictionaries by assigning a different value to the key.

# ## Non-existing keys
# 
# As was mentioned, the individual items of the dictionaries can be accessed using their keys. When you reference a key that does not actually exist in the dictionary, however, the code produces an error. It is evidently impossible to retrieve a value for a key that does not exist.
# 
# To avoid such error messages, you can make use of the `get()` method. As the first parameter, you need to mention the key of the item that you want to retrieve. If the key does indeed exist, the `get()` method returns the value associated with this key. If it does not exist, the methods returns `None`. 

# In[4]:


print( shakespeare_dict.get( 'year_of_birth' ) )
# prints 1564
print( shakespeare_dict.get( 'year_of_death' ) )
# prints None


# It is also possible to provide a default value which should be returned when the key that was supplied does not exist, as a second paramater of `get()`.
# 
# Because the key 'number_of_children' has not been set yet in the dictionary named 'shakespeare_dict', the code below prints the number 0, which is the value that is supplied as a second parameter. 

# In[5]:


print( shakespeare_dict.get( 'number_of_children', 0 ) )


# ## Another way of creating dictionaries
# 
# Instead of starting with an empty dictionary, and adding items one by one, it is also possible to populate full dictionaries upon their creation using a syntax that makes use of curly brackets.
# Within these brackets, you need to list all the needed key and value pairs.
# 
# The keys and the values need to be separated by a colon. All individual items in the dictionary (i.e. the full key and value pairs) need to separated by commas.
# 
# Let's create a dictionary of countries and their capitals.

# In[6]:


capitals = { 
    'France': 'Paris', 
    'Spain': 'Madrid',
    'The Netherlands' : 'Amsterdam', 
    'Belgium': 'Brussels',
    'Italy': 'Rome',
    'Germany': 'Berlin',
    'Denmark': 'Copenhagen'
} 


# ## Navigating a dictionary
# 
# You can list all the elements in a dictionary via the `for` keyword.
# When you *iterate over a dictionary*, you get its *keys*, one at a time.
# You can then use that key to look up its value.

# In[7]:


# Our dictionary has the country as the key, so we name our loop variable 'country'
for country in capitals:
    print( f'The capital of {country} is {capitals[country]}.' )


# ## Sorting a dictionary
# 
# By default, all the items in this dictionary are shown in the order in which they were added to the dictionary.  
# 
# When you have created a dictionary named `capitals`, using the code above, it can be sorted by index using the in-built `sorted()` function.
# Strings are sorted alphabetically and integers and floats are sorted numerically. 

# In[8]:


for country in sorted(capitals):
    print( f'The capital of {country} is {capitals[country]}.' )


# It is also possible to sort a dictionary by its values, but that is outside the scope of this tutorial.

# # Exercises

# ## Exercise 6.1.
# 
# The code below creates a new dictionary. This dictionary connects a number of ISBNs to the titles of the books they identify.

# In[9]:


# Create the dictionary
books_by_isbn = {
    9780143105985 : 'White Noise',
    9780241984536 : 'Libra',
    9781925480665 : 'Mao II',
    9781447289395 : 'Underworld',
    9780743595728 : 'The Body Artist',
    9781925480665 : 'Cosmopolis',
    9780330524919 : 'Falling man',
    9781439169971 : 'Point Omega'
}


# 
# Add the novel Zero K to the dictionary. This novel has ISBN13 9781501138072.

# In[15]:


books_by_isbn[9781501138072] = 'Zero K'


# Write some code which can print the title that corresponds to ISBN 9781447289395.

# In[18]:


isbn = 9781447289395
print(f'The title that corresponds with {isbn} is {books_by_isbn[isbn]}.')


# Print a list of all the novels. Display both the ISBN and the title. 

# In[20]:


for isbn in books_by_isbn : 
    print(f'The book {books_by_isbn[isbn]} has ISBN {isbn}.')


# ## Exercise 6.2.
# 
# Using the dictionary `person_data` below, print the following sentence: “Louis Elsevier was a printer. He was born in 1540 in Leuven and died in 1617 in Leiden.”

# In[2]:


person_data = dict()

person_data["firstName"] = 'louis'
person_data["lastName"] = 'elsevier'
person_data["profession"] = 'printer'
person_data["yob"] = 1540
person_data["yod"] = 1617
person_data["pob"] = 'leuven'
person_data["pod"] = 'leiden'

# Print the sentence
sentence = f"{person_data['firstName'].title()} {person_data['lastName'].title()} was a {person_data['profession']}. He was born in {person_data['yob']} in {person_data['pob'].title()} and died in {person_data['yod']} in {person_data['pod'].title()}."

print(sentence)


# ## Exercise 6.3.
# 
# We have a dictionary of countries in the European Union and their capitals.

# In[3]:


# Create the dictionary
eu_capitals = {
    'Italy': 'Rome', 'Luxembourg': 'Luxembourg',
    'Belgium': 'Brussels', 'Denmark': 'Copenhagen',
    'Finland': 'Helsinki', 'France': 'Paris',
    'Slovakia': 'Bratislava', 'Slovenia': 'Ljubljana',
    'Germany': 'Berlin', 'Greece': 'Athens',
    'Ireland': 'Dublin', 'Netherlands': 'Amsterdam',
    'Portugal': 'Lisbon', 'Spain': 'Madrid',
    'Sweden': 'Stockholm',
    'Cyprus': 'Nicosia', 'Lithuania': 'Vilnius', 
    'Czech Republic': 'Prague', 'Estonia': 'Tallin',
    'Hungary': 'Budapest', 'Latvia': 'Riga',
    'Malta': 'Valetta', 'Austria': 'Vienna',
    'Poland': 'Warsaw', 'Croatia': 'Zagreb',
    'Romania': 'Bucharest', 'Bulgaria': 'Sofia'
}


# Using this dictionary, print a sentence which gives information about the current number of countries in the EU.

# In[5]:


# How many countries are in the EU dictionary?
print(f' The EU has {len(eu_capitals)} countries.')


# Print a list of all the countries of the EU in alphabetical order.

# In[11]:


# Print the list of countries in alphabetical order
for eu_country in sorted(eu_capitals) :
    print (eu_country)


# Finally, for each country, print the following sentence: "The capital of [ *country* ] is [ *capital* ]."

# In[9]:


# Print the capitals of these countries
for eu_country in eu_capitals :
    print(f'The capital of {eu_country} is {eu_capitals[eu_country]}.')

