#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# your code here
plt.ylim(0, 80)
plt.title('Number of Fruit per Person')
plt.ylabel('Quantity of Fruit')
labels = np.array(['Farrah', 'Fred', 'Felicia'])
apples = plt.bar(labels, fruit[0], width=0.5, color='red',
                 label='apples')
bananas = plt.bar(labels, fruit[1], width=0.5, color='yellow',
                  bottom=fruit[0], label='bananas')
oranges = plt.bar(labels, fruit[2], width=0.5,
                  color='#FF8000', bottom=fruit[1]+fruit[0],
                  label='oranges')
peaches = plt.bar(labels, fruit[3], width=0.5,
                  color='#FFE5B4', bottom=fruit[0]+fruit[1]+fruit[2],
                  label='peaches')
plt.legend()
plt.show()