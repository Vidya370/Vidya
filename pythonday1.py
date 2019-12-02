#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=12
print(a)


# In[6]:


#Add two numbers

num1 = 1.5
num2 =6.3
sum = float(num1)+float(num2)
print(sum)


# In[10]:


#Find the largest number

num1 = 10
num2 = 14
num3 = 12
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


# In[11]:


# Program to check if a number is prime or not

num = 407
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       

else:
   print(num,"is not a prime number")


# In[1]:


full_name='vidya'
age= 24
is_new= True
print("hi"+ full_name)
print("you are" ,age)


# In[1]:


name= input("Enter your name")
age=input("Enter your age")
print("hi"+ name)
print("you are" ,age)



# In[1]:


name= input("what is your name? ")
color= input("which is your fav color? ")
print(f'{name} likes {color}')


# In[ ]:


birthdate= input("Enter your age")
age= 2019-int(birthdate)
print("your age is"+age)


# In[ ]:




