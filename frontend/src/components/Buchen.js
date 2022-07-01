import React, { useState, useEffect } from "react";
import { Grid, Typography, Button } from '@mui/material';
import TextField from "@material-ui/core/TextField";
import axios from 'axios';
import FormControl from '@mui/material/FormControl';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import InputLabel from '@mui/material/InputLabel';
import "../index.css"

/**
 * Beinhaltet die Buchungen für Projektarbeiten
 * 
 * @author [Talha Yildirim](https://github.com/talha16)
 * @author [Aykut Demir](https://github.com/AykutDemirr)
*/

export default function Buchen(props) {

  const [intervall, setIntervall] = useState("0h 0min");
  const [start, setStart] = useState(null);
  const [ende, setEnde] = useState(null);
  const [endeIsSet, setEndeIsSet] = useState(false);
  let defaultTime = new Date()
  defaultTime.setHours(0)
  defaultTime.setMinutes(0)
  defaultTime.setSeconds(0)
  const [endeTime, setEndeTime] = useState(defaultTime);
  const [startTime, setStartTime] = useState(defaultTime);
  const [gearbeitete_zeit, setGearbeiteteZeit] = useState("");

  const [aktivitaet_id, setAktivitaetID] = useState("");
  const [projekt_id, setProjektId] = useState("");
  const [mitarbeiterProjekte, setMitarbeiterProjekte] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null);
  const [person_id, setPersonID] = useState(null);
  const [aktivitätListe, setAktivitätListe] = useState([]);

  useEffect(() => {
    iDerhalten(props.id)
    FetchProjekte(props.id)
    let defaultTime = new Date()
    defaultTime.setHours(0)
    defaultTime.setMinutes(0)
    defaultTime.setSeconds(0)
    //console.log("defaultTime", defaultTime)

    //console.log("Default start (Date):", startTime)
    //console.log("Default ende (Date):", endeTime)
    setStart(defaultTime.toLocaleTimeString(navigator.language, { hour: '2-digit', minute: '2-digit' }))
    setEnde(defaultTime.toLocaleTimeString(navigator.language, { hour: '2-digit', minute: '2-digit' }))
  }, [props.id]
  );

  async function FetchProjekte(id) {
    //console.log("Perso GCKEN.")
    //console.log(id, "22")
    const url = `/zeit/projekt/mitarbeiter/${id}`;
    try {
      const response = await fetch(url);
      const data = await response.json();
      setMitarbeiterProjekte(data)
      //console.log(data)
      //console.log("ID---", data.id)
    } catch (e) {
      //console.log(e.message)
    }
  }

  async function FetchAktivität(mitarbeiter, id) {
    const url = `/zeit/aktivitaet/buchen/${mitarbeiter}/${id}`;
    //console.log(url)
    try {
      const response = await fetch(url);
      const data = await response.json();
      setAktivitätListe(data)
    } catch (e) {
      console.log(e.message)
    }
  }


  const changeStart = (event) => {
    var time = event.target.value;
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

  const changeEnde = (event) => {
    var time = event.target.value;
    setEnde(time)
    var ende1 = new Date()
    var timeInInt = time.split(":");
    //console.log(timeInInt[0], timeInInt[1])
    ende1.setHours(timeInInt[0])
    ende1.setMinutes(timeInInt[1])
    //console.log("Ende als Date nach Änderung:", ende1)
    setEndeTime(ende1)
    setEndeIsSet(true)
  }

  function setTime() {
    /* An dieser Stelle Problem: der zuletzt gesetzte wert stimmt, aber der andere nicht */
    //console.log("Time is Set!!")
    //console.log("Start:", startTime)
    //console.log("Ende:", endeTime)
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
    let gearbeiteteZeit = (hh + "." + mm)
    //console.log(hh + "." + mm)
    //console.log(hh + " Stunden" + " " + mm + " Minuten")
    let newIntervallString = hh + "h " + mm + "min"
    //console.log("Intervall in Stunde u Minuten:", newIntervallString)
    setIntervall(newIntervallString)
    postZeitintervallbuchung(1211, gearbeiteteZeit)
    postProjektarbeit(1211, gearbeiteteZeit)
    setProjektId("")
  }

  function postZeitintervallbuchung(id, gearbeitete_zeit) {
    const url = `/zeit/zeitintervallbuchungen`;
    //console.log("Post daten: " + "personId: " + person_id + "aktivität id: " + aktivitaet_id + "gearbeitete Zeit: " + gearbeitete_zeit + "projektId: " + projekt_id)
    axios.post(url, {
      id,
      projekt_id,
      person_id,
      aktivitaet_id,
      gearbeitete_zeit
    }).then((response) => {
      console.log(response)
    }, props.setAlertOpen(true)).catch(err => { console.log(err) })
  };

  function postProjektarbeit(id, gearbeitete_zeit) {
    const url = `/zeit/projektarbeit`;
    axios.post(url, {
      id,
      projekt_id,
      person_id,
      aktivitaet_id,
      gearbeitete_zeit
    }).then((response) => {
      console.log(response)
    }).catch(err => { console.log(err) })
  };

  const handleChangee = (event) => {
    setProjektId(event.target.value)
    //console.log({ projekt_id }, "huhu")
    FetchAktivität(person_id, event.target.value)
  }

  const iDerhalten = (id) => {
    setPersonID(id)
  }

  const handleChange1 = (event) => {
    setAktivitaetID(event.target.value)
  }



  return (
    <div>
      <Grid container
        direction="row"
        justifyContent="center"
        alignItems="center"
        id="buchen-grid"
      >
        <Grid item xs={12} sx={{ mb: 5 }}>
          <Typography variant="h5" align="center">Projektarbeit buchen</Typography>
        </Grid>
        <Grid item container justifyContent="center" lg={4} xs={12} sx={{ mr: 3 }}>
          <Grid item>
            <FormControl style={{ borderColor: "white", color: "white", backgroundColor: "rgba(79, 79, 79, 0.61)", borderRadius: "5px", minWidth: "270px" }} sx={{ m: 1, minWidth: 200 }} >
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
            <Typography style={{ color: "white", textAlign: "center" }} fontSize={9}>Wählen Sie ein Projekt aus.</Typography>
          </Grid>

        </Grid>

        {/** Aktivitätauswahl wird angezeigt, wenn Projekt ausgewählt wurde */}
        {
          projekt_id !== "" ?
            <>
              <Grid item container justifyContent="center" lg={4} xs={12} sx={{ mr: 3 }}>
                <Grid item>
                  <FormControl style={{ borderColor: "white", color: "white", backgroundColor: "rgba(79, 79, 79, 0.61)", borderRadius: "5px", minWidth: "270px" }} sx={{ m: 1, minWidth: 200 }} >
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
                </Grid>

              </Grid>
            </>
            : null
        }

        {/** Timepicker */}
        <Grid id="buchen-timepicker" item container justifyContent="space-evenly" direction="row" xs={10} lg={3} style={{ marginLeft: "1rem", marginBottom: "0.5rem" }}>
          <Grid item xs={6} >
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

          <Grid item xs={6} style={{ paddingLeft: "1rem" }}>
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
        </Grid>
      </Grid>
      {
        endeIsSet === true ?
          <>
            <Grid item container justifyContent="center" xs={12} style={{ paddingTop: "2rem" }}>
              <Grid item >
                <Button variant="outlined" onClick={setTime} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px", color: "red" }} >
                  Buchen
                </Button>

              </Grid>

            </Grid>
          </>
          : null
      }



    </div>
  )
}
