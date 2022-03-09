# JSC-Online

## Author 
Built by: [Timothy Mugendi](https://github.com/Timoh97)

# Description
This is a clone of the website for Instagram photo application.

#### Prerequisites 
* python3.8
* pip
* Flask

## User Story
* Sign in to the application to start using.
* See your profile.
* Search for different users using their usernames.
* Message other professionals.
* Leave a comment on comment box.

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the application | On application load | Display of Login Form |
| Create account by Sign Up | Enter email, username and password| Redirect to login|
| Login selected | Enter username and password you signed up with| Redirect to home page|
| Post remark/complaint button selected | Post | Input details in a form and upload |
| Click the other buttons on navbar | CLick | Redirected to page wih all the comments made on the post |
| Click the user profile icon | Select Profile | Redirected to profile page where you can edit profile |
| Click the user profile icon | Select Logout | Logout and redirected to login page |

# Setup and Installation
#### Cloning the repository
* Open Terminal:
```bash
        $ git clone https://github.com/Timoh97/JSC-Online.git
        $ cd JSC-Online
        $ code . or atom . based on your text editor 
```
* Navigate into the folder, install and activate virtual environment
```bash
      $ python -m venv virtual

      $ source virtual/bin/acivate
```
* Install all dependencies in requirements.txt
```bash
      $ pip install -r requirements.txt
```
#### Setup the Database
* Setup the database username, password, host then make migrations  
```bash
      $ python manage.py makemigrations 
```
* Run migrations
```bash
      $ python manage.py migrate
```
### Running the Application
* To run the application, open the cloned repo in terminal and run the following commands:
```bash
      $ python3 manage.py runserver
```
### Testing the Application       
* To run unittests for the class application and check if it functions well:
```bash
      $ python3 manage.py test ---
```
## Known Bugs
* No known bugs so far, incase a bug is spotted pull requests are allowed.


## Technologies Used
* markdown

* Django_Bootstrap4 - for bootstrap version 4

* Heroku - online deployment


## Support and contact details
Incase of any issues at hand, please email me at timohmugendi@gmail.com
## Preview
 <img src="./screenshots/1.png" alt="screenshot" />

  <img src="./screenshots/2.png" alt="screenshot" />

  <img src="./screenshots/3.png" alt="screenshot" />
  
### License
MIT LICENSE [**TIMOTHY MUGENDI**]