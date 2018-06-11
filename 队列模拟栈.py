class Queue(object):
	def __init__(self):
		self.queue = []
	def enqueue(self,val):
		self.queue.insert(0,val)
	def dequeue(self):
		if self.is_empty():
			return None
		else:
			return self.queue.pop()
	def size(self):
		return len(self.queue)
	def is_empty(self):
		return self.size() == 0

q = Queue()
for i in range(1,8):
	q.enqueue(i)

for i in range(q.size()):
	print(q.dequeue())

class StackByQueue(object):
	def __init__(self):
		self.stack = Queue()
	def push(self,val):
		self.stack.enqueue(val)

	def pop(self):
		for i in range(self.stack.size()-1):
			value = self.stack.dequeue()
			self.stack.enqueue(value)

		return self.stack.dequeue()

sbq = StackByQueue()
for i in range(1,4):
	sbq.push(i)
print(sbq.pop())
