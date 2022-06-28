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
    <div style={{marginTop:"20% !important"}} className="div5">
      {alertOpen ?
        <Stack sx={{ width: '25%' }} spacing={2} style={{marginTop:"20% !important"}}>
          <Alert onClose={ handleChange} style={{marginTop:"20% !important"}}
            icon={<CheckIcon fontSize="inherit" />} severity="success">{props.alertmessage}</Alert>
        </Stack>
        : null
      }

    </div>
  )
}
export default SuccessAlert