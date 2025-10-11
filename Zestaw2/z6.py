# Wyciągamy 3 karty z tali. Jakie jest prawdopodobienstwo, że żadna z kart nie będzie treflem.
import numpy as np
import random
# ===========================================================
# Podpunkt a
# ===========================================================

# Python ma wbudowany generator liczb losowych w module random. rand.randrange(dolna_granica, gorna_granica) - generuje liczby z podanego przedziału. Jesli chcemy generować liczby z zakresu (0, 1) to istnieje metoda rand.random()

# ===========================================================
# Podpunkt b
# ===========================================================
# Wylosować 1 karte mozna na 2 sposoby
random.randrange(0, 52)
int(random.random()*52)
# Z wygenerowanych liczb możemy przyjąć za trefle liczby od 0 do 12

# ===========================================================
# Podpunkt c
# ===========================================================

# Calculated in task 7 
expected_probability = float(703) / float(1700)
pError = 0.001 # 0.1% error for calculations

pBottomBoundry = expected_probability - pError
pTopBoundry = expected_probability + pError

samples =  0
picksWithoutSpades = 0

def sampleCards():
    global samples
    global picksWithoutSpades
    samples += 1
    # Sampling 3 cards from range [1, 52] without duplicates (returns list)
    cards = np.random.permutation(52)[:3] # bardziej elegnackie rozwiązanie niż ręczne zaprezentowane poniżej. (+ szybsze)
    # Wersja bez numpy
    # cards = [0,0,0]
    # while cards[0] == cards[1] or cards[0] == cards[2] or cards[1] == cards[2]:
    #     cards[0] = random.randrange(0, 52)
    #     cards[2] = random.randrange(0, 52)
    #     cards[2] = random.randrange(0, 52)

    # Define all spades as cards numbered [0, 12]
    for card in cards:
        if card < 13:
            return
    picksWithoutSpades += 1

sampleCards() # We need to take sample to avoid division by zero as samples is 0 at begining
while not ((float(picksWithoutSpades) / float(samples)) < pTopBoundry and (float(picksWithoutSpades) / float(samples)) > pBottomBoundry):
    sampleCards()


print("Picks with spades:", picksWithoutSpades, "Samples taken:", samples)
print("Calculated probability",picksWithoutSpades/samples, " Expected probability: ", expected_probability)
 