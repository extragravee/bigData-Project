'''
Classes:
Subject
SubjectInstance
SubjectInstance inherits from Subject
'''
import numpy as np
import math as mt
#===========================================================================================
class Subject:
	'''
	Base class for Subject, holds the name and the subject code
	'''
	def __init__(self, name, subjectCode):
		'''
		constructor for the subject class
		'''
		self.name = name 
		self.subjectCode = subjectCode 
		self.subject_instances = []

	def __str__(self):
		return "Subject: {}, SubjectCode: {}".format(self.name, self.subjectCode)


#===========================================================================================


class SubjectInstance(Subject):
	'''
	Child class for subject -> specific instance of each subject differentiated by the
	subject teaching period and the location it runs in
	'''
	def __init__(self, name, subjectCode, BlackboardKey, year, teachingPeriod, location):
		'''
		constructor for the SubjectInstance class
		'''
		Subject.__init__(self, name, subjectCode)   
		self.BlackboardKey = BlackboardKey
		self.year = year
		self.teachingPeriod = teachingPeriod
		self.max_depth = 0
		self.cntnt_document_count = 0
		self.cntnt_file_count = 0
		self.cntnt_folder_count = 0
		self.cntnt_externallink_count = 0
		self.cntnt_turnitin_count = 0
		self.cntnt_testlink_count = 0
		self.cntnt_other_count = 0
		self.location = location
		self.content_items = []

	def __str__(self):
		'''
		toString method 
		'''
		return "Subject Instance: {} subject (code:{}) runs in the year {}, in the teaching period {} in {}."\
		.format(self.name, self.subjectCode, self.year, self.teachingPeriod, self.location)

	def calculate_max_depth(self, parent_key):
		'''
		Calculates the maximum depth of the particular subject instance
		'''
		for content_item in self.content_items:
			i = content_item.parent_key
			count = 0
			while (i in parent_key):
				count +=1
				i = parent_key[i]
			if count > self.max_depth:
				self.max_depth = count
		return self.max_depth, self

	def calculate_item_types(self):
		'''
		calculates the number of each type of content item for each subject instance
		'''
		for content_item in self.content_items:
			if content_item.typee == "test-link":
				self.cntnt_testlink_count+=1
			elif content_item.typee == "folder":
				self.cntnt_folder_count+=1
			elif content_item.typee == "file":
				self.cntnt_file_count+=1
			elif content_item.typee == "externallink":
				self.cntnt_externallink_count+=1
			elif content_item.typee == "turnitin":
				self.cntnt_turnitin_count+=1
			elif content_item.typee == "document":
				self.cntnt_document_count+=1
			else:
				self.cntnt_other_count+=1

	def addContentItem(self, contentItem):
		'''
		adds a single content item to the calling subject instance
		'''
		self.contentItems.append(contentItem)

	def equals(self, other):
		'''
		equals method for the subjectInstance class
		'''
		if self.year == other.year:
			if (self.location == other.location):
				if self.name == other.name:
						if self.teachingPeriod == other.teachingPeriod:
							return True
		return False
	