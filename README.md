This Assigment 1 for Python for Web Development provided by OntarioLearn presented by Sheridan College Oakville

-- Admin access --
username: jeremy
password: Admin123

Assignment - Create & deploy a Django project

In this course, you will create a fully-functional blog which using Python and the Django framework. Each assignment will add new features to this project to ultimately produce a fully-featured web app. This assignment lays the foundation for the entire course and all subsequent assignments.

Use the mysite project built in this module as reference.
Requirements

Pick a topic for a blog. It could be a personal blog, or related to a special topic or interest.

    Set up your GitHub account if you have not already

    Create a new Django project - different than the one used in the course modules. In your ~/PycharmProjects folder, run:

    $ django-admin startproject <project-name> .

    Use snake_case naming for the Django project.

    Use the standard, out-of-box, sqlite3 database (db.sqlite3) to store data.

    Create an index view (at /) with an accompanying test to demonstrate a 200 HTTP response status code.

    Your app will be run locally on your (and the instructor's) machine. The website must run using python manage.py runserver
    Share github repo (public) for this assignment with the instructor

Evaluation

This assignment is graded using the following criteria, each is worth 3 points.
Points 	Criteria
/ 3 	The project contains a .gitignore file suitable for Python projects
/ 3 	Repository contains a functional Django project with a README file containing a short description of the project
/ 3 	The Django project has an index route at the root path: /
/ 3 	The project has a configured test suite and a test for the index view at the root path: /
/ 3 	The app is configured to connect to the local sqlite3 database in the settings.py file
/ 3 	The project has a valid requirements.txt file containing the libraries used in this project
/ 3 	The Django admin is functional and can be accessed by the instructor