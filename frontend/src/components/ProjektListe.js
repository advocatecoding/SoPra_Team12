import '../index.css';
import AccountTreeRoundedIcon from '@mui/icons-material/AccountTreeRounded';
import React, { useState, useEffect, useRef } from 'react';
import { CSSTransition } from 'react-transition-group';
import LoadingProgress from '../components/Loading/LoadingProgress';
import IconButton from "@material-ui/core/IconButton";
import { Button, Grid, Typography, withStyles, Box } from '@material-ui/core';
import ArticleIcon from '@mui/icons-material/Article';
import AddIcon from '@mui/icons-material/Add';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';

export default function ProjektListe(props) {

  const [projekte, setProjekte] = useState([]);
  const [mitarbeiterProjekte, setMitarbeiterProjekte] = useState([]);
  const [projektIds, setProjektIds] = useState([]);

  const [activeMenu, setActiveMenu] = useState('main');
  const dropdownRef = useRef(null);
  const [loadingInProgress, setLoading] = useState(true);
  const [loadingError, setLoadingError] = useState(null);
  



  useEffect(() => {
    // Update the document title using the browser API

    FetchProjekte(props.id)
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
    console.log("Open Modal")
  }

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
              <AddCircleOutlineIcon onClick={() => addProject}>
                      <ArticleIcon />
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
    </div>
  );
}