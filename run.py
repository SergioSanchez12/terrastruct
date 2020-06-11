from terrastruct.parser.terraform_parser import parse_tf_file

if __name__ == "__main__":
	terrastruct_obj = parse_tf_file('tests/sample_data/sample_3.tf')

	# List all blocks from the given terraform file
	terrastruct_obj.list_all()

	# List all resources and their respective names
	terrastruct_obj.list('resource')

	# List all variables and the respective name
	terrastruct_obj.list('variable')
