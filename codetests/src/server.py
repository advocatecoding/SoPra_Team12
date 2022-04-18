# Server wird mit Flask aufgebaut
from flask import Flask
# Flask-Restx ist eine Erweiterung (Extension) für Flask, die den Aufbau der REST-APIs erleichtert
from flask_restx import Api, Resource, fields
# Um CORS zu erlauben (es ist prinzipiell nicht erwünscht vom Client), nutzen wir auch die Erweiterung Flask-Cors
from flask_cors import CORS

# Zugriff auf Administration & BO-Klassen
from bo.Person import Person
from Administration import Administration


""" Wir erstellen ein "Flask-Objekt" """
app = Flask(__name__)

""" Wir wählen einen Prefix (namens "zeit") aus welcher für CORS freigegeben wird. """
CORS(app, ressources=r'/zeit/*')

""" Mithilfe von Flask-Restx wird die Datenstruktur aufgebaut """
api = Api(app, version='1.0', title="Zeiterfassung API")

""" Namespace definieren (es wird "zeit" gewählt, da Zeiterfassung ein zu langes Wort ist, also aus Bequemlichkeitsgründen) """
zeiterfassung = api.namespace("zeit", desription="Funktionen des ")

#bo = api.model('BusinessObject', {})

bo = api.model("BusinessObject", {
    "id": fields.String(attribute="_person_id", description="Id"),
    "datum_aenderung": fields.String(attribute="_person_id", description="Datum der letzten Änderung")
})

person = api.inherit('Person', bo, {
    "person_id": fields.String(attribute="_person_id", description="Person Id"),
    "vorname": fields.String(attribute="_vorname", description="Vorname der Person"),
    "nachname": fields.String(attribute="_nachname", description="Nachname der Person"),
    "mail_adresse": fields.String(attribute="_mail_adresse", description="Mail-Adresse der Person"),
    "benutzername": fields.String(attribute="_benutzername", description="Benutzer der Person"),
    "urlaubstage": fields.Integer(attribute="_urlaubstage", description="Anzahl der Urlaubstage" ),
    "überstunden": fields.Integer(attribute="_ueberstunden", description="Anzahl der Überstunden")
})

@zeiterfassung.route("/personen")
class PersonenListOperations(Resource):
    @zeiterfassung.marshal_with(person)
    def get(self):
        """ Auslesen der Personen-Objekte """
        adm = Administration()
        personen = adm.get_all_personen()
        return personen


""" Server läuft auf localhost:5500 bzw. 127.0.0.1:5500 """
if __name__ == '__main__':
    app.run(port= 5500, debug=True)

