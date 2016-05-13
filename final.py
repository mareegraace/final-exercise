
# coding: utf-8

# In[5]:

import csv
import matplotlib.pyplot as mplt

with open("gapminder_gdp_americas.csv") as csvf:
    f = csv.reader(csvf, delimiter = ',')
    i = 0
    gdps = [[]]
    
    
    for maris in f:
        for graces in maris:
            col = i % len(maris)
            if(len(gdps) < col + 1):
                gdps.append([])
            if(i > len(maris) and col > 0):
                gdps[col].append(float(graces))
            i += 1
    del gdps[0]
    averages = []
    for i in gdps:
        averages.append(sum(i)/len(i))
    
    n = []
    x = range(len(averages))
    for i in x:
        j = (i * 5) + 1952
        n += [str(j)]
    
    mplt.bar(x,averages)
    mplt.xticks(x, n, rotation = 'vertical')
    
    mplt.savefig('final.png')
    print("look at my graph huehue")


# In[ ]:



