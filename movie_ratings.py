
# coding: utf-8

# In[9]:

from urllib.request import Request, urlopen
import pickle
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from scipy import stats


# In[10]:

##download gross by movie rating

ratings = ['G', 'PG', 'PG-13', 'R', 'NC-17']


for rating in ratings:

    url = 'http://www.boxofficemojo.com/alltime/domestic/mpaa.htm?page='+rating+'&sort=gross&order=DESC&p=.htm' 
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    
    print (url)
    
    #save to disk
    filename = 'Data_Movies/'+ rating + '.html'
    f = open(filename,'w')
    f.write(html.decode('utf-8'))
    f.close()




# In[11]:

##parsing data


data = {}


for rating in ratings:
    
    filename = 'Data_Movies/'+ rating + '.html'
    soup = BeautifulSoup(open(filename), 'lxml')
    
    table = soup.find_all('table')
#     print (table[2].prettify())
    
    rows1 = table[2].find_all('tr', attrs={'bgcolor' : '#ffffff'})
    rows2 = table[2].find_all('tr', attrs={'bgcolor' : '#f4f4ff'})
    
   

    data[rating] = {}

    
    for row in rows1:
        columns = row.find_all('td')
        
        rank = columns[0].get_text()
        order = columns[1].get_text()
        name = columns[2].get_text()
        studio = columns[3].get_text()
        lf_gross = columns[4].get_text()
        year = columns[5].get_text()
        
        
        lf_gross = lf_gross.replace('$', '')
        lf_gross = lf_gross.replace(',', '')
        year = year.replace('^', '')
        
        data[rating][name] = []
        data[rating][name].append(float(year))
        data[rating][name].append(float(lf_gross))
        
#         print (rank, ':', order, ':', name,':', studio, ':', lf_gross, ':', year)
        
        
        
    for row in rows2:
        columns = row.find_all('td')
        
        rank = columns[0].get_text()
        order = columns[1].get_text()
        name = columns[2].get_text()
        studio = columns[3].get_text()
        lf_gross = columns[4].get_text()
        year = columns[5].get_text()
        
        
        lf_gross = lf_gross.replace('$', '')
        lf_gross = lf_gross.replace(',', '')
        year = year.replace('^', '')
        
        data[rating][name] = []
        data[rating][name].append(float(year))
        data[rating][name].append(float(lf_gross))
        
#          print (rank, ':', order, ':', name,':', studio, ':', lf_gross, ':', year)
        
        
        
    
    


# In[12]:

##save to hard drive
with open('dataset.pickle', 'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


# In[13]:

#read from hd
with open('dataset.pickle', 'rb') as handle:
    data_r = pickle.load(handle)
# print (data_r)


# In[ ]:




# In[14]:

plt.figure(figsize=(15,10))
plt.rc('text', usetex=True)
plt.rc('font', size=24, **{'family':'DejaVu Sans','sans-serif':['Helvetica']})
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8



#####

rating = 'G'  

x = []
y = []
for m in data[rating]:
    x.append(data[rating][m][0])
    y.append(data[rating][m][1])

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print ('rating : ', rating)
print ('alpha : ', intercept)
print ('beta : ', slope)
print ('correlation coefficient : ', r_value)
print ('\n')


plt.plot(x,y, marker='o', color ='blue', markersize=5, linewidth=0, label = rating)
best_fit_x = np.arange(1930, (2020- 1930 / 10000.0))
best_fit_y = intercept + slope * best_fit_x
plt.plot(best_fit_x, best_fit_y, color ='blue', markersize=0, linewidth=3, linestyle='-', alpha = 0.5)






#####

rating = 'PG'  

x = []
y = []
for m in data[rating]:
    x.append(data[rating][m][0])
    y.append(data[rating][m][1])

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print ('rating : ', rating)
print ('alpha : ', intercept)
print ('beta : ', slope)
print ('correlation coefficient : ', r_value)
print ('\n')


plt.plot(x,y, marker='s', color ='red', markersize=5, linewidth=0, label = rating)
best_fit_x = np.arange(1930, (2020- 1930 / 10000.0))
best_fit_y = intercept + slope * best_fit_x
plt.plot(best_fit_x, best_fit_y, color ='red', markersize=0, linewidth=3, linestyle='-', alpha = 0.5)



#####

rating = 'PG-13'  

x = []
y = []
for m in data[rating]:
    x.append(data[rating][m][0])
    y.append(data[rating][m][1])

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print ('rating : ', rating)
print ('alpha : ', intercept)
print ('beta : ', slope)
print ('correlation coefficient : ', r_value)
print ('\n')


plt.plot(x,y, marker='v', color ='black', markersize=5, linewidth=0, label = rating)
best_fit_x = np.arange(1930, 2020, (2020- 1930) / 10000.0)
best_fit_y = intercept + slope * best_fit_x
plt.plot(best_fit_x, best_fit_y, color ='black', markersize=0, linewidth=3, linestyle='-', alpha = 0.5)




#####

rating = 'R'  

x = []
y = []
for m in data[rating]:
    x.append(data[rating][m][0])
    y.append(data[rating][m][1])

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print ('rating : ', rating)
print ('alpha : ', intercept)
print ('beta : ', slope)
print ('correlation coefficient : ', r_value)
print ('\n')


plt.plot(x,y, marker='^', color ='green', markersize=5, linewidth=0, label = rating)
best_fit_x = np.arange(1930, 2020, (2020- 1930) / 10000.0)
best_fit_y = intercept + slope * best_fit_x
plt.plot(best_fit_x, best_fit_y, color ='green', markersize=0, linewidth=3, linestyle='-', alpha = 0.5)



    

    
    
plt.ylabel('gross')
plt.xlabel('year')
plt.legend(loc=2,  markerscale=2, numpoints=1, prop={'size':20})

plt.show()  


# In[ ]:



