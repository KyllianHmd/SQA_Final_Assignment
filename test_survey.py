import survey

def testCreateSurvey():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Cars Survey")
	assert surveyCreated == "Cars Survey have been created"

def testCreateSurvey2():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Food Survey")
	assert surveyCreated == "Food Survey have been created"

def testCreateSurvey3():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Test Survey")
	assert surveyCreated == "Test Survey have been created"

def testCreateSurvey4():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Kyllian's Survey")
	assert surveyCreated != "Florian's Survey have been created"

def testCreateSurvey5():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Mexican Survey")
	assert surveyCreated != "Indian Survey have been created"

def testCreateSurvey6():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Coding Survey")
	assert surveyCreated != "Programing Survey have been created"

def testGetSurveysList():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Mexican Survey")
	surveyList = example.GetSurveysList()
	for i in range(len(surveyList)):
		assert surveyList[i].surveyName == "Mexican Survey"
		
def testGetSurveysList2():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Mexican Survey")
	surveyCreated = example.CreateSurvey("Food Survey")
	surveyCreated = example.CreateSurvey("Lesson Survey")
	surveyList = example.GetSurveysList()
	for i in range(len(surveyList)):
		if (surveyList[i].surveyName == "Mexican Survey"):
			assert surveyList[i].surveyName == "Mexican Survey"
		if (surveyList[i].surveyName == "Food Survey"):
			assert surveyList[i].surveyName == "Food Survey"
		if (surveyList[i].surveyName == "Lesson Survey"):
			assert surveyList[i].surveyName == "Lesson Survey"

def testGetSurveysList3():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Mexican Survey")
	surveyCreated = example.CreateSurvey("Food Survey")
	surveyCreated = example.CreateSurvey("Cars Survey")
	surveyCreated = example.CreateSurvey("Coding Survey")
	surveyCreated = example.CreateSurvey("Kyllian's Survey")
	surveyCreated = example.CreateSurvey("Florian's Survey")
	surveyCreated = example.CreateSurvey("Diet Survey")
	surveyList = example.GetSurveysList()
	for i in range(len(surveyList)):
		if (surveyList[i].surveyName == "Mexican Survey"):
			assert surveyList[i].surveyName == "Mexican Survey"
		if (surveyList[i].surveyName == "Food Survey"):
			assert surveyList[i].surveyName == "Food Survey"
		if (surveyList[i].surveyName == "Cars Survey"):
			assert surveyList[i].surveyName == "Cars Survey"
		if (surveyList[i].surveyName == "Coding Survey"):
			assert surveyList[i].surveyName == "Coding Survey"
		if (surveyList[i].surveyName == "Kyllian's Survey"):
			assert surveyList[i].surveyName == "Kyllian's Survey"
		if (surveyList[i].surveyName == "Florian's Survey"):
			assert surveyList[i].surveyName == "Florian's Survey"
		if (surveyList[i].surveyName == "Diet Survey"):
			assert surveyList[i].surveyName == "Diet Survey"

def testAddQuestion():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Mexican Survey")
	addQuestion = example.AddQuestion("Mexican Survey", "Question1")
	assert addQuestion == "'Question1' have been added in your survey 'Mexican Survey'"

def testAddQuestion2():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Food Survey")
	addQuestion = example.AddQuestion("Food Survey", "Question1")
	assert addQuestion == "'Question1' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question2")
	assert addQuestion == "'Question2' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question1bis")
	assert addQuestion == "Error: Sorry, you can't add a question because the survey 'Mexican Survey' doesn't exist"
	addQuestion = example.AddQuestion("Life Survey", "Question2bis")
	assert addQuestion == "Error: Sorry, you can't add a question because the survey 'Life Survey' doesn't exist"

def testAddQuestion3():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Kyllian's Survey")
	surveyCreated = example.CreateSurvey("Florian's Survey")
	surveyCreated = example.CreateSurvey("Food Survey")
	addQuestion = example.AddQuestion("Kyllian's Survey", "Question1")
	assert addQuestion == "'Question1' have been added in your survey 'Kyllian's Survey'"
	addQuestion = example.AddQuestion("Kyllian's Survey", "Question2")
	assert addQuestion == "'Question2' have been added in your survey 'Kyllian's Survey'"
	addQuestion = example.AddQuestion("Florian's Survey", "Question1bis")
	assert addQuestion == "'Question1bis' have been added in your survey 'Florian's Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question1ter")
	assert addQuestion == "'Question1ter' have been added in your survey 'Food Survey'"

def testAddQuestion4():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Food Survey")
	addQuestion = example.AddQuestion("Food Survey", "Question1")
	assert addQuestion == "'Question1' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question2")
	assert addQuestion == "'Question2' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question3")
	assert addQuestion == "'Question3' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question4")
	assert addQuestion == "'Question4' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question5")
	assert addQuestion == "'Question5' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question6")
	assert addQuestion == "'Question6' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question7")
	assert addQuestion == "'Question7' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question8")
	assert addQuestion == "'Question8' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question9")
	assert addQuestion == "'Question9' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question10")
	assert addQuestion == "'Question10' have been added in your survey 'Food Survey'"
	addQuestion = example.AddQuestion("Food Survey", "Question11")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Food Survey", "Question12")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Food Survey", "Question13")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Food Survey", "Question14")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Food Survey", "Question15")
	assert addQuestion == "Error: You can't add more than 10 questions"

