import React, { useState, useEffect } from "react";
import { Grid, Fab, Button, Typography } from '@material-ui/core';
import TimelapseIcon from '@mui/icons-material/Timelapse';
import CloseIcon from '@mui/icons-material/Close';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContentText from '@mui/material/DialogContentText';
import './modals/modal.css'


export default function Stundenübersicht(props) {


    const [stundenübersicht, setStundenübersicht] = useState(null);
    const [openModal, setOpenModal] = useState(false);
    const [dataIsFetched, setDataIsFetched] = useState(false);


    useEffect(() => {
        fetchStundenübersicht(props.mitarbeiter_id)
    }, [])

    const handleClickOpen = () => {
        setOpenModal(true);
    };

    const handleClose = (e) => {
        e.preventDefault();
        setOpenModal(false);
    };


    // Stundenübersicht     
    async function fetchStundenübersicht(mitarbeiter_id) {
        console.log("Stundenübersicht wird gefetcht.")
        const url = `/zeit/persoenliche_mitarbeiteransicht/${mitarbeiter_id}`;
        try {
            const response = await fetch(url);
            const data = await response.json();
            console.log("jnnfskdfkfdkfds", data)
            setStundenübersicht(data)
            setDataIsFetched(true)
        } catch (e) {
            console.log(e.message)
        }
        ;
    }


    return (


        <div>
            <Fab variant="extended" onClick={() => { handleClickOpen() }} style={{ color: "white", backgroundColor: "#30343C" }} >
                <TimelapseIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />
                Stundenübersicht erzeugen
            </Fab>
            

            <Dialog open={openModal}
                PaperProps={{
                style: {
                  minHeight: 390,
                  minWidth: 600,
                  maxHeight: 280,
                  borderRadius: '12px',
                }
              }}>              
                <DialogTitle style={{ backgroundColor: "#ddd3d3"}}  sx={{ m: 0, p: 2 }}>Stundenübersicht
                    <Button startIcon={<CloseIcon />} onClick={handleClose}
                    sx={{
                        position: 'absolute',
                        right: 0,
                        }} ></Button>
                </DialogTitle>
                <DialogContent style={{ backgroundColor: "#ddd3d3"}}>
                    {dataIsFetched ?
                        <>
                            <DialogContentText >
                            <Grid xs={12}></Grid>
                            <Typography variant="h8"  style={{paddingLeft: "1px"}}>
                            Projekt Aktivität &nbsp; Gearbeitete_Zeit
                            <hr></hr>                     
                            </Typography>
                                {
                                    stundenübersicht.map((item) =>
                                        <Typography style={{paddingLeft: "1px"}}> {item.projekt }   {item.bezeichnung}  {item.gearbeitete_zeit}</Typography>
                                    )
                                }
                            </DialogContentText>
                        </>
                        : null
                    }
                </DialogContent>
            </Dialog>

        </div>
    );
}
