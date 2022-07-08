import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2200, 100000)
x = 16*np.sin(t)**3+25
y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t) + 20
plt.figure(figsize=(7,5))
plt.plot(x, y, color="pink", linewidth = 5)
plt.text(14, 19, "Lucerito", fontsize = 20, color = "red")
plt.show()

#plt.xlabel("X", fontsize = 20)
#plt.ylabel("Y", fontsize = 20)
#plt.title("Corazon", fontsize = 20)
#plt.grid(True)
