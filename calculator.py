import traceback


class Calculator:
	last_res = None
	
	
	def sum(self, n1, n2):
		self.last_res = n1 + n2
		return n1 + n2
	
	
	def difference(self, n1, n2):
		self.last_res = n1 - n2
		return n1 - n2
	
	
	def multiply(self, n1, n2):
		self.last_res = n1 * n2
		return n1 * n2
	
	
	def devide(self, n1, n2):
		try:
			self.last_res = n1 / n2
			return n1 / n2
		except:
			traceback.print_exc()
	
	def print_last_res(self):
		print(self.last_res)
	
	def bad_work(self):
		print(
			"""Ты сегодня плохо поработал
					Мы не дадим тебе новые награды в магазине
					Приходи завтра и исправляйся поскорей"""
			)
	
	def gut_work(self):
		print(
			"""ТЫ хорошо сегодня поработал
					Возращайся в следующий раз
					И не забудь забрать награды из магазина!"""
			)
	
calc = Calculator()


