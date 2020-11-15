import matplotlib.pyplot as graph

x = [2,4,6,8,10]
y = [3,5,7,8,4]

x2 = [1,3,5,7,9]
y2 = [2,4,6,8,10]

graph.bar(x,y,label = 'Company1',color = 'red')
graph.bar(x2,y2,label = 'Company2',color = 'blue')

graph.ylabel("Sales")
graph.xlabel("Years")

graph.title("Company Sales Graph")
graph.legend()
graph.show()