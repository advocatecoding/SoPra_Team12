import React, { useState, useEffect } from "react";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Typography from '@mui/material/Typography';


export default function Users({onChange}) {
    const [personen, setPersonen] = useState([1, 2]);
    //const [userSelected, setUserSelected] = useState(false);


    useEffect(() => {
        fetchAllPersonen()
    }, [])

    async function fetchAllPersonen() {
        const url = "/zeit/personen";
        try {
            //console.log(personen)
            const response = await fetch(url);
            //console.log(response.data)
            const data = await response.json();
            setPersonen(data)
        } catch (e) {
            console.log(e.message)
        }
        ;
    }
    
    const handleChange =({target})=>{    
        if(typeof onChange === 'function'){
           // call the callback passing in whatever parameters you decide
           // in this simple case just sending numeric value
            //console.log("Users", target.value)
           onChange(target.value)
        }    
        
    }


    return (
        <div>
            <FormControl style={{ borderColor: "#252827", color: "#252827", backgroundColor: "transparent", borderRadius: "5px" }} sx={{ m: 1, minWidth: 200 }} >
            <InputLabel id="demo-simple-select-helper-label">Name d. Mitarbeiters</InputLabel>
                <Select style={{ color: "#252827"}}
                    onChange={handleChange}
                    color="primary"
                >
                    {personen.map((item) =>
                        <MenuItem value={item.id} style={{ color: "#00bcd4" }}>{item.vorname} {item.nachname}</MenuItem>
                    )
                    }
                </Select>
            </FormControl>
            <Typography style={{ color: "white", textAlign: "center" }} fontSize={9}>Wählen Sie Ihren Benutzernamen aus.</Typography>
        </div>
    )
}


