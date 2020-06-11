import re

re_lib = {
	"start_block": re.compile(r"^(?P<type>[a-zA-Z_]*) (\"[a-zA-Z_]*\" )+{$"),
	"key_val": re.compile(r"^ +(?P<key>[a-zA-Z_]*) *= *(?P<val>.*)"),
	"end_block": re.compile(r"^}$"),
	"comment": re.compile(r"^#.*"),
	"start_comment": re.compile(r"^\/\*.*"),
	"end_comment": re.compile(r".*\*\/$")
}