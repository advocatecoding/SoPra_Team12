import React, { useState, useEffect } from "react";
import { Grid, Box, Fab } from '@material-ui/core';
import TimelapseIcon from '@mui/icons-material/Timelapse';

export default function Stundenübersicht(props) {

    const [openModal, setOpenModal] = useState(false);


    const handleChange = () => {
        console.log("Modal is shown.")
        props.openCheckProjectsModal(true)
    };

    return (
        <div>
            <Fab variant="extended" onClick={() => {handleChange()}} style={{color: "white", backgroundColor:"#30343C"}} >
                <TimelapseIcon sx={{ mr: "1rem" }} style={{color: "#00bcd4"}}/>
                Stundenübersicht erzeugen
            </Fab>

        </div>
    )
}
