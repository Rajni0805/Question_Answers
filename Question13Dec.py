#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1. python 2 has complicated syntax
#     python 3 has easier syntax
    
#     to check current version in cmd = python --version


# In[2]:


# Q3. string, list, boolean, tuple, dictionary, set, etc.


# In[3]:


# Q4. mutable data = in mutable data after passing entry data can change
# ex : dictionary, set, list
#     immutable data = in immutable data after passing entry data can not be change
# ex : string, boolean , tuple


# In[7]:


# Q5. because we dont need to print entry every time

# for loop ex:
# i = ["ram", "sam"]
# for x in i:
#     print(x)
    
    
# for b in "ram":
#     print(b)
    
# for c in range(10,101,10):
#     print(c)
    
    
# while loop can run infinite time
# while loop examples:

# i = 1
# n = 5
# while i<=5:
#     print(i)
#     i = i+1

# i = 1
# n = int(input("enter your number"))
# while i<=n:
#     print(i)
#     i = i+1


# In[9]:


# Q6. two type of functions pre defined & user defined
# use of functions = in function we create a code one time and use many times by call to function

# lambda function can take any number of arguments and lambda have only one expression 
# x = lambda a, b : a * b
# print(x(2,3))


# map function = to replace the value ex: male:0 , female:1


# In[ ]:


# Q7.
# list = list data only written in square bracket ex : []
#         list is mutable
    
# tuple = tuple data only written in round bracket ex: ()
#     tuple is immutable




# In[16]:


# Q8. dictionary = oredred collection of key & value   my_dict = {“name”: “Ram” , “age”: 20}



# set = unordered collection 

# x = {1, 2, 3}
# y = {1, 5, 3, 4,}

# z = x.intersection(y)
# print(z)


# a = {1, 2, 3}
# b = {1, 5, 3, 4,}

# c = a.union(b)
# print(c)


# In[19]:


# Q10. To create a new list using previous list
# a = ["ram", "shyam", "gopal"]
# newlist = []

# for x in a:
#   if "ram" in x:
#     newlist.append(x)

# print(newlist)


# In[28]:


# Q12. import numpy as np
# import pandas as pd

# a = np.array([1,2,3])
# b = np.array([4,5,6])

# np.hstack((a,b))
# np.vstack((a,b))


# In[35]:


# Q13. zeros() = to print array shape in zero value
# np.zeros((2,3))

# ones() = to print array shape in one value
# np.ones((2,3))

# eye() = diagonal elements are 1 and others are 0

# diag() = to print in diagonal shape value only 0

# rand() = to fill all random value

# randint() = to fill value like (0,5) 

# seed() = to create id for same value

# unique() = to sort unique value


# In[47]:


# Q14.
# a = np.array([[1,2,3,4,5,6]])
# a


# In[49]:


# b = a.reshape(3,2)
# b


# In[41]:


# Q15. 

# argmin() = where minimun number on which indexing
# a = np.array([1,2,3])
# np.argmin(a)


# argmax() = where maximum number on which indexing

# np.argmax(a)


# In[ ]:





# In[ ]:





# In[ ]:




