# Base Class for terraform objects

from typing import Dict, List

class BaseTerraform:
	
	def __init__(self, block_type: str, block_name: List):
		self.block_type = block_type
		self.block_name = block_name
		self.data = data

	def type():
		print(self.block_type)

	def labels():
		for name in self.block_name:
			print(name)

