import PersonBO from './PersonBO';

export default class ZeiterfassungAPI {

    static #api = null
    #serverUrl = "/zeit"
    #getPersonsURL = () => `${this.#serverUrl}/personen`;

    /**
     * Wir erstellen eine Sigelton Instanz
     * @public
     */
    static getAPI() {
        if (this.#api == null) {
      this.#api = new ZeiterfassungAPI();
    }
    return this.#api;
    }

    #fetchAdvanced = (url, init) => fetch(url, init)
        .then(res => {
            if (!res.ok) {
                throw Error(`${res.status} ${res.statusText}`);
            }
            return res.json();
        })

    /**
     * 
     * 
     * @public
     */
    getPersonen() {
        return this.#fetchAdvanced(this.#getPersonsURL()).then((responseJSON) =>{
            let personenBOs = PersonBO.convertFromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(personenBOs);
            })
        })
    }

}