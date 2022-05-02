import sqlalchemy

from app.db.base import metadata

quiz_question = sqlalchemy.Table(
    'quiz_question',
    metadata,
    sqlalchemy.Column('id_question', sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column('text_question', sqlalchemy.Text()),
    sqlalchemy.Column('text_answer', sqlalchemy.Text()),
    sqlalchemy.Column('date_create_quesstion', sqlalchemy.DateTime())
)