

lst = [115.3,123.5,234.5,197.3,210.1,155.6,123.2,151.1,151.1]



lst


import numpy as np
import pandas as pd

print("mean - ",np.mean(lst))


# In[36]:


print("median - ", np.median(lst))


# In[17]:


import statistics as st


# In[35]:


print("mode - ",st.mode(lst))


# In[33]:


print("standard deviation - ",np.std(lst))


# In[34]:


print("variance - ",st.variance(lst))


# In[30]:


# explicit function to normalize array
def normalize(arr, t_min, t_max):
	norm_arr = []
	diff = t_max - t_min
	diff_arr = max(arr) - min(arr)
	for i in arr:
		temp = (((i - min(arr))*diff)/diff_arr) + t_min
		norm_arr.append(temp)
	return norm_arr


range_to_normalize = (0,1)
normalized_array_1d = normalize(lst,
								range_to_normalize[0],
								range_to_normalize[1])

# display original and normalized array
print("Original Array = ",array_1d)
print("Normalized Array = ",normalized_array_1d)


# In[29]:


mean=np.mean(lst)
stan_dev=np.std(lst)
standardisation=[(x-mean)/(stan_dev) for x in lst]
standardisation




