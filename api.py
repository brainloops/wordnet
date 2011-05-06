from nltk.corpus import wordnet as wn

def definitions(word):
	def_dict = dict()
	words = wn.synsets(word)

	for x in words:
		# pos = part of speech
		pos = x.pos
		def_list = None
		if pos not in def_dict:
			def_list = list()	
			def_dict[x.pos] = def_list
		else:
			def_list = def_dict[x.pos]
		def_list.append(x.definition)
	return def_dict

def usage():
	print "supply a word at the command line"

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		word = sys.argv[1]
		print definitions(word)
	else:
		print usage()
	
