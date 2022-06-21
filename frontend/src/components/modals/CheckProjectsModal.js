import React, { useState, useEffect } from "react";
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import "./modal.css";
import Users from '../Users';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

// Tabelle 
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

export default function CheckProjectsModal(props) {

  const [projectsToCheck, setProjectsToCheck] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null);

  const [createListIsClicked, setCreateListIsClicked] = useState(false);


  useEffect(() => {
    fetchProjekteToCheck(props.mitarbeiter_id)
  }, [])

  // person_id eines Projektleiters
  async function fetchProjekteToCheck(person_id) {
    console.log(person_id)
    const url = `/zeit/projekt/projektleiter/${person_id}`;
    try {
      const response = await fetch(url);
      const data = await response.json();
      console.log("fetched Projekte!")
      console.log(data)
      setProjectsToCheck(data)
    } catch (e) {
      console.log(e.message)
    }
    ;
  }

  const handleChange = (event) => {
    setSelectedProject(event.target.value);
  };

  const openArbeitszeiten = () => {
    setCreateListIsClicked(true)
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

      {createListIsClicked == false ?
        <>
          <div className="title">
            <h2>Checken Sie die Projekte!</h2>
          </div>
          <div className="body">
            <div style={{ marginTop: "5rem" }}>

              <FormControl style={{ borderColor: "white", color: "white", backgroundColor: "rgba(79, 79, 79, 0.61)", borderRadius: "5px" }} sx={{ m: 1, minWidth: 200 }} >
                <InputLabel style={{ color: "white" }} id="demo-simple-select-autowidth-label">Projekte</InputLabel>
                <Select style={{ color: "white" }}
                  onChange={handleChange}
                  label="Projekte"
                  color="primary"
                >
                  {projectsToCheck.map((item) =>
                    <MenuItem value={item.id} style={{ color: "#00bcd4" }}>{item.projektname}</MenuItem>
                  )
                  }
                </Select>
              </FormControl>

              <Typography style={{ color: "white", textAlign: "center" }} fontSize={9}>Wählen Sie ein Projekt zum Kontrollieren aus.</Typography>

            </div>

            <div style={{ marginTop: "5rem" }}>
              <Button variant="outlined" onClick={() => { openArbeitszeiten() }} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px", textAlign: "center", display: "inline", marginBottom: "0" }} >
                Arbeitszeiten anzeigen
              </Button>
            </div>
          </div>

        </>
        :
        <>
          <div className="title">
            <h2>Stundenübersicht des Projekts {selectedProject}</h2>
          </div>
          <div className="body">
          <div style={{ marginTop: "5rem" }}>
              <ProjectTime projekt_id={selectedProject}/>

          </div>

          </div>
        </>

      }

    </div>




  )
}



function ProjectTime(props) {

  const[aktivitaet, setAktivitaet] = useState("");
  const[names, setNames] = useState("");
  const[istZeit, setIstZeit] = useState("");
  const[sollZeit, setSollZeit] = useState("");
  const[kontrolldaten, setKontrolldaten] = useState(null); 

  useEffect(() => {
    fetchIstZeit(props.projekt_id)
  }, [])

  // person_id eines Projektleiters
  async function fetchIstZeit(projekt_id) {
    const url = `/zeit/mitarbeiteransicht/${projekt_id}`;
    try {
      const response = await fetch(url);
      const data = await response.json();
      setKontrolldaten(data)

      //setIstZeit(data.gearbeitete_zeit)
      //setAktivitaet(data.bezeichnung)
    } catch (e) {
      console.log(e.message)
    }
    ;
  }

  return (
    <div>
      {console.log(kontrolldaten[0].vorname)}
      {kontrolldaten.map((item) => 
        <p> {item.vorname} {item.gearbeitete_zeit}  </p> 
      )}
      
      
    </div>
  )
}
