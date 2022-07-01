import React, { useState, useEffect } from 'react';
import { Grid, Button, Typography } from '@material-ui/core';
import TextField from "@material-ui/core/TextField";
import axios from 'axios';
import "../index.css"

function Pause(props) {
    const [person_id, setPersonID] = useState(null);
    //Post Pause
    const [start_pause, setStartPause] = useState(null);
    const [ende_pause, setEndePause] = useState(null);

    const [intervall, setIntervall] = useState("0h 0min");
    const [start, setStart] = useState(null);
    const [ende1, setEnde] = useState(null);
    let defaultTime = new Date()
    defaultTime.setHours(0)
    defaultTime.setMinutes(0)
    defaultTime.setSeconds(0)
    const [endeTime, setEndeTime] = useState(defaultTime);
    const [startTime, setStartTime] = useState(defaultTime);

    function postPause(id) {
        const url = `/zeit/pause`;
        console.log("Pause", id, person_id, start_pause)
        axios.post(url, {
            id,
            person_id,
            start_pause,
            ende_pause
        }).then(data => console.log(" Pause wurde gepostet", data).catch(err => console.log(err)))
    };

    function checkTime() {
        /* An dieser Stelle Problem: der zuletzt gesetzte wert stimmt, aber der andere nicht */
        console.log("Time is Set!!")
        console.log("Start:", start_pause)
        console.log("Ende:", ende_pause)
        let newIntervall = new Date();
        newIntervall = (endeTime - startTime)
        console.log("SetTime: start (Date):", startTime)
        console.log("SetTime: ende (Date):", endeTime)
        console.log("Intervallzeit als Date:", newIntervall)

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
        console.log("Intervall in Stunde u Minuten:", newIntervallString)
        {/** Wir prüfen ob die gebuchte Anwesenheit 7.5h überschritten hat oder nicht */ }
        if (newIntervallFloat > 0.3) {
            console.log("Die Pause ist zu lang!")
            props.setErrorAlertOpen(true)
        }
        else {
            console.log("Das passt!")
            props.setAlertOpen(true)
            postPause(1211)
        }
        setIntervall(newIntervallString)
    };

    const changePauseStart = (event) => {
        setStartPause(event.target.value)
        var time = event.target.value;
        console.log(time)
        setStart(time)
        var start1 = new Date()
        var timeInInt = time.split(":");
        console.log(timeInInt[0], timeInInt[1])
        start1.setHours(timeInInt[0])
        start1.setMinutes(timeInInt[1])
        console.log("Start als Date nach Änderung:", start1)
        setStartTime(start1)
    };

    const changePauseEnde = (event) => {
        setEndePause(event.target.value)
        var time = event.target.value;
        setEnde(time)
        var ende1 = new Date()
        var timeInInt = time.split(":");
        console.log(timeInInt[0], timeInInt[1])
        ende1.setHours(timeInInt[0])
        ende1.setMinutes(timeInInt[1])
        console.log("Ende als Date nach Änderung:", ende1)
        setEndeTime(ende1)
    };

    return (
        <div>
            <Grid id="pause-grid" container justify="center" alignItems="center" style={{ marginTop: "1rem" }}>
                <Grid item md={3} xs={6} style={{ alignSelf: "end" }}>
                    <Typography variant="h5" >Pause</Typography>
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
                            onChange={changePauseStart}
                        />
                    </form>
                </Grid>
                <Grid item xs={3} >
                    <form noValidate>
                        <TextField
                            className="time"
                            label="Ende"
                            type="time"
                            defaultValue="00:00"
                            InputLabelProps={{
                                shrink: true
                            }}
                            onChange={changePauseEnde}
                        />
                    </form>

                </Grid>
                <Grid item md={3} className="button-anwesenheit" >
                    <Button className="outlined-button" variant="outlined" onClick={checkTime} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px" }} >
                        Buchen
                    </Button>

                </Grid>
            </Grid>

        </div>
    )
}

export default Pause