
# coding: utf-8

# # Soccer scores and poisson distribution
# # Predicting Football Results With Statistical Modelling
# Data downloaded from [here](http://www.football-data.co.uk/englandm.php)
# 
# Some code has been taken from [here](https://dashee87.github.io/football/python/predicting-football-results-with-statistical-modelling/)

# In[1]:

import pandas as pd

import numpy as np
import seaborn
from scipy.stats import poisson,skellam

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:

epl_1617 = pd.read_csv("TeamStats.csv")
epl_1617 = epl_1617[['HomeTeam','AwayTeam','FTHG','FTAG']]
epl_1617 = epl_1617.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})
epl_1617.head()


# In[ ]:




# In[3]:

home = []
away = []
diff = []
total = []
for m in range(0, len(epl_1617)):
#  print (epl_1617['HomeGoals'][m], epl_1617['AwayGoals'][m])
    home.append(epl_1617['HomeGoals'][m])
    away.append(epl_1617['AwayGoals'][m])
    diff.append(epl_1617['HomeGoals'][m] - epl_1617['AwayGoals'][m])
    total.append(epl_1617['HomeGoals'][m] + epl_1617['AwayGoals'][m])


# In[4]:

#####################################
##Measure probability distribution. computes also average
## value and standard deviation
#####
def measure_probability_distribution (outcomes):
    
    average_value = 0.0
    variance = 0.0
    
    pdf = {}
    norm = 0.0
    
    ##count number of observations
    for x in outcomes:
        if x not in pdf:
            pdf[x] = 0.0
        pdf[x] += 1.0
        norm += 1.0
        
        average_value += x
        variance += x*x
        
        
    average_value /= norm
    variance /= norm
    variance = variance - average_value * average_value
        
        
    ##normalize pdf
    for x in pdf:
        pdf[x] /= norm
    
    
    return pdf, average_value, variance
#####################################



# In[6]:

pdf, av, var = measure_probability_distribution (total)






##visualize histogram

plt.figure(figsize=(10,10))
plt.rc('text', usetex=True)
plt.rc('font', size=32, **{'family':'DejaVu Sans','sans-serif':['Helvetica']})
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8


title = '$\\langle x \\rangle = ' + '% .2f' % av + ' \\quad \\sigma^2 = ' + '% .2f' % var + '$'
plt.title(title, fontsize = 20)


plt.xlabel('total number of goals in a game', size=32)
plt.ylabel('probability distribution', size=32)
plt.xticks(size=32)
plt.yticks(size=32)


##construct two lists for  visualization
x = []
Px = []
for q in pdf:
    x.append(q)
    Px.append(pdf[q])
    

plt.bar(x, Px, color = 'red', align='center', alpha=0.5)



plt.plot(x, poisson.pmf(x, av), linestyle='-', linewidth=2.0, color='k', label='poisson pmf')



plt.show()


# In[7]:

pdf_h, av_h, var_h = measure_probability_distribution (home)
pdf_v, av_v, var_v = measure_probability_distribution (away)





##visualize histogram

plt.figure(figsize=(10,10))
plt.rc('text', usetex=True)
plt.rc('font', size=32, **{'family':'DejaVu Sans','sans-serif':['Helvetica']})
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8



plt.xlabel('total number of points in a game')
plt.ylabel('probability distribution')


##construct two lists for  visualization
x = []
Px = []
for q in pdf_h:
    x.append(q)
    Px.append(pdf_h[q])
    

plt.bar(x, Px, color = 'red', align='center', alpha=0.5, label = 'home')
plt.plot(x, poisson.pmf(x, av_h), linestyle='-', linewidth=2.0, color='red', label = '$\lambda_h = '+'%.2f' % av_h+'$')




##construct two lists for  visualization
x = []
Px = []
for q in pdf_v:
    x.append(q)
    Px.append(pdf_v[q])
    

plt.bar(x, Px, color = 'blue', align='center', alpha=0.5, label = 'visitors')
plt.plot(x, poisson.pmf(x, av_v), linestyle='-', linewidth=2.0, color='blue', label = '$\lambda_a = '+'%.2f' % av_v+'$')


plt.xlabel('total number of goals in a game', size=32)
plt.ylabel('probability distribution', size=32)
plt.xticks(size=32)
plt.yticks(size=32)



plt.legend(loc=1,  numpoints=1, prop={'size':20})

plt.show()


# In[8]:

pdf, av, var = measure_probability_distribution (diff)






##visualize histogram

plt.figure(figsize=(10,10))
plt.rc('text', usetex=True)
plt.rc('font', size=32, **{'family':'DejaVu Sans','sans-serif':['Helvetica']})
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8


title = '$\\langle x \\rangle = ' + '% .2f' % av + ' \\quad \\sigma^2 = ' + '% .2f' % var + '$'
plt.title(title, fontsize = 20)


plt.xlabel('goal difference', size=32)
plt.ylabel('probability distribution', size=32)
plt.xticks(size=32)
plt.yticks(size=32)


##construct two lists for  visualization
x = []
Px = []
for q in pdf:
    x.append(q)
    Px.append(pdf[q])
    

plt.bar(x, Px, color = 'red', align='center', alpha=0.5)



#plt.plot(x, poisson.pmf(x, av), linestyle='-', linewidth=2.0, color='k', label='poisson pmf')




plt.plot(sorted(x), skellam.pmf(sorted(x), epl_1617.mean()[0],  epl_1617.mean()[1]), linestyle='-', linewidth=2.0, color='k', label='skellam pmf')



plt.show()


# In[ ]:



