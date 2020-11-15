import matplotlib.pyplot as graph

x = [1,2,8]
y = [5,7,2]
x1 = [1,5,9]
y1 = [3,6,4]

graph.plot(x,y,label = 'Object 1')
graph.plot(x1,y1,label = 'Object 2')

graph.ylabel("Distance")
graph.xlabel("Time")
graph.title("Variable Speed Graph")
graph.legend()
graph.show()



