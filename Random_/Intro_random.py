import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ('List:', l)
print('Random choice from list:', random.uniform(1, 3))

deck = list(range(1, 53))

print('All deck values: ', deck)

hand = random.sample(deck, k=5)
print('Picked only five: ', hand)