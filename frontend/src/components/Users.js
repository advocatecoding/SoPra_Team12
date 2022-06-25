import React, { useState, useEffect } from "react";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Typography from '@mui/material/Typography';
import LoadingProgress from "./Loading/LoadingProgress";
import "../index.css"

export default function Users(props) {
    const [personen, setPersonen] = useState([1, 2]);
    const [loadingInProgress, setLoadingInProgress] = useState(true);



    const handleChange = (event) => {
        props.setUsername(event.target.value)
    };

    useEffect(() => {
        fetchAllPersonen()
    }, [loadingInProgress])

    async function fetchAllPersonen() {
        const url = "/zeit/personen";
        try {
            //console.log(personen)
            const response = await fetch(url);
            //console.log(response.data)
            const data = await response.json();
            console.log("fetched Personen!")
            setPersonen(data)
            setLoadingInProgress(false)
        } catch (e) {
            console.log(e.message)
        }
        ;
    }


    return (
        <div>
            {
                loadingInProgress ?
                    <>
                        <LoadingProgress show={loadingInProgress}></LoadingProgress>
                    </>
                    :
                    <>
                        <FormControl style={{ borderColor: "white", color: "white", borderRadius: "5px" }} sx={{ m: 1, minWidth: 200 }} >
                            <InputLabel style={{ color: "white" }} id="demo-simple-select-autowidth-label">Username</InputLabel>

                            <Select style={{ color: "white" }}
                                onChange={handleChange}
                                label="Benutzer"
                                color="primary"
                            >
                                {personen.map((item) =>
                                    <MenuItem value={item.benutzername} style={{ color: "#00bcd4" }}>{item.benutzername}</MenuItem>
                                )
                                }
                            </Select>
                        </FormControl>
                        <Typography style={{ color: "white", textAlign: "center" }} fontSize={9}>Wählen Sie Ihren Benutzernamen aus.</Typography>
                    </>
            }



        </div>
    )
}


