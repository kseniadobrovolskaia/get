import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
    print(tmp)


data_array = np.loadtxt("data.txt", dtype = float)
data_array = [int(i) for i in data_array]

data_array = [i/100 for i in data_array]
time = [1 * i for i in range(len(data_array))]
print(data_array)
print(time)

fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(data_array, label = "V(t)", marker = "s")


ax.grid(which="major", linewidth=1.2)
ax.grid(which="minor", linestyle="--", color="grey", linewidth=0.5)

ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=2)
ax.tick_params(which='minor', length=5, width=1)




ax.text(16, .5, r'????? ?????? = 41 ?')
ax.text(16, .10, r'????? ??????? = 28 ?')
ax.set_xlabel('?????, ?')  
ax.set_ylabel('??????????, ?') 
ax.set_title("??????? ?????? ? ??????? ???????????? ? ???????")
plt.grid(True)
plt.legend();
plt.savefig("graphik.svg") 
plt.show()
