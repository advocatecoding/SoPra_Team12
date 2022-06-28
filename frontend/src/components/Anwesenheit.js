import React, { useState, useEffect } from 'react';
import { Grid, Button, Typography } from '@material-ui/core';
import TextField from "@material-ui/core/TextField";
import Aktivitäten from "./Aktivitäten";
import theme from "../Login";
import { paginationItemClasses, ThemeProvider } from '@mui/material';
import axios from 'axios';

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
    const [intervallTime, setIntervallTime] = useState("");

    // Post
    const [person_id, setPersonID] = useState(null);
    const [start_kommen, setStartKommen] = useState(null);
    const [ende, setGehen] = useState(null);

    //Post Pause
    const [start_pause, setStartPause] = useState(null);
    const [ende_pause, setEndePause] = useState(null);

    useEffect(() => {
        iDerhalten(props.id)
        let defaultTime = new Date()
        defaultTime.setHours(0)
        defaultTime.setMinutes(0)
        defaultTime.setSeconds(0)
        console.log("defaultTime", defaultTime)

        console.log("Default start (Date):", startTime)
        console.log("Default ende (Date):", endeTime)
        //setIntervall(defaultTime.toLocaleTimeString(navigator.language, { hour: '2-digit', minute: '2-digit' }))
        setStart(defaultTime.toLocaleTimeString(navigator.language, { hour: '2-digit', minute: '2-digit' }))
        setEnde(defaultTime.toLocaleTimeString(navigator.language, { hour: '2-digit', minute: '2-digit' }))
    }, []
    );


    const iDerhalten = (id) => {
        setPersonID(id)
        console.log("BRUDEEER" ,person_id)
      }

    const changeKommen = (event) => {
        setStartKommen(event.target.value)
    }

    const changeEnde=() =>{
        console.log("f")
    }



    function postKommen(id) {
        const url = `/zeit/kommen`;
        console.log("Aykut Kommen", id, person_id, start_kommen)
        axios.post(url, {
          id,
          person_id,
          start_kommen
        }).then(data => console.log(" Kommen wurde gepostet", data).catch(err => console.log(err)))
      };

    
    function postGehen(id) {
        const url = `/zeit/gehen`;
        console.log("Aykut Gehen", id, person_id, start_kommen)
        axios.post(url, {
          id,
          person_id,
          ende
        }).then(data => console.log(" Gehen wurde gepostet", data).catch(err => console.log(err)))
      };


    function postPause(id) {
        const url = `/zeit/pause`;
        console.log("Aykut Gehen", id, person_id, start_kommen)
        axios.post(url, {
          id,
          person_id,
          start_pause,
          ende_pause
        }).then(data => console.log(" Pause wurde gepostet", data).catch(err => console.log(err)))
      };

      

    const changeGehen = (event) => {
        setGehen(event.target.value)
    };

    const changePauseStart = (event) => {
        setStartPause(event.target.value)
    };


    const changePauseEnde = (event) => {
        setEndePause(event.target.value)
    };


    

    const PostKommenUndGehen = (e) => {
        e.preventDefault();
        postKommen(999)
        postGehen(999)
    };


    const ChangePause = (e) => {
        e.preventDefault();
        postPause(999)
    };


    


    

    function setTime() {
        /* An dieser Stelle Problem: der zuletzt gesetzte wert stimmt, aber der andere nicht */
        console.log("Time is Set!!")
        console.log("Start:", startTime)
        console.log("Ende:", endeTime)
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
        let newIntervallString = hh + "h " + mm + "min"
        console.log("Intervall in Stunde u Minuten:", newIntervallString)
        setIntervall(newIntervallString)
    };





    return (
        <div>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>

                <Grid item xs={3} style={{ alignSelf: "end" }}>
                    <Typography variant="h5" >Anwesenheit</Typography>
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
                <Grid item xs={3} style={{ alignSelf: "end" }}>
                    <Grid item >
                        <Button variant="outlined" onClick={PostKommenUndGehen} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px", color: "#00bcd4" }} >
                            Buchen
                        </Button>

                    </Grid>
                </Grid>


            </div>

            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: "1rem" }}>

                <Grid item xs={3} style={{ alignSelf: "end" }}>
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
                            onChange={changePauseEnde}
                        />
                    </form>
                </Grid>
                <Grid item xs={3} style={{ alignSelf: "end" }}>
                        <Button variant="outlined" onClick={ChangePause} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px", color: "#00bcd4 !important" }} >
                            Buchen
                        </Button>

                </Grid>

            </div>
        </div>

    )
}
