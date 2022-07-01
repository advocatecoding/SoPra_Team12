import React, { useState, useEffect } from 'react';
import Alert from '@mui/material/Alert';
import Stack from '@mui/material/Stack';
import CheckIcon from '@mui/icons-material/Check';
import "../../index.css"


/**
 * Success Alert, der angezeigt wird, wenn die Eingaben eines Posts erfolgreich waren 
 * 
 * @author [Talha Yildirim](https://github.com/talha16)
*/

function SuccessAlert(props) {

  const [alertOpen, setAlertOpen] = useState(true)

  useEffect(() => {
    setAlertOpen(true)
  }, [])

  const handleChange = () => {
    props.setAlertOpen(false)
  };

  return (
    <div >
      {alertOpen ?
        <Stack spacing={2}>
          <Alert id="success-alert" onClose={ handleChange} style={{marginTop:"20% !important"}}
            icon={<CheckIcon fontSize="inherit" />} severity="success">{props.alertmessage}</Alert>
        </Stack>
        : null
      }

    </div>
  )
}
export default SuccessAlert