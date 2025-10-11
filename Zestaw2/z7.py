# Pi approximation using random number generators
import random

def approxPi(samples: int) -> float:
    quaterCircleHits = 0
    for _ in range(samples):
        x = random.random()
        y = random.random()
        if x*x+y*y<1.0:
            quaterCircleHits += 1
    return float(quaterCircleHits)/float(samples)*4.0

print("π=" + str(approxPi(10**1)), "dla 10^1")
print("π=" + str(approxPi(10**2)), "dla 10^2")
print("π=" + str(approxPi(10**3)), "dla 10^3")
print("π=" + str(approxPi(10**4)), "dla 10^4")
print("π=" + str(approxPi(10**5)), "dla 10^5")
print("π=" + str(approxPi(10**6)), "dla 10^6")
print("π=" + str(approxPi(10**7)), "dla 10^7")
