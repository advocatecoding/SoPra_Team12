import React, { useState, useEffect } from "react";
import { Fab, Button, Typography } from '@material-ui/core';
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
                sx: {
                  minHeight: 370,
                  minWidth: 600,
                  maxHeight: 280,
                }
                
              }} >
                
                <DialogTitle sx={{ m: 0, p: 2 }}>Stundenübersicht
                    <Button startIcon={<CloseIcon />} onClick={handleClose}
                         sx={{
                            position: 'absolute',
                            right: 8,
                            top: 8,
                            color: (theme) => theme.palette.grey[500],
                          }} ></Button>
                </DialogTitle>
                <DialogContent>
                    {dataIsFetched ?
                        <>
                            <DialogContentText >
                                {
                                    stundenübersicht.map((item) =>
                                        <Typography>{item.projekt} {item.bezeichnung} {item.gearbeitete_zeit}</Typography>
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
