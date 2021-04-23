from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
import glob
import os
import tqdm

schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True))
if not os.path.exists("indexdir"):
	os.mkdir("indexdir")
	ix = create_in("indexdir", schema)
else:
	ix = open_dir("indexdir")

writer = ix.writer()
texts = glob.glob("*.txt")
print(f"Found {len(texts)} documents, indexing...")
for i,txt in enumerate(tqdm.tqdm(texts)):
	with open(txt, 'r') as f:
		writer.add_document(title=txt, path=str(i), content=f.read())
print("Committing documents...")
writer.commit()
print("Complete")
