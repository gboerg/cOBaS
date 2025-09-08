from peewee import *



db = SqliteDatabase('src/database/cobas.db')


class selected(Model):
    id = CharField()
    recording = BooleanField(default=False)
    streming = BooleanField(default=False)
    class Meta: 
        database = db


db.create_tables([selected])

# selected.get_or_create()