
from collections import deque
import random

def isEmpty(queue):
    return len(queue)==0

def timeStamp(animal):
    while animal not in dict1:
        ts = random.randint(10, 50)
        if ts not in dict1.values():
            dict1[animal] = ts

# animal shelter
# here, nc = no. of cats, nd = no. of dogs, ch = choice made
def animalShelter(nc, nd, ch):
    # time stap record dictionary

    # Cats queue
    for i in range(0, nc):
        cats.append("C"+str(i))
        timeStamp("C"+str(i))


    # Dogs queue
    for i in range(0, nd):
        dogs.append("D"+str(i))
        timeStamp("D"+str(i))

    # 2 choices
    # 1. Adopt the oldest of all animals
    # 2. Select a cat or a dog and adopt the oldest, dogs[0] or cats[0]

    if ch == "any":
        if(dict1[dogs[0]] > dict1[cats[0]]):
            return "Congratulations, now you are a parent of a cute dog named "+dogs[0]
        else:
            return "Congratulations, now you are a parent of a cute cat named "+cats[0]

    elif ch == "cat":
        return "Congratulations, now you are a parent of a cute cat named "+cats[0]

    elif ch == "dog":
        return "Congratulations, now you are a parent of a cute dog named "+dogs[0]


dict1 = {}
cats = deque()
dogs = deque()
print(animalShelter(3, 3, "cat"))
print(dict1)
print(cats)
print(dogs)
