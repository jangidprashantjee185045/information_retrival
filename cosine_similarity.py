from word_processor import pre_processing
import math
import pickle
import numpy as np

from add_document import load_files

#function to return the cosine Similarity score of two vectors
def get_cosine_similiarity(terms,document):
    return np.dot(terms,document)/(math.sqrt(np.sum(terms**2))*math.sqrt(np.sum(document**2)))


# function :  process_querry
# parameters  -----------
# 1) words :- string containing the querry
# 2) dic  :- dictionary containing the document lists
# 3) df :- dictionary containing the document frequency of each term
# 4) docs :- list of dictionaries containing the termFrequency of words in each document

def process_querry(words,dic,df,docs):
	# preprocess the querry and convert it into list of valid words
	words = pre_processing(words)

	N = len(dic)

	# dictionary to store the terms in query and their frequency
	terms = {}

	for word in words:
		if word in terms:
			terms[word] += 1
		else:
			terms[word] = 1

	# idfs is list that contains inverse document frequency of each term
	idfs = []
	for term in terms:
		if term in df:
			idfs.append(math.log(N/df[term]))
		else:
			idfs.append(math.log(N))

	# term_vector is the vector that stores the array of the frequency of each term in query
	term_vector = np.fromiter(terms.values(), dtype=float)
	term_vector = term_vector*np.array(idfs)

	# doc_vectors will store the list of all the arrays of frequency of terms in respective document
	doc_vectors = []

	i = 0
	for file in dic:
		tf = docs[file]
		doc_vectors.append([])
		j = 0
		for term in terms:
			if term in tf:
				doc_vectors[i].append(tf[term]*idfs[j])
			else:
				doc_vectors[i].append(idfs[j])
			j += 1
		i += 1
	doc_vectors = np.array(doc_vectors)

	# rank dictionary stores the cosine Similarity score of each document
	rank = {}
	i = 0
	for file in dic:
		rank[file] = get_cosine_similiarity(term_vector,doc_vectors[i])
		i += 1

	# return rank dictionary
	return rank

#process_querry(input('Query : '))
#dic,df,docs = load_files()
