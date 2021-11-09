import PyPDF2
import pickle
import os

from word_processor import pre_processing


# fucntion => load_file(void)
# retruns dic , df , docs
# 1) dic : dictionary of files
# 2) df : dictionary that stores the document frequency of each documnet
# 3) docs : list of dictionaries of the term frequencies of each document
def load_files():
	ind_file = open('indexes/documents.txt','rb')
	dic = pickle.load(ind_file)
	ind_file.close()

	ind_file = open('indexes/documents_freq.txt','rb')
	df = pickle.load(ind_file)
	ind_file.close()

	docs = {}
	for file in dic:
		ind_file = open('indexes/'+str(dic[file])+'.txt','rb')
		docs[file] = pickle.load(ind_file)
		ind_file.close()

	return dic, df, docs


# function => get_term_frequency(termFrequency,words)
# param :
# 	1) termFrequency : original dictionary of term frequencies
# 	2) words : list of words to to added to termFrequency dictionary
# return :
#	termFrequency : updated dictionary
def get_term_frequency(termFrequency,words):
    for word in words:
        if word in termFrequency:
            termFrequency[word] += 1
        else:
            termFrequency[word] = 1
    return termFrequency



# function => get_document_frequency(documents_freq,term_freq)
# param :
# 	1) documents_freq : original dictionary of document frequencies
# 	2) list of words to to added to documents_freq dictionary
# return :
#	documents_freq : updated dictionary
def get_document_frequency(documents_freq,term_freq):
    for word in term_freq:
        if word in documents_freq:
            documents_freq[word] += 1
        else:
            documents_freq[word] = 1
    return documents_freq



# function => reset_documents(void)
# resets the indexes in document and empty the document list
def reset_documents():
    ind_file = open('indexes/documents.txt','rb')
    dic = pickle.load(ind_file)
    ind_file.close()
    for i in range(len(dic)):
        ind_file = open('indexes/'+str(i)+'.txt','wb')
        pickle.dump({},ind_file)
        ind_file.close()
    ind_file = open('indexes/documents.txt','wb')
    pickle.dump({},ind_file)
    ind_file.close()
    ind_file = open('indexes/documents_freq.txt','wb')
    pickle.dump({},ind_file)
    ind_file.close()



# function => add_document(file_name)
# param :
# 	1) file_name : name of the document in documents/ directory to be indexed
def add_document(file_name):

	# check if file exists in directory
    if not os.path.isfile('./documents/' + file_name):
        print('no file named ' + file_name)
        return -1

	# load the list of documents
    ind_file = open('indexes/documents.txt','rb')
    dic = pickle.load(ind_file)
    ind_file.close()

	# check if given file exists (so it would not be indexed again)
    if file_name in dic.keys():
        print('file aleardy exists')
        return 0

	# add the document to the list
    dic[file_name] = len(dic)

	# load the document frequency dictionary
    doc_freq_file = open('indexes/documents_freq.txt','rb')
    df = pickle.load(doc_freq_file)
    doc_freq_file.close()

	#load the content of file to list of words
    split_up = os.path.splitext(file_name)
    if split_up[1] == '.pdf':
        pdffileobj=open('documents/'+file_name,'rb')
        pdfreader=PyPDF2.PdfFileReader(pdffileobj)
        text=''
        for i in range(pdfreader.numPages):
            pageobj=pdfreader.getPage(i)
            text+=pageobj.extractText()

    elif split_up[1] != '.txt':
        print('extension must be .txt or .pdf')
        return 0

    else:
        text=open('documents/'+file_name,'rb')

	# process the list of words (cleaning the data)
    text = pre_processing(text)

	# update term frequency
    term_freq = get_term_frequency({},text)

	# update document frequency
    df = get_document_frequency(df,term_freq)

    #print(term_freq)

	# store the term frequency in new index
    ind_file = open('indexes/'+str(dic[file_name])+'.txt','wb')
    pickle.dump(term_freq,ind_file)
    ind_file.close()

	# store the document frequency in the index
    doc_freq_file = open('indexes/documents_freq.txt','wb')
    pickle.dump(df,doc_freq_file)
    doc_freq_file.close()

	# store the documents list in file
    ind_file = open('indexes/documents.txt','wb')
    pickle.dump(dic,ind_file)
    ind_file.close()

    documents()




# function => documents(void)
# prints the list of documents with Id
def documents():
    ind_file = open('indexes/documents.txt','rb')
    dic = pickle.load(ind_file)
    ind_file.close()
    col = ['Filename','Id']
    s = "Documents : \n%50s%10s\n\n" % (col[0],col[1])
    for a in dic:
        s += "%50s%10s\n" % (a,dic[a])
    print(s)

#add_document(input('Filename : '))
#reset_documents()
#files = ['BooleanRetrieval.pdf'  ,'DictionaryAndPostingList.pdf' , 'TolerentRetrieval.pdf' , 'IndexCompression.pdf' , 'IndexConstruction.pdf']

#for file in files:
    #add_document(file)
