import matplotlib.pyplot as graph

population_ages = [20,28,56,34,89,12,6,78,45,66,102,69,34,18,9,63,50,112,73,44,10]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]
graph.hist(population_ages,bins,histtype='bar',rwidth=0.8)

graph.ylabel("Population")
graph.xlabel("Ages")
graph.title("Population Graph")
graph.show()