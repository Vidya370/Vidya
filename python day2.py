#!/usr/bin/env python
# coding: utf-8

# ##Check all built-in lists methods and examples;
# 
# 
# 

# In[3]:


##index()

vowels = ['a', 'e', 'i', 'o', 'i', 'u']
index = vowels.index('e')
print('The index of e:', index)
index = vowels.index('i')
print('The index of i:', index)


# In[4]:


##extend()

language = ['French', 'English', 'German']

language1 = ['Spanish', 'Portuguese']

language.extend(language1)

print('Language List: ', language)


# In[5]:


##insert()

vowel = ['a', 'e', 'i', 'u']

vowel.insert(3, 'o')

print('Updated List: ', vowel)


# In[7]:


##remove()

animals = ['cat', 'dog', 'rabbit', 'guinea pig']

animals.remove('rabbit')

print('Updated animals list: ', animals)


# In[8]:


##count()

vowels = ['a', 'e', 'i', 'o', 'i', 'u']

count = vowels.count('i')

print('The count of i is:', count)


# In[9]:


##pop()

languages = ['Python', 'Java', 'C++', 'French', 'C']

return_value = languages.pop(3)

print('Return Value:', return_value)

print('Updated List:', languages)


# In[10]:


##reverse()

os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

os.reverse()

print('Updated List:', os)


# In[11]:


##sort()

vowels = ['e', 'a', 'u', 'o', 'i']

vowels.sort()

print('Sorted list:', vowels)


# In[12]:


##copy()

list = ['cat', 0, 6.7]

new_list = list.copy()

new_list.append('dog')

print('Old List: ', list)
print('New List: ', new_list)


# In[13]:


##clear()

list = [{1, 2}, ('a'), ['1.1', '2.2']]

list.clear()

print('List:', list)


# In[14]:


##append()

animals = ['cat', 'dog', 'rabbit']

animals.append('goat')

print('Updated animals list: ', animals)


# ##Program Reverse strings using queue.

# In[ ]:





# #Print last 5 lines using queue

# In[ ]:





# 

# ##compare two lists using set theory

# In[1]:


test_list1 = [1, 2, 4, 3, 5] 
test_list2 = [1, 2, 4, 3, 5] 
  
print ("The first list is : " + str(test_list1)) 
print ("The second list is : " + str(test_list2)) 
  
test_list1.sort() 
test_list2.sort() 

if test_list1 == test_list2: 
    print ("The lists are identical") 
else : 
    print ("The lists are not identical") 


# 

# In[21]:


##Print all missing elements in the lists 

test_list = [3, 5, 6, 8, 10] 

print("The original list : " + str(test_list)) 
  
res = [ele for ele in range(max(test_list)+1) if ele not in test_list] 
  
print("The list of missing elements : " + str(res)) 


# In[22]:


##Find the duplicates elements in the lists

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      

duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
print(Remove(duplicate)) 


# In[ ]:




