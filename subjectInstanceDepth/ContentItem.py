class ContentItem:
	'''
	Class for each entry in the cleaned data file, 
	each instance represents a content item in the Blackboard LMS

	These will be stored as a collection in the ActivityLog class.
	'''

	def __init__(self, BlackboardKey, _type, parent_key, subjectFK, startDate, endDate, typee):
		'''
		Constructor method for the ContentItem class
		'''

		self.BlackboardKey = BlackboardKey
		self._type = _type
		self.parent_key = parent_key
		self.subjectFK = subjectFK
		self.startDate = startDate
		self.endDate = endDate
		self.typee = typee

	def __str__(self):
		'''
		Discover which content item is being referred to and what subject it belongs to. 
		'''
		return "BlackboardKey: {}, parent_key: {}, Type: {}, StartDate: {}, endDate: {}".format(self.BlackboardKey, self.parent_key, self._type, self.startDate, self.endDate)


