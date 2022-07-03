import React, { useState, useEffect } from 'react';
import { Grid, Button, Typography } from '@material-ui/core';
import TextField from "@material-ui/core/TextField";
import axios from 'axios';
import "../index.css"

/**
 * Beinhaltet die Buchungen für Kommen und Gehen
 * 
 * @author [Talha Yildirim](https://github.com/talha16)
 * @author [Aykut Demir](https://github.com/AykutDemirr)
*/

export default function Anwesenheit(props) {
    const [intervall, setIntervall] = useState("0h 0min");
    const [start, setStart] = useState(null);
    const [ende1, setEnde] = useState(null);
    let defaultTime = new Date()
    defaultTime.setHours(0)
    defaultTime.setMinutes(0)
    defaultTime.setSeconds(0)
    const [endeTime, setEndeTime] = useState(defaultTime);
    const [startTime, setStartTime] = useState(defaultTime);

    // Post
    const [person_id, setPersonID] = useState(null);
    const [start_kommen, setStartKommen] = useState(null);
    const [ende, setGehen] = useState(null);



    useEffect(() => {
        iDerhalten(props.id)
        let defaultTime = new Date()
        defaultTime.setHours(0)
        defaultTime.setMinutes(0)
        defaultTime.setSeconds(0)
        //console.log("defaultTime", defaultTime)
        //console.log("Default start (Date):", startTime)
        //console.log("Default ende (Date):", endeTime)
        //setIntervall(defaultTime.toLocaleTimeString(navigator.language, { hour: '2-digit', minute: '2-digit' }))
        setStart(defaultTime.toLocaleTimeString(navigator.language, { hour: '2-digit', minute: '2-digit' }))
        setEnde(defaultTime.toLocaleTimeString(navigator.language, { hour: '2-digit', minute: '2-digit' }))
    }, []
    );


    const iDerhalten = (id) => {
        setPersonID(id)
        //console.log("Person Id", person_id)
    }

    

    function postEreignisBuchung(id, kommen_id, gehen_id) {
        const url = `/zeit/ereignisbuchung`;
        //console.log("Ereignisbuchung:", id, kommen_id, gehen_id)
        axios.post(url, {
            id,
            kommen_id,
            gehen_id
        }).then(data => {console.log(" Ereignisbuchung wurde gepostet", data)})
        .catch(err => {console.log(err)})
    };

    function postKommen(id) {
        const url = `/zeit/kommen`;
        //console.log("Kommen", id, person_id, start_kommen)
        axios.post(url, {
            id,
            person_id,
            start_kommen
        })
        .then((response) => {
            console.log("Kommen wurde gepostet",response)
            const data = response.data;
            let kommen_id = data.id
            let gehen_id = data.id
            console.log("Kommen Response",kommen_id)     
            postGehen(1211)
            
        }).catch(err => {console.log(err)})
    };

    function postGehen(id) {
        const url = `/zeit/gehen`;
        console.log("Gehen saaaa", id, person_id, ende)
        axios.post(url, {
            id,
            person_id,
            ende
        }).then((response) => {
            console.log("Gehen wurde gepostet",response)
            const data = response.data;
            let kommen_id = data.id
            let gehen_id = data.id
            //console.log("Wert",gehen_id)
            postEreignisBuchung(1211, kommen_id, gehen_id)     
        }).catch(err => {console.log(err)})
    };

    const changeKommen = (event) => {
        setStartKommen(event.target.value)
        var time = event.target.value;
        //console.log(time)
        setStart(time)
        var start1 = new Date()
        var timeInInt = time.split(":");
        //console.log(timeInInt[0], timeInInt[1])
        start1.setHours(timeInInt[0])
        start1.setMinutes(timeInInt[1])
        //console.log("Start als Date nach Änderung:", start1)
        //console.log("Ende als Date nach Änderung:",endeTime)
        setStartTime(start1)
    }

    const changeGehen = (event) => {
        setGehen(event.target.value)
        var time = event.target.value;
        setEnde(time)
        var ende1 = new Date()
        var timeInInt = time.split(":");
        //console.log(timeInInt[0], timeInInt[1])
        ende1.setHours(timeInInt[0])
        ende1.setMinutes(timeInInt[1])
        //console.log("Ende als Date nach Änderung:", ende1)
        setEndeTime(ende1)
    };

    const PostKommenUndGehen = () => {
        postKommen(1211)


    };

    function checkTime() {
        /* An dieser Stelle Problem: der zuletzt gesetzte wert stimmt, aber der andere nicht */
        //console.log("Time is Set!!")
        //console.log("Start:", start_kommen)
        //console.log("Ende:", ende)
        let newIntervall = new Date();
        newIntervall = (endeTime - startTime)
        //console.log("SetTime: start (Date):", startTime)
        //console.log("SetTime: ende (Date):", endeTime)
        //console.log("Intervallzeit als Date:", newIntervall)

        var msec = newIntervall;
        var hh = Math.floor(msec / 1000 / 60 / 60);
        msec -= hh * 1000 * 60 * 60;
        var mm = Math.floor(msec / 1000 / 60);
        msec -= mm * 1000 * 60;
        var newIntervallObject = new Date();
        newIntervallObject.setHours(hh)
        newIntervallObject.setMinutes(mm)
        //console.log(hh + " Stunden" + " " + mm + " Minuten")
        let newIntervallString = hh + "." + mm + "h"
        let newIntervallFloat = parseFloat(newIntervallString)
        //console.log("Intervall in Stunde u Minuten:", newIntervallString)
        {/** Wir prüfen ob die gebuchte Anwesenheit 7.5h überschritten hat oder nicht */ }
        if (newIntervallFloat > 7.3) {
            props.setErrorAlertOpen(true)
        }
        else {
            //console.log("Das passt!")
            props.setAlertOpen(true)
            PostKommenUndGehen()
        }
        setIntervall(newIntervallString)
    };

    return (
        <div>
            <Grid container justify="center" alignItems="center">
                <Grid item md={3} xs={6} style={{ alignSelf: "end" }}>
                    <Typography variant="h5">Anwesenheit</Typography>
                </Grid>
                <Grid item xs={3}>
                    <form noValidate>
                        <TextField
                            className="time"
                            label="Start"
                            type="time"
                            defaultValue="00:00"
                            InputLabelProps={{
                                shrink: true
                            }}
                            onChange={changeKommen}
                        />
                    </form>
                </Grid>
                <Grid item xs={3}>
                    <form noValidate>
                        <TextField
                            className="time"
                            label="Ende"
                            type="time"
                            defaultValue="00:00"
                            InputLabelProps={{
                                shrink: true
                            }}
                            onChange={changeGehen}
                        />
                    </form>
                </Grid>
                <Grid item md={3} className="button-anwesenheit">
                    <Grid item >
                        <Button className="outlined-button" variant="outlined" onClick={() => checkTime()} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px", color: "#00bcd4" }} >
                            Buchen
                        </Button>

                    </Grid>
                </Grid>
            </Grid>


          
        </div>

    )
}
