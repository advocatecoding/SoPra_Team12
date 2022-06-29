import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Button, Grid, Typography, withStyles, Box } from '@material-ui/core';

    /**
     * Wir nutzen dieselbe SignIn Datei, wie im Bankbeispiel, sodass
     sich die Nutzer über Firebase einloggen, um unser System nutzen zu können.
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
				<Box sx= {{mt: 5}}></Box>
				<Typography className={classes.root} style={textColor} align='center' >Willkommen in der Zeiterfassung HdM WebApp!</Typography>
				<Typography className={classes.root} style={textColor} align='center'>Es sieht so aus, als ob Sie noch nicht angemeldet sind.</Typography>
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