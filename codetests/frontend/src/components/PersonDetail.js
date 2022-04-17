import React, { Component } from 'react';
import PropTypes from 'prop-types';
import ZeiterfassungAPI from '../api/ZeiterfassungAPI';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';


class PersonDetail extends Component {
    constructor(props) {
        super(props);

        this.state = {
            customer: null
        }
    }

    /**
     * Wir fragen genau eine Person ab
     */
    getPerson = () => {
        ZeiterfassungAPI.getAPI().getPerson()
    }


    render() {
        return(
            <Paper variant="outlined" className={paperStyle}>
                <Typography variant="h4">
                    Person: {this.props.vorname}, {this.props.nachname}
                </Typography>
            </Paper>
        )
    }
}

const paperStyle =  {
    width: "100%",
    backgroundColor: "#252827"
}

export default PersonDetail;