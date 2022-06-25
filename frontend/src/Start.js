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
      {checkProjects ?
        <>
          <CheckProjectsModal setOpenModal={setCheckProjects} mitarbeiter_id={userId} />
        </>
        : null
      }

      {urlaubModalOpen && <UrlaubBuchenModal setOpenModal={setUrlaubModalOpen} id={userId}></UrlaubBuchenModal>}

      {AktivitätModalOpen && <AktivitätBuchenModal setOpenModal={setAktivitätModalOpen} id={userId}></AktivitätBuchenModal>}

      <ThemeProvider theme={theme}>
        {/* Abstand */}
        <Box sx={{ mt: 5 }}></Box>


        <Grid container justify="space-between"
        >
          {/* Sidebar -> Projektübersicht */}
          <Grid lg={3} xs={8} md={4} style={{ display: "flex", flexDirection: "column", alignItems: "center", marginLeft: "auto", marginRight: "auto", padding: "1rem" }}>
            <div >
              {
                userId !== "" ?
                  <>
                    <ProjektListe id={userId}></ProjektListe>
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
          <Grid container direction="row" justifyContent="space-between" alignItems="start" lg={10} xs={12} md={8} style={{ border: "1px solid gray", borderRadius: "8px", maxWidth: "900px", height:"700px", margin: "auto", padding: "1rem" }}>
            <Grid container item style={{ borderRadius: "8px", height:"25%", justifyContent:"center", display:"flex",  }} >
              {/* Benutzerinformation*/}
              <Grid xs={8} item container  style={{ backgroundColor: "#262A2E", borderRadius: "17px", display:"flex", justifyContent: "flex-start"}}>
                <div style={{ padding: "0.5rem" }}>
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
              <Grid xs={4} item container direction="column" justifyContent="start" alignItems="flex-start"  >
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
            <Grid container  item xs={12} style={{ backgroundColor: "#262A2E", borderRadius: "17px", borderRadius: "17px", marginTop:"2rem", height:"65%" }}>
                
            <Grid style={{ height: "30%", width: "100%", padding:"2rem" }}>
                <Anwesenheit></Anwesenheit>

              </Grid>
              <Grid style={{ height: "70%", width: "100%", padding:"2rem" }}>
                <Buchen />

              </Grid>





            </Grid>

          </Grid>

        </Grid>
      </ThemeProvider>
    </div >
  )
}


export default Start