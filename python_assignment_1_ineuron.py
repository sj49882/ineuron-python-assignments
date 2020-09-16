#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed  in a comma-separated sequence on a single line. 

m = list()
for i in range(2000, 3200):
    if (i % 7) == 0 and (i % 5) != 0:
        m.append(i)
        print(str(m)[1:-1], sep = ",")
        


# In[4]:


#Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name. 

first_name = input("Input your First Name:")
last_name = input("Input your Last Name:")
print(last_name + " " + first_name)


# In[5]:


#Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r 3 

pi = 3.14
r = 6.0
V = 4.0/3.0 * pi * r**3
print("The volume of sphere is:", V)


# In[ ]:




