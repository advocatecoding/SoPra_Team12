import React, { useState, useEffect } from "react";
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import "./modal.css";
import { TextField } from "@mui/material";
import axios from 'axios';
import FormControl from '@mui/material/FormControl';
import MenuItem from '@mui/material/MenuItem';
import SaveAsRoundedIcon from '@mui/icons-material/SaveAsRounded';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';
import Select from '@mui/material/Select';
import InputLabel from '@mui/material/InputLabel';
import "../../index.css"

export default function AktivitätBuchenModal(props) {

  // mit setSelectedProject den nächsten fetch ausführen

  const [start_datum, setStartDatum] = useState(null);
  const [gebuchte_stunden, setStunden] = useState(null);
  const [mitarbeiter, setPersonID] = useState(null);
  const [aktivitaet, setAktivitaetID] = useState(null);
  const [projekt_id, setSelectedProject] = useState(null);
  const [mitarbeiterProjekte, setMitarbeiterProjekte] = useState([]);
  const [aktivitätListe, setAktivitätListe] = useState([]);
  const [loadingInProgress, setLoading] = useState(true);

  // Post für Empty Zeitintervall
  const [person_id, setPersonID2] = useState(null);
  const [aktivitaet_id, setAktivitaetID2] = useState(null);

  useEffect(() => {
    iDerhalten(props.id)
    FetchProjekte(props.id)
  }, [])



  async function FetchProjekte(id) {
    //console.log("Perso GCKEN.")
    //console.log(id, "22")
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


  async function FetchAktivität(id) {
    //console.log("Kommt was an.", projekt_id)
    const url = `/zeit/aktivitaet/projekt/${id}`;

    //console.log(url)
    try {
      const response = await fetch(url);
      const data = await response.json();
      setAktivitätListe(data)
    } catch (e) {
      console.log(e.message)
    }
  }


  function postAktivität() {
    const url = `/zeit/verkaufte_stunden_in_aktivitaet`;
    //console.log(mitarbeiter, aktivitaet, gebuchte_stunden, "ZEIG AN")
    axios.post(url, {
      mitarbeiter,
      aktivitaet,
      gebuchte_stunden
    }).then(data => {console.log("Gebuchte Stunden wurde gepostet", data)}, props.setAlertOpen(true)).catch(err => console.log(err))
  };


  function postEmptyZeitintervallBuchung(id, gearbeitete_zeit) {
    const url = `/zeit/zeitintervallbuchungen`;
    axios.post(url, {
      id,
      projekt_id,
      person_id,
      aktivitaet_id,
      gearbeitete_zeit
    }).then(data => {console.log("Zeitintervall wurde gepostet", data)})
    .catch(err => console.log(err))
  };


  const changeStunden = (event) => {
    setStunden(event.target.value)
  }

  const iDerhalten = (id) => {
    setPersonID(id)
    setPersonID2(id)
  }

  const HandleClose = (e) => {
    e.preventDefault();
    props.setOpenModal(false);
    postAktivität();
    postEmptyZeitintervallBuchung(999,0)
  }

  const handleChange1 = (event) => {
    setAktivitaetID(event.target.value)
    setAktivitaetID2(event.target.value)
  }


  const handleChangee = (event) => {
    setSelectedProject(event.target.value)
    //console.log({ projekt_id }, "huhu")
    FetchAktivität(event.target.value)
  }

  return (
    <div className="modalContainer">
      <div className="titleCloseBtn">
        <button
          onClick={() => {
            props.setOpenModal(false);
          }}
        >
          X 
        </button>
      </div>
      <div className="title">
        <h2> <CalendarMonthIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />Aktivität zuweisen
        </h2>
      </div>
      <div className="body">
        <div style={{ marginTop: "1rem" }}>
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

          <div style={{paddingTop:"1rem"}}>
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

            <div style={{paddingTop:"1rem"}}>
            <TextField autoFocus
            required
            margin="dense"
            label="Stunden buchen"
            type="text"
            variant="standard" placeholder="Stunden" style={{ borderColor: "white", color: "white", backgroundColor: "rgba(79, 79, 79, 0.61)", borderRadius: "5px", minWidth:"270px" }} sx={{ m: 1, minWidth: 240 }}
            onChange={changeStunden}>
          </TextField>
          <Typography style={{ color: "white", textAlign: "center" }} fontSize={9}>Stunden buchen</Typography>
            </div>
         
        </div>

        <div style={{ paddingTop:"1rem" }}>
          <Button variant="outlined" onClick={HandleClose} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px", textAlign: "center", display: "inline", marginBottom: "0" }} >
          <SaveAsRoundedIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />
            Speichern
          </Button>
        </div>
      </div>
    </div>
  )
}




