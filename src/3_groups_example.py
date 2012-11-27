"""
http://orange.biolab.si/doc/ofb/c_basics.htm
http://orange.biolab.si/doc/ofb/c_performance.htm

"""
import Orange,numpy, os, orange
from Orange.regression import earth
from matplotlib import pylab as pl
from numpy import *
import matplotlib.pyplot as plt

# Change working directory to get data
#os.chdir("C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507--Project-3")
os.chdir('C:/Documents and Settings/amcelhinney/My Documents/GitHub/MCS507HW/MCS 507 Homework 4/MCS507--Project-3')



data = orange.ExampleTable("3_groups")
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

#group_1
group_1=[]
for i in range(len(p[0])):
    group_1.append([float(p[0][i][0]),float(p[0][i][1])])
group_1=array(group_1)

c1=cov(group_1.T)
m1=mean(group_1.T[0]);m2=mean(group_1.T[1])
#mu=[m1,m2]
mu1=[m1 for i in range(len(group_1.T[0]))]
mu2=[m2 for i in range(len(group_1.T[0]))]
mu_1=[mu1,mu2]

#group_2
group_2=[]
for i in range(len(p[1])):
    group_2.append([float(p[1][i][0]),float(p[1][i][1])])
group_2=array(group_2)

c2=cov(group_2.T)
m1=mean(group_2.T[0]);m2=mean(group_2.T[1])
#mu=[m1,m2]
mu1=[m1 for i in range(len(group_2.T[0]))]
mu2=[m2 for i in range(len(group_2.T[0]))]
mu_2=[mu1,mu2]

#group_3
group_3=[]
for i in range(len(p[2])):
    group_3.append([float(p[2][i][0]),float(p[2][i][1])])
group_3=array(group_3)

c3=cov(group_3.T)
m1=mean(group_3.T[0]);m2=mean(group_3.T[1])
#mu=[m1,m2]
mu1=[m1 for i in range(len(group_3.T[0]))]
mu2=[m2 for i in range(len(group_3.T[0]))]
mu_3=[mu1,mu2]


# Multivariate Normal Density
def mvnorm(b,mean,cov):
    """
    Returns vector of densities
    Adapted from http://lmf-ramblings.blogspot.com/2009/07/multivariate-normal-distribution-in.html
    """
    k = b.shape[0]
    part1 = numpy.exp(-0.5*k*numpy.log(2*numpy.pi))
    part2 = numpy.power(numpy.linalg.det(cov),-0.5)
    dev = b-mean
    part3 = numpy.exp(-0.5*numpy.dot(numpy.dot(dev.transpose(),numpy.linalg.inv(cov)),dev))
    dmvnorm = part1*part2*part3
    return dmvnorm

# Verify that the mean of group 1 in p1 is higher than p2 and p3
p1=mvnorm(group_1.T,mu_1,c1)
# Group 2
m1=mean(group_2.T[0]);m2=mean(group_2.T[1])
mu1=[m1 for i in range(len(group_1.T[0]))]
mu2=[m2 for i in range(len(group_1.T[0]))]
mu_2=[mu1,mu2]
p2=mvnorm(group_1.T,mu_2,c2)
# Group 3
m1=mean(group_3.T[0]);m2=mean(group_3.T[1])
mu1=[m1 for i in range(len(group_1.T[0]))]
mu2=[m2 for i in range(len(group_1.T[0]))]
mu_3=[mu1,mu2]
p3=mvnorm(group_1.T,mu_3,c3)


mean(p1)
mean(p2)
mean(p3)

# Score group 1
scored=[]
for i in range(len(p1)):
    if (p1[i]>=p2[i] and p1[i]>=p3[i]):
        scored.append(1)
    elif (p1[i]<=p2[i] and p1[i]>=p3[i]):
        scored.append(2)
    elif (p1[i]>=p2[i] and p1[i]<=p3[i]):
        scored.append(3)
    else:
        scored.append(999)
    


    
        
        
        


# Orange Code
import orange, orngTest, orngStat, orngTree   
classifier = orange.BayesLearner(data)
bayes = orange.BayesLearner()
bayes.name = "bayes"
learners = [bayes]
results = orngTest.crossValidation(learners, data, folds=10)
# output the results
print "Learner CA IS Brier AUC"
for i in range(len(learners)):
    print "%-8s %5.3f %5.3f %5.3f %5.3f" % (learners[i].name, \
                                            orngStat.CA(results)[i], orngStat.IS(results)[i], orngStat.BrierScore(results)[i], orngStat.AUC(results)[i])
            
