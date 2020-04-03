# BashMyCode - WAD2 Group Project

This project was created using Python 3.8 and Django 3.0.

Hosted version: https://mohibfd.pythonanywhere.com/bashmycode/
GitHub repository: https://github.com/liam-halpin/wad2_group_project

## Using this Repository

This repository uses a virtual environment which have specific packages installed.  The following is a guide on how to create the environment and install the necessary packages successfully:

### Virtual Environment (Anaconda)

Firstly navigate to the C:\ drive on your machine using 'cd'.  Then, navigate to 'Workspace' (create using 'mkdir' if you haven't already).

`(base) ~$ conda create -n bashmycode`

`(base) ~$ conda activate bashmycode`

### Installling Packages
To install the required packages run:

`(bashmycode) ~$ pip install -r requirements.txt`
or
`(bashmycode) ~$ pip3 install -r requirements.txt`

### Running the Application
Now, run this command to start the server (make sure you are in the project's directory):

`(bashmycode) ~$ python manage.py runserver`

Now, navigate to <http://127.0.0.1:8000/> using your browser.

### Populating the Database
To populate the database ensure that there is no existing db.sqlite3 file.

To make the initial migrations:

`~$ python manage.py makemigrations`

Then, apply the migrations:

`~$ python manage.py migrate`

Then, finally, run the population script:

`~$ python populate.py`

NOTE: for the steps above you must be in the project's directory

## Team Members

* Mohib Akoum (2431135a)
* Gordon Ferguson (2393832f)
* Alana Grant (2390384g)
* Liam Halpin (2383998h)
* Erin Morgan (2343910m)
