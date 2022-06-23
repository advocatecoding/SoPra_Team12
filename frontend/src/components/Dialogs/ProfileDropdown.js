import React, { Component, createRef } from 'react';
import PropTypes from 'prop-types';
import { Popover, IconButton, Avatar, ClickAwayListener, Typography, Paper, Button, Grid, Divider } from '@mui/material';
import { getAuth, signOut } from "firebase/auth";


class ProfileDropDown extends Component {

  // a refernce to the avatar button
  #avatarButtonRef = createRef();

  constructor(props) {
    super(props);

    // Init the state
    this.state = {
      open: false,
    }
  }

  handleAvatarButtonClick = () => {
    this.setState({
      open: !this.state.open
    });
  }

  handleClose = () => {
    this.setState({
      open: false
    });
  }


  handleSignOutButtonClicked = () => {
    const auth = getAuth();
    signOut(auth);
  }

  render() {
    const { user } = this.props;
    const { open } = this.state;

    return (
      user ?
        <div>
          <IconButton sx={{ float: 'right' }} ref={this.#avatarButtonRef} onClick={this.handleAvatarButtonClick}>
            <Avatar src={user.photoURL} />
          </IconButton>

          <Popover open={open} anchorEl={this.#avatarButtonRef.current} onClose={this.handleClose}
            anchorOrigin={{
              vertical: 'top',
              horizontal: 'left',
            }}
            transformOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}>
            <ClickAwayListener onClickAway={this.handleClose}>
              <Paper sx={{ padding: 1, bgcolor: 'background.default' }}>
                <Typography align='center'>Hello</Typography>
                <Divider sx={{ margin: 1 }} />
                <Typography align='center' variant='body2'>{user.displayName}</Typography>
                <Typography align='center' variant='body2'>{user.email}</Typography>
                <Divider sx={{ margin: 1 }} />
                <Grid container justifyContent='center'>
                  <Grid item>
                    <Button color='primary' onClick={this.handleSignOutButtonClicked}>Logout</Button>
                  </Grid>
                </Grid>
              </Paper>
            </ClickAwayListener>
          </Popover>
        </div>
        : null
    )
  }
}

/** PropTypes */
ProfileDropDown.propTypes = {
  /** The logged in firesbase user */
  user: PropTypes.object,
}

export default ProfileDropDown;
