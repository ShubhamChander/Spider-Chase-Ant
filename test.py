import queue
from Stack import Stack

q = queue.Queue()
stack = Stack()

q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.put(6)

print(q.get())
print(q.get())
print(q.get())
print("\n")

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


list = [1,2,"asdf",[23,34]]
print(list[3])

if([23,34] in list):
	print("bothot hard")


