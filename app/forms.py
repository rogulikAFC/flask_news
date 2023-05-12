from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Optional

from .models import Category

# class FeedbackForm(FlaskForm):
#     name = StringField('Имя',
#                        validators=[DataRequired(message="Поле не должно быть пустым")])
#     text = TextAreaField('Текст отзыва',
#                          validators=[DataRequired(message="Поле не должно быть пустым")])
#     email = EmailField('Ваш email', validators=[Optional()])
#     rating = SelectField('Ваша оценка?', choices=[1, 2, 3, 4, 5])
#     submit = SubmitField('Добавить')

def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]

class NewsForm(FlaskForm):
    title = StringField(
        'Название',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=255, message='Введите заголовок длиной до 255 символов')]
    )
    text = TextAreaField(
        'Текст',
        validators=[DataRequired(message="Поле не должно быть пустым")])
    category = SelectField(choices=get_categories())
    submit = SubmitField('Добавить')
