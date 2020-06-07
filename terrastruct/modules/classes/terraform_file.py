
from .base_terraform import BaseTerraform

class TerraformFile:

	def __init__(self, path: str):
		
		self.blocks = []

	def add_block(self, new_block: BaseTerraform):
		self.blocks.append(new_block)

	def list(self, target_type: str):
		for block in self.blocks:
			if block.type == target_type:
				print(f"{target_type}: {block.names}")

	def list_all(self):
		for block in self.blocks
			print(f"{block.type}: {block.names}")


