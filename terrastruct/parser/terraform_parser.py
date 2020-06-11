import re
from ..modules.base_terraform import BaseTerraform
from ..modules.terraform_file import TerraformFile
from .regex_def import re_lib


def parse_tf_file(path: str):

	"""
	Function to parse a terraform file to create BaseTerraform objects
	from the data in the file
	"""

	tf_lines = iter(open(path, 'r').readlines())

	cur_line = next(tf_lines, None)
	line_type, match = _line_parser(cur_line)

	tf_file = TerraformFile(path)

	while cur_line != None:
		if line_type == "start_block":

			tf_obj = BaseTerraform(
				match.group("type"), 
				[x.strip('\"') for x in re.findall("\"[a-zA-Z_]+\"", cur_line)]
			)

			while line_type != "end_block":

				cur_line = next(tf_lines, None)
				line_type, match = _line_parser(cur_line)

				if line_type == "key_val":
					tf_obj.add_arg(match.group("key"), match.group("val"))

			tf_file.add_block(tf_obj)

		if line_type == "start_comment":
			while line_type != "end_comment":
				cur_line = next(tf_lines, None)
				line_type, match = _line_parser(cur_line)

		cur_line = next(tf_lines, None)
		line_type, match = _line_parser(cur_line)

	return tf_file


def _line_parser(line):

	"""
	Helper function to parse and identify a single line in a terraform
	file based on the re_lib regex definitions.
	"""

	for line_type, regex in re_lib.items():
		try:
			match = regex.search(line)
		except TypeError:
			return None, None
		if match:
			return line_type, match

	return None, None