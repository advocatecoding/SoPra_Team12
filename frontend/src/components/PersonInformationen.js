import ZeiterfassungAPI from "../api/ZeiterfassungAPI";
import React, { useState, useEffect } from "react";
import { Component } from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import Divider from '@mui/material/Divider';
import ListItemText from '@mui/material/ListItemText';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import Avatar from '@mui/material/Avatar';
import Typography from '@mui/material/Typography';
import PersonDetail from "./PersonDetail";
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import CommentIcon from '@mui/icons-material/Comment';
import IconButton from '@mui/material/IconButton';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';





export default function PersonInformationen(props) {

    const [personData, setPersonData] = useState("")

    useEffect(() => {
        fetchPersonById(props.id)
    }, [])


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
        <div>
            <AccountCircleIcon style={{ color: "#00bcd4", fontSize: "40px" }}></AccountCircleIcon>
            <Typography color="white" variant="h6" style={{paddingLeft: "0.4rem"}}>
                Name: {personData.vorname} {personData.nachname}
                <br/>
                Benutzername: {personData.benutzername}
            </Typography>
           
        </div>
    )
}

