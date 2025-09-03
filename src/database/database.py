import sqlite3
from peewee import *

db = SqliteDatabase("src/database/cobas.db")

class State(Model):
    # Dies ist ein fester Primärschlüssel, der sicherstellt, dass es nur eine Zeile gibt.
    # Da dies die einzige Zeile sein wird, benötigen Sie keinen dynamischen Namen.
    state_id = CharField(primary_key=True, default='current_state')
    record = BooleanField(default=False)
    stream = BooleanField(default=False)
    # Sie können hier weitere boolesche Felder hinzufügen, und der Code funktioniert trotzdem.
    other_status = BooleanField(default=False)

    class Meta:
        database = db

db.connect()
db.create_tables([State])

# Holen Sie sich den einzigen Eintrag oder erstellen Sie ihn, falls er nicht existiert.
# Der Primärschlüssel 'current_state' sorgt dafür, dass nur eine Zeile erstellt wird.
state_entry, created = State.get_or_create(state_id='current_state')

# Setzen Sie alle booleschen Felder dynamisch auf False.
for field_name, field_instance in state_entry._meta.fields.items():
    if isinstance(field_instance, BooleanField):
        setattr(state_entry, field_name, False)

# Speichern Sie die Änderungen in der Datenbank.
state_entry.save()

print("Alle booleschen Felder im State-Modell wurden auf False gesetzt.")

db.close()