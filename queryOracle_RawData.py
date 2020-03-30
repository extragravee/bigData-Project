'''
File is to read the data from oracle database, in a importable format to python pandas in order to create a df online, table bb_bb60.course_contents
'''

import pandas.io.sql
import cx_Oracle
import datetime 
import yaml

import pickle

try:
	from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
	from yaml import Loader, Dumper


with open('config.yaml', 'r') as f:
	config = yaml.load(f, Loader = Loader)
connection = cx_Oracle.connect(config['db_string'])
curr = connection.cursor()
###############################################################################################
### Total rows = 261555

with open(config['raw_output_file'], "w") as output:

	###raw data dump
	# curr.execute("select pk1,'|',dtcreated,'|',content_type,'|',start_date,'|',crsmain_pk1,'|',end_date,'|',lesson_ind,'|',folder_ind,'|',parent_pk1,'|',folder_type,'|',dbms_lob.substr(main_data, 100,1) from bb_bb60.course_contents")
	curr.execute("select A.pk1,'|',A.dtcreated,'|',A.cnthndlr_handle,'|',A.start_date,'|',A.crsmain_pk1,'|',A.end_date,'|',A.parent_pk1,'|',B.course_name,'|', B.course_id FROM bb_bb60.course_contents A join bb_bb60.course_main B ON A.crsmain_pk1 = B.pk1")
	'''

	Main query needs the following logic:
	Select all items from course_contents table 
	EXCEPT IF 
	ITEM is a folder AND
	does NOT have a PARENT_PK1 AND
	PK1 exists in the following query

	Gets PK from table of contents, need PK to exist in here to be valid available content item, if PK not in this query, its just a remnant of a copied over item
	select course_contents_pk1 from bb_bb60.course_toc WHERE target_type = 'CONTENT_LINK' ;

	'''
	res = curr.fetchall()
	
	for line in res:
		output.write(str(line)+"\n")


###############################################################################################
curr.close()
connection.close()
print("==============Done==============")
