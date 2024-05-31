##PREDICTIVE NONDETERMINISM
# The world isnt inherently unpredictable, but our lack of knowledge does not allow us to make accurate predictions therefore we treat it as inherently unpredictable
# This is predicitive nondeterminism

# A stochastic process is an ongoing process where the next state might depend on both the previous states and some random element

# example
import random
import math

random.seed = 0  # random function doesnt actually generate random number but does it based of a time stamp in computer which we do not know. the seed just sets this time stamp so we know it


def rollDie():
    # returns a random int between 1 and 6
    return random.choice([1, 2, 3, 4, 5, 6])


def testroll(n):
    result = ""
    for i in range(n):
        result = result + str(rollDie())
        print(result)


# testroll(5) #running testroll


##generate a simulation to find probabilities of events
## we are going to generate a simulation to find out probability of certain sequences of rolls
def runSim(goal, numtrails, txt):
    total = 0
    for i in range(numtrails):
        result = ""
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print("Actual probability of", txt, "=", round(1 / (6 ** len(goal)), 8))
    estProbability = round(total / numtrails, 8)
    print("Estimated Probability of", txt, "=", round(estProbability))


# runSim('11111', 1000, '11111')

# Notes on writing simulations
# it takes a lot of trails to get a good estimate of the frequency of occurrence of rare event. Will discover later how to know when is enough trails
# dont confuse sample probability with actual probability
# no need for this to be down by simulations as the correct answer easy to find. but simulations are useful

##Birthday problem
# whats probability of at least two people shoring the same birthday. If we assume each birthday equivalent very possible to derive formula
# 1-no one shares a birthday

##Approx using simulation


def sameDate(numPeople, numSame):
    possibleDates = range(366)
    birthdays = [0] * 366
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] += 1
    return max(birthdays) >= numSame


def birthdayProb(numPeople, numSame, numTrails):
    numHits = 0
    for t in range(numTrails):
        if sameDate(numPeople, numSame):
            numHits += 1
    return numHits / numTrails


for numPeople in [10, 20, 40, 100]:
    print(
        "For",
        numPeople,
        "est. prob of shared Bday is",
        birthdayProb(numPeople, 2, 10000),
    )
    numerator = math.factorial(366)
    denom = (366**numPeople) * math.factorial(366 - numPeople)
    print("Actual prob. for N = 100 =", 1 - numerator / denom)

# again this simulation isnt that necessary as estimating prob of 2 birthdays isnt thaT hard
# however problem is generated when we want to find prob of 3 birthdays. math is much more difficult
# and what if not all birthdays are distinct(which is true)

# very difficult math but adjusting the simulator is very easy


def sameDate2(numPeople, numSame):
    possibleDates = 4 * list(
        range(0, 57) + [58] + 4 * range(59, 366) + 4 * list(180, 270)
    )
    birthdays = [0] * 366
    for p in range(numPeople):
        birthDate = random.choice(possibleDates)
        birthdays += 1
    return max(birthdays) >= numSame


##note simulations are used alot to 1.model systems, extract useful indeterminate results, success refinement, start random walks
