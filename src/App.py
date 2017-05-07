import sys
import os
import random

POP_SIZE=40
class Animal:
    __uid = None
    __c1 = 0
    __c2 = 0
    __c3 = 0

    def __init__(self, uid=None, c1=None, c2=None, c3=None):
        if (uid != None):
            self.__uid = uid
            self.__c1 = c1
            self.__c2 = c2
            self.__c3 = c3
        else:
            self.__uid = random.random()
            self.__c1 = random.randint(1, 255)
            self.__c2 = random.randint(1, 255)
            self.__c3 = random.randint(1, 255)

    def set_uid(self, uid):
        self.__uid = uid

    def set_c1(self, c1):
        self.__c1 = c1

    def set_c2(self, c2):
        self.__c2 = c2

    def set_c3(self, c3):
        self.__c3 = c3

    def toString(self):
        return "id {} c1 {} c2 {} c3 {}".format(self.__uid, self.__c1, self.__c2, self.__c3)

    def getFitness(self):
        return (self.__c1/255)*(self.__c2/255)*(self.__c3/255)

    def getUid(self):
        return self.__uid

    def getC1(self):
        return self.__c1

    def getC2(self):
        return self.__c2

    def getC3(self):
        return self.__c3

def printMyList(p):
    print(" Prob %f for prob %f for animal %s" % (p[1], p[0].getFitness(), p[0].toString()))

def fitFunc(popul):
    temp1=[]
    for x in popul:
        temp1.append([x,x.getFitness()])
    tot=0.000
    '''sum all Fitness'''
    for y in temp1:
        tot=tot+y[1]
    #print("Total Fitness %f",tot)

    temp2=[]
    '''calculate Roulette wheel share'''
    for z in temp1:
        temp2.append([z[0],z[1]/tot])

    sort_by_fitness_weight = sorted(temp2, key=lambda tup: tup[1])

    #for xx in sort_by_fitness_weight:
     #   print(" Prob %f for prob %f for animal %s" % (xx[1], xx[0].getFitness(),xx[0].toString()))

    return sort_by_fitness_weight

def rouletteSelect(sortedPop):
    #print(random.random())
    tot=random.random()
    for x in sortedPop:
        tot=tot-x[1]
        if(tot<=0):
            return x[0]
    return sortedPop[len(sortedPop)-1][0]


def getChild(p,m):
    x=random.randint(1,3)
    if(x==1):
        ch = Animal(random.random(),m.getC1(),p.getC2(),p.getC3())
    elif(x==2):
        ch = Animal(random.random(),p.getC1(), m.getC2(), p.getC3())
    elif(x==3):
        ch = Animal(random.random(),p.getC1(), p.getC2(), m.getC3())
    #Probability of mutation 0.01 for every code
    #for z in range(3):
        if(random.randint(1,100)==1):
            #print("$$$$$$$$$$$$$$$$$$ MUTATION $$$$$$$$$$$$$$$$$$$")
            if(random.randint(1,3)==1):
                ch.set_c1(random.randint(1,255))
            elif (random.randint(1, 3) == 2):
                ch.set_c2(random.randint(1, 255))
            elif (random.randint(1, 3) == 3):
                ch.set_c3(random.randint(1, 255))
    return ch


def evalFunc(popul):
    tot=1
    '''sum all Fitness'''
    for y in popul:
        tot=tot*y.getFitness()
    print("  ************************ Populatioin Fitness %f ****************************",round(tot,3))
    return tot

def runcycle(popl):
    '''if getFitness(popl) >= 1:
        print(" GOT IDEAL GENER %f" % (getFitness(popl)))
        return popl'''
    newGen=[]
    rr = fitFunc(popl)
    for i in range(POP_SIZE):
        papa = rouletteSelect(rr)
        mama = rouletteSelect(rr)
        '''print("PAPA MAMA")
        print(papa.toString())
        print(mama.toString())'''
        ch = getChild(papa, mama)
        #print("Child")
        #print(ch.toString())
        newGen.append(ch)
    return newGen

def runcyclerecur(popl):
    if evalFunc(popl) >= 1:
        print(" GOT IDEAL GENER %f" % (evalFunc(popl)))
        return popl
    newGen=[]
    rr = fitFunc(popl)
    for i in range(POP_SIZE):
        papa = rouletteSelect(rr)
        mama = rouletteSelect(rr)
        #print("PAPA MAMA")
        #print(papa.toString())
        #print(mama.toString())
        ch = getChild(papa, mama)
        #print("Child")
        #print(ch.toString())
        newGen.append(ch)
    return runcyclerecur(newGen)


'''ani1 = Animal(22, 33, 44, 55)
ani2 = Animal()
print(ani1.toString())
print(ani2.toString())'''
initpop=[]
for x in range(POP_SIZE):
    initpop.append(Animal())


#for r in rr:
#    print(" Prob %f for Animal prob %f"%(r[1],r[0].getProb()) )

'''dtot=0.0
for a in rr:
      dtot=dtot+a[1]
print(dtot)'''
gen=1
while evalFunc(initpop)<1:
    print("GENERATION = %d"%(gen))
    xyz=runcycle(initpop)
    #getFitness(xyz)
    initpop.clear()
    initpop=xyz
    gen=gen+1

for x in initpop:
    print(x.toString())


#runcyclerecur(initpop)
