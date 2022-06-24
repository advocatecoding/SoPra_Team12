import React, { useState, useEffect } from "react";
import { Grid, Box } from '@material-ui/core';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import PersonInformationen from './components/PersonInformationen';
import ProjektListe from './components/ProjektListe';
import CheckProjects from "./components/CheckProjects";
import CheckProjectsModal from "./components/modals/CheckProjectsModal"
import Stundenübersicht from "./components/Stundenübersicht";
import UrlaubBuchen from "./components/UrlaubBuchen";
import UrlaubBuchenModal from "./components/modals/UrlaubBuchenModal";



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
  const [urlaubModalOpen, setUrlaubModalOpen] = useState (false);

  



  useEffect(() => {
    fetchPersonByUsername(props.username)
  }, [props.username])


  async function fetchPersonByUsername(username) {
    console.log("Person wird gefetcht. in Start")
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
      {console.log("user id bla bla   ", userId)}
      {checkProjects ?
        <>
          <CheckProjectsModal setOpenModal={setCheckProjects} mitarbeiter_id={userId} />
        </>
        : null
      }

      {urlaubModalOpen && <UrlaubBuchenModal setOpenModal={setUrlaubModalOpen} id={userId}></UrlaubBuchenModal>}
     
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
              <div style={{display:"flex", justifyContent:"center"}}>
                <CheckProjects openCheckProjectsModal={open => setCheckProjects(open)}></CheckProjects>

              
              </div>

            </div>
          </Grid>


          {/* Hauptbereich */}
          <Grid container lg={10} xs={12} md={8} style={{ backgroundColor: "grey", borderRadius: "8px", maxWidth: "900px", height: "600px", margin: "auto", padding: "1rem" }}>
            <Grid container style={{ borderRadius: "8px" }} >
              {/* Benutzerinformation*/}
              <Grid xs={8} style={{ backgroundColor: "#842680", height: "200px", borderRadius: "8px" }}>
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

              {/* Stundenübersicht erstellen Button*/}
              <Grid container
                justifyContent="center"
                alignItems="start" xs={4} style={{ backgroundColor: "#834534", borderRadius: "8px" }}>
                {
                  userIdIsSet ?
                    <>
                      <Stundenübersicht mitarbeiter_id={userId} />
                    </>
                    : null
                }

              </Grid>


              {/* Buchbereich*/}
              <Grid container xs={12} style={{ backgroundColor: "#447F50", minHeight: "400px", borderRadius: "8px", marginTop: "2rem" }}>
              <div style={{marginLeft: "auto", height:"20%"}}>
                <UrlaubBuchen openUrlaubBuchenModal={open => setUrlaubModalOpen(open)}></UrlaubBuchen>
              </div>
              
              <Grid style={{ backgroundColor: "yellow", height:"100%", width:"100%"}}>

              </Grid>

              

              

              </Grid>
            </Grid>
          </Grid>

        </Grid>
      </ThemeProvider>
    </div>
  )
}


export default Start