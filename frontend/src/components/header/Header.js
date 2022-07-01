import React, { useState, useEffect } from 'react'
import { Typography, Box, Grid } from '@material-ui/core';
import PropTypes from 'prop-types';
import ProfileDropDown from '../Dialogs/ProfileDropdown';
import Avatar from '@mui/material/Avatar';
import logo from '../../assets/logo_transparent512.png'; 
import Divider from '@mui/material/Divider';

/**
 * Der Header beinhaltet die Überschrift der WebApp, sowie das Logo und das Profil
 * des eingeloggten Googleusers
 * 
 * @author [Talha Yildirim](https://github.com/talha16)
 * @author [Dennis Kühnberger](https://github.com/Dennis-248)
*/


function Header(props) {
  const [user, setUser] = useState(null)
  useEffect(() => {
    setUser(props.user)
  }, [props.user])

  return (

    <div>

      <Box sx={{ mt: 2 }}></Box>

      <Grid container
        direction="row"
        justifyContent="space-between"
        alignItems="center">
        <Grid item >
        <Avatar alt="Logo" src={logo} />
        
        </Grid>

        <Grid item xs={8}>
          <Typography align='center' variant='h4'>Zeiterfassung HdM WebApp</Typography>
        </Grid>
        <Grid item>
          <ProfileDropDown user={user}></ProfileDropDown>
        </Grid>


      </Grid>

      <Divider style={{backgroundColor: "white", marginTop:"1rem"}}></Divider>

    </div>
  )
}

const textColor = {
  color: "white"
}
/** PropTypes */
Header.propTypes = {
  /** The logged in firesbase user */
  user: PropTypes.object,
}


export default Header;