import React, { useState, useEffect } from 'react';
import Alert from '@mui/material/Alert';
import Stack from '@mui/material/Stack';
import CheckIcon from '@mui/icons-material/Check';
import "../../index.css"



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
          <Alert onClose={ handleChange} style={{marginTop:"20% !important"}}
            icon={<CheckIcon fontSize="inherit" />} severity="success">{props.alertmessage}</Alert>
        </Stack>
        : null
      }

    </div>
  )
}
export default SuccessAlert