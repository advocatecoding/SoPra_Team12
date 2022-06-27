import React, { useState, useEffect } from "react";
import Typography from '@mui/material/Typography';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';


export default function PersonInformationen(props) {

    const [personData, setPersonData] = useState("")

    useEffect(() => {
        fetchPersonById(props.id)
    }, [props.id])


    async function fetchPersonById(id) {
        console.log("Person wird gefetcht.")
        try {
            const response = await fetch(`/zeit/personen/${id}`);
            const data = await response.json();
            setPersonData(data)
        } catch (e) {
            console.log(e.message)
        }
    }


    return (
        <div style={{display:"flex"}}>
            <AccountCircleIcon style={{ color: "#00bcd4", fontSize: "40px" }}></AccountCircleIcon>
            <Typography color="white" variant="h6" style={{paddingLeft: "1.2rem", marginTop:"-2px"}}>
                Name: {personData.vorname} {personData.nachname}
                <br/>
                Benutzername: {personData.benutzername}
            </Typography>
           
        </div>
    )
}

