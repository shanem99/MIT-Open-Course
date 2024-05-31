#monte carlo simulation is a method of estimating the value of an unknown quantity using the principles of interential statistics

#inferential statistics:
# population: a set of examples 
# sample: a propewr subset of a population 

#key fact is that a random sample tends to exhibit the same properties as the population from which it is drawn. 

# simulting roulette:

# code is set up that if you loose return is nothing and if you win return is x36 and only allowing betting on numbers means expected outcome is 0 
import random


class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        self.ball = None
        self.pocketOdds = len(self.pockets)-1 
    
    def spin(self):
        self.ball = random.choice(self.pockets)

    def betPocket(self, pocket, amt):
        if str(pocket)==str(self.ball):
            return amt*self.pocketOdds
        else:
         return -amt
        
    def __str__(self):
        return 'Fair Roulette'

def playRoulette(game, numSpins, pocket, bet, toPrint):
    totPocket = 0
    for i in range(numSpins):
        game.spin()
        totPocket += game.betPocket(pocket, bet)
    if toPrint:
        print(numSpins, 'spin of', game)
        print('Expected return betting', pocket, '=', str(100*totPocket/numSpins) +  '%\n')
    return(totPocket/numSpins)

game = FairRoulette()
for numSpins in (100, 100000):
    for i in range (3):
        playRoulette(game, numSpins, 2, 1, True)

##results show expected value of betting much lower variance with large number of bets

#Bernoullis law: In repeated independent tests with the same actual probability p of a particular outcome in each test, the chance that the fraction of 
#times the outcome differs from p converges to 0 as the number of trials goes to infinity 

#NOT TRUE: current deviations will always be evened out.

#Regression to the mean: following an exterme event the next random event is likely to be les extreme

##Gamblers falacy-- likely to get more black numbers if we get 10 nred numbers in a row 

#in reality roulette has 0 and 00 hake house favourite

class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    
    def __str__(self):
        return 'European Roulette'


class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')
    def __str__(self):
        return 'American Roulette'

# need to separate what is true and what is exactly true
# how many trails do we need for confidence i our answer


def findPocketReturn(game, numtrials, trialsize, toPrint):
    pocketReturns = []
    for t in range(numtrials):
        trialVals = playRoulette(game, trialsize, 2, 1, toPrint )
        pocketReturns.append(trialVals)
    return pocketReturns



random.seed(0)
numtrials=20
resultsDict = {}
games = ( FairRoulette, EuRoulette, AmRoulette)
for G in games: 
    resultsDict[G().__str__()]=[]
for numspins in (1000, 10000, 100000, 1000000):
    print('\nSimulate', numtrials, 'trials of',numSpins, 'spins each')
    for G in games:
        pocketreturns = findPocketReturn(G(), numtrials, numSpins, False)
        expReturn = 100*sum(pocketreturns)/len(pocketreturns)
        print('Exp. return for', G(), '=', str(round(expReturn, 4)) + '%')

## can never garantee peferct accuracy. Therefore need to know how many sample we need before we have confidence in answer. This depends on variability in underlying distribution

#code for standard deviation

def getMeanAndStd(x):
    mean = sum(x)/float(len(x))
    tot = 0.0 
    for i in x:
        tot += (i-mean)**2
    std = (tot/len(x))**0.5
    return mean, std 

## confidence interval provides range
# Example: The return on betting a pocket 10K times in EU roul;ette is -3.3% the margin of error is +/- 3.5% with 95% confidence
# this mean expected averasge is -3.3% and my return would be between roughtly -6.8% and +0.2% 95% of the time

#EMPERICAL RULE 
#68% of data lies within one std 
#95% of data lies within 1.96 std
#99.7% of data lies within 3std

#Applying imperical rule
resultDict = []
games = (FairRoulette, EuRoulette, AmRoulette)
for G in games:
    resultsDict[G().__str__()] =[]
for numSpins in (100, 1000, 10000):
    print('\nSimulate betting a pocket for', numtrials, 'trails of', numSpins, 'spins each')
    for G in games:
        pocketReturns = findPocketReturn(G(), 20, numSpins, False)
        mean, std = getMeanAndStd(pocketReturns)
        resultsDict[G().__str__()].append((numSpins, 100*mean, 100*std))

        print('Exp. return for', G(), '=', str(round(100*mean, 3))+'%', '+/-', str(round(100*1.96*std, 3)) + '% with 95% confidence')

#Assumptions about empirical rule
# 1. mean estimation error is zero
# 2. the distribution of errors in the estimate is normal

