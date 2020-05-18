# SQA - Final Assignment

## Introduction

First of all, this project is a software component in Python to store information about surveys and responses. This document is an handbook of best practices which highlights the good methods to follow in order to carry out a project successfully in a company. This document will cover these following themes:
- [SQA - Final Assignment](#sqa---final-assignment)
	- [Introduction](#introduction)
	- [Project description](#project-description)
- [Sprint backlog and task estimation](#sprint-backlog-and-task-estimation)
	- [- **Task n°1: Create the Controller**](#ul-litask-n%c2%b01-create-the-controllerli-ul)

- [SQA - Final Assignment](#sqa---final-assignment)
	- [Introduction](#introduction)
	- [Project description](#project-description)
- [Sprint backlog and task estimation](#sprint-backlog-and-task-estimation)
	- [- **Task n°1: Create the Controller**](#ul-litask-n%c2%b01-create-the-controllerli-ul)

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
