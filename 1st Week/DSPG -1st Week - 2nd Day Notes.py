#!/usr/bin/env python
# coding: utf-8

# # **DATA SCIENCE FOR PUBLIC GOOD**

# ` 1. HAFTA 2.GÜN`
# 

# ## 1. Stringlerde indexleme 
# 
# 

# In[12]:


"deniz"[1]


# In[4]:


a = "ahmet"
print(a[3])
print(a[-1])


# In[6]:


a[len(a)-1]  # son değişkene ulaşmak n_1.ci elemana ulaşmak demektir.


# In[8]:


a[5]  # index sayısını fazla yazdığımızda index out of range hatası alırız


# In[10]:


isim = "deniz"
isim[-5]  #ilk elemanı verir


# **Stringlerde indexleme yapılaiblir ancak Stringle "immutable" yapılar oldukları için eleman değişimi yapılamaz.**

# ## 2. Stringlerde slicing
# 
# a[başlangıç:bitiş:adım]

# In[14]:


isim[:3]


# In[15]:


isim[:]


# In[18]:


isim[1:20]  #İndexing yaparken alınan out of range erroru burada slicingde alınmıyor.


# In[22]:


isim[0:4:2]


# In[25]:


isim[0:10:-1]


# In[28]:


isim[10:0:-1] #0'a kadar aldı son sayıyı dahil etmedi.


# In[31]:


isim[10::-1]


# In[34]:


isim[::20]


# In[36]:


isim[::-20]


# ## 3. Stringlerde Casting

# In[43]:


l = [3,6,4,7,2]
l.sort()    #Obje üzerinde metot çağırma yapıldığında l listesi değiştirilmiş olur.
l


# In[48]:


l = [3,6,4,7,2]   # Bu şekilde yapmış olsaydık değişime uğramayacaktı.
sorted(l)        # Metotlar bu şekilde kullanılır. Orneğin listlerde .apped(), setlerde .add() metotları o variable çeşidine uygundur.


# In[49]:


l


# In[52]:


a ="5"
int(a)


# In[55]:


a = "5.6"
int(a)       #inte cevirebilmem için önce floata sonra inte çevirmem gerekir.


# In[58]:


int(float(a))


# In[61]:


ord("a")  #"bianary sayı sistemindeki karşılığı vermiş oluyor."


# ## 4. Input

# In[64]:


x = input("bir sayı girin:")


# In[66]:


x + 10  #inputlar string olarak döner.


# In[69]:


x = int(input("bir sayı girin:"))
x + 10


# In[70]:


type(x)


# ## 5. Comments

# In[72]:


# "#" işareti ile kodun devamına başına yorum yazılabilir


# In[73]:


#fonksiyonların içine üç tırnak ile comment blogu eklenebilir '''gibi'''


# In[75]:


# crtl ile paralel olarka iki imleç oluşturma 


# In[ ]:


# find + replace ile değişkenlerin adını tolu olarak değiştirebiliriz. (ctrl+f ile veya  editten)


# In[ ]:




