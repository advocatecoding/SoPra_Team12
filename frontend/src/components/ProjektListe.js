import '../index.css';
import React, { useState, useEffect, useRef } from 'react';
import { CSSTransition } from 'react-transition-group';
import LoadingProgress from '../components/Loading/LoadingProgress';
import IconButton from "@material-ui/core/IconButton";
import { Typography } from '@material-ui/core';
import ArticleIcon from '@mui/icons-material/Article';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import ReplayIcon from '@mui/icons-material/Replay';
import SuccessAlert from './Alerts/SuccessAlert';
import CreateProjectModal from './modals/CreateProjectModal';

/**
 * Gibt die Projekte aus, die dem eingeloggten User zugewiesen sind
 * 
 * @author [Talha Yildirim](https://github.com/talha16)
 * @author [Aykut Demir](https://github.com/AykutDemirr)
*/

export default function ProjektListe(props) {

  const [mitarbeiterProjekte, setMitarbeiterProjekte] = useState([]);
  const dropdownRef = useRef(null);
  const [loadingInProgress, setLoading] = useState(true);


  const [userIdIsSet, setUserIdTrue] = useState(false);

  // Usestates für Post Projekt
  const [projektleiter, setProjekleiter] = useState("");
  const [showModal, setShowModal] = useState(false);

  const [successAlertProjektOpen, setSuccessAlertProjektOpen] = useState(false);


  useEffect(() => {
    // Update the document title using the browser API
    FetchProjekte(props.id)
    iDerhalten(props.id)
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
      //console.log("Projekte gefetcht!")
    } catch (e) {
      console.log(e.message)
    }
  }

  const reloadData = () => {
    FetchProjekte(props.id)
    props.setAlertOpen(true)
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

  const addProject = (e) => {
    e.preventDefault();
    setShowModal(true);
  }

  const iDerhalten = (id) => {
    setProjekleiter(id)
    setUserIdTrue(true)
  }

  return (
    <div>
      {successAlertProjektOpen ?
        <div style={{ position: "absolute", display: "flex", justifyContent: "center", width: "100%", height: "100%", left: "50%", top: "0", transform: "translate(-50%, 0)", zIndex: "999", backgroundColor: "rgba(0,0,0,0.7)" }}>
          <SuccessAlert setAlertOpen={open => setSuccessAlertProjektOpen(open)} alertmessage={"Das Erstellen eines neuen Projekts war erfolgreich!"}></SuccessAlert>
        </div>

        : null
      }
      <div className="dropdown" style={{ minHeight: "300px", maxHeight: "500px", overflowY: "scroll" }} ref={dropdownRef}>
        <CSSTransition
          timeout={500}
        >
          <div className="menu" >
            <div style={{ display: "flex", marginBottom: "1rem" }}>
              <div style={{ display: "inline-block" }}>
                <Typography variant="h5" style={{ color: "white", paddingLeft: "1rem" }}>Meine Projekte</Typography>
              </div>
              <div style={{ display: "flex", flexDirection: "row", marginLeft: "auto", paddingRight: "1rem" }}>
                <div>
                  <ReplayIcon id="add-project-icon" style={{ color: "#00bcd4", transform: "scale(1.3)", cursor: "pointer", paddingLeft: "1rem" }} onClick={reloadData} />
                </div>
                <div>
                  <AddCircleOutlineIcon id="add-project-icon" style={{ color: "#00bcd4", transform: "scale(1.3)", cursor: "pointer", paddingLeft: "1rem" }} onClick={addProject} />
                </div>


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

        {
          userIdIsSet ?
            <>
              <CreateProjectModal setAlertOpen={open => setSuccessAlertProjektOpen(open)} id={projektleiter} closeModal={close => setShowModal(close)} showModal={showModal}></CreateProjectModal>
            </>
            : null
        }
      </div>
    </div>

  );
}