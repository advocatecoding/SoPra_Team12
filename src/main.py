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
from bo.VerkaufteStundenInAktivitaet import VerkaufteStundenInAktivitaet
from bo.SollZeit import Sollzeit

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
    "projekt_id": fields.String(attribute="_projektleiter", description="Projektleiter")
})


aktivitaet = api.inherit('Aktivitaet', bo, {
    "aktivitaetname": fields.String(attribute="_name", description="Aktivitätenname"),
    "projektname": fields.String(attribute="_projektname", description="Projektname"),
    "dauer": fields.String(attribute="_dauer", description="Dauer"),
    "kapazität": fields.String(attribute="_kapazität", description="Kapazität")
})

mitarbeiter_in_projekt = api.inherit('Mitarbeiterinprojekt', bo, {
    "mitarbeiter": fields.String(attribute="_person", description="Mitarbeiter"),
    "projekt": fields.String(attribute="_projekt", description="Projekt"),
    "verkaufte_stunden": fields.String(attribute="_verkaufte_stunden", description="verkaufte Stunden")
})

urlaub = api.inherit('Urlaub', bo, {
    "person_id": fields.String(attribute="_person_id", description="Mitarbeiter"),
    "start_datum": fields.String(attribute="_start_date", description="Urlaubsbeginn"),
    "end_datum": fields.String(attribute="_end_date", description="Urlaubsende")
})

verkaufte_stunden_in_aktivitaet = api.inherit('VerkaufteStundenInAktivitaet', bo, {
    "mitarbeiter": fields.String(attribute="_person", description="Mitarbeiter"),
    "aktivitaet": fields.String(attribute="_aktivitaet", description="Aktivität"),
    "gebuchte_stunden": fields.String(attribute="_gebuchte_stunden", description="gebuchte Stunden")
})

sollzeit = api.inherit('SollZeit', bo, {
    "mitarbeiter": fields.String(attribute="_person", description="Mitarbeiter"),
    "aktivitaet": fields.String(attribute="_aktivitaet", description="Aktivität"),
    "projekt": fields.String(attribute="_projekt", description="Projekt"),
    "gebuchte_stunden": fields.String(attribute="_gebuchte_stunden", description="gebuchte Stunden"),
    "bezeichnung": fields.String(attribute="_bezeichnung", description="Bezeichnung")

})

mitarbeiteransicht = api.inherit('MitarbeiterAnsicht', bo, {
    "vorname": fields.String(attribute="_person", description="Mitarbeiter"),
    "bezeichnung": fields.String(attribute="_aktivitaet", description="Aktivität"),
    "projekt": fields.String(attribute="_projekt", description="Projekt"),
    "gearbeitete_zeit": fields.String(attribute="_gearbeitete_zeit", description="gebuchte Stunden")
})

