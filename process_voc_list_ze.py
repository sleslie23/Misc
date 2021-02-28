# Outputs a tsv file that can be imported into Flashcard Hero. This app does not allow multiple side which is a problem for Chinese
# Output is in a format that is usable in Flashcard Hero.
# Input is a tsv file with 3 columns (ze/pinyin/en)

file_list = {"intro.tsv", "Unit-1.tsv", "Unit-2.tsv", "Unit-3.tsv", "Unit-4.tsv", "Unit-5.tsv", "Unit-6.tsv", "Unit-7.tsv", "Professions.tsv"}

for file in file_list:

	infile = open(file)
	out_string = "out/" + file
	outfile = open(out_string, 'w+')
	lines = infile.readlines()	
	for line in lines:
		split_line = line.split("\t")
		pinyin_temp = "(" + split_line[1] + ")"
		split_line[1] = pinyin_temp
		def_temp = split_line[2].rstrip()
		split_line[2] = def_temp
		print(split_line)

		out_string = "\"" + split_line[0] + "\n" + split_line[1] + "\"" + "\t" + split_line[2] + "\n"
		outfile.write(out_string)
