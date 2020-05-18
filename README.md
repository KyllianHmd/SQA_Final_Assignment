# SQA - Final Assignment

## Introduction

First of all, this project is a software component in Python to store information about surveys and responses. This document is an handbook of best practices which highlights the good methods to follow in order to carry out a project successfully in a company. This document will cover these following themes:

- [SQA - Final Assignment](#sqa---final-assignment)
	- [Introduction](#introduction)
	- [Project description](#project-description)
- [Sprint backlog and task estimation](#sprint-backlog-and-task-estimation)
- [Velocity Metric](#velocity-metric)

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

  **Description:** The controller allows access to the different functions of our class "Survey" and our class "SurveyResponse". So, from the controller, we can for example create a survey, add a question or even get the statistics of a survey. In short, the controller is the structure of our program.
  <br/>

  **Task Estimation:** 1 hour.
  <br/>

  **Explanation:** Taking into account the implementation of all the functions of our classes, the controller is a longer task because it is simply the structure of our program. It is via this class Controller that we will manage the whole creation of a survey, add questions, answers and call the statistics functions.

- **Task n°2: Create a Survey**
  
  **Description:** It is essential to be able to create a survey. Therefore you need to create a function in our class "Survey", called in our Controller class, to be able to create a survey. The function will take the name of the survey you want to create as a parameter. When the function is called and does not return an error, it returns that the survey has been created successfully.
  <br/>

  **Task Estimation:** 40 minutes.
  <br/>

  **Explanation:** Create a survey takes 40 minutes to do because you have to consider the fact that it creates the class "Survey", while managing the error handling (for example, if the name of the survey is well given). The possibility of calling the function via the Controller must also be implemented. This is a much shorter task than the creation of the controller but it is still a main and important function for the realization of a survey.


- **Task n°3: Add a Question**

  **Description:** In a survey, it is essential to add a question. Now that the class "Survey" has been created, we just have the function to create and implement in our class Controller and in our class Survey. The function takes in parameter the name of the survey in which we want to add the question and finally the question. When the function doesn't return any errors, we are left with the fact that the question has been added.
  <br/>

  **Task Estimation:** 20 minutes.
  <br/>

  **Explanation:** Adding a question in a survey takes 20 minutes to do because you have to manage all the error handling (for example, if the survey is already created before adding a question). To compare with the Task n°2, it's shorter because we can see that there is just the function to create and implement in our class Controller and Survey.


- **Task n°4: Get a list of all surveys**

  **Description:** This function allows you to have a list of all the surveys you have created. This function doesn't take anything in parameters because we only want to get the list of all the surveys we have created before.
  <br/>

  **Task Estimation:** 5 minutes.
  <br/>

  **Explanation:** Getting a list of all the surveys you have created is very simple. In fact, you just have to return the array containing all the surveys. When there is no survey created, the function only returns an empty table. The estimation of this task is therefore very short compared to other functions.

- **Task n°5: Get a specific survey**

  **Description:** This function allows us to access a particular survey via its name. Indeed, the function takes the name of the survey we are looking for and if it exists, the survey is returned and we can access the questions we have added to it.
  <br/>

  **Task Estimation:** 10 minutes.
  <br/>

  **Explanation:** Just like Task n°4, it is quite similar but a little bit longer to do because there is an error handling to implement because the survey in question must be created beforehand otherwise an error will appear. It is a simple task on the whole and requires little implementation time.


- **Task n°6: Add a response**

  **Description:** Adding a response to a survey question is one of the main features of our project. Indeed, this function will lead to the creation of another class that will be called "SurveyResponse". In this class, we will link each response to a survey. And each response will be linked to a user. This function will therefore take the name of the survey, the response and finally the user email in order to identify the person who responded to the survey.
  <br/>
  
  **Task Estimation:** 1 hour.
  <br/>

  **Explanation:** Similar to Task n°3, this task is more complicated because it involves the creation of another "SurveyResponse" class and the fact that you have to link a user's responses to a survey. In comparison, having a large error handling and implementation via our Controller, our Survey class and finally in the last "SurveyResponse" class, this task will take about 1 hour to complete.

- **Task n°7: Get Survey Responses**

  **Description:** This function will allow you to have all the answers given by all the users of a particular survey. This function will just take the name of the survey in parameter and return an array with all the answers of each user.
  <br/>

  **Task Estimation:** 10 minutes.
  <br/>

  **Explanation:** Like Task n°5, it is simply a matter of returning all the answers to a particular survey. The error handling will take a few minutes to do but the task is quite simple to perform.


- **Task n°8: Get Survey Statistics**

  **Description:** This function allows you to have statistics of a survey in its entirety with all the answers of all the users. This function will take the name of the survey and return the minimum, maximum, average and standard deviation. An error will be returned if something goes wrong.
  <br/>
  
  **Task Estimation:** 20 minutes.
  <br/>

  **Explanation:** In terms of difficulty, this is not the hardest task because in Python, we can easily make quick calculations such as average, min or max value, or even standard deviation. The longest thing to do will be the structure of the function to know how to get all the answers from all the users and how to calculate all the values between them.

- **Task n°9: Get Question Statistics**

  **Description:** This function should provide the average, standard deviation, minimum and maximum score for a specific question on a Survey. The function will then take the question and the name of the survey as parameters. The function will then return the values of the different calculations.
  <br/>

  **Task Estimation:** 20 minutes.
  <br/>

  **Explanation:** Almost the same task as the Task n°8, there is a strong errors handling required for this function. The calculations are not the hardest to do but the structure of the code is, it will take 20 minutes to correctly implement this function in our different classes.

- **Task n°10: Other functions needed**

  **Description:** We will need 3 other functions (out of features) that will allow us to manage error handling and statistics. One function will have the role of simply giving the average of an array. Another function will tell us if an index exists in an array to avoid crashing our program. Finally, the last function will allow us to know if the user has put an answer between 1 and 5. (as the liker scale model).
  <br/>

  **Task Estimation:** 15 minutes.
  <br/>

  **Explanation:** About 5 minutes per function, they are not hard to develop but they are necessary for the good development of our program and will help us for the error management.

# Velocity Metric

Velocity is the number of tasks a team completes during a sprint. To measure it, simply add up the number of tasks delivered in the last few sprints and average them. To have a reliable average, the velocity must be calculated over a minimum of 3 sprints. In addition, the experience helps in measuring the velocity metric of a sprint.

Velocity metric is an essential feedback mechanism for the team. It helps them measure whether the process changes they make improve or hinder their productivity. It also allows them to predict very precisely how many stories a team can make in a sprint.

Without the Velocity, release planning is impossible. By knowing speed, a product owner can determine how many sprints it will take the team to reach the desired level of functionality, which can then be delivered. Based on the duration of the sprint, the product owner can set a release date.