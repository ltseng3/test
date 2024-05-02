import numpy as np
import matplotlib.pyplot as plt
 

# protocol = ("Pineapple", "PQR", "Gryff", "EPaxos", "MPaxos", "MPaxos(L)")
# tpt = {
#     '1%': (30772.94425, 24249.231832, 17075.2883105, 22915.6537885, 9724.844812, 14632.561195),
#     '10%': (28337.268506, 24147.875347, 15400.924352, 22920.9873955, 9886.746953, 14171.820116),
# }

rmw = ("RMW% = 1%", "RMW% = 10%", "RMW% = 50%")
protocol = {
    'Pineapple': (30772.94425, 28337.268506, 13630.374506),
    'PQR': (24249.231832, 24147.875347, 9934.020803),
    'Gryff': (17075.2883105, 15400.924352, 13423.845762),
    'EPaxos': (22915.6537885, 22920.9873955, 23421.330286),
    'MPaxos': (9724.844812, 9886.746953, 10112.152145),
    'MPaxos(L)': (14632.561195, 14171.820116, 11858.539616),
}

x = np.arange(len(rmw))  # the label locations
width = 0.15  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained', figsize = (15, 2))

for attribute, measurement in protocol.items():
    offset = width * multiplier
    if attribute == 'Pineapple':
        rects = ax.bar(x + offset, measurement, width, label=attribute, color='orange')
    if attribute == 'PQR':
        rects = ax.bar(x + offset, measurement, width, label=attribute, color='blue')
    if attribute == 'Gryff':
        rects = ax.bar(x + offset, measurement, width, label=attribute, color='green')
    if attribute == 'EPaxos':
        rects = ax.bar(x + offset, measurement, width, label=attribute, color='red')
    if attribute == 'MPaxos':
        rects = ax.bar(x + offset, measurement, width, label=attribute, color='black')
    if attribute == 'MPaxos(L)':
        rects = ax.bar(x + offset, measurement, width, label=attribute, color='brown')
    # ax.bar_label(rects, padding=3)
    multiplier += 1

# for x in range(2):
#     rects[6*x].set_color('orange')
#     rects[6*x+1].set_color('blue')
    # rects[6*x+2].set_color('green')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Throughput (Ops/sec)')
#ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, rmw)
ax.legend(loc='upper right', ncols=6)
ax.set_ylim(0, 35000)

# plt.show()


plt.savefig("./tpt-group.png", bbox_inches="tight")
