# Python - KYLLIAN HAMADOU - D19124158

class SurveyResponse:
	def __init__(self):
		pass


class Survey:
	def __init__(self, surveyName):
		self.surveyName = surveyName
		self.questions = []
		self.surveyResponses = []

class Controller:
	def __init__(self):
		self.surveyslist = []

	def CreateSurvey(self, surveyName):
		newSurvey = Survey(surveyName)
		self.surveyslist.append(newSurvey)
		return newSurvey.surveyName + ' have been created'