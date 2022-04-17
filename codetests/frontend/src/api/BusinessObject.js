

export default class BusinessObject {
    constructor() {
        this.id = 0;
        this.datetime = null;
    }


    setId(value) {
        this.id = value;
    }

    getId(){
        return this.id;
    }

}