from peewee import *



db = SqliteDatabase('src/database/cobas.db')


class selected(Model):
    id = CharField()
    recording = BooleanField(default=False)
    streming = BooleanField(default=False)
    class Meta: 
        database = db


class websockets(Model):
    id = AutoField()
    host = IntegerField(default=0)
    port= IntegerField(default=0)
    password = IntegerField(default=0)
    class Meta: 
        database = db


db.create_tables([selected, websockets])

# selected.get_or_create()