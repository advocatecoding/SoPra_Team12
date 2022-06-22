import '../index.css';
import AccountTreeRoundedIcon from '@mui/icons-material/AccountTreeRounded';
import React, { useState, useEffect, useRef } from 'react';
import { CSSTransition } from 'react-transition-group';
import LoadingProgress from '../components/Loading/LoadingProgress';
import IconButton from "@material-ui/core/IconButton";
import { Button, Grid, Typography, withStyles, Box, TextField } from '@material-ui/core';
import ArticleIcon from '@mui/icons-material/Article';
import AddIcon from '@mui/icons-material/Add';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import axios from 'axios';
import Dialog from '@mui/material/Dialog';
import CloseIcon from '@mui/icons-material/Close';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import SaveAsIcon from '@mui/icons-material/SaveAs';
import DialogActions from '@mui/material/DialogActions';

export default function ProjektListe(props) {

  const [projekte, setProjekte] = useState([]);
  const [mitarbeiterProjekte, setMitarbeiterProjekte] = useState([]);


  const [projektIds, setProjektIds] = useState([]);

  const [activeMenu, setActiveMenu] = useState('main');
  const dropdownRef = useRef(null);
  const [loadingInProgress, setLoading] = useState(true);
  const [loadingError, setLoadingError] = useState(null);


  // Usestates für Post Projekt
  const [projektname, setProjektname] = useState("");
  const [auftraggeber, setAuftraggeber] = useState("");
  const [projektleiter, setProjekleiter] = useState("");
  const [ProjektErstellen, SetProjekteErstellen] = useState(false);

  



  useEffect(() => {
    // Update the document title using the browser API

    FetchProjekte(props.id)
    iDerhalten(props.id)
    /**
     * Leere Liste: [] muss übergeben werden um einen infinite Loop zu verhindern
     */
  }, [])



  async function FetchProjekte(id) {
      console.log("Perso GCKEN.")
      console.log(id, "22")
      const url = `/zeit/projekt/mitarbeiter/${id}`;
      
      console.log(url)
      try {
        const response = await fetch(url);
        const data = await response.json();
        setMitarbeiterProjekte(data)
        setLoading(false)
      } catch (e) {
         console.log(e.message)
      }
    }

   
    
    function postProjekt (id){
      const url = `/zeit/projekte`;
        axios.post(url, {
            id,
            projektname,
            auftraggeber,
            projektleiter
        }).then(data => console.log("Projekt wurde gepostet", data).catch(err => console.log(err)))
    };  






  function ListItem(props) {
    return (
      <a href="#" className="menu-item" >
        <span className="icon-button" >{props.leftIcon}</span>
        <div className="parent">
          {props.children}
        </div>
      </a>
    );
  }

  const addProject = () => {
    SetProjekteErstellen(true);
  }

  const changeProjektname = (event) => {
    setProjektname(event.target.value)
}

const iDerhalten = (id) => {
  setProjekleiter(id)
}

  const changeAuftraggeber = (event) => {
  setAuftraggeber(event.target.value)
}

  const handleCloseEmpty = (e) => {
    e.preventDefault();
    SetProjekteErstellen(false);
};

const handleClose = (e) => {
  e.preventDefault();
  SetProjekteErstellen(false);
  postProjekt(1211);
};


  return (
    <div className="dropdown" style={{ minHeight: "300px", maxHeight: "500px", overflowY: "scroll" }} ref={dropdownRef}>
      
      <CSSTransition
        in={activeMenu === 'main'}
        timeout={500}
      >
        <div className="menu" >
          <div style={{textAlign: "center", marginBottom: "1rem"}}>
              <div style={{display: "inline-block"}}>
              <Typography  variant="h5" style={{color: "white"}}>Meine Projekte</Typography> 
              </div>
              <div style={{display: "inline-block", marginLeft: "auto"}}>
              <AddCircleOutlineIcon startIcon={<ArticleIcon />} onClick={addProject}>
              </AddCircleOutlineIcon>
              </div>
            
          </div>
          {
            mitarbeiterProjekte.map((item) =>
              <ListItem
                leftIcon={
                  <div >
                       <IconButton>
                      <ArticleIcon />
                    </IconButton>
                  </div>
                }
              >
                <h3>{item.projektname} von {item.auftraggeber}</h3>
              </ListItem>
            )
          }
        </div>
      </CSSTransition>
      <LoadingProgress show={loadingInProgress}></LoadingProgress>

      <Dialog open={ProjektErstellen}
      PaperProps={{
        sx: {
          minHeight: 270,
          minWidth: 400,
          maxHeight: 280
        }
      }}>
        <DialogTitle sx={{ m: 0, p: 2 }}>Ein neues Projekt erstellen <Button startIcon={<CloseIcon />} onClick={handleCloseEmpty}
                    sx={{
                        position: 'absolute',
                        right: 0,
                        color: (theme) => theme.palette.grey[500],
                    }} ></Button>
                </DialogTitle>
                <DialogContent dividers>
                    <TextField
                        autoFocus
                        required
                        margin="dense"
                        id="projektname"
                        label="Projektname"
                        type="text"
                        fullWidth
                        variant="standard"
                        onChange={changeProjektname}
                    />
                    <TextField
                        autoFocus
                        required
                        margin="dense"
                        id="auftraggeber"
                        label="Auftraggeber"
                        type="text"
                        fullWidth
                        variant="standard"
                        onChange={changeAuftraggeber}
                    />
                </DialogContent>
                <DialogActions>
                    <Button startIcon={<SaveAsIcon />} onClick={handleClose}>Erstellen</Button>
                </DialogActions>

      </Dialog>

      




    </div>
  );
}