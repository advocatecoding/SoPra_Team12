import React, { useState, useEffect } from "react";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Typography from '@mui/material/Typography';


export default function Users(props) {
    const [personen, setPersonen] = useState([1, 2]);
    const [userSelected, setUserSelected] = useState(false);


    const handleChange = (event) => {
        props.setUsername(event.target.value)
    };

    useEffect(() => {
        fetchAllPersonen()
    }, [])

    async function fetchAllPersonen() {
        const url = "https://learned-surge-353408.ey.r.appspot.com/zeit/personen";
        try {
            //console.log(personen)
            const response = await fetch(url);
            //console.log(response.data)
            const data = await response.json();
            console.log("fetched Personen!")
            setPersonen(data)
        } catch (e) {
            console.log(e.message)
        }
        ;
    }


    //const list1 = ["chocolate", "vanilla", "ice"]
    return (
        <div>
            <FormControl style={{ borderColor: "white", color: "white", backgroundColor: "gray", borderRadius: "5px" }} sx={{ m: 1, minWidth: 200 }} >
                <InputLabel style={{ color: "white" }} id="demo-simple-select-autowidth-label">Username</InputLabel>
                <Select
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
        </div>
    )
}