personeliche_mitarbeiteransicht = api.inherit('MitarbeiterAnsicht', bo, {
    "vorname": fields.String(attribute="_person", description="Mitarbeiter"),
    "bezeichnung": fields.String(attribute="_aktivitaet", description="Aktivität"),
    "projekt": fields.String(attribute="_projekt", description="Projekt"),
    "gearbeitete_zeit": fields.String(attribute="_gearbeitete_zeit", description="gebuchte Stunden")
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
    def get(self, person_id):
        """ Auslesen der Person Instanz.
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        person = adm.get_person_by_id(person_id)
        return person

    def delete(self, person_id):
        """Löschen einer Person Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        person = adm.delete_person_by_person_id(person_id)
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

""" Ein bestimmtes Person Objekt wird anhand des Benutzernamens ausgelesen   """
@zeiterfassung.route("/personen/<string:benutzername>")
@zeiterfassung.param("benutzername", "Der Benutzername der gewünschten Person")
class BenutzerListOperations(Resource):
    @zeiterfassung.marshal_with(person)
    def get(self, benutzername):
        """ Auslesen der Person Instanz.
        Das zu auslesende Objekt wird anhand des Benutzernamens bestimmt
        """
        adm = Administration()
        person = adm.get_person_by_benutzername(benutzername)
        return person


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
    def get(self,projekt_id):
        """ Auslesen der Projekt Instanz.
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        projekt = adm.get_projekt_by_id(projekt_id)
        return projekt

    def delete(self, projekt_id):
        """Löschen einer Projekt Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        projekt = adm.delete_projekt_by_id(projekt_id)
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
        """Dennis Kühnberger """
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
            c = adm.create_aktivitaet(aktivitaet_object.get_projektname(), aktivitaet_object.get_name(), aktivitaet_object.get_dauer(),
                                      aktivitaet_object.get_kapazitaet())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


""" Aktivität Objekt wird gelöscht und erstellt - ein bestimmtes Aktivität Objekt wird gelesen """
@zeiterfassung.route("/aktivitaten/<int:aktivitaet_id>")
@zeiterfassung.param("aktivitaet_id", "Die Id der gewünschten Aktivität")
class AktivitaetenByIdOperations(Resource):
    @zeiterfassung.marshal_with(aktivitaet)
    def delete(self, aktivitaet_id):
        """Löschen einer Aktivität Instanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        aktivitaet = adm.delete_aktivitaet_by_aktivitaet_id(aktivitaet_id)
        return aktivitaet


    """ Aktivitäten Objekt(e) werden gelesen und erstellt, eine bestimmte Aktivität wird herausgelesen  """

    @zeiterfassung.route("/aktivitaet/<int:aktivitaet_id>")
    @zeiterfassung.param("aktivitaet_id", "Die Id der gewünschten Aktivitaet")
    class AktivitaetenByIdOperations(Resource):
        @zeiterfassung.marshal_with(aktivitaet)
        def get(self, aktivitaet_id):
            """ Auslesen der Aktivität-Objekte, das ausgelesene Objekt wird anhand der Id bestimmt """
            adm = Administration()
            aktivitaet = adm.get_aktivitaet_by_id(aktivitaet_id)
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


""" Alle Aktivitäten in einem Projekt ausgeben """
@zeiterfassung.route("/aktivitaet/projekt/<int:projekt_id>")
@zeiterfassung.param("projekt_id", "Die Id des gewünschten Projektes")
class AktivitaetenInProjektByIdOperations(Resource):
    @zeiterfassung.marshal_with(aktivitaet)
    def get(self, projekt_id):
        """ Auslesen aller Aktivitaeten in einer Projekt Instanz.
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        aktivitaeten = adm.get_all_aktivitaeten_by_projekt_id(projekt_id)
        return aktivitaeten



@zeiterfassung.route("/urlaub")
class UrlaubListOperations(Resource):
    @zeiterfassung.marshal_with(urlaub)
    def get(self):
        """ Auslesen der Urlaub-Objekte """
        adm = Administration()
        urlaub = adm.get_all_urlaub()
        return urlaub

    @zeiterfassung.marshal_with(urlaub, code=201)
    @zeiterfassung.expect(urlaub)
    def post(self):
        """ Urlaubs Instanz erstellen """
        adm = Administration()
        """ Wir setzen den api.payload in die from_dict Methode ein und erstellen damit Urlaub, indem wir die 
        Attribute aus den Werten von api.payload setzen. urlaub_object = Urlaub-Objekt """
        urlaub_object = Urlaub.from_dict(api.payload)

        if urlaub_object is not None:
            """ Wir erstellen in Administration Urlaub mithilfe der Daten vom api.payload """
            c = adm.create_urlaub(urlaub_object.get_person_id(), urlaub_object.get_end_date(), urlaub_object.get_start_date())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500


@zeiterfassung.route("/urlaub/<int:urlaub_id>")
@zeiterfassung.expect(urlaub, validate=True)
class UrlaubByIdOperations(Resource):
    @zeiterfassung.marshal_with(urlaub)
    def delete(self, urlaub_id):
        """Löschen einer Urlaubsinstanz.
        Das zu löschende Objekt wird anhand der id bestimmt.
        """
        adm = Administration()
        urlaub = adm.delete_urlaub_by_urlaub_id(urlaub_id)
        print(urlaub)
        return urlaub

    def put(self, urlaub_id):
        """ Urlaubsinstanz updaten """
        adm = Administration()
        urlaub_object = Urlaub.from_dict(api.payload)

        if urlaub_object is not None:
            """Hierdurch wird die id des zu überschreibenden Urlaub-Objekts gesetzt.
            """
            urlaub_object.set_id(urlaub_id)
            adm.update_urlaub(urlaub_object)
            return '', 200
        else:
            return '', 500








""" Mitarbeiter werden zur zugeordneten Projekt_ID ausgegeben """
@zeiterfassung.route("/mitarbeiter_in_projekt/<int:person_idd>")
@zeiterfassung.param("person_idd", "Die Id der gewünschten Person")
class MitarbeiterInProjektById(Resource):
    @zeiterfassung.marshal_with(mitarbeiter_in_projekt)
    def get(self, person_idd):
        """ Auslesen der Mitarbeiter innerhalb eines Projektes"""
        adm = Administration()
        person = adm.get_mitarbeiter_in_projekt_by_idd(person_idd)
        print(person)
        return person





""" Verkaufte_Stunden_in_Aktivität(e) wird gelesen und erstellt  """
@zeiterfassung.route("/verkaufte_stunden_in_aktivitaet")
class VerkaufteStundenInAktivitaetOperations(Resource):
    @zeiterfassung.marshal_with(verkaufte_stunden_in_aktivitaet)
    def get(self):
        """ Auslesen der Verkaufte_Stunden_in_Aktivität """
        adm = Administration()
        verkaufte_stunden = adm.get_all_verkaufte_stunden_in_aktivitaet()
        return verkaufte_stunden



    @zeiterfassung.marshal_with(verkaufte_stunden_in_aktivitaet, code=201)
    @zeiterfassung.expect(verkaufte_stunden_in_aktivitaet)
    def post(self):
        """ Verkaufte_Stunden_in_Aktivität erstellen """
        adm = Administration()
        """ Wir setzen den api.payload in die from_dict Methode ein und erstellen damit eine Person, indem wir ihre 
        Attribute aus den Werten von api.payload setzen. person_object = Person-Objekt """
        person_object = VerkaufteStundenInAktivitaet.from_dict(api.payload)

        if person_object is not None:
            """ Wir erstellen in Administration eine verkaufte_stunden_in_aktivitaet mithilfe der Daten vom api.payload """
            c = adm.create_verkaufte_stunden_in_aktivitaet(person_object.get_aktivitaet(), person_object.get_person(),
                                  person_object.get_gebuchte_stunden())
            return c, 200
        else:
            # Wenn irgendetwas schiefgeht, dann geben wir nichts zurück und werfen einen Server-Fehler.
            return '', 500




""" Sollzeit  """
@zeiterfassung.route("/sollzeit/<int:projekt_id>")
@zeiterfassung.param("projekt_id", "Die Id des gewünschten Projektes")
class SollzeitOperations(Resource):
    @zeiterfassung.marshal_with(sollzeit)
    def get(self,projekt_id):
        """ Auslesen der Sollzeit szenario 4.
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        projekt = adm.get_sollzeit_by_id(projekt_id)
        return projekt



@zeiterfassung.route("/mitarbeiteransicht/<int:projekt_id>")
@zeiterfassung.param("projekt_id", "Die Id des gewünschten Projektes")
class MitarbeiteransichtOperations(Resource):
    @zeiterfassung.marshal_with(mitarbeiteransicht)
    def get(self,projekt_id):
        """ Auslesen der IstStunden szenario 4.
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        projekt = adm.get_mitarbeiteransicht_by_id(projekt_id)
        return projekt



@zeiterfassung.route("/persoenliche_mitarbeiteransicht/<int:person_id>")
@zeiterfassung.param("person_id", "Die Id der gewünschten Person")
class PersoenlicheOperations(Resource):
    @zeiterfassung.marshal_with(mitarbeiteransicht)
    def get(self,person_id):
        """ Auslesen der IstStunden auf allen Projekten szenario 3.
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        projekt = adm.get_persoenliche_mitarbeiteransicht_by_id(person_id)
        return projekt



""" Projekt Objekte werden anhand dem projektleiter ausgegeben"""
@zeiterfassung.route("/projekt/projektleiter/<int:projektleiter>")
@zeiterfassung.param("projektleiter", "Die Id des gewünschten Projektleiters")
class ProjByIdOperations(Resource):
    @zeiterfassung.marshal_with(projekt)
    def get(self,projektleiter):
        """ Projekt Objekte werden anhand dem projektleiter ausgegeben
        Das zu auslesende Objekt wird anhand der person_id bestimmt
        """
        adm = Administration()
        projekt = adm.projekte_by_projektleiter(projektleiter)
        return projekt


""" Es werden alle Projekte angezeigt in der eine Person arbeitet"""
@zeiterfassung.route("/projekt/mitarbeiter/<int:person_id>")
@zeiterfassung.param("person_id", "Die Id der gewünschten Person")
class ProjektByIdMitarbeiterOperations(Resource):
    @zeiterfassung.marshal_with(projekt)
    def get(self,person_id):
        """ Es werden alle Projekte angezeigt in der eine Person arbeitet
        Das zu auslesende Objekt wird anhand der id bestimmt
        """
        adm = Administration()
        projekt = adm.get_all_projekte_by_mitarbeiter_id(person_id)
        return projekt



""" Server läuft auf localhost:5000 bzw. 127.0.0.1:5000 """
if __name__ == '__main__':
    app.run(debug=True)

