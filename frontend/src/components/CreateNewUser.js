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




export default function CreateNewUser(props) {

    const [newuser, setnewuser] = useState(null);
    const [openModal, setOpenModal] = useState(false);
  
    const pressButton = (event) =>  {
        event.preventDefault();
        console.log("button clicked");
       
    };

    useEffect(() => {
        
    }, [])

    const handleClickOpen = () => {
        setOpenModal(true);
    };

    const handleClose = (e) => {
        e.preventDefault();
        setOpenModal(false);
    };



return (


        <div align="center">
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
                
                    <Button startIcon={<CloseIcon/>} onClick={handleClose}
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
                                />
                                <TextField
                                required
                                id="filled-required"
                                label="Nachname"
                                type="text"
                                variant="standard" placeholder="Nachname"
                                />
                                <TextField
                                required
                                id="filled-required"
                                label="E-Mail-Adresse"
                                type="text"
                                variant="standard" placeholder="E-Mail-Adresse"
                                />
                                <TextField
                                required
                                id="filled-required"
                                label="Benutzername"
                                type="text"
                                variant="standard" placeholder="Benutzername"
                                />
                                </div>
                                <Box mt={8} />
                                <div> <Typography>Sind Ihre Eingaben korrekt? Wenn ja, dann drücken Sie auf <span style={{color: "#00bcd4"}}>Speichern</span></Typography></div>
                                <Box mt={2} />
                                <Fab variant="extended" onClick={() => { handleClickOpen() }} style={{ color: "white", backgroundColor: "#30343C" }} >
                                    <SaveAsRoundedIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />
                                     Speichern
                                </Fab>
                            </DialogContentText>
                </DialogContent>
            </Dialog>

        </div>
    ); 

}