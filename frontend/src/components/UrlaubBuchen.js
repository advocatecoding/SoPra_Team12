import React from "react";
import Button from '@mui/material/Button';
import { Fab } from '@material-ui/core';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';



export default function UrlaubBuchen(props) {



    const handleChange = () => {
        console.log("Modal is shown.")
        props.openUrlaubBuchenModal(true)
    };


    return (

        <div style={{marginTop: "2rem"}}>
            <Fab variant="extended" onClick={() => { handleChange() }} style={{ color: "white", backgroundColor: "#30343C" }}>
                <CalendarMonthIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />
                Urlaub buchen
            </Fab>
        </div>
    )
}
