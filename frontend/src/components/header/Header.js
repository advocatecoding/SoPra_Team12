import React from 'react'
import {Typography, Box, Grid} from '@material-ui/core';

function Header() {
  return (

    <div>
      <Box sx= {{mt: 2}}></Box>
      <Grid container>
        <Grid>
          
        </Grid>
        <Grid>
        <Typography style={textColor} align='center' variant='h4'>Zeiterfassung HdM WebApp</Typography>
        </Grid>
      
      </Grid>
      
    </div>
  )
}

const textColor = {
	color: "white"
}


export default Header;