"""
Example of "Earth" statistical analysis
http://orange.biolab.si/blog/2011/12/20/earth-multivariate-adaptive-regression-splines/
"""
import Orange,numpy, os, orange
from Orange.regression import earth
from matplotlib import pylab as pl
from numpy import polyfit, array, poly1d


# Change working directory to get data
os.chdir("C:/Documents and Settings/amcelhinney/My Documents/GitHub\
/MCS507--Project-3")



data = orange.ExampleTable("4_groups")
print data.domain.attributes
print data[:4]


# Divide data into training and validation data sets
index=Orange.data.sample.SubsetIndices2(p0=0.70)
ind=index(data)
data_training=data.select(ind,0)
data_validation=data.select(ind,1)

# Verify the num. training + num. validation data = num. original data
len(data_training)+len(data_validation)==len(data)



def unique(data, class_col):
    """
    Creates a list of unique obversations from data
    class_col=the column number containing the group
    """
    groups=[]
    for i in range(len(data)):
        # Check to see if this group has been added to groups
        if data[i][class_col] not in groups:
            groups.append(data[i][class_col])
    return groups

r=unique(data,2); r


# Split the data into unique groups
def unique_split(data,class_col):
    # Get the list of unique groups
    r=unique(data,class_col)
    p=[]
    for q in range(len(r)):
        p.append([])
    for i in range(len(data)):
        #print i
        for j in range(len(r)):
            #print j
            if data[i][class_col]==r[j]:
                p[j].append(data[i])

    return p

p=unique_split(data,2)

# Calculate the mean and standard deviations for each class
def summary_stats(data, class_col):
    """
    Returns the mean and standard deviation of the data set for ecah category
    """
    p=unique_split(data,class_col)
    for i in range(len(p)):
        
        





    
        
        
        




            
            
            
            
            
