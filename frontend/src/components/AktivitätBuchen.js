import React from "react";
import { Fab } from '@material-ui/core';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';
import "../index.css"

/**
 * @author [Aykut Demir](https://github.com/AykutDemirr)
*/


export default function AktivitätBuchen(props) {
    


    const handleChange = () => {
        props.openAktivitätModal(true)
    };


    return (

        <div className="buttons-right" style={{marginTop: "2rem"}}>
            <Fab variant="extended" onClick={() => { handleChange() }} style={{ color: "white", backgroundColor: "#30343C" }}>
                <CalendarMonthIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />
                Aktivitäten zuweisen
            </Fab>
        </div>
    )
}
