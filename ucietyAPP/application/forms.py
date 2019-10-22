#Importation of relevant modules needed

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, Form, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import University, StudentUsers, Society, Notes
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import LoginManager, current_user, UserMixin

######################STUDENT REGISTRATION FORM#############################

class StudentRegistrationForm(FlaskForm):
	first_name = StringField('First Name', #Plain text fields to enter user credentials
		validators=[
			DataRequired()
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired()
        ])

	lists = University.query.filter_by(uni_name=University.uni_name).all()
	#[(1, 'A'), (2, 'B'), (3, 'C')]
	names = []

	for i in range(int(len(lists))):
		temp = [lists[i].id, lists[i].uni_name] #Produces a drop down list which passes a integer through to the database to enable relationship between tables
		names.append(temp)

	uni_id = SelectField("University",
		choices=names,
		coerce=int) 

	lists = University.query.filter_by(uni_name=University.uni_name).all()
	#[(1, 'A'), (2, 'B'), (3, 'C')]
	names = []

	for i in range(int(len(lists))):
		temp = [lists[i].uni_name, lists[i].uni_name] #Produces a drop down list which passes a string through to the database
		names.append(temp)

	uni_name = SelectField("Confirm University",
		choices=names) 

	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	confirm_password = PasswordField('Confirm Password',
		validators=[
			DataRequired(),
			EqualTo('password') #Ensures that the password that has been re-entered is equivalent to the inital entry
		])
	submit = SubmitField('Sign Up')

	def validate_email(self, email): #A function which ensures duplicate emails are not present in the database
		user=StudentUsers.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')

##########################################################################
######################STUDENT LOGIN FORM####################################

class StudentLoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	remember = BooleanField('Remember Me') #checkbox that allows the app to remember the specific user
	submit = SubmitField('Login')

##########################################################################
######################UPDATE ACCOUNT FORM####################################

class UpdateAccountForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired()
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired()
        ])

	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])

	lists = Society.query.filter_by(uni_id=StudentUsers.uni_id).all() #Queries the database to present results in a dropdown format of all univeristy societies for the current user
	names = []

	for i in range(int(len(lists))):
		temp = [lists[i].SocietyName, lists[i].SocietyName] 
		names.append(temp) #This method adds a the previous item (name) to the existing list of society names

	SocietyName = SelectField("Confirm University",
		choices=names)

	submit = SubmitField('Update')

	def validate_email(self, email): #A function which ensures duplicate emails are not present in the database
		if email.data != current_user.email:
			user=StudentUsers.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use! - Please choose another')

######################NOTES FORM###################################################

class NotesForm(FlaskForm):
	title = StringField('Title', 
		validators=[
			DataRequired()
		])
	content = TextAreaField('Content', #Text area field gives the user better UI Visualisation in regards to what they're inputting
		validators=[
			DataRequired()
		])
	submit = SubmitField('Post Note')


