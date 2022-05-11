import ZeiterfassungAPI from "../api/ZeiterfassungAPI";
import * as React from 'react';
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



class PersonenList extends Component {
    constructor(props) {
        super(props)

        this.state = {
            personen: [],
        };
    }

    /**
     * Wir fetchen alle PersonenBOs von der REST-API, der durch die server.py bereitgestellt wird
    */
    getPersonenList = () => {
        console.log("SJNADFKS")
        ZeiterfassungAPI.getAPI().getPersonen()
            .then(x =>
                console.log(x)
            ).catch(e =>
                this.setState({
                    personen: [],
                }))
    }

    async componentDidMount() {
        const url = "http://localhost:5500/zeit/personen";
        const response = await fetch(url);
        //console.log(response.data)
        const data = await response.json();
        //console.log(data);
        this.setState({ personen: data });
        //console.log("dskmfd", this.state.customer[0].vorname)
        this.state.personen.map((d) => console.log(d.vorname))
        console.log("1", this.state.personen)
    }



    render() {
        const { items } = this.state;
        //const list = [1, 2, 3, 4, 5]
        return (
            <div style={{ width: "100%" }}>
                {this.state.personen.map((x) =>
                    <ListItem>
                        <IconButton>
                            <AccountCircleIcon style={{color:"#00bcd4", fontSize:"40px"}}></AccountCircleIcon>
                        </IconButton>
                        <Typography color="white" variant="h6">
                            Name: {x.vorname} {x.nachname} 
                            <br></br>
                            Benutzername: {x.benutzername}
                        </Typography>
                    </ListItem>
                )}
            </div>
        )

    }
}
export default PersonenList;