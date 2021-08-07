#!/usr/bin/env python
# coding: utf-8

#  **Data Science for Public Good Bootcamp** 
# ---
# 

# `1. Hafta Ders Notları-31/07/2021`

# **Scalar Veri Tipleri:**
# Alt parçalara bölünemeyen, alt karakter içermeyen veri tipleridir.
# * **Integer:** 5, 6 7
# * **Float:** 0.56 , 6.0
# * **Boolean:** True, False

# **Non Scalar Veri Tipleri:** 
# Daha alt parçalara bölünebilen içsel yapısına erişilebilen ver tipleridir.
# * **String:** "Elif"
# * **List:** [1, 2, 3]
# * **Tuple:** (1, 2, 3)
# * **Dictionary:** [a = "ali", b = "ayşe"]

# **Type Casting:** Veri tiplerini farklı tiplere dönüştürmek için kullanılır.

# In[8]:


int(2.4) # Dönüştürme


# In[9]:


int(2.9)


# In[12]:


float(4)


# **Reserved Keywords:** Pythonun daha önce kendisine ayırmış olduğu *for, if result, print* gibi ifadelerdi. Bu ifadeler Variables olarak kullanılmamalıdır. 

# **Variable Assignment:** 

# In[17]:


limon_fiyat = 10


# In[18]:


a1 = limon_fiyat * 100


# In[19]:


a2 = limon_fiyat * 70


# In[21]:


a3 = limon_fiyat * 30


# In[22]:


print(a1, a2, a3)


# **Expressions (İfadeler):**

# * **Object** ve **operatorler** birleşimi **expressionsları** oluşturur.
# * İfadeler (object) (operator) (object) -> (object)
# * Expressionsların tiplerini operatorun uygulantığı objectler belirler.

# **Math Operators**
# * **Additions: +**
# * **Substraction: -**
# * **Multiplication: ***
# * **Division: /**

# In[26]:


4 + 4.5  # Toplanan objelerden biri floatsa sonuç floattır.


# In[28]:


5.5-2.5  #  Objelerden biri floatsa sonuç floattır.


# In[29]:


6 / 2 #Tüm bölme işlemlerinde sonuç floattır


# * **Int Division  //**: Birinci objenin içinde ikinci objeden tam olarak kaç tane vardır.

# In[32]:


5 // 2


# In[34]:


5 //2.0 # Objelerden biri foat ise sonuç floattır.


# In[35]:


4.2 // 5


# * **Mod Operator %**: Kalan operatorü değildir. Pozitif sayılarda kalanı verir. Negatif sayılarda ise ozitif değerlere kadar ekleyerek ilerler.

# In[37]:


5 % 2


# In[40]:


10 % 3


# In[43]:


-22 % 5


# In[48]:


-22 % 2  # Tam bölünen negatif sayıları kontrol etmek için kullanılabilir.


# In[50]:


35 % 3 


# In[51]:


-35 % -3


# * ** **Operator** :

# In[53]:


2**3


# **String Veri Tipi:** Karakterlerden veya onların çeşitli kombinasyonlarından oluşur. 
# * **Immutable veri tipidir** Yani elemanları değiştirilemez. 
# * Ancak indexing veya slicing işlemleri yapılabilir. 

# In[54]:


"merhaba"


# In[55]:


type("merhaba")


# In[60]:


"merhaba"[0] # Non-scalar veri tipi olan bir string ifadenin alt karakterleride string dolayısıyla non-scalardır.


# In[58]:


type("merhaba"[0]) 


# **Escape Sequence**: \ opr. öncesinde geldiği karakterin özel olarak algılanmasını sağlar.

# In[61]:


'Bugün Kadıköy\'e gidiyorum'


# In[68]:


print("hey\nnasilsin")  # \n: alt satırdan başlatmak için kullanılır.


# In[71]:


print("hey\tnasilsin") # \t: 4 boşluk bırakmak için kullanılır.


# In[74]:


print("hmmm \"")


# **String Concatenation**

# In[76]:


"elif"+" "+"baghirov"


# In[77]:


a ="elif"
b ="baghirov"


# In[78]:


isim = a + " " + b


# In[79]:


isim


# In[83]:


isim*4


# **len():** karakterleri sayar. Boşluklarda karakter olarak sayılır.

# In[85]:


len("elif baghirov")


# In[ ]:




