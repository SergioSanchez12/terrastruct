import os
import re
from modules.base_terraform import BaseTerraform

re_lib = {
	"start_block": re.compile(r"^(?P<block_type>[a-zA-Z_]* )(\"[a-zA-Z_]*\" )+{$"),
	"key_val": re.compile(r"^ +(?P<key>[a-zA-Z_]*) +=(?P<val>[^\S]*)"),
	"end_block": re.compile(r"^}$"),
	"comment": re.compile(r"^#.*"),
	"start_comment": re.compile(r"^\/\*.*"),
	"end_comment": re.compile(r".*\*\/$")
}


def _line_parser(line):
	for line_type, regex in re_lib.items():
		if regex.search(line):
			return line_type

	return None



terraform_file = open('./sample_data/sample.tf', 'r')
lines = terraform_file.readlines()

eof = False
line_num = 0

while not eof:
	line_type = _line_parser(lines[line_num])
	if line_type == "comment":

	elif line_type == "start_comment"
		while _line_parser(lines[line_num]) != "end_comment":
			line_num++
	elif line_type == start_block:

	elif line_type == end_block:

	line_num++





	






		





