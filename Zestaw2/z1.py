# Na płaszczyzne naniesiono siatke kwadratowa o boku a. Rzucamy moneta o promieniu r < a / 2. Jakie jest prawdopodobienstwo, że rzucona moneta nie dotknie lini siatki.

import random

a = 40
r = 10 # r < a / 2

samples = 1_000_000
grid_hits = 0
for _ in range(samples):
    x = random.randrange(int(a/2))
    y = random.randrange(int(a/2))
    if x < r or y < r:
        grid_hits += 1

print("hits: ", grid_hits)
print("Probality of not hitting grid: ", float(samples-grid_hits)/float(samples)*100, "%")
print("Expected probality: ", float(a*a-4*a*r+4*r*r)/float(a*a) * 100, "%")