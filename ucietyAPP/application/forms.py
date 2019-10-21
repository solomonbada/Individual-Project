from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, Form, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import University, StudentUsers, Society, Notes
from wtforms_sqlalchemy.fields import QuerySelectField
from flask_login import LoginManager, current_user, UserMixin

######################STUDENT REGISTRATION FORM#############################

class StudentRegistrationForm(FlaskForm):
	first_name = StringField('First Name',
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
		temp = [lists[i].id, lists[i].uni_name] #id, uni_name
		names.append(temp)

	uni_id = SelectField("University",
		choices=names,
		coerce=int) 

	lists = University.query.filter_by(uni_name=University.uni_name).all()
	#[(1, 'A'), (2, 'B'), (3, 'C')]
	names = []

	for i in range(int(len(lists))):
		temp = [lists[i].uni_name, lists[i].uni_name] #uni_name
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
			EqualTo('password')
		])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user=StudentUsers.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')


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
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


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

	lists = Society.query.filter_by(uni_id=StudentUsers.uni_id).all()
	#[(1, 'A'), (2, 'B'), (3, 'C')]
	names = []

	for i in range(int(len(lists))):
		temp = [lists[i].SocietyName, lists[i].SocietyName] #SocietyName
		names.append(temp)

	SocietyName = SelectField("Confirm University",
		choices=names) 

	submit = SubmitField('Update')

	def validate_email(self, email):
		if email.data != current_user.email:
			user=StudentUsers.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use! - Please choose another')

######################NOTES FORM#############################

class NotesForm(FlaskForm):
	title = StringField('Title', 
		validators=[
			DataRequired()
		])
	content = TextAreaField('Content',
		validators=[
			DataRequired()
		])
	submit = SubmitField('Post Note')


