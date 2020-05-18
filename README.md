# SQA - Final Assignment

## Introduction

First of all, this project is a software component in Python to store information about surveys and responses. This document is an handbook of best practices which highlights the good methods to follow in order to carry out a project successfully in a company. This document will cover these following themes:
- [SQA - Final Assignment](#sqa---final-assignment)
	- [Introduction](#introduction)
	- [Project description](#project-description)

- [**Sprint backlog and task estimation**](#sprint-backlog-and-task-estimation)
  - [**Velocity metric**](#velocity-metric)

- [**Project Documentation**](#project-documentation)

- [**Unit testing and Test-Driven development**](#unit-testing-and-test-driven-development)

- [**Test coverage metric**](#test-coverage-metric)

- [**Team version-control**](#team-version-control)

- [**Code-review checklist**](#code-review-checklist)

## Project description

The goal of this project is to create a software component for storing survey and response information. Each survey is composed of several questions (up to a maximum of 10). Each SurveyResponse must contain an answer to each question in its survey, where the answer will be an integer value between 1 and 5 (i.e. representing a Likert scale).