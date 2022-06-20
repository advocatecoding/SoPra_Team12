import React from 'react';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import "./modal.css";
import Users from '../Users';

export default function CheckProjectsModal({ setOpenModal }) {

  const openArbeitszeiten = () => {

  }

  return (
        <div className="modalContainer">
            <div className="titleCloseBtn">
          <button
            onClick={() => {
              setOpenModal(false);
            }}
          >
            X
          </button>
        </div>
        <div className="title">
        <h1>Checken Sie die Projekte!</h1>
        </div>
            <div className="body">
                <div style={{marginTop: "5rem"}}>
                <Users  style={{ minWidth: "100px", marginTop:"100px" }}></Users>
                </div>

                <div style={{marginTop: "5rem"}}>
                <Button variant="outlined" onClick={() => {openArbeitszeiten()}} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px", textAlign: "center", display:"inline", marginBottom:"0" }} >
                    Arbeitszeiten anzeigen 
                </Button>
                </div>
                
                
            </div>
        </div>
  )
}
