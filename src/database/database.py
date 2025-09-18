from peewee import *
import customtkinter as ctk


db = SqliteDatabase('src/database/cobas.db')


class Features(Model):
    feature = CharField()
    feature_color = CharField()
    feature_text_color = CharField()
    
    once = BooleanField(default=False)
    allow_follow = BooleanField(default=False)

    class Meta: 
        database = db
        unique_together = (('feature'),)




class Builder(Model):
    # id = AutoField()
    feature = CharField(primary_key=True)
    name  = CharField()
    previous_feature= CharField(null= True)
    location = IntegerField()
    
    value = CharField(null=True)
    value2 = CharField(null = True)
    value3 = CharField(null = True)
    value4 = CharField(null = True)
    value5 = CharField(null = True)

    class Meta: 
        database = db

class Colors(Model):
    id= AutoField()
    widget = CharField()
    widget_id = CharField()
    hex_bg = CharField(default="")
    hex_hover = CharField(default="")
    hex_text = CharField(default="")
    class Meta: 
        database = db
        

class websockets(Model):
    id = AutoField()
    name = CharField(default="")
    host = CharField()
    port = IntegerField()
    password = CharField()
    all_field = CharField()
    
    color = CharField()
    text_color = CharField()

    class Meta:
        database = db
        # Setze die einzigartige Beschränkung auf die Kombination aus host und port
        unique_together = (('host', 'port'),)

db.create_tables([Features, websockets, Colors, Builder])

# selected.get_or_create()