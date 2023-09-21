import numpy as np
import matplotlib.pyplot as plt

y = [0.45, 0.71, 1.15, 1.62, 1.99, 2.43, 3.09, 4.4, 5.91]
x = [6446, 11331, 13114, 13872, 14164, 14304, 14714, 15539, 15921]

y1 = [0.35, 0.49, 0.83, 1.23, 2.59, 1.96, 2.58, 3.89, 5.15]
x1 = [8033, 17373, 20270, 20657, 21435, 21813, 22263, 22377, 22680]

#fig = plt.figure(figsize = (10, 3))

fig, ax = plt.subplots()

fig.set_figheight(3)
fig.set_figwidth(10)


ax.plot(x, y, color='green', linestyle="dashdot", label="Gryff")
ax.plot(x1,y1, color='orange', linestyle="solid", label="Pineapple")

ax.set_ylabel("Latency (ms)")
ax.set_xlabel("Throughput (Ops/sec)")

ax.legend(('Gryff','Pineapple'))

fig.savefig("latency-tput.png", bbox_inches="tight")
