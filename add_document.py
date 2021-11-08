import PyPDF2
import pickle
import os

from word_processor import pre_processing

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

def get_term_frequency(termFrequency,words):
    for word in words:
        if word in termFrequency:
            termFrequency[word] += 1
        else:
            termFrequency[word] = 1
    return termFrequency

def get_document_frequency(documents_freq,term_freq):
    for word in term_freq:
        if word in documents_freq:
            documents_freq[word] += 1
        else:
            documents_freq[word] = 1
    return documents_freq

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


def add_document(file_name):
    if not os.path.isfile('./documents/' + file_name):
        print('no file named ' + file_name)
        return -1
    #df = pd.read_csv('indexes/documents.csv')

    ind_file = open('indexes/documents.txt','rb')
    dic = pickle.load(ind_file)
    ind_file.close()

    if file_name in dic.keys():
        print('file aleardy exists')
        return 0

    dic[file_name] = len(dic)

    doc_freq_file = open('indexes/documents_freq.txt','rb')
    df = pickle.load(doc_freq_file)
    doc_freq_file.close()

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
    text = pre_processing(text)
    term_freq = get_term_frequency({},text)
    df = get_document_frequency(df,term_freq)

    print(term_freq)

    ind_file = open('indexes/'+str(dic[file_name])+'.txt','wb')
    pickle.dump(term_freq,ind_file)
    ind_file.close()

    doc_freq_file = open('indexes/documents_freq.txt','wb')
    pickle.dump(df,doc_freq_file)
    doc_freq_file.close()

    ind_file = open('indexes/documents.txt','wb')
    pickle.dump(dic,ind_file)
    ind_file.close()

    documents()


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
