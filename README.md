# SQA - Final Assignment

## Introduction

First of all, this project is a software component in Python to store information about surveys and responses. This document is an handbook of best practices which highlights the good methods to follow in order to carry out a project successfully in a company. This document will cover these following themes:
- [SQA - Final Assignment](#sqa---final-assignment)
	- [Introduction](#introduction)
	- [Project description](#project-description)
- [Sprint backlog and task estimation](#sprint-backlog-and-task-estimation)
	- [- **Task n°1: Create the Controller**](#ul-litask-n%c2%b01-create-the-controllerli-ul)
	- [- **Task n°2: Create a Survey**](#ul-litask-n%c2%b02-create-a-surveyli-ul)
	- [- **Task n°3: Add a Question**](#ul-litask-n%c2%b03-add-a-questionli-ul)
	- [- **Task n°4: Get a list of all surveys**](#ul-litask-n%c2%b04-get-a-list-of-all-surveysli-ul)
	- [- **Task n°5: Get a specific survey**](#ul-litask-n%c2%b05-get-a-specific-surveyli-ul)

- [SQA - Final Assignment](#sqa---final-assignment)
	- [Introduction](#introduction)
	- [Project description](#project-description)
- [Sprint backlog and task estimation](#sprint-backlog-and-task-estimation)
	- [- **Task n°1: Create the Controller**](#ul-litask-n%c2%b01-create-the-controllerli-ul)
	- [- **Task n°2: Create a Survey**](#ul-litask-n%c2%b02-create-a-surveyli-ul)
	- [- **Task n°3: Add a Question**](#ul-litask-n%c2%b03-add-a-questionli-ul)
	- [- **Task n°4: Get a list of all surveys**](#ul-litask-n%c2%b04-get-a-list-of-all-surveysli-ul)
	- [- **Task n°5: Get a specific survey**](#ul-litask-n%c2%b05-get-a-specific-surveyli-ul)

- [**Project Documentation**](#project-documentation)

- [**Unit testing and Test-Driven development**](#unit-testing-and-test-driven-development)

- [**Test coverage metric**](#test-coverage-metric)

- [**Team version-control**](#team-version-control)

- [**Code-review checklist**](#code-review-checklist)

## Project description

The goal of this project is to create a software component for storing survey and response information. Each survey is composed of several questions (up to a maximum of 10). Each SurveyResponse must contain an answer to each question in its survey, where the answer will be an integer value between 1 and 5 (i.e. representing a Likert scale).

# Sprint backlog and task estimation

As a reminder, the sprint backlog is the set of user stories from the product backlog that the team commits to deliver by the end of the sprint (user stories are put in the sprint backlog according to their business value and technical complexity). Thus, the most important work will be done first.

- **Task n°1: Create the Controller**
---
  **Description:** The controller allows access to the different functions of our class "Survey" and our class "SurveyResponse". So, from the controller, we can for example create a survey, add a question or even get the statistics of a survey. In short, the controller is the structure of our program.
  <br/>

  **Task Estimation:** 1 hour.
  <br/>

  **Explanation:** Taking into account the implementation of all the functions of our classes, the controller is a longer task because it is simply the structure of our program. It is via this class Controller that we will manage the whole creation of a survey, add questions, answers and call the statistics functions.

- **Task n°2: Create a Survey**
---
  **Description:** It is essential to be able to create a survey. Therefore you need to create a function in our class "Survey", called in our Controller class, to be able to create a survey. The function will take the name of the survey you want to create as a parameter. When the function is called and does not return an error, it returns that the survey has been created successfully.
  <br/>

  **Task Estimation:** 40 minutes.
  <br/>

  **Explanation:** Create a survey takes 40 minutes to do because you have to consider the fact that it creates the class "Survey", while managing the error handling (for example, if the name of the survey is well given). The possibility of calling the function via the Controller must also be implemented. This is a much shorter task than the creation of the controller but it is still a main and important function for the realization of a survey.


- **Task n°3: Add a Question**
---
  **Description:** In a survey, it is essential to add a question. Now that the class "Survey" has been created, we just have the function to create and implement in our class Controller and in our class Survey. The function takes in parameter the name of the survey in which we want to add the question and finally the question. When the function doesn't return any errors, we are left with the fact that the question has been added.
  <br/>

  **Task Estimation:** 20 minutes.
  <br/>

  **Explanation:** Adding a question in a survey takes 20 minutes to do because you have to manage all the error handling (for example, if the survey is already created before adding a question). To compare with the Task n°2, it's shorter because we can see that there is just the function to create and implement in our class Controller and Survey.


- **Task n°4: Get a list of all surveys**
---
  **Description:** This function allows you to have a list of all the surveys you have created. This function doesn't take anything in parameters because we only want to get the list of all the surveys we have created before.
  <br/>

  **Task Estimation:** 5 minutes.
  <br/>

  **Explanation:** Getting a list of all the surveys you have created is very simple. In fact, you just have to return the array containing all the surveys. When there is no survey created, the function only returns an empty table. The estimation of this task is therefore very short compared to other functions.

- **Task n°5: Get a specific survey**
---
  **Description:** This function allows us to access a particular survey via its name. Indeed, the function takes the name of the survey we are looking for and if it exists, the survey is returned and we can access the questions we have added to it.
  <br/>

  **Task Estimation:** 10 minutes.
  <br/>

  **Explanation:** Just like Task n°4, it is quite similar but a little bit longer to do because there is an error handling to implement because the survey in question must be created beforehand otherwise an error will appear. It is a simple task on the whole and requires little implementation time.