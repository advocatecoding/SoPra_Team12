import React from "react";
import { Fab } from '@material-ui/core';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';

/**
 * @author [Dennis Kühnberger](https://github.com/Dennis-248)
 * @author [Aykut Demir](https://github.com/AykutDemirr)
*/

export default function UrlaubBuchen(props) {



    const handleChange = () => {
        props.openUrlaubBuchenModal(true)
    };


    return (

        <div className="buttons-right" style={{marginTop: "2rem", marginLeft: "auto"}}>
            <Fab variant="extended" onClick={() => { handleChange() }} style={{ color: "white", backgroundColor: "#30343C" }}>
                <CalendarMonthIcon sx={{ mr: "1rem" }} style={{ color: "#00bcd4" }} />
                Urlaub buchen
            </Fab>
        </div>
    )
}
