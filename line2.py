import numpy as np
import matplotlib.pyplot as plt

pineappley50 = [4.591268, 2.4810335, 1.4597639999999998, 0.765056, 0.328578]
pineappley90 = [7.279256600000003, 3.9458115, 2.2388941, 1.1972183000000007, 0.4462818]
pineapplex = [30772.94425, 28516.851289500002, 26004.472306499996, 24427.757136499997, 14543.563719999998]

pqry50 = [0.29848450000000004, 0.218675]
pqry90 = [6.906273900000001, 0.218675]
pqrx = [24249.231832, 18170.879123]

gryffy50 = [7.719378, 3.9422585000000003, 2.1926835000000002, 1.243434, 0.465789]
gryffy90 = [18.0490124, 8.740376300000001, 4.6261305, 2.3577768, 0.65785]
gryffx = [17075.2883105, 16996.4420625, 16107.253977, 14457.392739, 10327.650847500001]

epaxosy50 = [6.0528379999999995, 3.270225, 2.063268, 1.30152, 0.378406]
epaxosy90 = [10.903227, 5.5593446, 3.3387264000000005, 2.2216960000000006, 0.6942381999999994]
epaxosx = [22915.6537885, 21745.812353, 19165.836774, 14796.676275500002, 10078.824631]

mpaxosy50 = [15.7132295, 7.509401, 4.0179975, 1.886107, 0.47423]
mpaxosy90 = [18.241745, 9.3639232, 5.2179492000000005, 2.5441434000000003, 0.6648536]
mpaxosx = [9724.844812, 10016.747331, 9989.242756, 10534.279111, 9928.679009]

mpaxosly50 = [10.227046999999999, 4.7815815, 2.6022795, 1.3168005, 0.322689]
mpaxosly90 = [11.880867700000001, 5.8513808, 3.2879736000000004, 1.7502937, 0.5354656000000001]
mpaxoslx = [14632.561195, 15530.824080000002, 15179.297636, 14917.486127, 14311.760710999999]

#fig = plt.figure(figsize = (10, 3))

fig, ax = plt.subplots(figsize = (12, 1))

#fig.set_figheight(3)
#fig.set_figwidth(10)


# ax.plot(pineapplex, pineappley50, color='orange', linestyle="solid", label="Pineapple")
# ax.plot(gryffx,gryffy50, color='green', linestyle="solid", label="Gryff")
# ax.plot(epaxosx,epaxosy50, color='red', linestyle="solid", label="EPaxos")
# ax.plot(mpaxosx,mpaxosy50, color='black', linestyle="solid", label="MPaxos")
# ax.plot(mpaxoslx,mpaxosly50, color='brown', linestyle="solid", label="MPaxos(L")
# ax.set_ylabel("p50 Latency (ms)")


ax.plot(pineapplex, pineappley90, color='orange', linestyle="solid", label="Pineapple")
ax.plot(gryffx,gryffy90, color='green', linestyle="solid", label="Gryff")
ax.plot(epaxosx,epaxosy90, color='red', linestyle="solid", label="EPaxos")
ax.plot(mpaxosx,mpaxosy90, color='black', linestyle="solid", label="MPaxos")
ax.plot(mpaxoslx,mpaxosly90, color='brown', linestyle="solid", label="MPaxos(L)")
ax.set_ylabel("p99 Latency (ms)")


ax.set_xlim(left=0)
ax.set_xlabel("Throughput (Ops/sec)")
ax.legend(('Pineapple', 'Gryff', 'EPaxos', 'MPaxos', 'MPaxos(L)'))
ax.legend(loc='upper left', ncols=2)
# plt.show()

fig.savefig("latency-tput-90.png", bbox_inches="tight")