def testAddQuestion5():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Life Survey")
	surveyCreated = example.CreateSurvey("Mexican Survey")
	addQuestion = example.AddQuestion("Life Survey", "Question1")
	assert addQuestion == "'Question1' have been added in your survey 'Life Survey'"
	addQuestion = example.AddQuestion("Life Survey", "Question2")
	assert addQuestion == "'Question2' have been added in your survey 'Life Survey'"
	addQuestion = example.AddQuestion("Life Survey", "Question3")
	assert addQuestion == "'Question3' have been added in your survey 'Life Survey'"
	addQuestion = example.AddQuestion("Life Survey", "Question4")
	assert addQuestion == "'Question4' have been added in your survey 'Life Survey'"
	addQuestion = example.AddQuestion("Life Survey", "Question5")
	assert addQuestion == "'Question5' have been added in your survey 'Life Survey'"
	addQuestion = example.AddQuestion("Life Survey", "Question6")
	assert addQuestion == "'Question6' have been added in your survey 'Life Survey'"
	addQuestion = example.AddQuestion("Life Survey", "Question7")
	assert addQuestion == "'Question7' have been added in your survey 'Life Survey'"
	addQuestion = example.AddQuestion("Life Survey", "Question8")
	assert addQuestion == "'Question8' have been added in your survey 'Life Survey'"
	addQuestion = example.AddQuestion("Life Survey", "Question9")
	assert addQuestion == "'Question9' have been added in your survey 'Life Survey'"
	addQuestion = example.AddQuestion("Life Survey", "Question10")
	assert addQuestion == "'Question10' have been added in your survey 'Life Survey'"
	addQuestion = example.AddQuestion("Life Survey", "Question11")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Life Survey", "Question12")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Life Survey", "Question13")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Life Survey", "Question14")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Life Survey", "Question15")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Mexican Survey", "Question1")
	assert addQuestion == "'Question1' have been added in your survey 'Mexican Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question2")
	assert addQuestion == "'Question2' have been added in your survey 'Mexican Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question3")
	assert addQuestion == "'Question3' have been added in your survey 'Mexican Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question4")
	assert addQuestion == "'Question4' have been added in your survey 'Mexican Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question5")
	assert addQuestion == "'Question5' have been added in your survey 'Mexican Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question6")
	assert addQuestion == "'Question6' have been added in your survey 'Mexican Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question7")
	assert addQuestion == "'Question7' have been added in your survey 'Mexican Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question8")
	assert addQuestion == "'Question8' have been added in your survey 'Mexican Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question9")
	assert addQuestion == "'Question9' have been added in your survey 'Mexican Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question10")
	assert addQuestion == "'Question10' have been added in your survey 'Mexican Survey'"
	addQuestion = example.AddQuestion("Mexican Survey", "Question11")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Mexican Survey", "Question12")
	assert addQuestion == "Error: You can't add more than 10 questions"
	addQuestion = example.AddQuestion("Blablabla Survey", "Question1bis")
	assert addQuestion == "Error: Sorry, you can't add a question because the survey 'Blablabla Survey' doesn't exist"
	addQuestion = example.AddQuestion("France Survey", "Question2bis")
	assert addQuestion == "Error: Sorry, you can't add a question because the survey 'France Survey' doesn't exist"
	addQuestion = example.AddQuestion("YesYes Survey", "Question3bis")
	assert addQuestion == "Error: Sorry, you can't add a question because the survey 'YesYes Survey' doesn't exist"

def testAddResponse():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Cars Survey")
	addResponse = example.AddResponse("Cars Survey", 2, "kyllian@epitech.eu")
	assert addResponse == "Error: Sorry, you can't add a response because there are no questions"
	addResponse = example.AddResponse("Cars Survey", 3, "kyllian@epitech.eu")
	assert addResponse == "Error: Sorry, you can't add a response because there are no questions"

def testAddResponse2():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Cars Survey")
	addQuestion = example.AddQuestion("Cars Survey", "Question1")
	addResponse = example.AddResponse("Cars Survey", 2, "kyllian@epitech.eu")
	assert addResponse == "The response '2' have been added by 'kyllian@epitech.eu' in the survey 'Cars Survey'"
	addResponse = example.AddResponse("Cars Survey", 5, "kyllian@epitech.eu")
	assert addResponse == "Error: You can't add more responses than the number of question."

