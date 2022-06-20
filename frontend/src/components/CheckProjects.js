import React, { useState, useEffect } from "react";
import Button from '@mui/material/Button';
import CheckProjectsModal from "./modals/CheckProjectsModal";



export default function CheckProjects(props) {

    const [openModal, setOpenModal] = useState(false);


    const handleChange = () => {
        console.log("Modal is shown.")
        props.openCheckProjectsModal(true)
    };


    return (

        <div style={{marginTop: "2rem"}}>
            <Button variant="outlined" onClick={() => {handleChange()}} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px" }} >
                Projektkontrolle durchführen
            </Button>

            



        </div>
    )
}
