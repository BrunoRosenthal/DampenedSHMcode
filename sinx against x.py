import math
import matplotlib.pyplot as plt

percentDiff = [0]
value = [0]

for i in range(1,90):
    j = math.radians(i)
    s = math.sin(j)
    percent = abs((j - s)/s)*100
    percentDiff.append(percent)
    value.append(j)

plt.plot(value, percentDiff)
plt.xlabel("Angle.radians")
plt.ylabel("Percentage Difference from sin(x)")
plt.show()
    
