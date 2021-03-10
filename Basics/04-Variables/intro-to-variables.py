###################################################################################
###################################################################################
## Section 04 - Variables in Python
###################################################################################
###################################################################################

# Variable - A Name\Label assigned to an object
# == Assignemnt Operator

name = "Ravi"
age = 30
# snake_case - seperating words with underscore
# snake_case is used by community
print(name)
print(age//2)
print("My name is", name, "and age is", age)
#value of variable can change over execution of program

age = 31
print("My name is", name, "and age is", age)
age = 27+10
# what happens on RIGHT of =, gets evaluated first

fact_or_fiction = 6<10
print(fact_or_fiction)
 # In dynamically typed language (Pytjon), a variable can be reassinged to any 
 # type of object

 ######################################
# Python is a consenting adult language
# Technically, ules are not required, but we follow some while writing code
# like snake_case

### Variable Namind Rules

# No space
# first char= Letter\_
# Variable names are Case-sensitive
#

###################################################################################
## Multiple Variable Assignment
###################################################################################

a=5
b=5
# Better method
a=b=5
# can be done for integers
# we are not poining a to b, a is not permanently tied to b
print(a,b)
# if we change b, a wont change
b=10
print(a,b)
# It's just two different datatypes poining to same  value

##### Assigning multiple variable to multiple values
a,b = 15,20
print(a,b)
## On RIGHT side, type values, on LEFT type variable names (in same order)
# Python uses Tuples to achienve this
c,r,e = [a],'a',{'a'}
print(c,r,e )
print(type(c))
print(type(r))
print(type(e))

###################################################################################
## Augmented Assignment Operator
###################################################################################

# A shortcut to overwrite variable value.
# came in python 2.0

a = 1
a =  a + 2
print(a)

# Pythons preffererd way
a += 2 # Augmented Assignemt Operator
print(a)


word = 'race'
word += 'car'
print(word)


#a += b is essentially the same as a = a + b, except that:
    # + always returns a newly allocated object, but += should 
    #   (but doesn't have to) modify the object in-place if it's mutable (
    #    e.g. list or dict, but int and str are immutable).
    # In a = a + b, a is evaluated twice.


###################################################################################
## Collecting User Input with the Input Function
###################################################################################
first_name  = input("What is your First Name ")
#Always pass a SPACE at end, as pythons puts cursor at the end
print("Hello ", first_name)

# Prompt the user for two numbers, one at a time
# Print sum of both

a = int(input("Enter a Number: "))
b = eval(input("Enter another Number: "))
print('Sum is ', a+b)


# Can use nested functions. 
#Python workds inside out (in nested functions)

#  https://realpython.com/inner-functions-what-are-they-good-for/


###################################################################################
##  Name Error, Value Error--- Exceptions!
###################################################################################

# Syntactitacl, logical, langauage specific errors come
# Traceback: A records which shows where interpreter ran into error while running code

#Built in Exceptions->
### NameError:
#   when interpreter is unable to find name ( a variable)
#   When we forget to define variable\typeerror


## TypeError:
# Add a string and number!
# Operating on mismatching DataTypes

#print("5"+3) != print(3+"5")
# whatever is left, python sees that as base Type

##Value Error
#   Right Type, but inappropriate value
#   int("xyz")


## SyntaxError
#   When we type wrong syntax. This is not parsed
#  EOL while scanning file scanning literal


