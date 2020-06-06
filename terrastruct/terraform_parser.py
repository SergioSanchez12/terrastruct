import os
import re
from modules.base_terraform import BaseTerraform

re_lib = {
	"start_block": re.compile(r"^(?P<block_type>[a-zA-Z_]* )(\"[a-zA-Z_]*\" )+{$"),
	"key_val": re.compile(r"^ +(?P<key>[a-zA-Z_]*) *= *(?P<val>.*)"),
	"end_block": re.compile(r"^}$"),
	"comment": re.compile(r"^#.*"),
	"start_comment": re.compile(r"^\/\*.*"),
	"end_comment": re.compile(r".*\*\/$")
}


def _line_parser(line):
	for line_type, regex in re_lib.items():
		try:
			match = regex.search(line)
		except TypeError:
			return None, None
		if match:
			return line_type, match

	return None, None



tf_file = open('./sample_data/sample_3.tf', 'r')
tf_lines = iter(tf_file.readlines())

eof = False
line_num = 0

in_comment = False
in_block = False

cur_line = next(tf_lines, None)
line_type, re_match = _line_parser(cur_line)

while cur_line != None:
	# in block
	if line_type == "start_block":
		tf_obj = BaseTerraform(
			re_match.group("block_type"), 
			[x.strip('\"') for x in re.findall("\"[a-zA-Z_]+\"", cur_line)]
		)
		while line_type != "end_block":
			cur_line = next(tf_lines)
			line_type, re_match = _line_parser(cur_line)
			if line_type == "key_val":
				tf_obj.add_arg(re_match.group("key"), re_match.group("val"))


	tf_obj.disp()

	cur_line = next(tf_lines, None)
	line_type, re_match = _line_parser(cur_line)





# x.strip('\"') for x in 



# 	if in_comment

# 	# not in comment

# 	elif line_type == start_block:

# 	elif line_type == end_block:


# while not eof:
# 	line_type = _line_parser(lines[line_num])
# 	if line_type == "comment":

# 	elif line_type == "start_comment":
# 		while _line_parser(lines[line_num]) != "end_comment":
# 			line_num++
# 	elif line_type == start_block:

# 	elif line_type == end_block:

# 	line_num++





	






		





