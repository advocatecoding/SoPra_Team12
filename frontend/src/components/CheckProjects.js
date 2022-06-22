import React, { useState, useEffect } from "react";
import { Fab } from '@material-ui/core';
import DashboardIcon from '@mui/icons-material/Dashboard';


export default function CheckProjects(props) {

    const [openModal, setOpenModal] = useState(false);


    const handleChange = () => {
        console.log("Modal is shown.")
        props.openCheckProjectsModal(true)
    };


    return (

        <div style={{marginTop: "2rem"}}>
             <Fab variant="extended" onClick={() => {handleChange()}} style={{color: "white", backgroundColor:"#30343C"}}>
                <DashboardIcon sx={{ mr: "1rem" }}  onClick={() => {handleChange()}} style={{color: "#00bcd4"}} />
                Projektkontrolle durchführen
            </Fab>
         
        </div>
    )
}
