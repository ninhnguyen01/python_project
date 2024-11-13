# Import package
import random

probability = 0.4

if random.random() < probability:
    print("Decision with probability 0.4", '\n')
else:
    print("Decision with probability 0.6", '\n')