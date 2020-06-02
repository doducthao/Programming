# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# Constraints:

# Methods pop, top and getMin operations will always be called on non-empty stacks.


class MinStack:
# 	Runtime: 68 ms
# Memory Usage: 17.4 MB
	def __init__(self):
		self.stack = []
		self.minstack = [float("inf")]
		self.min = float("inf")

	def push(self, x):
		self.stack.append(x)
		m = self.min 
		if x < m:
			self.min = x
			self.minstack.append(x)
		else:
			self.minstack.append(m)

	def pop(self):
		self.stack.pop()
		minstack = self.minstack
		minstack.pop()
		self.min = minstack[-1]

	def top(self):
		return self.stack[-1]

	def getMin(self):
		return self.min


class MinStack_2:

	def __init__(self):
		self.stack = []
		self.minstack = []

	def push(self, x):
		self.stack.append(x)
		if len(self.minstack) != 0:
			if x < self.minstack[-1]:
				self.minstack.append(x)
		else:
			self.minstack.append(x)


	def pop(self):
		a = self.stack.pop()
		if a == self.minstack[-1]:
			self.minstack.pop()


	def top(self):
		return self.stack[-1]

	def getMin(self):
		return self.minstack[-1]


class MinStack_3:
	# 	Runtime: 52 ms
# Memory Usage: 17.6 MB
	def __init__(self):
		self.stack = []
		self.minstack = []
		
	def push(self, x):
		self.stack.append(x)
		if self.minstack:
			val,count = self.minstack[-1] 
			if val>x:
				self.minstack.append((x,1))
			elif val==x:
				self.minstack[-1] = (val,count+1)
		else:
			self.minstack.append((x,1))
			
	def pop(self):
		val,count = self.minstack[-1]
		if val==self.stack[-1]:
			count -=1
			if count == 0 : self.minstack.pop()
			else : self.minstack[-1] = (val,count)
		return self.stack.pop()
	
	def top(self):
		return self.stack[-1]
	
	def getMin(self):
		val,count = self.minstack[-1]
		return val





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
	# print(4>-float("inf"))
	obj = MinStack_3()
	obj.push(4)
	obj.push(4)
	obj.push(-2)
	obj.push(0)
	obj.push(-5)
	obj.push(6)
	obj.push(3)
	obj.push(-1)
	print(obj.stack)
	print(obj.minstack)
	print(obj.getMin())
	obj.pop()
	print(obj.stack)
	print(obj.top())
	print(obj.getMin())





