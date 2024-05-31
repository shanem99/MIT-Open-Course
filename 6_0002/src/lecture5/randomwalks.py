from cmath import sqrt
from tabnanny import check


##structure of random walk simulations
#simulate one walk of k steps
#simulate n such walks
#report average distance from origin 

#useful avbstractions: location- a place, field- a collection of places and drunks, drunk- somebody who weanders from place to place in a field 

class Location(object):
    def __init__(self, x, y):
        ##x and y and floats##
        self.x = x
        self.y = y
    
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y+deltaY)

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y 

    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y = other.getY()
        return(xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' +str(self.x)+' ,'+str(self.y)+'>'

class Drunk(object):#this class is to form a base class or a inherited  class
    def __init__(self, name = None):
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        else: 
            return 'Anonymous'

#want 2 subclasses of drunk: usual-random wonderer and masochistic - tries to move northward 

import random  
random.seed(0)

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =  [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices) 

class MasochistDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.1), (0.0,-0.9),(1.0, 0.0), (-1.0, 0.0)] ##steps north 2 tenth more opten than south 
        return random.choice(stepChoices) 

class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunK(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk]= loc
    
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]
    
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)

##Definig a single walk, assumes a field f, drunk d and numsteps an int>=0 

def walk(f, d, numsteps):
    start = f.getLoc(d)
    for s in range(numsteps):
        f.moveDrunk(d)
        return start.distFrom(f.getLoc(d))


##simulating multiple walks

def simWalks(numsteps, numtrails, dClass): #dClass is subclass of drunk
    Homer = dClass()
    origin = Location(0,0)
    distances = []
    for t in range(numtrails):
        f = Field()
        f.addDrunK(Homer, origin)
        distances.append(round(walk(f, Homer, numsteps), 1)) ## need to append numsteps
    return distances

## putting it all together 

def drunkTest(walkLengths, numTrials, dClass):
#Assumes walkLengths a sequence of ints >= 0 numTrials an int > 0, dClass a subclass of Drunk For each number of steps in walkLengths, runs simWalks with numTrials walks and prints results
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))

drunkTest((10, 100, 1000, 10000), 100, UsualDrunk)

#for low numbers we have sanity check

drunkTest((1, 1, 2), 100, UsualDrunk) ## originially our sanity check doesnt work this is bescause we append numtrails whgich is a constamt and not numsteps -see above 