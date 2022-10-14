from flask import request, json
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, TextAreaField, HiddenField, StringField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo

SFTEXT = 'Megpróbálom ezt: '


        

# Creating an instance of Word, parameter passed to "setattr" to create a dymanic SubmitField attribute,
# so that each Wordform can be identified by their own SubmitField attribute.       
def WordForm(submitx):    
    class Word(FlaskForm):
        tw1 = SelectField('Word here', choices=[])
        tw2 = SelectField('Word here', choices=[])
        tw3 = SelectField('Word here', choices=[])
        tw4 = SelectField('Word here', choices=[])
        tw5 = SelectField('Word here', choices=[])
        tw6 = SelectField('Word here', choices=[])
        tw7 = SelectField('Word here', choices=[])
        tw8 = SelectField('Word here', choices=[])
        submit_all =[]
        submit = SubmitField('Ellenőrzés...')

    setattr(Word, submitx, SubmitField())
    
    return Word()


class CreateForm(FlaskForm):
    hun = StringField('Sentence to be translated', validators=[DataRequired(), Length(min=5)])
    english_full = StringField('Full sentence to translate (unseen for students)', validators=[DataRequired(), Length(min=10)])
    type = StringField('Type (helps with proper word picks)', validators=[DataRequired(), Length(min=5)])
    w_number = IntegerField(DataRequired())
    number = IntegerField(DataRequired()) # This field completed automatically by checking how many object are in json file. 
    submit_field = StringField(DataRequired()) # This field completed automatically by checking how many object are in json file. 
    completed = False
    
    word1_choice1 = StringField(validators=[DataRequired(), Length(min=1)])
    word1_choice2 = StringField(validators=[DataRequired(), Length(min=1)])
    word1_choice3 = StringField(validators=[DataRequired(), Length(min=1)])
    word1_choice4 = StringField(validators=[DataRequired(), Length(min=1)])

    word2_choice1 = StringField(validators=[DataRequired(), Length(min=1)])
    word2_choice2 = StringField(validators=[DataRequired(), Length(min=1)])
    word2_choice3 = StringField(validators=[DataRequired(), Length(min=1)])
    word2_choice4 = StringField(validators=[DataRequired(), Length(min=1)])

    word3_choice1 = StringField(validators=[DataRequired(), Length(min=1)])
    word3_choice2 = StringField(validators=[DataRequired(), Length(min=1)])
    word3_choice3 = StringField(validators=[DataRequired(), Length(min=1)])
    word3_choice4 = StringField(validators=[DataRequired(), Length(min=1)])

    word4_choice1 = StringField(validators=[DataRequired(), Length(min=1)])
    word4_choice2 = StringField(validators=[DataRequired(), Length(min=1)])
    word4_choice3 = StringField(validators=[DataRequired(), Length(min=1)])
    word4_choice4 = StringField(validators=[DataRequired(), Length(min=1)])



    submit = SubmitField('Add to json Database')
