#!/usr/bin/env python
# coding: utf-8

# # 1.What are the two values of the Boolean data type? How do you write them?

# The two types of bollean data types are "True" and "False" and they represent if the given statement is true or false.
# Both will be written in the form they are true = "True" and false ="False"
#     

# # 2. What are the three different types of Boolean operators?
# 
# The three typer of boolean operator are "OR(", "AND", "NOT"
# 

# # 3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# AND Operator :
# Input A	Input B	Output
# FALSE	FALSE	FALSE
# FALSE	TRUE	FALSE
# TRUE	FALSE	FALSE
# TRUE	TRUE	TRUE
# 
# 
# OR Operator :
# 
# Input A	Input B	Output
# FALSE	FALSE	FALSE
# FALSE	TRUE	TRUE
# TRUE	FALSE	TRUE
# TRUE	TRUE	TRUE
# 
# 
# NOT Operator:
# 
# Input	Output
# FALSE	TRUE
# TRUE	FALSE
# 

# # 4. What are the values of the following expressions?
# (5 &gt; 4) and (3 == 5)
# not (5 &gt; 4)
# (5 &gt; 4) or (3 == 5)
# not ((5 &gt; 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)

# In[4]:


a=3
b=4
c=5

(c>b) and (a==c)


# In[6]:


if not (c>b):
    print(True)
else:
    print(False)


# In[7]:


if (c>b) or (a == c):
    print(True)
else:
    print(False)


# In[8]:


if not  (c>b) or (a == c):
    print(True)
else:
    print(False)


# In[9]:


if (True and True) and (True == False):
    print (True)
else:
    print(False)


# In[10]:


if (not False) or (not True):
    print (True)
else:
    print(False)


# In[ ]:





# # 5.What are the six comparison operators?

# Equal to (==): This operator checks if the given two values are equal and returns true if they are, and false otherwise. For example, 8 == 8 evaluates to true.
# 
# Not equal to (!=): This operator checks if two values are not equal and returns true if they are not, and false otherwise. For example, 7 != 3 evaluates to true.
# 
# Greater than (>): This operator checks if the left operand is greater than the right operand and returns true if it is, and false otherwise. For example, 7 > 3 evaluates to true.
# 
# Less than (<): This operator checks if the left operand is less than the right operand and returns true if it is, and false otherwise. For example, 7 < 3 evaluates to false.
# 
# Greater than or equal to (>=): This operator checks if the left operand is greater than or equal to the right operand and returns true if it is, and false otherwise. For example, 5 >= 5 evaluates to true.
# 
# Less than or equal to (<=): This operator checks if the left operand is less than or equal to the right operand and returns true if it is, and false otherwise. For example, 5 <= 3 evaluates to false.

# # 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

# Equal to (==) operator is used to compare the equality of two values, while the assignment (=) operator is used to assign a value to a variable.
# 

# In[11]:


#Example
a=2   #assigning the value
b=8
if a==b:# comparing the equality
    print("EQUAL")
else:
    print("NOT EQUAL")


# # 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print(&#39;eggs&#39;)
# if spam &gt; 5:
# print(&#39;bacon&#39;)
# else:
# print(&#39;ham&#39;)
# print(&#39;spam&#39;)
# print(&#39;spam&#39;)

# Answer: Three blocks are 
#     #1 if spam == 10:
#     #2 if spam &gt; 5:
#     #3 else:

# # 8 Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and printsGreetings! if anything else is stored in spam.

# In[13]:


a = float(input("Please enter value of a: "))
if a==1:
    print ("Hello")
elif a==2:
    print("Howdy")
else:
    print("Greetings!")


# # 9.If your programme is stuck in an endless loop, what keys you’ll press?
# If the programme is stuck in an endless loop then we have to press ctrl+c to interupt the loop.

# # 10. How can you tell the difference between break and continue?
# Break statement is use to terminate the loop and transfers control to the next statement after the loop. It is often used to exit a loop based on a certain condition.
# Continue statement is use when encountered inside a loop, the continue statement skips the rest of the current iteration and moves to the next iteration of the loop. It allows you to skip certain parts of the loop's code and continue with the next iteration.

# # 11 In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# range(10)- this will create a sequence of number starting from 0 to 9 as 10 will be excluded (upperbound) andi0 will be included lower bound
# 

# In[14]:


for i in range(10):
    print(i)


# range (0,10) - this will also create a sequence of number starting from 0 to 9 as 10 will be excluded (upperbound) and 0 will be included (lowerbound)
# 

# In[15]:


for i in range(0,10):
    print(i)


# range (0,10,1) - This is similar to range(0, 10), but it includes a third argument, which represents the step value. In this case, the step value is 1, which means it will generate numbers by incrementing 1 at each iteration. So, it will produce the same sequence of numbers as the previous examples, i.e., 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. 

# In[16]:


for i in range(0,10,1):
    print(i)


# # 12 Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[17]:


for i in range (1,11):
    print(i)


# In[19]:


i = 1

while i <= 10:
    print(i)
    i += 1


# # 13 If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# In[20]:


import spam
spam.bacon()


# In[ ]:




