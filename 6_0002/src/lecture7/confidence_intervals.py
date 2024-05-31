import random, numpy
import matplotlib.pylab as pylab

#from lecture6.monte_carlo import FairRoulette, playRoulette, findPocketReturn, getMeanAndStd


#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
#set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1


#quick generation of normally distributed data

random.seed(1)
dist, numsamples = [], 1000000

for i in range(numsamples):
    dist.append(random.gauss(0,100))

weights = [1/numsamples]*len(dist)
v = pylab.hist(dist, bins = 100, weights = [1/numsamples]*len(dist))

print('Fraction within ~200 of mean =', sum(v[0][30:70]))

def guassian(x, mu, sigma):
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2

xVals, yVals = [], []
mu, sigma = 0, 1 
x=-4
while x <= 4:
    xVals.append(x)
    yVals.append(guassian(x, mu, sigma))
    x += 0.05
pylab.plot(xVals, yVals)




