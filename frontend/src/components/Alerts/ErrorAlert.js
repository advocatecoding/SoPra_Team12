import React, { useState, useEffect } from 'react';
import Alert from '@mui/material/Alert';
import Stack from '@mui/material/Stack';
import ErrorOutlineIcon from '@mui/icons-material/ErrorOutline';
import "../../index.css"


function ErrorAlert(props) {

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
          <Alert id="error-alert" onClose={handleChange} style={{marginTop:"20% !important"}}
            icon={<ErrorOutlineIcon id="error-icon" fontSize="inherit" />} severity="error">{props.alertmessage}</Alert>
        </Stack>
        : null
      }

    </div>
  )
}
export default ErrorAlert