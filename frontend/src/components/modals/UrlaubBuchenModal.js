import React, { useState, useEffect } from "react";
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import "./modal.css";
import { TextField } from "@mui/material";
import axios from 'axios';

export default function UrlaubBuchenModal(props) {



  const [start_datum, setStartDatum] = useState(null);
  const [end_datum, setEndDatum] = useState(null);
  const [person_id, setPersonID] = useState(null);


  useEffect(() => {
    iDerhalten(props.id)
  }, [props.id])



  function postUrlaub(id) {
    const url = `/zeit/urlaub`;
    axios.post(url, {
      id,
      person_id,
      start_datum,
      end_datum
    })
    .then(data => {
      console.log("Urlaub wure gepostet", data)
    })
    .catch(err => { console.log(err) })
  };

  const changeStartDatum = (event) => {
    setStartDatum(event.target.value)
  }

  const changeEndDatum = (event) => {
    setEndDatum(event.target.value)
  }

  const iDerhalten = (id) => {
    setPersonID(id)
  }

  const HandleClose = (e) => {
    e.preventDefault();
    props.setOpenModal(false);
    postUrlaub(1211);
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
        <h2>Buchen Sie Urlaub!</h2>
      </div>
      <div className="body">
        <div style={{ marginTop: "5rem" }}>

          <TextField autoFocus
            required
            margin="dense"
            label="Startdatum"
            type="text"
            variant="standard" placeholder="Format: JJJJ-MM-TT" style={{ borderColor: "white", color: "white", backgroundColor: "rgba(79, 79, 79, 0.61)", borderRadius: "5px" }} sx={{ m: 1, minWidth: 240 }}
            onChange={changeStartDatum}>
          </TextField>
          <Typography style={{ color: "white", textAlign: "center" }} fontSize={9}>Startdatum</Typography>
          <TextField autoFocus
            required
            margin="dense"
            label="Enddatum"
            type="text"
            variant="standard" placeholder="Format: JJJJ-MM-TT" style={{ borderColor: "white", color: "white", backgroundColor: "rgba(79, 79, 79, 0.61)", borderRadius: "5px" }} sx={{ m: 1, minWidth: 240 }}
            onChange={changeEndDatum}>
          </TextField>
          <Typography style={{ color: "white", textAlign: "center" }} fontSize={9}>Enddatum</Typography>
        </div>

        <div style={{ marginTop: "5rem" }}>
          <Button variant="outlined" onClick={HandleClose} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px", textAlign: "center", display: "inline", marginBottom: "0" }} >
            Urlaub buchen
          </Button>
        </div>
      </div>
    </div>
  )
}