def testAddResponse3():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Cars Survey")
	addQuestion = example.AddQuestion("Cars Survey", "Question1")
	addQuestion = example.AddQuestion("Cars Survey", "Question2")
	addQuestion = example.AddQuestion("Cars Survey", "Question3")
	addQuestion = example.AddQuestion("Cars Survey", "Question4")
	addResponse = example.AddResponse("Cars Survey", 2, "kyllian@epitech.eu")
	assert addResponse == "The response '2' have been added by 'kyllian@epitech.eu' in the survey 'Cars Survey'"
	addResponse = example.AddResponse("Cars Survey", 5, "kyllian@epitech.eu")
	assert addResponse == "The response '5' have been added by 'kyllian@epitech.eu' in the survey 'Cars Survey'"
	addResponse = example.AddResponse("Cars Survey", 1, "kyllian@epitech.eu")
	assert addResponse == "The response '1' have been added by 'kyllian@epitech.eu' in the survey 'Cars Survey'"
	addResponse = example.AddResponse("Cars Survey", 1, "kyllian@epitech.eu")
	assert addResponse == "The response '1' have been added by 'kyllian@epitech.eu' in the survey 'Cars Survey'"

def testAddResponse4():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Cars Survey")
	addQuestion = example.AddQuestion("Cars Survey", "Question1")
	addQuestion = example.AddQuestion("Cars Survey", "Question2")
	addResponse = example.AddResponse("Cars Survey", 7, "kyllian@epitech.eu")
	assert addResponse == "Error: The response must be an integer between 1 and 5."
	addResponse = example.AddResponse("Cars Survey", 10, "kyllian@epitech.eu")
	assert addResponse == "Error: The response must be an integer between 1 and 5."
	addResponse = example.AddResponse("Cars Survey", 5, "kyllian@epitech.eu")
	assert addResponse == "The response '5' have been added by 'kyllian@epitech.eu' in the survey 'Cars Survey'"

def testAddResponse5():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Cars Survey")
	addQuestion = example.AddQuestion("Cars Survey", "Question1")
	addQuestion = example.AddQuestion("Cars Survey", "Question2")
	addResponse = example.AddResponse("Cars Survey", 1, "florian@epitech.eu")
	assert addResponse == "The response '1' have been added by 'florian@epitech.eu' in the survey 'Cars Survey'"
	addResponse = example.AddResponse("Cars Survey", 3, "thomas@epitech.eu")
	assert addResponse == "The response '3' have been added by 'thomas@epitech.eu' in the survey 'Cars Survey'"
	addResponse = example.AddResponse("Cars Survey", 4, "kyllian@epitech.eu")
	assert addResponse == "The response '4' have been added by 'kyllian@epitech.eu' in the survey 'Cars Survey'"

def testAddResponse6():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Cars Survey")
	addQuestion = example.AddQuestion("Cars Survey", "Question1")
	addQuestion = example.AddQuestion("Cars Survey", "Question2")
	addResponse = example.AddResponse("Food Survey", 1, "florian@epitech.eu")
	assert addResponse == "Error: Sorry, you can't add a response because the survey 'Food Survey' doesn't exist."
	addResponse = example.AddResponse("Yes Survey", 3, "thomas@epitech.eu")
	assert addResponse == "Error: Sorry, you can't add a response because the survey 'Yes Survey' doesn't exist."
	addResponse = example.AddResponse("Football Survey", 4, "kyllian@epitech.eu")
	assert addResponse == "Error: Sorry, you can't add a response because the survey 'Football Survey' doesn't exist."

def testAddResponse7():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Cars Survey")
	addQuestion = example.AddQuestion("Cars Survey", "Question1")
	addQuestion = example.AddQuestion("Cars Survey", "Question2")
	addResponse = example.AddResponse("Cars Survey", "Blablabla", "florian@epitech.eu")
	assert addResponse == "Error: The response must be a valid integer."

def testAddResponse8():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Cars Survey")
	addQuestion = example.AddQuestion("Cars Survey", "Question1")
	addQuestion = example.AddQuestion("Cars Survey", "Question2")
	addResponse = example.AddResponse("Cars Survey", "Blablabla", "florian@epitech.eu")
	assert addResponse == "Error: The response must be a valid integer."
	addResponse = example.AddResponse("Cars Survey", "123HEY123", "florian@epitech.eu")
	assert addResponse == "Error: The response must be a valid integer."

def testAddResponse9():
	example = survey.Controller()
	surveyCreated = example.CreateSurvey("Cars Survey")
	addQuestion = example.AddQuestion("Cars Survey", "Question1")
	addQuestion = example.AddQuestion("Cars Survey", "Question2")
	addResponse = example.AddResponse("Cars Survey", "Blablabla", "florian@epitech.eu")
	assert addResponse == "Error: The response must be a valid integer."
	addResponse = example.AddResponse("Cars Survey", 10, "florian@epitech.eu")
	assert addResponse == "Error: The response must be an integer between 1 and 5."
	addResponse = example.AddResponse("Football Survey", 4, "kyllian@epitech.eu")
	assert addResponse == "Error: Sorry, you can't add a response because the survey 'Football Survey' doesn't exist."
	addResponse = example.AddResponse("Cars Survey", 2, "riwan@epitech.eu")
	assert addResponse == "The response '2' have been added by 'riwan@epitech.eu' in the survey 'Cars Survey'"
