from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
import subprocess
import inquirer
from colorama import Fore, Back, Style

def search(phrase, limit=10):
	searcher = ix.searcher()
	query = QueryParser("content", ix.schema).parse(phrase)
	phrase_hits = searcher.search(query, limit=limit)
	phrase_hits_count = len(phrase_hits)
	all_hits = searcher.search(query, limit=None)
	document_hits = set(res['title'] for res in all_hits)
	document_hits_count = len(document_hits)
	print(Fore.BLUE + f'found {phrase_hits_count} hits in {document_hits_count} documents')
	return(phrase_hits, list(document_hits))

def open_files(filenames, limit=10):
	for fname in filenames[:limit]:
		if sys.platform == 'darwin':
			subprocess.call(['open', '-a', 'TextEdit', fname])
		else:
			os.system('notepad.exe '+fname)
	return

def print_documents(filenames):
	for fname in filenames:
		print(Fore.BLUE + fname)

def get_key_terms(hits):
	kterms = hits.key_terms('content', numterms=20)
	ret = []
	for term, score in kterms:
		if score>.18:
			ret.append(term)
	return(ret)

def generate_next_question():
	q = [
	inquirer.List('Next',
		message='What would you like to do next?',
		choices=['Print all results',
		'Get key terms',
		'Open files',
		'Search again',
		'Exit'],
		default='Exit')
	]
	return(q)

def print_logo():
	print(Fore.RED + r"""
	 _____ ______ _   __                          _     
	/  __ \| ___ \ | / /                         | |    
	| /  \/| |_/ / |/ /   ___  ___  __ _ _ __ ___| |__  
	| |    |  __/|    \  / __|/ _ \/ _` | '__/ __| '_ \ 
	| \__/\| |   | |\  \ \__ \  __/ (_| | | | (__| | | |
	 \____/\_|   \_| \_/ |___/\___|\__,_|_|  \___|_| |_|
	 """)
	return

if __name__ == '__main__':
	print_logo()
	ix = open_dir('indexdir')
	q = [
    inquirer.Text('Search',
                  message='Search')
	]	
	answers = inquirer.prompt(q)
	search_phrase = answers['Search']
	phrase_hits, doc_hits = search(search_phrase)
	q = generate_next_question()
	next_ = inquirer.prompt(q)
	next_ = next_['Next']
	while next_ != 'Exit':
		if 'Get key terms' == next_:
			terms = get_key_terms(phrase_hits)
			print(Fore.BLUE + 'getting key terms')
			for term in terms:
				print(Fore.BLUE + term)
		elif 'Open files' == next_:
			q = [inquirer.Text('num_to_open',
				message='how many to open?',
				default='10')]
			answer = inquirer.prompt(q)
			lim = int(answer['num_to_open'])
			print(Fore.BLUE + 'opening...')
			fnames = [res['title'] for res in phrase_hits]
			open_files(fnames, limit=lim)
		elif 'Print all results' == next_:
			fnames = [res['title'] for res in phrase_hits]
			print_documents(doc_hits)
		elif 'Search again' == next_:
			q = [
		    inquirer.Text('Search',
		                  message='Search')
			]	
			answers = inquirer.prompt(q)
			search_phrase = answers['Search']
			phrase_hits, doc_hits = search(search_phrase)
		else:
			print(Fore.BLUE + 'error')
		q = generate_next_question()
		next_ = inquirer.prompt(q)
		next_ = next_['Next']
	print(Fore.BLUE + 'Thank you, finished!')





