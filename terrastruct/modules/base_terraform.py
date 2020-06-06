# Base Class for terraform objects

from typing import Dict, List

class BaseTerraform:
	
	def __init__(self, block_type: str, block_names: List):
		self.block_type = block_type
		self.block_names = block_names
		self.args = {}

	def add_arg(self, key: str, val: str):
		self.args.update({key: val})


	def disp(self):
		print("block_type: " + self.block_type)
		for name in self.block_names:
			print("block_name: " + name)
		print("arguments")
		print(self.args)

