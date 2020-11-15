import matplotlib.pyplot as graph

Sleeping = [4,6,8,9,5]
Working  = [3,5,9,3,6]
Coding   = [8,9,2,5,10]
Playing  = [1,5,7,5,2]

slices = [7,2,5,4]
activities = ['Sleeping','Working','coding','Playing']
cols = ['red','blue','yellow','m']
graph.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,autopct='%1.1f%%')

graph.title("My Pie Chart")
graph.show()