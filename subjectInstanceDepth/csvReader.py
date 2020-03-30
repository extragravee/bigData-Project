import pandas as pd
import numpy as np

class csvReader:
	'''
	This class reads through the clean output file csv, and transforms each row into a ContentItem object.

	Steps followed:
	1. Read csv row
	2. Determine if that subject instance exists
	3. Add subject instance to the collection if required
	'''

	def __init__(self, path):
		'''
		contructor method for the csv reader 
		'''
		self.read_csv(path)
		self.create_lookup_dict()

	def read_csv(self, path):
		'''
		reads in and stores the clean csv in a static variable: df
		'''
		#parse csv
		dtypes = {'pk1': 'int', 'dtcreated': 'str', 'cntnt_hndlr':'str', 'start_date':'str', 'crsmain_pk1':'int', 'end_date':'str', 'parent_pk1':'int', 'course_name':'str', 'course_id': 'str', 'counts':'int',
		'main_code': 'str', 'year':'int', 'semester':'str', 'location':'str'}
		parse_dates = ['dtcreated', 'start_date', 'end_date']
		self.df = pd.read_csv(path, dtype = dtypes, parse_dates = parse_dates)

		#set index to pk, delete counts column, add locations in, print preview
		self.df.set_index(['pk1'], inplace = True)
		del self.df['counts']
		self.df.location.fillna('PAR_1', inplace = True)

		#edit content handler column to make it easy to read
		content_types = self.df.cntnt_hndlr.values
		aux_array = []

		rownum = 0
		for content_type in content_types:
			if(content_type.find("folder")>-1):
				aux_array.append("folder")
			elif (content_type.find("document")>-1):
				aux_array.append("document")
			elif (content_type.find("file")>-1):
				aux_array.append("file")
			elif (content_type.find("externallink")>-1):
				aux_array.append("externallink")	
			elif (content_type.find("turnitin")>-1):
				aux_array.append("turnitin")
			elif (content_type.find("test-link")>-1):
 				aux_array.append("test-link")
			else:
				aux_array.append("other")
			rownum+=1
		self.df['cntnt_hndlr'] = aux_array
		self.remove_invalid()
		print(self.df.head(124))

	def return_row(self, rownum):
		'''
		returns row located at rownum
		'''
		return [self.df.loc[rownum], rownum]

	def create_lookup_dict(self):
		'''
		creates the content_item, parent key dictionary
		'''
		self.parent_key = {}
		for i in self.df.index:
			self.parent_key[i] = self.df.loc[i, 'parent_pk1']


	def remove_invalid(self):
		'''
		removes content items which are remnants of copied over subjects from
		previous years. Ensures the dterministic trends from the time series
		are removed
		'''
		pks_file = open("shorter_toc.txt", "r")
		lines = pks_file.read().split('\n')
		lines = [int(x) if x!='' else 0 for x in lines]
		to_delete = self.df[self.df.parent_pk1 == 0]
		to_delete = to_delete[to_delete.cntnt_hndlr == 'folder']
		to_delete = to_delete[~to_delete.index.isin(lines)]
		to_delete = to_delete.index.values
		self.df.drop(to_delete, inplace = True)
		# print(self.df)