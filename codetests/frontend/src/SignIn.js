import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Button, Grid, Typography, withStyles, Box } from '@material-ui/core';
import { cyan } from "@mui/material/colors";
import { createTheme } from '@mui/material/styles';


/** 
 * Renders a landing page for users who are not signed in. Provides a sign in button 
 * for using an existing google account to sign in. The component uses firebase to 
 * do redirect based signin process.
 * 
 * @see See Googles [firebase authentication](https://firebase.google.com/docs/web/setup)
 * @see See Googles [firebase API reference](https://firebase.google.com/docs/reference/js)
 * 
 */


class SignIn extends Component {

	/** 
	 * Handles the click event of the sign in button an calls the prop onSignIn handler
	 */
	handleSignInButtonClicked = () => {
		this.props.onSignIn();
	}

	/** Renders the sign in page, if user objext is null */
	render() {
		const { classes } = this.props;

		return (
			<div>
				<Typography className={classes.root} style={textColor} align='center' variant='h6'>Welcome to the HdM React/Python Project Showcase</Typography>
				<Typography className={classes.root} style={textColor} align='center'>It appears, that you are not signed in.</Typography>
				<Box sx= {{mt: 5}}></Box>
				<Typography className={classes.root} style={{color: "#00bcd4"}} align='center'>Um die HdMWebapp zu nutzen, müssen Sie sich</Typography>
				<Box sx= {{mt: 2}}></Box>
				<Grid container justifyContent='center'>
					<Grid item>
					<Button variant="outlined" style={{color: "#00bcd4", borderColor: "#00bcd4", borderWidth:"2px", borderRadius:"50px"}} onClick={this.handleSignInButtonClicked}>
						Mit Google anmelden
					</Button>
					</Grid>
				</Grid>
			</div>
		);
	}
}


const textColor = {
	color: "white"
}

/** Component specific styles */
const styles = theme => ({
	root: {
		margin: theme.spacing(2)
	}
});

/** PropTypes */
SignIn.propTypes = {
	/** @ignore */
	classes: PropTypes.object.isRequired,
	/** 
	 * Handler function, which is called if the user wants to sign in.
	 */
	onSignIn: PropTypes.func.isRequired,
}

export default withStyles(styles)(SignIn)