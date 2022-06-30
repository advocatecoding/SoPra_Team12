import React, { useState, useEffect } from "react";
import { Fab, Button, Typography } from '@material-ui/core';
import './modals/modal.css'
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import PersonAddAltRoundedIcon from '@mui/icons-material/PersonAddAltRounded';
import SaveAsRoundedIcon from '@mui/icons-material/SaveAsRounded';
import CloseIcon from '@mui/icons-material/Close';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContentText from '@mui/material/DialogContentText';
import axios from 'axios';
import SuccessAlert from "./Alerts/SuccessAlert";
import "../index.css"


export default function CreateNewUser(props) {

    //const [newuser, setnewuser] = useState(null);
    const [openModal, setOpenModal] = useState(false);

    const [vorname, setVorname] = useState(null);
    const [nachname, setNachname] = useState(null);
    const [mail_adresse, setMail] = useState(null);
    const [benutzername, setBenutzername] = useState(null);
    const [successAlertOpen, setSuccessAlertOpen] = useState(false);

    function postMitarbeiter(id, urlaubstage, überstunden) {
        const url = `/zeit/personen`;
        console.log("Mitarbeiter", id, vorname, nachname,mail_adresse,benutzername)
        axios.post(url, {
          id,
          vorname,
          nachname,
          mail_adresse,
          benutzername,
          urlaubstage,
          überstunden
        })
        .then(data => console.log(" Mitarbeiter wurde gepostet", data), openAlert())
        .catch(err => console.log(err))
        
      };


    const handleClickOpen = () => {
        setOpenModal(true);
    };

    const handleClose = () => {
        setOpenModal(false);
        postMitarbeiter(999,30,0)
    };



    const changeVorname = (event) => {
        setVorname(event.target.value)
    }

    const changeNachname = (event) => {
        setNachname(event.target.value)
    }

    const changeMail = (event) => {
        setMail(event.target.value)
    }

    const changeBenutzername = (event) => {
        setBenutzername(event.target.value)
    }

    const openAlert = () => {
        setSuccessAlertOpen(true)
    }


    return (
       
        <div align="center"  >
            {successAlertOpen ?
            <div style={{position:"absolute", width:"100%", height:"100%",  left: "50%", top:"0", transform: "translate(-50%, 0)", zIndex: "999", backgroundColor:"rgba(0,0,0,0.7)"}}>
            <SuccessAlert style={{marginTop:"20% !important", width:"5rem"}} setAlertOpen={open => setSuccessAlertOpen(open)} alertmessage={"Das Anlegen eines neuen Benutzers war erfolgreich!"}></SuccessAlert>            
            </div> 
            
            : null
            }
            <Typography style={{ marginTop: "50px", color: "white" }}>Sie haben noch keinen Benutzer?</Typography>
            <Box mt={3} />
            <Fab variant="extended" onClick={() => { handleClickOpen() }} style={{ color: "white", backgroundColor: "#30343C" }}>
                <PersonAddAltRoundedIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />
                Benutzer erstellen
            </Fab>


            <Dialog open={openModal} style={{ backgroundColor: "rgba(33,37,31, 0.7)" }}
                PaperProps={{
                    style: {
                        minHeight: 390,
                        minWidth: 600,
                        maxHeight: 280,
                        borderRadius: '12px',
                    }
                }}>
                <DialogTitle className="dialog-bg" sx={{ m: 0, p: 2 }}>
                    <PersonAddAltRoundedIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />Benutzer erstellen

                    <Button startIcon={<CloseIcon />} onClick={handleClose}
                        sx={{
                            position: 'absolute',
                            right: 0,
                        }} ></Button>
                </DialogTitle>
                <DialogContent className="dialog-bg">

                    <DialogContentText
                        component="form"
                        sx={{
                            '& .MuiTextField-root': { m: 1, width: '25ch' },
                        }}
                        noValidate
                        autoComplete="off">
                        <div>
                            <TextField
                                required
                                id="filled-required"
                                label="Vorname"
                                type="text"
                                variant="standard" placeholder="Vorname"
                                onChange={changeVorname}
                            />
                            <TextField
                                required
                                id="filled-required"
                                label="Nachname"
                                type="text"
                                variant="standard" placeholder="Nachname"
                                onChange={changeNachname}
                            />
                            <TextField
                                required
                                id="filled-required"
                                label="E-Mail-Adresse"
                                type="text"
                                variant="standard" placeholder="E-Mail-Adresse"
                                onChange={changeMail}
                            />
                            <TextField
                                required
                                id="filled-required"
                                label="Benutzername"
                                type="text"
                                variant="standard" placeholder="Benutzername"
                                onChange={changeBenutzername}
                            />
                        </div>
                        <Box mt={8} />
                        <div> <Typography>Sind Ihre Eingaben korrekt? Wenn ja, dann drücken Sie auf <span style={{ color: "#00bcd4" }}>Speichern</span></Typography></div>
                        <Box mt={2} />
                        <Fab variant="extended" onClick={() => { handleClose() }} style={{ color: "white", backgroundColor: "#30343C" }} >
                            <SaveAsRoundedIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />
                            Speichern
                        </Fab>
                    </DialogContentText>
                </DialogContent>
            </Dialog>

        </div>
    );

}



