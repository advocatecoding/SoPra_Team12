import React, { useState, useEffect } from "react";
import * as Max from "@mui/material";
import { Grid, Typography, Button } from '@mui/material';
import TextField from "@material-ui/core/TextField";
import axios from 'axios';
import FormControl from '@mui/material/FormControl';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import InputLabel from '@mui/material/InputLabel';


export default function Buchen(props) {

    const [aktivitPar, setAktivitätPar] = useState(" ");
    const [intervall, setIntervall] = useState("0h 0min");
    const [start, setStart] = useState(null);
    const [ende, setEnde] = useState(null);
    let defaultTime = new Date()
    defaultTime.setHours(0)
    defaultTime.setMinutes(0)
    defaultTime.setSeconds(0)
    const [endeTime, setEndeTime] = useState(defaultTime);
    const [startTime, setStartTime] = useState(defaultTime);
    const [intervallTime, setIntervallTime] = useState("");



    const [mitarbeiterProjekte, setMitarbeiterProjekte] = useState([]);
    const [selectedProject, setSelectedProject] = useState(null);
    const [mitarbeiter, setPersonID] = useState(null);
    const [aktivitaet, setAktivitaetID] = useState(null);
    const [aktivitätListe, setAktivitätListe] = useState([]);



    async function FetchProjekte(id) {
        console.log("Perso GCKEN.")
        console.log(id, "22")
        const url = `/zeit/projekt/mitarbeiter/${id}`;
    
        console.log(url)
        try {
          const response = await fetch(url);
          const data = await response.json();
          setMitarbeiterProjekte(data)
        } catch (e) {
          console.log(e.message)
        }
      }


      async function FetchAktivität(mitarbeiter, id ) {
        console.log("Kommt ws an.", selectedProject)
        const url = `/zeit/aktivitaet/buchen/${mitarbeiter}/${id}`;
    
        console.log(url)
        try {
          const response = await fetch(url);
          const data = await response.json();
          setAktivitätListe(data)
        } catch (e) {
          console.log(e.message)
        }
      }

    
      function postZeintervall() {
        const url = `/zeit/verkaufte_stunden_in_aktivitaet`;
        console.log(mitarbeiter, aktivitaet, "ZEIG AN")
        axios.post(url, {
          mitarbeiter,
          aktivitaet,
        }).then(data => console.log("Gebuchte Stunden wurde gepostet", data).catch(err => console.log(err)))
      };



    useEffect(() => {
        iDerhalten(props.id)
        FetchProjekte(props.id)
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

    const changeStart = (event) => {
        var time = event.target.value;
        setStart(time)
        var start1 = new Date()
        var timeInInt = time.split(":");
        console.log(timeInInt[0], timeInInt[1])
        start1.setHours(timeInInt[0])
        start1.setMinutes(timeInInt[1])
        console.log("sjahdsajknjcd Start als Date nach Änderung:", start1)
        //console.log("Ende als Date nach Änderung:",endeTime)
        setStartTime(start1)

    }

    const changeEnde = (event) => {
        var time = event.target.value;
        setEnde(time)
        var ende1 = new Date()
        var timeInInt = time.split(":");
        console.log(timeInInt[0], timeInInt[1])
        ende1.setHours(timeInInt[0])
        ende1.setMinutes(timeInInt[1])
        console.log("asgvasbhsabkdas Ende als Date nach Änderung:", ende1)
        setEndeTime(ende1)

    }

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
    }


    const handleChangee = (event) => {
        setSelectedProject(event.target.value)
        console.log({ selectedProject }, "huhu")
        FetchAktivität(mitarbeiter, event.target.value)
      }

      const iDerhalten = (id) => {
        setPersonID(id)
      }

      const handleChange1 = (event) => {
        setAktivitaetID(event.target.value)
      }



    return (
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>

        <div style={{ marginTop: "2rem" }}>
          <FormControl style={{ borderColor: "white", color: "white", backgroundColor: "rgba(79, 79, 79, 0.61)", borderRadius: "5px" ,  minWidth:"270px" }} sx={{ m: 1, minWidth: 200 }} >
            <InputLabel style={{ color: "white" }} id="demo-simple-select-autowidth-label">Projekt</InputLabel>
            <Select style={{ color: "white" }}
              onChange={handleChangee}
              label="Projekttest"
              color="primary"
            >
              {mitarbeiterProjekte.map((item) =>
                <MenuItem value={item.id} style={{ color: "#00bcd4" }}>{item.projektname}</MenuItem>
              )
              }
            </Select>
          </FormControl>
          <Typography style={{ color: "white", textAlign: "center" }} fontSize={9}>Wählen Sie eine Projekt aus.</Typography>

          </div>

          <div style={{paddingTop:"1.5rem"}}>
            <FormControl style={{ borderColor: "white", color: "white", backgroundColor: "rgba(79, 79, 79, 0.61)", borderRadius: "5px",  minWidth:"270px" }} sx={{ m: 1, minWidth: 200 }} >
              <InputLabel style={{ color: "white" }} id="demo-simple-select-autowidth-label">Aktivität</InputLabel>
              <Select style={{ color: "white" }}
                onChange={handleChange1}
                label="Aktivität"
                color="primary"
              >
                {aktivitätListe.map((item) =>
                  <MenuItem value={item.id} style={{ color: "#00bcd4" }}>{item.aktivitaetname}</MenuItem>
                )
                }
              </Select>
            </FormControl>
            <Typography style={{ color: "white", textAlign: "center" }} fontSize={9}>Wählen Sie eine Aktivität aus.</Typography>
          </div>
                <Grid item xs={2}>
                    <form noValidate>
                        <TextField
                            className="time"
                            label="Start"
                            type="time"
                            defaultValue="00:00"
                            InputLabelProps={{
                                shrink: true
                            }}
                            onChange={changeStart}
                        />
                    </form>
                </Grid>
                <Grid item xs={2}>
                    <form noValidate>
                        <TextField
                            className="time"
                            label="Ende"
                            type="time"
                            defaultValue="00:00"


                            InputLabelProps={{
                                shrink: true
                            }}
                            onChange={changeEnde}
                        />
                    </form>
                </Grid>
                <Grid item xs={4}>
                    <Button variant="outlined" onClick={postZeintervall} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px", color: "#00bcd4" }} >
                        Buchen
                    </Button>
                </Grid>
                {/** <Grid item xs={3}>
                    <Typography color={"white"} >Zeitintervall: {intervall} </Typography>
                    <Typography color={"white"}>von {start} und {ende}</Typography>


                </Grid>*/}

        </div>
    )
}
