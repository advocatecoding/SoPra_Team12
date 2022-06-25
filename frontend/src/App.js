import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { Container } from '@material-ui/core';
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import SignIn from './SignIn';
import Header from './components/header/Header'
import Login from './Login'
import Start from './Start';

class App extends React.Component {

    #firebaseConfig = {
        apiKey: "AIzaSyCrUgCRiHcbrdWEhdm5_J1P570Ps3uaHpc",
        authDomain: "zeiterfassung-e0590.firebaseapp.com",
        projectId: "zeiterfassung-e0590",
        storageBucket: "zeiterfassung-e0590.appspot.com",
        messagingSenderId: "579508962479",
        appId: "1:579508962479:web:5a8fa311cf54b53315005a"
       };


	/** Constructor of the app, which initializes firebase  */
	constructor(props) {
		super(props);

		// Init an empty state
		this.state = {
			currentUser: null,
			appError: null,
			authError: null,
			authLoading: false
		};
	}

	/** 
	 * Create an error boundary for this app and recieve all errors from below the component tree.
 	 */
	static getDerivedStateFromError(error) {
		// Update state so the next render will show the fallback UI.
		return { appError: error };
	}

	/** Handles firebase users logged in state changes  */
	handleAuthStateChange = user => {
		if (user) {
			this.setState({
				authLoading: true
			});
			// The user is signed in
			user.getIdToken().then(token => {
				// Add the token to the browser's cookies. The server will then be
				// able to verify the token against the API.
				// SECURITY NOTE: As cookies can easily be modified, only put the
				// token (which is verified server-side) in a cookie; do not add other
				// user information.
				document.cookie = `token=${token};path=/`;

				// Set the user not before the token arrived 
				this.setState({
					currentUser: user,
					authError: null,
					authLoading: false
				});
			}).catch(e => {
				this.setState({
					authError: e,
					authLoading: false
				});
			});
		} else {
			// User has logged out, so clear the id token
			document.cookie = 'token=;path=/';

			// Set the logged out user to null
			this.setState({
				currentUser: null,
				authLoading: false
			});
		}
	}

  /** 
   * Handles the sign in request of the SignIn component uses the firebase.auth() component to sign in.
	 */
	handleSignIn = () => {
		this.setState({
			authLoading: true
		});
		const provider = new firebase.auth.GoogleAuthProvider();
		firebase.auth().signInWithRedirect(provider);
	}

	/**
	 * Lifecycle method, which is called when the component gets inserted into the browsers DOM.
	 * Initializes the firebase SDK.
	 */
	componentDidMount() {
		firebase.initializeApp(this.#firebaseConfig);
		firebase.auth().languageCode = 'en';
		firebase.auth().onAuthStateChanged(this.handleAuthStateChange);
	}



	/** Renders the whole app */
	render() {
		const { currentUser } = this.state;
		return (
          <Router basename={process.env.PUBLIC_URL}>
					<Container maxWidth='xl'>
					<Header user={currentUser}></Header>
						{
							// Ist der Benutzer schon eingeloggt -> Dann soll <Login> geladen werden
							currentUser ?
								<>
								{/** zu Testzwecken wird Login übersprungen */}
									<Login></Login>
								</>
								:
								// Wenn der Benutzer nicht eingeloggt ist -> Dann soll <SignIn> geladen werden
								<>
									<SignIn onSignIn={this.handleSignIn} />
								</>
						}
					</Container>
				</Router>
		);
	}
}

export default App;
