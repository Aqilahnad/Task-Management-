# Task Management System

# Overview
The Task Management System is a robust tool designed to help individuals efficiently manage and track their tasks. This system supports creating, updating, deleting tasks, assigning tasks to users, setting deadlines, and monitoring task progress. 

# Features
Task Creation: Users can create new tasks with details such as title, category and description.
Task Editing: Existing tasks can be updated with new information.
Task Deletion: Tasks can be deleted when they are no longer needed.
User Assignment: Tasks can be assigned to specific users.
Status Tracking: Tasks can have different statuses (e.g., To Do, In Progress, Completed).
Categorization: Tasks can be categorized into different projects or labels.

# Setup
Prerequisites
Python 3.8+
Django 3.2+
Virtualenv (optional but recommended)

# Installation
1.Clone the Repository:
git clone https://github.com/Aqilahnad/task_management_system.git
cd task_management_system

2.Create and Activate Virtual Environment (optional but recommended):
py -m virtualenv myenv
myenv\scripts\activate 
pip install django

3.Run Migrations:
py manage.py migrate

4.Create Superuser
py manage.py createsuperuser

5.Run the Server:
py manage.py runserver

6.Access the Application:
Open your web browser and go to http://127.0.0.1:8000.

# Task Management
Create a Task: Navigate to the task creation page, fill out the form with task details, and submit.
Edit a Task: Click on a task to view details and use the edit option to update the task.
Delete a Task: Click on a task and use the delete option to remove the task.
Assign a Task: While creating or editing a task, assign it to a user from the user dropdown.

# User 
username = qiqi
password = Aqilah00!

username = erik
password = kire1234!@#$

