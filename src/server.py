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
zeiterfassung = api.namespace("zeit", desription="Funktionen der Zeiterfassung WebApp")

#bo = api.model('BusinessObject', {})

bo = api.model("BusinessObject", {
    "id": fields.String(attribute="_id", description="Id"),
    "letzte_änderung": fields.String(attribute="_letzte_aenderung", description="Datum der letzten Änderung")
})

person = api.inherit('Person', bo, {
    "vorname": fields.String(attribute="_vorname", description="Vorname der Person"),
    "nachname": fields.String(attribute="_nachname", description="Nachname der Person"),
    "mail_adresse": fields.String(attribute="_mail_adresse", description="Mail-Adresse der Person"),
    "benutzername": fields.String(attribute="_benutzername", description="Benutzer der Person"),
    "urlaubstage": fields.Integer(attribute="_urlaubstage", description="Anzahl der Urlaubstage" ),
    "überstunden": fields.Integer(attribute="_ueberstunden", description="Anzahl der Überstunden")
})

projekt = api.inherit('Projekt', bo, {
    "projektname": fields.String(attribute="_projektname", description="Projektname"),
    "auftraggeber": fields.String(attribute="_auftraggeber", description="Auftraggeber des Projekts"),
    "projektleiter": fields.String(attribute="_projektleiter", description="Projektleiter")
})


aktivitaet = api.inherit('Aktivitaet', bo, {
    "aktivitaetname": fields.String(attribute="_name", description="Aktivitätenname"),
})




@zeiterfassung.route("/personen")
class PersonenListOperations(Resource):
    @zeiterfassung.marshal_with(person)
    def get(self):
        """ Auslesen der Personen-Objekte """
        adm = Administration()
        personen = adm.get_all_personen()
        return personen

@zeiterfassung.route("/projekte")
class PersonenListOperations(Resource):
    @zeiterfassung.marshal_with(projekt)
    def get(self):
        """ Auslesen der Projekt-Objekte """
        adm = Administration()
        projekte = adm.get_all_projekte()
        return projekte

""" Aktivitäten werden zur zugeordneten Projekt_ID ausgegeben """
@zeiterfassung.route("/aktivitaten/<int:projekt_id>")
@zeiterfassung.param("projekt_id", "Die Id des gewünschten Projekts")
class PersonenListOperations(Resource):
    @zeiterfassung.marshal_with(aktivitaet)
    def get(self, projekt_id):
        """ Auslesen der Aktivitäten innerhalb eines Projektes"""
        adm = Administration()
        aktivitaeten = adm.get_aktivitaeten_by_projekt_id(projekt_id)
        print(aktivitaeten)
        return aktivitaeten


""" Server läuft auf localhost:5500 bzw. 127.0.0.1:5500 """
if __name__ == '__main__':
    app.run(port= 5500, debug=True)

