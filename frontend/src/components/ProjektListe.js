import '../index.css';
import { ReactComponent as ArrowIcon } from '../icons/arrow.svg';
import { ReactComponent as BoltIcon } from '../icons/bolt.svg';
import AccountTreeRoundedIcon from '@mui/icons-material/AccountTreeRounded';
import React, { useState, useEffect, useRef } from 'react';
import { CSSTransition } from 'react-transition-group';
import LoadingProgress from '../components/Loading/LoadingProgress';
import IconButton from "@material-ui/core/IconButton";


export default function ProjektListe() {

    const [projekte, setProjekte] = useState([1, 2]);
    const [aktivitaeten, setAktivitaeten] = useState([])
    const [activeMenu, setActiveMenu] = useState('main');
    const [menuHeight, setMenuHeight] = useState(null);
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
      console.log("sfmgddlgdl")
      const url = "http://localhost:5500/zeit/projekte";
      try {
        //console.log(projekte)
        const response = await fetch(url);
        //console.log(response.data)
        const data = await response.json();
        //console.log(data);
        //updateProjekte(data)
        setProjekte(data)
        setLoading(false)
      } catch (e) {
        console.log(e.message)
        setLoadingError(e)
      }
      ;
    }
  
    async function fetchAktivatenByProjektId(id, idx) {
      console.log("fetched!")
      try {
        const response = await fetch(`http://localhost:5500/zeit/aktivitaten/${id}`);
        const data = await response.json();
        setAktivitaeten(data)
      } catch (e) {
        console.log(e.message)
      }
    }
  
  
    function DropdownItem(props) {
      return (
        <a href="#" className="menu-item" >
          <span className="icon-button" onClick={() => props.menu && setMenuMain(props.menu)}>{props.leftIcon}</span>
          <div className="parent">
            {props.children}
          </div>
  
        </a>
      );
    }
  
    function setMenuMain(menu) {
      setActiveMenu(menu)
      console.log(activeMenu)
    }
  
  
    return (
      <div className="dropdown" style={{maxWidth:"350px", minHeight: "300px", overflowY: "scroll" }} ref={dropdownRef}>
        {console.log(activeMenu)}
  
        <CSSTransition
          in={activeMenu === 'main'}
          timeout={500}
          classNames="menu-primary"
          unmountOnExit
        >
          <div className="menu" >
            {
              projekte.map((item, idx) =>
                  <DropdownItem
                    leftIcon={
                      <div >
                        <IconButton onClick={() => fetchAktivatenByProjektId(idx + 1) && setActiveMenu(`projekt${idx}`)}>
                          <AccountTreeRoundedIcon />
                        </IconButton>
                      </div>
                    }
                    goToMenu={`projekt${idx}`}
                    projId={idx}
                  >
                    <h3>{item.projektname} von {item.auftraggeber}</h3>
                  </DropdownItem>
              )
            }
          </div>
        </CSSTransition>
        <LoadingProgress show={loadingInProgress}></LoadingProgress>
  
        {
          projekte.map((item, idx) =>
  
            <CSSTransition
              in={activeMenu === `projekt${idx}`}
              timeout={500}
              classNames="menu-secondary"
              unmountOnExit
            >
              <div className="menu" style={{ height: menuHeight }}>
  
                <DropdownItem leftIcon={
                  <IconButton onClick={() => setMenuMain("main")}>
                    <ArrowIcon menu={"main"} style={{ color: "#00bcd4" }}></ArrowIcon>
                  </IconButton>
                } >
                  <h3 >Aktivitäten</h3>
                </DropdownItem>
  
                {
                  aktivitaeten.map((item) =>
                    <DropdownItem leftIcon={<BoltIcon />}>
                      {console.log(aktivitaeten)}
                      Aktivität: {item.aktivitaetname}
                    </DropdownItem>)
                }
              </div>
            </CSSTransition>
          )
        }
  
  
      </div>
    );
  }