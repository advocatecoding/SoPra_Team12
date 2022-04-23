import BusinessObject from "./BusinessObject";

export default class PersonBO extends BusinessObject {
    /**
     * Wir erstellen einen Konstruktor
     */
    constructor(vorname, nachname) {
        super();
        this.vorname = vorname;
        this.nachname = nachname;
    }



    getVorname(){
        return this.vorname
    }

    setVorname(value) {
        this.vorname = value
    }

    getNachname() {
        return this.nachname
    }

    setNachname(value) {
        this.nachname = value
    }

    /**
     * Wir nehmen die vom Server bekommene Json-Datei und fügen sie in eine Liste ein um im Frontend mit diesen Werten
     * arbeiten zu können 
     */
    static convertFromJson(personen) {
        let result = []
        /** Prüfen ob der eingegebene Parameterwert eine Liste ist*/
        if (Array.isArray(personen)) {
            personen.forEach((x) => {
                Object.setPrototypeOf(x, PersonBO.prototype)
                result.push(x)
            })
        } else {
            // keine Liste -> einzelnes Objekt
            let x = personen;
            Object.setPrototypeOf(x, PersonBO.prototype);
            result.push(x)
        }
        console.log(result)
        return result;
    }





}