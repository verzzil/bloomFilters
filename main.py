import numpy
import math
import hashlib

arr = []
with open("text.txt","r") as text:
   for i in text.read().replace(".","").replace(",","").replace("(","").replace(")","").replace("!","").split(" "):
       arr.append(i)
n = int(((len(arr) * math.log(0.0001)) / math.log(2) ** 2) * -1)
k = int((n / len(arr)) * math.log(2))
bloomFilter = numpy.zeros(n)
p = 1 - (1 - math.e ** (-(k * len(arr)) / n )) ** k

def getPositions(word):
   hash = hashlib.md5(word.encode()).hexdigest()
   long = int(hash,16)
   g = []
   for i in range(1,k+1):
       g.append(long % int((i/k)*n))
   return g

def addElems():
   for i in arr:
       g = getPositions(i)
       for j in g:
           bloomFilter[j] += 1

addElems()

def check(mas):
   for i in mas:
       a = getPositions(i)
       contain_zero = False
       for j in a:
           if bloomFilter[j] == 0:
               contain_zero = True
       if contain_zero:
           print(str(i) + " - Вероятность существования 0")
       else:
           print(str(i) + " - Вероятность существования "+ str(p))

check(["Lorem", "in", "sunt", "laboris", "Albert"])