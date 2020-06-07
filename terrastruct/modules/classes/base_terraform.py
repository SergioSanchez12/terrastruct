# Base Class for terraform objects

from typing import List

class BaseTerraform:
	
	def __init__(self, tf_type: str, names: List):
		self.type = tf_type
		self.names = names
		self.args = {}

	def add_arg(self, key: str, val: str):
		self.args.update({key: val})

	def get_arg(self, key: str):
		return self.args.get(key)

	def disp(self):
		print("type: " + self.type)
		for name in self.names:
			print("name: " + name)
		print("arguments")
		print(self.args)

