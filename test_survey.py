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
