import React from 'react'
import {Typography, Box} from '@material-ui/core';

function Header() {
  return (

    <div>
      <Box sx= {{mt: 2}}></Box>
      <Typography style={textColor} align='center' variant='h4'>Zeiterfassung HdM WebApp</Typography>
    </div>
  )
}

const textColor = {
	color: "white"
}


export default Header;