# authentication-protocol-project

README FILE FOR RYAN OPOKU QMUL PROJECT SUBMISSION

INTRODUCTION
------------
The following readme file is submitted as part of the MSc Computing and Information Systems project component.

The application developed is a user logging in and registration system built using Python Script, which allows a user to create an account, login to that account and stores these information into an external SQLite 3 based database. Once an account is created, a user enters their username and memorable word that they selected when they registered, and then to fully authenticate themselves, they must enter a 12 digit One time Password that has been emailed to their email that they provided. A user canÕt login until these 12 character one time password has been entered.

It is not possible to include an executable exe file, therefore source code consisting of the python file, that can be executed with the Microsoft Visual Studio interpreter is included.  

REQUIREMENTS & INSTRUCTIONS

RECOMMENDED: MICROSOFT VISUAL STUDIO CODE (https://visualstudio.microsoft.com/downloads/)
Compatible with both MacOS and Windows Based systems.
Ensure that Python modules are installed as part of Microsoft Visual Studio.

SQLite3: https://sqlitebrowser.org/dl/
Compatible with both MacOS and Windows Based systems.


Alternatively:
PyScripter: (https://sourceforge.net/projects/pyscripter/)
Compatible with only Windows OS

Python 3 is required to be installed if using PyScripter, and can be installed via: https://www.python.org/downloads/


Instructions:

Open program.py file with Microsoft Visual Studio.
Run python file in program.
Proceed to either create an account or login to account.
Follow the necessary steps and once email address and password entered, check your email account for a one time password that is required to be entered to fully login.

Troubleshooting:

How can I view the users stored in the database?
Accounts are stored and located within a database file called qmulProject_DB.db

I am not receiving an email with the one time password?
Emails are sent using SMTP SSL details. Please check all your email folders including your spam/junk mail, as emails from this application may end up there. Emails will be sent from the email address qmulproject@bazoogo.com.
