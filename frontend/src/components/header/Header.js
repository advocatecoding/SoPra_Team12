import React from 'react'
import {Typography, Box, Grid} from '@material-ui/core';
import ProfileDropDown from '../Dialogs/ProfileDropdown';


function Header() {
  
  return (

    <div>
      
      <Box sx= {{mt: 2}}></Box>
      <Typography style={textColor} align='center' variant='h4'>Zeiterfassung HdM WebApp</Typography>
      <Grid container>
        
        
      
      </Grid>
      <ProfileDropDown></ProfileDropDown>
      
    </div>
  )
}

const textColor = {
	color: "white"
}



export default Header;