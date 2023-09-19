import numpy as np
import matplotlib.pyplot as plt
 
  
# creating the dataset
data = {'PQR (0.125)': 21632.61, 'Pineapple (0.125)': 30760.99, 'EPaxos (0.125)': 14142.10, 'PQR (0.25)': 20909.21, 'Pineapple (0.25)':  25733.42, 'EPaxos (0.25)': 14721.87, 'PQR (0.5)': 20031.99, 'Pineapple (0.5)': 22391.78, 'EPaxos (0.5)': 13455.03, 'PQR (1.0)': 18397.87, 'Pineapple (1.0)': 18304.74, 'EPaxos (1.0)': 14657.05}
protocol = list(data.keys())
tpt = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
bars = plt.bar(protocol, tpt, 
        width = 1)

for x in range(4):
    bars[3*x].set_color('blue')
    bars[3*x+1].set_color('orange')
    bars[3*x+2].set_color('green')

plt.xticks(rotation=45)

 
plt.xlabel("Systems (RMW Ratio)")
plt.ylabel("Throughput (Ops/sec)")
#plt.title("Students enrolled in different courses")
#plt.show()
plt.savefig("test3-1.png", bbox_inches="tight")


bars = plt.bar(protocol, tpt, 
        width = 1.5)
plt.savefig("test3-1.5.png", bbox_inches="tight")
