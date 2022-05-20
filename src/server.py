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
from bo.Urlaub import Urlaub

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
    "verkaufte_stunden": fields.String(attribute="_verkaufte_stunden", description="verkaufte Stunden")
})

urlaub = api.inherit('Urlaub', bo, {
    "projekt_id": fields.String(attribute="_projekt_id", description="Projekt"),
    "person_id": fields.String(attribute="_person_id", description="Mitarbeiter"),
    "start_datum": fields.String(attribute="_start_date", description="Urlaubsbeginn"),
    "end_datum": fields.String(attribute="_end_date", description="Urlaubsende")
})


""" Person Objekt(e) wird gelesen und erstellt  """
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


""" Person Objekt wird gelöscht und erstellt - ein bestimmtes Person Objekt wird gelesen   """
@zeiterfassung.route("/personen/<int:person_id>")
@zeiterfassung.param("person_id", "Die Id der gewünschten Person")
class PersonByIdOperations(Resource):
    @zeiterfassung.marshal_with(person)
    def delete(self, person_id):
        """Löschen einer Person Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        person = adm.get_person_by_person_id(person_id)
        print(person)
        return person

    """Manuel Bräuninger """
    def get(self, person_id):
        pass

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



""" Projekt Objekt(e) wird gelesen und erstellt  """
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


""" Projekt Objekt wird gelöscht und erstellt - ein bestimmtes Projekt Objekt wird gelesen """
@zeiterfassung.route("/projekt/<int:projekt_id>")
@zeiterfassung.param("projekt_id", "Die Id des gewünschten Projektes")
class ProjektByIdOperations(Resource):
    @zeiterfassung.marshal_with(projekt)
    def delete(self, projekt_id):
        """Löschen einer Projekt Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        projekt = adm.get_projekt_by_projekt_id(projekt_id)
        print(projekt)
        return projekt

    """Manuel Bräuninger """
    def get(self,projekt_id):
        pass

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



""" Mitarbeiter_in_Projekt Objekt(e) wird gelesen und erstellt  """
@zeiterfassung.route("/mitarbeiter_in_projekt")
class MitarbeiterInProjektListOperations(Resource):
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


""" Mitarbeiter_in_Projekt wird gelöscht und erstellt """
@zeiterfassung.route("/mitarbeiter_in_projekt/<int:person_idd>/<int:projekt_id>")
@zeiterfassung.doc(params={"projekt_id": {"description:" : "Die Id des gewünschten Projekts"},
                           "person_idd" :{"description:" : "Die Id der gewünschten Person"}})
class MitarbeiterInProjektByIdOperations(Resource):
    @zeiterfassung.marshal_with(mitarbeiter_in_projekt)
    def delete(self, person_idd, projekt_id):
        """Löschen einer Mitarbeiter_in_Projekt Instanz.
        Das zu löschende Objekt wird anhand  zwei id's bestimmt.
        """
        adm = Administration()
        mip = adm.get_person_by_person_id_and_projekt_by_projekt_id(person_idd, projekt_id)
        print(mip)
        return mip

    """Dennis Kühnberger """
    def put(self, projekt_id):
        pass



""" Aktivität Objekt(e) wird gelesen und erstellt  """
@zeiterfassung.route("/aktivitaten")
class AktivitaetenListOperations(Resource):
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


""" Aktivität Objekt wird gelöscht und erstellt - ein bestimmtes Mitarbeiter Objekt wird gelesen """
@zeiterfassung.route("/aktivität/<int:aktivitaet_id>")
@zeiterfassung.param("aktivitaet_id", "Die Id der gewünschten Aktivität")
class AktivitaetenByIdOperations(Resource):
    @zeiterfassung.marshal_with(aktivitaet)
    def delete(self, aktivitaet_id):
        """Löschen einer Aktivität Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        aktivitaet = adm.get_aktivitaet_by_aktivitaet_id(aktivitaet_id)
        print(aktivitaet)
        return aktivitaet

    """Dennis Kühnberger """
    def get(self, projekt_id):
        pass


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









"""rudimentär, neue Mapper erstellen und die von der alten dorthin übertragen"""
"""Aktivitäten_in_Projekt"""
"""Dennis Kühnberger Post, Delete, Weiteres Get, PUT  """

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


""" Server läuft auf localhost:5500 bzw. 127.0.0.1:5500 """
if __name__ == '__main__':
    app.run(port= 5500, debug=True)

