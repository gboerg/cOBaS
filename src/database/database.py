from peewee import *



db = SqliteDatabase('src/database/cobas.db')


class Features(Model):
    feature = CharField()
    count = IntegerField(default=0)
    status = BooleanField(default=False)
    class Meta: 
        database = db


class websockets(Model):
    id = AutoField()
    host = CharField()
    port = IntegerField()
    password = CharField()

    class Meta:
        database = db
        # Setze die einzigartige Beschränkung auf die Kombination aus host und port
        unique_together = (('host', 'port'),)

db.create_tables([Features, websockets])

# selected.get_or_create()