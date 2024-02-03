import traceback


class Calculator:
	last_res = None
	
	
	def sum(self, n1, n2):
		self.last_res = n1 + n2
		return n1 + n2
	
	def multiply(self, n1, n2):
		self.last_res = n1 * n2
		return n1 * n2
	
	
	def devide(self, n1, n2):
		try:
			self.last_res = n1 / n2
			return n1 / n2
		except:
			traceback.print_exc()
			
	
	def printify(self):
		print(self.last_res)
		

calc = Calculator()


