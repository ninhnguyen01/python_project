# Import package
from string import punctuation, ascii_letters, digits
import random

symbol = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()

password = ''.join(secure_random.choice(symbol) for i in range(16))
print(f'Default Password: {password} \n')