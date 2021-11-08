from word_processor import pre_processing
import math
import pickle
import numpy as np

from add_document import load_files

def get_cosine_similiarity(terms,document):
    return np.dot(terms,document)/(math.sqrt(np.sum(terms**2))*math.sqrt(np.sum(document**2)))


def process_querry(words,dic,df,docs):
	words = pre_processing(words)
	#print(words)
	N = len(dic)
	terms = {}
	for word in words:
		if word in terms:
			terms[word] += 1
		else:
			terms[word] = 1
	idfs = []
	for term in terms:
		if term in df:
			idfs.append(math.log(N/df[term]))
		else:
			idfs.append(0)
	term_vector = np.fromiter(terms.values(), dtype=float)
	term_vector = term_vector*np.array(idfs)
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
	rank = {}
	i = 0
	for file in dic:
		rank[file] = get_cosine_similiarity(term_vector,doc_vectors[i])
		i += 1
	return rank

#process_querry(input('Query : '))
#dic,df,docs = load_files()
