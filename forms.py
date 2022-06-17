from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, PasswordField, RadioField, IntegerField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo, NumberRange

# class RequiredIf(DataRequired):
#     """Validator which makes a field required if another field is set and has a truthy value.

#     Sources:
#         - http://wtforms.simplecodes.com/docs/1.0.1/validators.html
#         - http://stackoverflow.com/questions/8463209/how-to-make-a-field-conditionally-optional-in-wtforms

#     """
#     field_flags = ('requiredif',)

#     def __init__(self, other_field_name, message=None, *args, **kwargs):
#         self.other_field_name = other_field_name
#         self.message = message

#     def __call__(self, form, field):
#         other_field = form[self.other_field_name]
#         if other_field is None:
#             raise Exception('no field named "%s" in form' % self.other_field_name)
#         if other_field.data == 'Computer':
#             super(RequiredIf, self).__call__(form, field)

class GameForm(FlaskForm):
    # opponent = RadioField('Opponent', choices = ['Human', 'Computer'], validators=[DataRequired()])
    difficulty = RadioField('Difficulty Level', choices = ['Easy', 'Medium', 'Hard'], validators=[DataRequired()])
    submit = SubmitField('Play Game')
    
class MoveForm(FlaskForm):
    location = IntegerField('location', validators=[DataRequired(), NumberRange(min=0, max=6, message='Number must be between 0 and 6')])
    submit = SubmitField('Submit Move')
    
class ToDoForm(FlaskForm):
    todo = StringField('Todo', validators=[DataRequired()])
    submit = SubmitField('Submit Move')
    
class NumberForm(FlaskForm):
    zero = SubmitField('0')
    one = SubmitField('1')
    two = SubmitField('2')
    three = SubmitField('3')
    four = SubmitField('4')
    five = SubmitField('5')
    six = SubmitField('6')
    

# class PasswordForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired(), Length(max=50, min=5)])
#     email = StringField('Email', validators=[DataRequired(), Email('Please enter your email address'), Length(max=100)])
#     password = PasswordField('Password', validators=[DataRequired(), Length(max=50, min=5)])
#     repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password'), Length(max=50, min=5)])
#     submit = SubmitField('Submit')

# dct = {}
# for x in range(1, 8):
#     for y in range(1, 7):
#         dct[str(x) + str(y)] = None
# print(dct)

# dct2 = {str(x) + str(y): None for x in range(1,8) for y in range(1,7) }
# print(dct2)