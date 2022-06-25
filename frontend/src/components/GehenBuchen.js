import React from "react";
import Button from '@mui/material/Button';
import { Fab } from '@material-ui/core';
import MoreTimeIcon from '@mui/icons-material/MoreTime';



export default function GehenBuchen(props) {


/** Falls Modal noch genutz werden muss?  */
    const handleChange = () => {
        console.log("Modal is shown.")
        props.openGehen(true)
    };


    return (

        <div style={{marginTop: "2rem"}}>
            <Fab variant="extended" onClick={() => { handleChange() }} style={{ color: "white", backgroundColor: "#30343C" }}>
                <MoreTimeIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />
                Gehen buchen 
            </Fab>
        </div>
    )
}
