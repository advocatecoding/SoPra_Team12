import '../index.css';
import AccountTreeRoundedIcon from '@mui/icons-material/AccountTreeRounded';
import React, { useState, useEffect, useRef } from 'react';
import { CSSTransition } from 'react-transition-group';
import LoadingProgress from '../components/Loading/LoadingProgress';
import IconButton from "@material-ui/core/IconButton";
import { Button, Grid, Typography, withStyles, Box } from '@material-ui/core';
import ArticleIcon from '@mui/icons-material/Article';

export default function ProjektListe() {

  const [projekte, setProjekte] = useState([1, 2]);
  const [projektIds, setProjektIds] = useState([]);

  const [activeMenu, setActiveMenu] = useState('main');
  const dropdownRef = useRef(null);
  const [loadingInProgress, setLoading] = useState(true);
  const [loadingError, setLoadingError] = useState(null);
  



  useEffect(() => {
    // Update the document title using the browser API
    fetchAllProjekte()
    /**
     * Leere Liste: [] muss übergeben werden um einen infinite Loop zu verhindern
     */
  }, []);

  async function fetchAllProjekte() {
    const url = "/zeit/projekte";
    try {
      const response = await fetch(url);
      const data = await response.json();
      setProjekte(data)
      setLoading(false)
    } catch (e) {
      setLoadingError(e)
    }
    ;
  }


  // Es werden
  async function fetchAssignedProjekte(person_id) {
    const url = `/zeit/mitarbeiter_in_projekt/${person_id}`;
    try {
      const response = await fetch(url);
      const data = await response.json();
      setProjekte(data)
      setLoading(false)
    } catch (e) {
      setLoadingError(e)
    }
    ;
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


  // Szenario 5 - Projektkontrolle
  // Projektleiter sieht was die Mitarbeiter im jeweiligen Projekt gemacht haben
  function checkProject() {
    console.log("Projektinformationen werden angezeigt")
  }

  function setMenuMain(menu) {
    setActiveMenu(menu)
    //console.log(activeMenu)
  }


  return (
    <div className="dropdown" style={{ maxWidth: "350px", minHeight: "300px", maxHeight: "500px", overflowY: "scroll" }} ref={dropdownRef}>

      <CSSTransition
        in={activeMenu === 'main'}
        timeout={500}
        classNames="menu-primary"
        unmountOnExit
      >
        <div className="menu" >
          <div style={{textAlign: "center", marginBottom: "1rem"}}>
          <Typography  variant="h5" style={{color: "white"}}>Meine Projekte</Typography>  
          </div>
          
          
          {
            projekte.map((item, idx) =>
              <ListItem
                leftIcon={
                  <div >
                       <IconButton onClick={() => checkProject()}>
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