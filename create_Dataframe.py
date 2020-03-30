import pandas as p
import datetime as dt
import yaml
import ast
import time
import numpy as np

try:
	from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
	from yaml import Loader, DUmper

with open('config.yaml', 'r') as f:
	config = yaml.load(f, Loader = Loader)

# 	p.set_option('display.max_columns', 20)
	p.set_option('display.width', None)
# 

#============================>>>>>>>>>>>>>>>>> changed config file to read in the spud raw output file instead of the sandpit one
df = p.read_csv(config['spud_raw_file'], sep=", '\|',", engine = "python")
df.columns = ['pk1', 'dtcreated', 'cntnt_hndlr', 'start_date', 'crsmain_pk1', 'end_date', 'parent_pk1', 'course_name', 'course_id']

df['pk1'] = df['pk1'].str[1:]
df['course_id'] = df['course_id'].str[:-1]

#convert pk1 to numeric values, set that as the primary index, sort all rows based on the pk1 index


df['pk1'] = p.to_numeric(df['pk1']) 
df.set_index(['pk1'], inplace = True)
df = df.sort_index()

# convert the datetime fields to datetimes from string ONLY DO IF DATETIMES ARE REQUIRED=====================

def convert_datetimes2(a):
    if(a[1]=="N"):
        return
    else:
    	temp = a[18:]
    	temp = dt.datetime(*ast.literal_eval(temp))
    	return temp

df['dtcreated']=df.dtcreated.apply(convert_datetimes2)
df['start_date']=df.start_date.apply(convert_datetimes2)
df['end_date'] = df.end_date.apply(convert_datetimes2)


#depth of content logic -> hashmap of index and parent_pk1========================================================
parent_key = {}
#filter out items which are at the base level
has_pk1 = df['parent_pk1'] != " None"
df1 = df[has_pk1]

for i in df1.index:
	parent_key[i] = int(df.loc[i,'parent_pk1'])


counts = []

for index in df.index:
	i = index
	count = 0
	while (i in parent_key):
		count +=1
		i = parent_key[i]
	counts.append(count)

df['counts'] = counts



# split up the subject code into the required elements================================================================ 

def split_subject_codes(a):
	temp = a[2:-1] 
	index = temp.find("_")
	#Case 1: no underscore - test subjects/ playpen subjects 
	if(index!=-1):
		main_code = temp[:index]
		temp = temp[index+1:]
		# print(main_code, temp)
		index = temp.find("_")
		year = temp[:index]
		temp = temp[index+1:]
		# print(year, temp)
		index = temp.find("_")
		if(index>0):
			semester = temp[:index]
			temp = temp[index+1:]
			# print(semester, temp)
			location = temp
		else:
			semester = temp
			location = None
		return [main_code, year, semester, location]
	else:
		return [temp,0,0,0]

df['stuff'] = df.course_id.apply(split_subject_codes)
df[['main_code','year', 'semester', 'location']] = p.DataFrame(df.stuff.values.tolist(), index= df.index)
del df['stuff']

df['parent_pk1'].replace(' None', 0, inplace=True)
df['year'] = df.year.apply(lambda x: np.where(str(x).isdigit(),x,0))
#=====================================================================================================================


# if a pickle object is needed, please run this code below============================================================ 
# with open('data_pick.pkl', 'wb') as pickle_file:
#  pickle.dump(df, pickle_file)                                          ***IF PICKLE OBJECT NEEDED***
#=====================================================================================================================

# if a CSV of the data is needed======================================================================================
if 'raw_data_needed' in list(config) and config['raw_data_needed']:
	df.to_csv(config['df_output_file'], sep=',')           

#=====================================================================================================================
# # without course id
# # df_depth= df.groupby(['course_name'], sort = False)['counts'].max()

# to include the counts in the main df table
# (df.groupby('course_name').agg({'counts':'max', 'course_id':'first'})).to_csv(config['df_depthreport'], sep=',')
# df.to_csv(config['df_depthreport'], sep=',')

df_depth= df.groupby('course_name').agg({'counts':'max', 'course_id':'first'})
df_depth.to_csv(config['df_depthreport'], sep=',')
