import React from 'react'
import IconButton from '@mui/material/IconButton';
import LogoutIcon from '@mui/icons-material/Logout';
import "../index.css"

/**
 * Loggt User aus, indem es die Webapp neu lädt
 * 
 * @author [Talha Yildirim](https://github.com/talha16)
*/

export default function LogoutUser() {

    function refreshPage() {
        window.location.reload(false);
    }

    return (
        <div id="logout-user">
            <IconButton aria-label="delete" size="small" onClick={refreshPage}>
                <LogoutIcon fontSize="inherit" />
            </IconButton>
        </div>
    )
}
