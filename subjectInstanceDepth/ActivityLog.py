from csvReader import csvReader
from Subject import Subject, SubjectInstance
from ContentItem import ContentItem
import ctypes
import cProfile
import pandas as pd
import datetime
import matplotlib as mpl 
import matplotlib.pyplot as plt
mpl.style.use(['ggplot'])



class ActivityLog:
	'''
	This is the wrapper class and therefore doesn't need a constructor.
	Tracks all of the SI created

	Steps:
	1. lookup and check if subject instance exits, if not create it
	2. add the relevant content item to that subject instance
	3. abstract out the dicitonary loolup function in another script
	4. use that script for both create_dataframe and for each subject instance here.
	'''

	# this dictionary records the individual subject instances, key is the subject instance name, and the value
	# is the subjectInstance object. Main purpose is to have a searchable collection to find if a subject
	# instance has already been inserted
	def __init__(self):
		self.subject_dict = {}

	def add_subject_instance(self, x, dictionary_of_subjects, rownum):
		'''
		To create subject objects within the activity log
		'''
		match = False #flag variable to see if subject instance was found
		temp = SubjectInstance(x['course_name'], x['main_code'], rownum, x['year'], x['semester'], x['location']) #create the current row into a temp subject instance object
		if(temp.name not in dictionary_of_subjects): #if the subject does not yet exist, create the subject key entry and add the subject instance to it 
			dictionary_of_subjects[temp.name] = (Subject(x.course_name, x.main_code))
			(dictionary_of_subjects[temp.name]).subject_instances.append(temp);
			return id(temp)	

		else:	#subject exists in dictionary
			subject_temp = dictionary_of_subjects[temp.name]
			subject_instances_temp = subject_temp.subject_instances
			for x in subject_instances_temp:
				if temp.equals(x):
					# print("duplicate")
					return id(x)
					match = True
					break
			if(match==False): 
				subject_instances_temp.append(temp)
				return id(temp) #return unique id of the inserted / matched subject instance

	def calculate_max_depth(self,dictionary_of_subjects):
		'''
		calucaltes and records the maximum subject depth, and outputs the absolute maximum depth outof any subjects to stdout
		'''
		self.max_max_depth = 0
		maxSI = []
		for subject in dictionary_of_subjects:
			subject = dictionary_of_subjects[subject]

			#Sort the subject instances within the subject on (year,semester)
			subject.subject_instances.sort(key = lambda x: (x.year, x.teachingPeriod)) 

			for subject_instance in subject.subject_instances:
				# print("			{}, {}".format(subject_instance.teachingPeriod,subject_instance.year)) #testing for 
				max_depth, SI= subject_instance.calculate_max_depth(csv.parent_key)

				if(max_depth > self.max_max_depth):
					self.max_max_depth = max_depth
					maxSI = [SI]

				elif(max_depth == self.max_max_depth):
					maxSI.append(SI)

			#get the max of the max depths, and a list of the subjects that have this depth			
		print("Max_max_depth: {}, {}".format(self.max_max_depth, [[x.name,x.subjectCode] for x in maxSI]))	


#buiding=========================================================================================

