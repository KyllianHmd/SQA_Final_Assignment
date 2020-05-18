# Python - KYLLIAN HAMADOU - D19124158

class SurveyResponse:
	def __init__(self):
		pass


class Survey:
	def __init__(self, surveyName):
		self.surveyName = surveyName
		self.questions = []
		self.surveyResponses = []

	def AddQuestion(self, question):
		if (len(self.questions) < 10):
			self.questions.append(question)
			return None
		else:
			return "Error: You can't add more than 10 questions"

class Controller:
	def __init__(self):
		self.surveyslist = []

	def CreateSurvey(self, surveyName):
		newSurvey = Survey(surveyName)
		self.surveyslist.append(newSurvey)
		return newSurvey.surveyName + ' have been created'

	def AddQuestion(self, surveyName, question):
		for survey in self.surveyslist:
			i = 0
			if survey.surveyName == surveyName:
				i = 1
				err = survey.AddQuestion(question)
				if err != None:
					return err
				return "'" + question + "' have been added in your survey '" + surveyName + "'"
		if i == 0:
			err = "Error: Sorry, you can't add a question because the survey '" + surveyName + "' doesn't exist"
			return err