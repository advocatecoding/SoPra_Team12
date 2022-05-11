import React from 'react'
import { Grid, Box } from '@material-ui/core';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import PersonenList from './components/PersonenList';
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



function Start() {
  //const [open, setOpen] = React.useState(true);
  return (
    <div >
      <ThemeProvider theme={theme}>
      {/* Abstand */}
      <Box sx={{ mt: 5 }}></Box>

      {/* Sidebar -> Projektübersicht */}
      <Grid container justify="space-between" gap={2} >
        <Grid xs={4} style={{minWidth:"300px"}}>
           <ProjektListe></ProjektListe>        
        </Grid>
        {/* Personenliste wird angezeigt */}
        <Grid xs={7} style={{ backgroundColor: "grey", borderRadius:"8px", maxWidth:"900px", height:"600px"}}>
          <PersonenList></PersonenList>
        </Grid>
      </Grid>
      </ThemeProvider>
    </div>
  )
}


export default Start