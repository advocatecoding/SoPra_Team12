# Server wird mit Flask aufgebaut
from flask import Flask
# Flask-Restx ist eine Erweiterung (Extension) für Flask, die den Aufbau der REST-APIs erleichtert
from flask_restx import Api, Resource, fields
# Um CORS zu erlauben (es ist prinzipiell nicht erwünscht vom Client), nutzen wir auch die Erweiterung Flask-Cors
from flask_cors import CORS

# Zugriff auf Administration & BO-Klassen
from bo.Person import Person
from bo.Projekt import Projekt
from Administration import Administration
from bo.Aktivitaet import Aktivitaet
from bo.Mitarbeiterinprojekt import MitarbeiterInProjekt

""" Wir erstellen ein "Flask-Objekt" """
app = Flask(__name__)

""" Wir wählen einen Prefix (namens "zeit") aus welcher für CORS freigegeben wird. """
CORS(app, ressources=r'/zeit/*')

""" Mithilfe von Flask-Restx wird die Datenstruktur aufgebaut """
api = Api(app, version='1.0', title="Zeiterfassung API")

""" Namespace definieren (es wird "zeit" gewählt, da Zeiterfassung ein zu langes Wort ist, also aus Bequemlichkeitsgründen) """
zeiterfassung = api.namespace("zeit", desription="Funktionen der Zeiterfassung WebApp")

""" api.payload: 
    Bei Eingabe der Werte wird jeweils immer ein Key und ein Value gespeichert, wodurch eine dictionary-Struktur 
    erstellt wird. Dies wird als api.payload gespeichert. """

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
    "dauer": fields.String(attribute="_dauer", description="Dauer"),
    "kapazität": fields.String(attribute="_kapazität", description="Kapazität")
})

mitarbeiter_in_projekt = api.inherit('Mitarbeiterinprojekt', bo, {
    "mitarbeiter": fields.String(attribute="_person", description="Mitarbeiter"),
    "projekt": fields.String(attribute="_projekt", description="Projekt"),
    "verkaufte_stunden": fields.String(attribute="_verkaufte_stunden", description="verkaufte Stunden"),
})



@zeiterfassung.route("/mitarbeiter_in_projekt")
class PersonenListOperations(Resource):
    @zeiterfassung.marshal_with(mitarbeiter_in_projekt)
    def get(self):
        """ Auslesen der Mitarbeiter_in_Projekt -Objekte """
        adm = Administration()
        mitarbeiter_in_projekt = adm.get_all_mitarbeiter_in_projekt()
        return mitarbeiter_in_projekt

    @zeiterfassung.marshal_with(mitarbeiter_in_projekt, code=201)
    @zeiterfassung.expect(mitarbeiter_in_projekt)
    def post(self):
        """ Mitarbeiter_in_Projekt Instanz erstellen """
        adm = Administration()
        """ Wir setzen den api.payload in die from_dict Methode ein und erstellen damit eine Person, indem wir ihre 
        Attribute aus den Werten von api.payload setzen. """
        mitarbeiter_in_projekt_object = MitarbeiterInProjekt.from_dict(api.payload)

        if mitarbeiter_in_projekt_object is not None:
            """ Wir erstellen in Administration eine Mitarbeiter in Projekt Instanz mithilfe der Daten vom api.payload """
            c = adm.create_mitarbeiter_in_projekt(mitarbeiter_in_projekt_object.get_person(), mitarbeiter_in_projekt_object.get_projekt(),
                                  mitarbeiter_in_projekt_object.get_verkaufte_stunden())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


""" Mitarbeiter in Projekt Objekt wird gelöscht """
@zeiterfassung.route("/mitarbeiter_in_projekt/<int:person_idd>")
@zeiterfassung.param("person_idd", "Die erste Id der gewünschten Instanz ")
class PersonOberationsById(Resource):
    @zeiterfassung.marshal_with(mitarbeiter_in_projekt)
    def delete(self, person_idd):
        """Löschen eines Mitarbeiter in Projekt Instanz.
        Das zu löschende Objekt wird anhand der zwei übergebenen id's bestimmt.
        """
        adm = Administration()
        projekt = adm.get_projekt_by_projekt_id(person_idd)
        print(projekt)
        return projekt



@zeiterfassung.route("/personen")
class PersonenListOperations(Resource):
    @zeiterfassung.marshal_with(person)
    def get(self):
        """ Auslesen der Personen-Objekte """
        adm = Administration()
        personen = adm.get_all_personen()
        return personen

    @zeiterfassung.marshal_with(person, code=201)
    @zeiterfassung.expect(person)
    def post(self):
        """ Person Instanz erstellen """
        adm = Administration()
        """ Wir setzen den api.payload in die from_dict Methode ein und erstellen damit eine Person, indem wir ihre 
        Attribute aus den Werten von api.payload setzen. person_object = Person-Objekt """
        person_object = Person.from_dict(api.payload)

        if person_object is not None:
            """ Wir erstellen in Administration eine Person mithilfe der Daten vom api.payload """
            c = adm.create_person(person_object.get_vorname(), person_object.get_nachname(),
                                  person_object.get_mail_adresse(), person_object.get_benutzername())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500