if __name__ == "__main__":
	csv = csvReader('df_spud_output.csv')
	a = ActivityLog()
	dictionary_of_subjects = a.subject_dict
	# exit()
	#loop through csv to obtain each row
	for pk in csv.df.index:
		'''
		Add the subject instance itself, this returns the id of the subject instance that is added/
		the subject instance that is a direct match or a duplicate. Use this id to add the phsyical content
		item in there as well
		'''
		x = (csv.return_row(pk))
		series_name = (x[-1]) #actual row returned
		x=x[0]	#index of row / pk of the row returned

		# returns the unique id of the subject instance which is either inserted, or is a match
		matching_instance = a.add_subject_instance(x, dictionary_of_subjects, series_name)
		y = ctypes.cast(matching_instance, ctypes.py_object).value
		y.content_items.append(ContentItem(pk, x.cntnt_hndlr, x.parent_pk1, x.crsmain_pk1, x.start_date, x.end_date, x.cntnt_hndlr))
	

	#calls the method to calcualte the maximum depth of each subject instance
	a.calculate_max_depth(dictionary_of_subjects)
	filename = 0
	plot_flag = True
	for subject in dictionary_of_subjects:
		subject = dictionary_of_subjects[subject]
		row_list = []
		filename +=1
		plot_flag = True
		for subject_instance in subject.subject_instances:
			subject_instance.calculate_item_types()
			if subject_instance.teachingPeriod != '0':
				dict1 ={}
				dict1['folder_count'] = subject_instance.cntnt_folder_count
				dict1['file_count'] = subject_instance.cntnt_file_count
				dict1['testlink_count'] = subject_instance.cntnt_testlink_count
				dict1['turnitin_count'] = subject_instance.cntnt_turnitin_count
				dict1['externallink_count'] = subject_instance.cntnt_externallink_count
				dict1['other_count'] = subject_instance.cntnt_other_count
				dict1['document'] = subject_instance.cntnt_document_count

				dict1['year'] = subject_instance.year
				dict1['teachingPeriod'] = subject_instance.teachingPeriod
				if subject_instance.teachingPeriod in ['SM1','MAR', 'YRL']:
					dict1['timestamp'] = datetime.date(subject_instance.year, 3, 1)
				elif subject_instance.teachingPeriod in ['SM2','JUN'] :
					dict1['timestamp'] = datetime.date(subject_instance.year, 6, 1)
				elif subject_instance.teachingPeriod in ['JAN','RS1','SUM','RS2', 'TM1']:
					dict1['timestamp'] = datetime.date(subject_instance.year, 1, 1)
				elif subject_instance.teachingPeriod == 'FEB':
					dict1['timestamp'] = datetime.date(subject_instance.year, 2, 1)
				elif subject_instance.teachingPeriod in ['APR', 'TM2']:
					dict1['timestamp'] = datetime.date(subject_instance.year, 4, 1)
				elif subject_instance.teachingPeriod == 'MAY':
					dict1['timestamp'] = datetime.date(subject_instance.year, 5, 1)
				elif subject_instance.teachingPeriod in ['JUL','RS2','WIN','TM3']:
					dict1['timestamp'] = datetime.date(subject_instance.year, 7, 1)
				elif subject_instance.teachingPeriod == 'AUG':
					dict1['timestamp'] = datetime.date(subject_instance.year, 8, 1)
				elif subject_instance.teachingPeriod == 'SEP':
					dict1['timestamp'] = datetime.date(subject_instance.year, 9, 1)
				elif subject_instance.teachingPeriod in ['TM4', 'OCT']:
					dict1['timestamp'] = datetime.date(subject_instance.year, 10, 1)
				elif subject_instance.teachingPeriod == 'NOV':
					dict1['timestamp'] = datetime.date(subject_instance.year, 11, 1)
				elif subject_instance.teachingPeriod == 'DEC':
					dict1['timestamp'] = datetime.date(subject_instance.year, 12, 1)	
				
				else:
					plot_flag = False
					break

				dict1['max_depth'] = subject_instance.max_depth
				row_list.append(dict1)

		if (plot_flag) and (len(row_list)>0):		
			df = pd.DataFrame(row_list)
			plot = df.plot(x='timestamp', y = ['testlink_count', 'folder_count', 'file_count', 'externallink_count', 'turnitin_count', 'other_count', 'max_depth'], kind = 'line', marker='.', \
				title = (subject_instance.name[2:-1] +" ("+ subject_instance.subjectCode+ ")"), label = ['Test-Links', 'Folders', 'Files', 'External Links', 'TurnItIn(s)', 'Other', 'Depth'])
			plot.set_xlabel("Time Period")
			plt.xlim(datetime.date(2011,1,1), datetime.date(2019,12,31))
			plot.set_ylabel("Maximum depth of LMS content items")
			plt.ylim(bottom = -0.4)
			plt.savefig("plots_SPUD/" + str(filename)+ ". " + subject_instance.subjectCode + ".png")
			plt.close()



	'''
	write completed subject- subject-instance - contentitems structure to output file
	'''
	with open('subject_dictionary.txt', 'w') as output:
		for subject in dictionary_of_subjects:
			subject = dictionary_of_subjects[subject]
			# print(subject)
			output.write(subject.__str__()+"\n")
			for subject_instance in subject.subject_instances:
				output.write("		" + subject_instance.__str__()+"\n")
				output.write("		" + "Max Depth: " + str(subject_instance.max_depth)+"\n")
				for cont_item in subject_instance.content_items:
					output.write("				" + cont_item.__str__()+"\n")