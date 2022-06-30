import React, { useState, useEffect } from "react";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Typography from '@mui/material/Typography';
import "../index.css"


export default function Aktivitäten(props) {
    const [aktivitäten, setAktivitäten] = useState([1, 2]);

    const handleChange = (event) => {
        props.setAktivität(event.target.value)
    };

    useEffect(() => {
        fetchAllPersonen()
    }, [])

    async function fetchAllPersonen() {
        const url = "/zeit/aktivitaten";
        try {
            //console.log(personen)
            const response = await fetch(url);
            //console.log(response.data)
            const data = await response.json();
            setAktivitäten(data)
        } catch (e) {
            console.log(e.message)
        }
        ;
    }


    //const list1 = ["chocolate", "vanilla", "ice"]
    return (
        <div>
            <FormControl sx={{ m: 1, minWidth: 200 }} >
                <InputLabel id="demo-simple-select-autowidth-label">Aktivität</InputLabel>
                <Select
                    onChange={handleChange}
                    label="Benutzer"
                    color="primary"
                >
                    {aktivitäten.map((item) =>
                        <MenuItem value={item.aktivitaetname} style={{ color: "#00bcd4" }}>{item.aktivitaetname}</MenuItem>
                    )
                    }
                </Select>
            </FormControl>
        </div>
    )
}


