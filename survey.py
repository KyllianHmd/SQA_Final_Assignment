# Python - KYLLIAN HAMADOU - D19124158

from statistics import stdev

def IndexInList(index, lst):
	if (index < len(lst)):
		return True
	return False

def Average(lst): 
    return sum(lst) / len(lst)

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
		
class SurveyResponse:
	def __init__(self, userEmail):
		self.userEmail = userEmail
		self.responses = []

	def AddResponse(self, response, userEmail, questionsNumber):
		if questionsNumber <= len(self.responses):
			return "Error: You can't add more responses than the number of question."
		self.responses.append(response)
		return None

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

	def AddResponse(self, response, userEmail):
		if len(self.questions) == 0:
			return "Error: Sorry, you can't add a response because there are no questions"
		for surveyResponse in self.surveyResponses:
			if surveyResponse.userEmail == userEmail:
				err = surveyResponse.AddResponse(response, userEmail, len(self.questions))
				if err != None:
					return err
				return None

		newSurveyResponse = SurveyResponse(userEmail)
		newSurveyResponse.AddResponse(response, userEmail, len(self.questions))
		self.surveyResponses.append(newSurveyResponse)
		return None

	def GetSurveyResponses(self):
		return self.surveyResponses

	def GetSurveyStatistics(self):
		score = 0
		scoreValues = []
		for surveyResponse in self.surveyResponses:
			score = sum(surveyResponse.responses)
			scoreValues.append(score)

		minValue = min(scoreValues)
		maxValue = max(scoreValues)
		average = Average(scoreValues)
		average = round(average, 2)
		if len(scoreValues) <= 1:
			sd = "Error: It requires a minimum of 2 users to calculate the standard deviation"
		else:
			sd = stdev(scoreValues)
			sd = round(sd, 2)
		return minValue, maxValue, average, sd, "None"

	def GetQuestionStatistics(self, question):
		indexQ = self.questions.index(question)

		score = 0
		scoreValues = []
		for surveyResponse in self.surveyResponses:
			inList = IndexInList(indexQ, surveyResponse.responses)
			if inList == False:
				minValue = min(scoreValues)
				maxValue = max(scoreValues)
				average = Average(scoreValues)
				average = round(average, 2)
				if len(scoreValues) <= 1:
					sd = "Error: It requires a minimum of 2 users to calculate the standard deviation"
				else:
					sd = stdev(scoreValues)
					sd = round(sd, 2)
				return minValue, maxValue, average, sd, "None"
			score = surveyResponse.responses[indexQ]
			scoreValues.append(score)

		minValue = min(scoreValues)
		maxValue = max(scoreValues)
		average = Average(scoreValues)
		average = round(average, 2)
		if len(scoreValues) <= 1:
			sd = "Error: It requires a minimum of 2 users to calculate the standard deviation"
		else:
			sd = stdev(scoreValues)
			sd = round(sd, 2)
		return minValue, maxValue, average, sd, "None"


class Controller:
	def __init__(self):
		self.surveyslist = []

	def CreateSurvey(self, surveyName):
		newSurvey = Survey(surveyName)
		self.surveyslist.append(newSurvey)
		return newSurvey.surveyName + ' have been created'

	def GetSurveysList(self):
		return self.surveyslist

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

	def GetSurvey(self, surveyName):
		for survey in self.surveyslist:
			i = 0
			if survey.surveyName == surveyName:
				i = 1 
				return survey
		if i == 0:
			err = "Error: Sorry, the survey '" + surveyName + "' doesn't exist"
			return err

	def AddResponse(self, surveyName, response, userEmail):
		if (RepresentsInt(response) == True):
			if (int(response) <= 5 and int(response) >= 1):
				for survey in self.surveyslist:
					i = 0
					if survey.surveyName == surveyName:
						i = 1
						err = survey.AddResponse(int(response), userEmail)
						if err != None:
							return err
						else:
							return "The response '" + str(response) + "' have been added by '" + userEmail + "' in the survey '" + surveyName + "'"
				if i == 0:
					err = "Error: Sorry, you can't add a response because the survey '" + surveyName + "' doesn't exist."
					return err
			else:
				return "Error: The response must be an integer between 1 and 5."
		else:
			return "Error: The response must be a valid integer."

	def GetSurveyResponses(self, surveyName):
		for survey in self.surveyslist:
			i = 0
			if survey.surveyName == surveyName:
				i = 1
				surveyResponses = survey.GetSurveyResponses()
				return surveyResponses
		if i == 0:
			return "Error: Sorry, the survey '" + surveyName + "' doesn't exist."
	
	def GetSurveyStatistics(self, surveyName):
		for survey in self.surveyslist:
			i = 0
			if survey.surveyName == surveyName:
				i = 1 
				minValue, maxValue, average, sd, err = survey.GetSurveyStatistics()
				return minValue, maxValue, average, sd, err
		if i == 0:
			return 0, 0, 0, 0, "Error: Sorry, the survey '" + surveyName + "' doesn't exist."

	def GetQuestionStatistics(self, question, surveyName):
		for survey in self.surveyslist:
			i = 0
			if survey.surveyName == surveyName:
				i = 1 
				minValue, maxValue, average, sd, err = survey.GetQuestionStatistics(question)
				return minValue, maxValue, average, sd, err
		if i == 0:
			return 0, 0, 0, 0, "Error: Sorry, the survey '" + surveyName + "' doesn't exist."