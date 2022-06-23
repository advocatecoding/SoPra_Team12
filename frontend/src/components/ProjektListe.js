import '../index.css';
import React, { useState, useEffect, useRef } from 'react';
import { CSSTransition } from 'react-transition-group';
import LoadingProgress from '../components/Loading/LoadingProgress';
import IconButton from "@material-ui/core/IconButton";
import { Button, Typography, TextField } from '@material-ui/core';
import Box from '@mui/material/Box';
import ArticleIcon from '@mui/icons-material/Article';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import axios from 'axios';
import Dialog from '@mui/material/Dialog';
import CloseIcon from '@mui/icons-material/Close';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import SaveAsIcon from '@mui/icons-material/SaveAs';
import DialogActions from '@mui/material/DialogActions';
import FormControl from '@mui/material/FormControl';
import InputAdornment from '@mui/material/InputAdornment';
import OutlinedInput from '@mui/material/OutlinedInput';
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';
import { v4 as uuidv4 } from 'uuid';

import CreateProjectModal from './modals/CreateProjectModal';



export default function ProjektListe(props) {

  const [mitarbeiterProjekte, setMitarbeiterProjekte] = useState([]);
  const dropdownRef = useRef(null);
  const [loadingInProgress, setLoading] = useState(true);


  // Usestates für Post Projekt
  const [projektname, setProjektname] = useState("");
  const [auftraggeber, setAuftraggeber] = useState("");
  const [projektleiter, setProjekleiter] = useState("");
  const [showModal, setShowModal] = useState(false);




  useEffect(() => {
    // Update the document title using the browser API

    //FetchProjekte(props.id)
    //iDerhalten(props.id)

    // Testzwecke
    FetchProjekte(1)
    iDerhalten(1)

    /**
     * Leere Liste: [] muss übergeben werden um einen infinite Loop zu verhindern
     */
  }, [props.id])



  async function FetchProjekte(id) {
    const url = `/zeit/projekt/mitarbeiter/${id}`;
    try {
      const response = await fetch(url);
      const data = await response.json();
      setMitarbeiterProjekte(data)
      setLoading(false)
    } catch (e) {
      console.log(e.message)
    }
  }



  function postProjekt(id) {
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

  const addProject = (e) => {
    e.preventDefault();
    setShowModal(true);
  }

  const iDerhalten = (id) => {
    setProjekleiter(id)
  }

 

 


  return (
    <div className="dropdown" style={{ minHeight: "300px", maxHeight: "500px", overflowY: "scroll" }} ref={dropdownRef}>
      <CSSTransition
        timeout={500}
      >
        <div className="menu" >
          <div style={{ display: "flex", marginBottom: "1rem" }}>
            <div style={{ display: "inline-block" }}>
              <Typography variant="h5" style={{ color: "white", paddingLeft: "1rem" }}>Meine Projekte</Typography>
            </div>
            <div style={{ display: "inline-block", marginLeft: "auto", paddingRight: "1rem" }}>
              <AddCircleOutlineIcon id="add-project-icon" style={{ color: "#00bcd4", transform: "scale(1.3)", cursor: "pointer" }} onClick={addProject}>
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

      <CreateProjectModal  setOpenModal={setShowModal} showModal={showModal}></CreateProjectModal>
    </div>
  );
}