""" Person Objekt wird gelöscht """
@zeiterfassung.route("/personen/<int:person_id>")
@zeiterfassung.param("person_id", "Die Id der gewünschten Person")
class PersonOberationsById(Resource):
    @zeiterfassung.marshal_with(person)
    def delete(self, person_id):
        """Löschen einer Person Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        person = adm.get_person_by_person_id(person_id)
        print(person)
        return person

    @zeiterfassung.marshal_with(person)
    @zeiterfassung.expect(person, validate=True)
    def put(self, person_id):
        """ Person Instanz updaten """
        adm = Administration()
        person_object = Person.from_dict(api.payload)

        if person_object is not None:
            """Hierdurch wird die id des zu überschreibenden Person-Objekts gesetzt.
            """
            person_object.set_id(person_id)
            adm.update_person(person_object)
            return '', 200
        else:
            return '', 500


@zeiterfassung.route("/projekte")
class ProjekteListOperations(Resource):
    @zeiterfassung.marshal_with(projekt)
    def get(self):
        """ Auslesen der Projekt-Objekte """
        adm = Administration()
        projekte = adm.get_all_projekte()
        return projekte


    @zeiterfassung.marshal_with(projekt, code=201)
    @zeiterfassung.expect(projekt)
    def post(self):
        """ Projekt Instanz erstellen """
        adm = Administration()
        """ Wir setzen den api.payload in die from_dict Methode ein und erstellen damit ein Projekt, indem wir ihre 
        Attribute aus den Werten von api.payload setzen. projekt_object = Projekt-Objekt """
        projekt_object = Projekt.from_dict(api.payload)

        if projekt_object is not None:
            """ Wir erstellen in Administration eine Person mithilfe der Daten vom api.payload """
            c = adm.create_projekt(projekt_object.get_projektleiter(), projekt_object.get_name(),
                                  projekt_object.get_auftraggeber())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500




""" Aktivitäten werden zur zugeordneten Projekt_ID ausgegeben """
@zeiterfassung.route("/aktivitaten/<int:projekt_id>")
@zeiterfassung.param("projekt_id", "Die Id des gewünschten Projekts")
class AktivitaetenByProjektId(Resource):
    @zeiterfassung.marshal_with(aktivitaet)
    def get(self, projekt_id):
        """ Auslesen der Aktivitäten innerhalb eines Projektes"""
        adm = Administration()
        aktivitaeten = adm.get_aktivitaeten_by_projekt_id(projekt_id)
        print(aktivitaeten)
        return aktivitaeten















@zeiterfassung.route("/aktivitaten")
class ProjekteListOperations(Resource):
    @zeiterfassung.marshal_with(aktivitaet)
    def get(self):
        """ Auslesen der Aktivität-Objekte """
        adm = Administration()
        aktivitaet = adm.get_all_aktivitaeten()
        return aktivitaet

    @zeiterfassung.marshal_with(aktivitaet, code=201)
    @zeiterfassung.expect(aktivitaet)
    def post(self):
        """ Aktivität Instanz erstellen """
        adm = Administration()
        """ Wir setzen den api.payload in die from_dict Methode ein und erstellen damit ein Projekt, indem wir ihre 
        Attribute aus den Werten von api.payload setzen. projekt_object = Projekt-Objekt """
        aktivitaet_object = Aktivitaet.from_dict(api.payload)

        if aktivitaet_object is not None:
            """ Wir erstellen in Administration eine Person mithilfe der Daten vom api.payload """
            c = adm.create_aktivitaet(aktivitaet_object.get_name(), aktivitaet_object.get_dauer(),
                                      aktivitaet_object.get_kapazität())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500







""" Aktivität Objekt wird gelöscht """
@zeiterfassung.route("/aktivität/<int:aktivitaet_id>")
@zeiterfassung.param("aktivitaet_id", "Die Id der gewünschten Aktivität")
class PersonOberationsById(Resource):
    @zeiterfassung.marshal_with(aktivitaet)
    def delete(self, aktivitaet_id):
        """Löschen einer Aktivität Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        aktivitaet = adm.get_aktivitaet_by_aktivitaet_id(aktivitaet_id)
        print(aktivitaet)
        return aktivitaet


    @zeiterfassung.marshal_with(aktivitaet)
    @zeiterfassung.expect(aktivitaet, validate=True)
    def put(self, aktivitaet_id):
        """ Aktivität Instanz updaten """
        adm = Administration()
        aktivitaet_object = Aktivitaet.from_dict(api.payload)

        if aktivitaet_object is not None:
            """Hierdurch wird die id des zu überschreibenden Aktivität-Objekts gesetzt.
            """
            aktivitaet_object.set_id(aktivitaet_id)
            adm.update_aktivitaet(aktivitaet_object)
            return '', 200
        else:
            return '', 500












""" Projekt Objekt wird gelöscht """
@zeiterfassung.route("/projekt/<int:projekt_id>")
@zeiterfassung.param("projekt_id", "Die Id des gewünschten Projektes")
class PersonOberationsById(Resource):
    @zeiterfassung.marshal_with(projekt)
    def delete(self, projekt_id):
        """Löschen einer Projekt Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        projekt = adm.get_projekt_by_projekt_id(projekt_id)
        print(projekt)
        return projekt


    @zeiterfassung.marshal_with(projekt)
    @zeiterfassung.expect(projekt, validate=True)
    def put(self, projekt_id):
        """ Projekt Instanz updaten """
        adm = Administration()
        projekt_object = Projekt.from_dict(api.payload)

        if projekt_object is not None:
            """Hierdurch wird die id des zu überschreibenden Projekt-Objekts gesetzt.
            """
            projekt_object.set_id(projekt_id)
            adm.update_projekt(projekt_object)
            return '', 200
        else:
            return '', 500





























































""" Server läuft auf localhost:5500 bzw. 127.0.0.1:5500 """
if __name__ == '__main__':
    app.run(port= 5500, debug=True)

