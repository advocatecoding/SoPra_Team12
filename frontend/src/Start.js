import React, { useState, useEffect } from "react";
import { Grid, Box } from '@material-ui/core';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import PersonInformationen from './components/PersonInformationen';
import ProjektListe from './components/ProjektListe';


const theme = createTheme({
  palette: {
    primary: {
      main: "#00bcd4",
    }, secondary: {
      main: "#151616",
    }
  },
});




function Start(props) {
  //const [open, setOpen] = React.useState(true);
  const [personData, setPersonData] = useState("");
  const [userId, setUserId] = useState(1);

  return (
    <div >
      <ThemeProvider theme={theme}>
      {/* Abstand */}
      <Box sx={{ mt: 5 }}></Box>

      
      <Grid container justify="space-between" gap={2} >
        {/* Sidebar -> Projektübersicht */}
        <Grid xs={4} style={{minWidth:"300px"}}>
           <ProjektListe></ProjektListe>        
        </Grid>

        {/* Hauptbereich */}
        <Grid xs={8} style={{ backgroundColor: "grey", borderRadius:"8px", maxWidth:"900px", height:"600px"}}>
          <Grid container style={{borderRadius:"8px"}} >
            {/* Benutzerinformation*/}
            <Grid xs={8}  style={{backgroundColor: "#842680",height:"200px", borderRadius:"8px"}}>
              <div style={{padding: "0.5rem"}}>
              <PersonInformationen id={userId}></PersonInformationen>
              </div>
              
            </Grid>
            
            {/* Stundenübersicht erstellen Button*/}
            <Grid xs={4} style={{backgroundColor: "#834534", borderRadius:"8px"}}>

            </Grid>


            {/* Buchbereich*/}
            <Grid xs={12} style={{backgroundColor: "#447F50", minHeight:"400px", borderRadius:"8px", marginTop: "2rem"}}>
                
            </Grid>
          </Grid>
        </Grid>

      </Grid>
      </ThemeProvider>
    </div>
  )
}


export default Start