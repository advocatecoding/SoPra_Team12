import React, { useState } from "react";
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import { createTheme } from '@mui/material/styles';
import { ThemeProvider } from '@mui/material'
import { red } from '@mui/material/colors';
import createPalette from '@material-ui/core/styles/createPalette';
import { withStyles } from '@material-ui/core/styles';
import Start from './Start'

import Users from './components/Users'



const theme = createTheme({
    palette: {
        primary: {
            main: "#00bcd4",
        }, secondary: {
            main: red[500],
        }
    },
});


function Login() {
    const [usernamePar, setUsernamePar] = useState('');
    const [userIsSelected, selectUser] = useState(false);
    const username = ""


    const pressButton = (event) =>  {
        event.preventDefault();
        console.log("button clicked");
        selectUser(true);
    };


    function setSomething(x) {
        console.log(x)
    }

    return (
        
        <ThemeProvider theme={theme}>
            {
                userIsSelected ? 
                <>
                <Start></Start>
                </>
                :
                <>
            <Grid container
                spacing={0}
                direction="column"
                alignItems="center"
                justifyContent="center">
                <Typography style={{ marginTop: "50px", color: "white" }} fontSize={25}>Wählen Sie ihren Benutzer aus und drücken Sie auf weiter {usernamePar}</Typography>
                <Box mt={5} />
                <Users setUsername={user => setUsernamePar(user)} style={{ minWidth: "100px" }}></Users>
                {
                    usernamePar !== "" ?
                        <div align="center">
                            <Typography style={{ marginTop: "50px", color: "white" }} fontSize={20}>Sind Sie sicher, dass Ihr Benutzername: {usernamePar} ist?</Typography>
                            <Box mt={3} />
                            <Button variant="outlined" onClick={pressButton} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px" }} >
                                Anmelden
                            </Button>
                        </div>
                        :
                        null
                }
                <Box mt={10} />
                <Typography fontSize={20} color="white" >Sie haben noch keinen Benutzer?</Typography>
                <Box mt={3} />
                <Button variant="outlined"  style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px" }} >
                    Benutzer erstellen
                </Button>
            </Grid>
            </>
            }
        </ThemeProvider>
    );
}

export default withStyles({ withTheme: true })(Login);