# Modify path for testing
import os,sys
if __name__ == "__main__":
	# Append settings folder to path
	sys.path.append('C:\\Users\\jsteffen\\Documents\\dev\\acescisat\\')
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acescisat.settings")

	# Testing Imports
	import django
	django.setup()

from django.shortcuts import render_to_response
from publications.models import Publication,List,PublicationLists

class pub:
	def __init__(self,authors,title,journal,volume,pages,pdf):
		self.authors = authors
		self.title = title
		self.journal = journal
		self.volume = volume
		self.pages = pages
		self.pdf = pdf

	def __str__(self):
		text = "{}, {}, {}, {}, {}".format(self.authors, self.title, self.journal, self.volume, self.pages)
		return text
		
	def __repr__(self):
		text = "{}, {}, {}, {}, {}".format(self.authors, self.title, self.journal, self.volume, self.pages)
		return text

# Create your views here.
def index(request):
	# id, publication_id, list_id
	pub2mol = PublicationLists.objects.all() 
	
	# list_id as id, list, description
	molecules =  List.objects.filter(list__contains='mol') 
	
	# pub_id as id, authors, title, journal, volume, pages, pdf
	pubs = Publication.objects.all() 
	
	mol_dict = {}
	count = 0
	for entry in pub2mol:
		cur_lid = entry.list_id
		cur_pid = entry.publication_id

		# Check if current list id exists in filtered molecules list.
		if molecules.filter(id = cur_lid).exists():
			list_query = molecules.get(id = cur_lid)
		else:
			continue
			
		pub_query = pubs.get(id = cur_pid)
		
		cur_mol = list_query.list.replace('mol_','').replace('_val','')
		cur_pub = pub(pub_query.authors, pub_query.title, pub_query.journal, 
		              pub_query.volume, pub_query.pages, pub_query.pdf)
					  
		if cur_mol in mol_dict:
			existing_entry = mol_dict[cur_mol]
			existing_entry.append(cur_pub)
			mol_dict[cur_mol] = existing_entry
		else:
			mol_dict[cur_mol] = [cur_pub]
		
		#print(cur_mol)
		#print(cur_pub,'\n')
		
		# if count==15:
			# for key,value in mol_dict.items():
				# print(key,value,'\n')

			# sys.exit()
		# else:
			# count += 1
			
	return render_to_response(os.path.join('molecules','index.html'),
	context={})
	
def molecules35(request):
	return render_to_response(os.path.join('molecules','molecules35.html'))
	
def molecules30(request):
	return render_to_response(os.path.join('molecules','molecules30.html'))
	
def molecules22(request):
	return render_to_response(os.path.join('molecules','molecules22.html'))
	
def validation_O3(request):
	return render_to_response(os.path.join('molecules','validation_O3.html'))
	
def testtable(request):
	return render_to_response(os.path.join('molecules','testtable.html'))

if __name__ == '__main__':
	index('garbage')