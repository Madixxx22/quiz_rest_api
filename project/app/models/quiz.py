import sqlalchemy

from app.db.base import metadata

quiz_question = sqlalchemy.Table(
    'quiz_question',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column('id_question', sqlalchemy.Integer(), unique=True),
    sqlalchemy.Column('text_question', sqlalchemy.Text()),
    sqlalchemy.Column('text_answer', sqlalchemy.Text()),
    sqlalchemy.Column('date_create_question', sqlalchemy.DateTime(timezone='UTC'))
)