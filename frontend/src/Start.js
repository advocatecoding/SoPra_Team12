import React, { useState, useEffect } from "react";
import { Grid, Box, Typography } from '@material-ui/core';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import PersonInformationen from './components/PersonInformationen';
import ProjektListe from './components/ProjektListe';
import CheckProjects from "./components/CheckProjects";
import CheckProjectsModal from "./components/modals/CheckProjectsModal"
import Stundenübersicht from "./components/Stundenübersicht";
import UrlaubBuchen from "./components/UrlaubBuchen";
import UrlaubBuchenModal from "./components/modals/UrlaubBuchenModal";
import AktivitätBuchen from "./components/AktivitätBuchen";
import AktivitätBuchenModal from "./components/modals/AktivitätBuchenModal";
import Buchen from "./components/Buchen";
import Anwesenheit from "./components/Anwesenheit";
import SuccessAlert from "./components/Alerts/SuccessAlert";
import "./index.css"


const theme = createTheme({
  palette: {
    primary: {
      main: "#00bcd4",
    }, secondary: {
      main: "#151616",
    }
  },
});


function Start(props) {
  const [userId, setUserId] = useState("");
  const [userIdIsSet, setUserIdTrue] = useState(false);
  const [checkProjects, setCheckProjects] = useState(false);
  const [urlaubModalOpen, setUrlaubModalOpen] = useState(false);
  const [AktivitätModalOpen, setAktivitätModalOpen] = useState(false);
  const [successAlertOpen, setSuccessAlertOpen] = useState(false);
  const [successAlertBuchenOpen, setSuccessAlertBuchenOpen] = useState(false);
  const [successAlertAktivitätOpen, setSuccessAlertAktivitätOpen] = useState(false);
  const [successAlertProjekteOpen, setSuccessAlertProjekteOpen] = useState(false);
  const [successAlertAnwesenheitOpen, setSuccessAlertAnwesenheitOpen] = useState(false);

  const[errorAlertAnwesenheitOpen, setErrorAlertAnwesenheitOpen] = useState(false)
  


  useEffect(() => {
    fetchPersonByUsername(props.username)
  }, [props.username])


  async function fetchPersonByUsername(username) {
    //console.log("Person wird gefetcht. in Start")
    try {
      const response = await fetch(`/zeit/personen/${username}`);
      const data = await response.json();
      setUserId(data.id)
      console.log(data.id)
      setUserIdTrue(true)
    } catch (e) {
      console.log(e.message)
    }
  }


  return (
    <div >
      {/** Hier werden die Success Alerts geladen, falls die Posts bzw. Fetches erfolgreich ausgeführt wurden */}
      {successAlertOpen ?
        <div style={{ position: "absolute", display: "flex", justifyContent: "center", width: "100%", height: "100%", left: "50%", top: "0", transform: "translate(-50%, 0)", zIndex: "999", backgroundColor: "rgba(0,0,0,0.7)" }}>
          <SuccessAlert setAlertOpen={open => setSuccessAlertOpen(open)} alertmessage={"Das Buchen eines neuen Urlaubs war erfolgreich!"}></SuccessAlert>
        </div>

        : null
      }

      {successAlertBuchenOpen ?
        <div style={{ position: "absolute", display: "flex", justifyContent: "center", width: "100%", height: "100%", left: "50%", top: "0", transform: "translate(-50%, 0)", zIndex: "999", backgroundColor: "rgba(0,0,0,0.7)" }}>
          <SuccessAlert setAlertOpen={open => setSuccessAlertBuchenOpen(open)} alertmessage={"Das Buchen einer neuen Projektarbeit war erfolgreich!"}></SuccessAlert>
        </div>

        : null
      }

      {successAlertAktivitätOpen ?
        <div style={{ position: "absolute", display: "flex", justifyContent: "center", width: "100%", height: "100%", left: "50%", top: "0", transform: "translate(-50%, 0)", zIndex: "999", backgroundColor: "rgba(0,0,0,0.7)" }}>
          <SuccessAlert setAlertOpen={open => setSuccessAlertAktivitätOpen(open)} alertmessage={"Das Zuweisen von einer neuen Aktivität war erfolgreich!"}></SuccessAlert>
        </div>

        : null
      }

{successAlertProjekteOpen ?
        <div style={{ position: "absolute", display: "flex", justifyContent: "center", width: "100%", height: "100%", left: "50%", top: "0", transform: "translate(-50%, 0)", zIndex: "999", backgroundColor: "rgba(0,0,0,0.7)" }}>
          <SuccessAlert setAlertOpen={open => setSuccessAlertProjekteOpen(open)} alertmessage={"Das Laden der Projekte war erfolgreich!"}></SuccessAlert>
        </div>

        : null
      }

    {successAlertAnwesenheitOpen ?
        <div style={{ position: "absolute", display: "flex", justifyContent: "center", width: "100%", height: "100%", left: "50%", top: "0", transform: "translate(-50%, 0)", zIndex: "999", backgroundColor: "rgba(0,0,0,0.7)" }}>
          <SuccessAlert setAlertOpen={open => setSuccessAlertAnwesenheitOpen(open)} alertmessage={"Das Buchen Ihrer Anwesenheit war erfolgreich!"}></SuccessAlert>
        </div>
        : null
      }

      {errorAlertAnwesenheitOpen ?
        <div style={{ position: "absolute", display: "flex", justifyContent: "center", width: "100%", height: "100%", left: "50%", top: "0", transform: "translate(-50%, 0)", zIndex: "999", backgroundColor: "rgba(0,0,0,0.7)" }}>
          <SuccessAlert setAlertOpen={open => setErrorAlertAnwesenheitOpen(open)} alertmessage={"Überprüfen Sie Ihre Eingabe. Sie dürfen nicht mehr als 7.5h pro Tag buchen."}></SuccessAlert>
        </div>

        : null
      }


      {checkProjects ?
        <>
          <CheckProjectsModal setOpenModal={setCheckProjects} mitarbeiter_id={userId} />
        </>
        : null
      }
      

      {urlaubModalOpen && <UrlaubBuchenModal setAlertOpen={setSuccessAlertOpen} setOpenModal={setUrlaubModalOpen} id={userId}></UrlaubBuchenModal>}


      {AktivitätModalOpen && <AktivitätBuchenModal setAlertOpen={setSuccessAlertAktivitätOpen} setOpenModal={setAktivitätModalOpen} id={userId}></AktivitätBuchenModal>}

      <ThemeProvider theme={theme}>
        {/* Abstand */}
        <Box sx={{ mt: 5 }}></Box>
        <Grid container justify="space-between"
        id="main-grid"
        >
          {/* Sidebar -> Projektübersicht */}
          <Grid lg={3} xs={8} md={4} style={{ display: "flex", flexDirection: "column", alignItems: "center", marginLeft: "auto", marginRight: "auto", padding: "1rem" }}>
            <div >
              {
                userId !== "" ?
                  <>
                    <ProjektListe setAlertOpen={setSuccessAlertProjekteOpen} id={userId}></ProjektListe>
                  </>
                  : null
              }
              {/* Sidebar -> Projektkontrolle durchführen Button*/}
              <div style={{ display: "flex", justifyContent: "center", alignContent: "center", flexDirection: "column" }}>
                <div>
                  <CheckProjects openCheckProjectsModal={open => setCheckProjects(open)}></CheckProjects>
                </div>
                <div>
                  <AktivitätBuchen openAktivitätModal={open => setAktivitätModalOpen(open)}></AktivitätBuchen>
                </div>


              </div>

            </div>
          </Grid>


          {/* Hauptbereich */}
          <Grid container direction="row" justifyContent="space-between" alignItems="start" lg={10} xs={12} md={8} style={{ borderRadius: "14px", maxWidth: "900px", margin: "auto", padding: "1rem" }}>
            <Grid id="restbereich" container item style={{ borderRadius: "14px", height: "25%", justifyContent: "center", display: "flex", }} >
              {/* Benutzerinformation*/}
              <Grid xs={12} md={8} item container style={{ backgroundColor: "#262A2E", borderRadius: "14px", display: "flex", justifyContent: "flex-start" }}>
                <div style={{ paddingLeft: "1.5rem", paddingTop: "1.5rem" }}>
                  {
                    userIdIsSet ?
                      <>
                        <PersonInformationen id={userId}></PersonInformationen>
                      </>
                      : null
                  }
                </div>
              </Grid>

              {/* Stundenübersicht erstellen + Urlaub buchen Button*/}
              <Grid xs={12} md={4} item container direction="column" justifyContent="start" alignItems="flex-start"  >
                <Grid item container >
                  {
                    userIdIsSet ?
                      <>
                        <Stundenübersicht mitarbeiter_id={userId} />
                      </>
                      : null
                  }
                </Grid>
                <Grid item container>
                  <UrlaubBuchen openUrlaubBuchenModal={open => setUrlaubModalOpen(open)}></UrlaubBuchen>
                </Grid>
              </Grid>
            </Grid>

            {/* Buchbereich*/}
            <Grid id="buchbereich" container item xs={12} style={{ backgroundColor: "#262A2E", borderRadius: "14px", marginTop: "2rem", height: "65%" }}>

              <Grid style={{ height: "30%", width: "100%", padding: "2rem", paddingBottom: "0rem" }}>
                <Typography variant="h5" align="center" style={{ marginBottom: "2rem" }}>Buchbereich</Typography>
                <Anwesenheit setErrorAlertOpen={open => setErrorAlertAnwesenheitOpen(open)} setAlertOpen={open => setSuccessAlertAnwesenheitOpen(open)} id={userId} />
              </Grid>

              <Grid style={{ height: "70%", width: "100%", padding: "2rem", paddingTop: "5rem" }}>
                <Buchen setAlertOpen={open => setSuccessAlertBuchenOpen(open)} id={userId} />
              </Grid>
            </Grid>
          </Grid>

        </Grid>
      </ThemeProvider>
    </div >
  )
}


export default Start