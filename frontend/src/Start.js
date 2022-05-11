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
      <Grid container justify="space-between">
        <Grid item xs={4}>
           <ProjektListe></ProjektListe>        
        </Grid>

        {/* Personenliste wird angezeigt */}
        <Grid item xs={8} style={{ backgroundColor: "#262A2E", borderRadius:"8px", height:"600px"}}>
          <PersonenList></PersonenList>
        </Grid>
      </Grid>
      </ThemeProvider>
    </div>
  )
}


export default Start