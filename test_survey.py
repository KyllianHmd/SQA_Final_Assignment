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
