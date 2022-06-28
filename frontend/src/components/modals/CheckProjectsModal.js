import React, { useState, useEffect } from "react";
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import "./modal.css";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import DashboardIcon from '@mui/icons-material/Dashboard';
import "../../index.css"

export default function CheckProjectsModal(props) {

  const [projectsToCheck, setProjectsToCheck] = useState([]);
  const [selectedProject, setSelectedProject] = useState(null); 

  const [createListIsClicked, setCreateListIsClicked] = useState(false);


  useEffect(() => {
    fetchProjekteToCheck(props.mitarbeiter_id)
  }, [props.mitarbeiter_id])

  // person_id eines Projektleiters
  async function fetchProjekteToCheck(person_id) {
    console.log(person_id)
    const url = `/zeit/projekt/projektleiter/${person_id}`;
    try {
      const response = await fetch(url);
      const data = await response.json();
      setProjectsToCheck(data)
    } catch (e) {
      console.log(e.message)
    }
    ;
  }

  const handleChange = (event) => {
    setSelectedProject(event.target.value);
  };

  const openArbeitszeiten = () => {
    setCreateListIsClicked(true)
  }

  return (
    <div className="modalContainer">
      <div className="titleCloseBtn">
        <button
          onClick={() => {
            props.setOpenModal(false);
          }}
        >
          X
        </button>
      </div>

      {createListIsClicked === false ?
        <>
          <div className="title">
            <h2> <DashboardIcon sx={{ mr: "1rem" }} onClick={() => { handleChange() }} style={{ color: "#00bcd4" }} />Checken Sie hier die Projekte!</h2>
          </div>
          <div className="body">
            <div style={{ marginTop: "5rem" }}>

              <FormControl style={{ borderColor: "white", color: "white", backgroundColor: "rgba(79, 79, 79, 0.61)", borderRadius: "5px" }} sx={{ m: 1, minWidth: 200 }} >
                <InputLabel style={{ color: "white" }} id="demo-simple-select-autowidth-label">Projekte</InputLabel>
                <Select style={{ color: "white" }}
                  onChange={handleChange}
                  label="Projekte"
                  color="primary"
                >
                  {projectsToCheck.map((item) =>
                    <MenuItem value={item.id} style={{ color: "#00bcd4" }}>{item.projektname}</MenuItem>
                  )
                  }
                </Select>
              </FormControl>

              <Typography style={{ color: "white", textAlign: "center" }} fontSize={9}>Wählen Sie ein Projekt zum Kontrollieren aus.</Typography>

            </div>

            <div style={{ marginTop: "5rem" }}>
              <Button variant="outlined" onClick={() => { openArbeitszeiten() }} style={{ borderWidth: "2px", borderRadius: "25px", height: "50px", minWidth: "180px", textAlign: "center", display: "inline", marginBottom: "0" }} >
                Arbeitszeiten anzeigen
              </Button>
            </div>
          </div>

        </>
        :
        <>
          <div className="title">
            <h2>Stundenübersicht des Projekts</h2>
          </div>
          <div className="body" style={{height:"100%"}}>
            <div>
              <ProjectTime projekt_id={selectedProject} />
            </div>

          </div>
        </>

      }

    </div>
  )
}



function ProjectTime(props) {

  const [dataIsOrdered, setDataIsOrdered] = useState(false);
  const [sollZeitIsAdded, setSollZeitIsAdded] = useState(false);
  const [orderedDataX, setOrderedDataX] = useState([])

  const [aktivitäten, setAktivitäten] = useState(null)
  const [rows, setRows] = useState(0)

  const [mainData, setMainData] = useState({});

  var orderedData = []


  useEffect(() => {
    fetchIstZeit(props.projekt_id)
  }, [props.projekt_id])

  async function fetchIstZeit(projekt_id) {
    const url = `/zeit/mitarbeiteransicht/${projekt_id}`;
    try {
      if (!dataIsOrdered) {
        const response = await fetch(url);
        const data = await response.json();
        orderData(data)
      }
    } catch (e) {
      console.log(e.message)
    }
    ;
  }

  async function fetchSollZeit(projekt_id) {
    const url = `/zeit/sollzeit/${projekt_id}`;
    try {
      if (!sollZeitIsAdded) {
        console.log("fetchSollZeit")
        const response = await fetch(url);
        const data = await response.json();
        addSollzeitToOrderedData(data)
      }
    } catch (e) {
      console.log(e.message)
    }
    ;
  }

  let mainDataNew = []

  const aktivitäten1 = []
  /* Algorithmus, der die Daten des Json-Objekts in 
  die benötigte Reihenfolge bringt und in ein neues Array lädt **/
  function orderData(data) {
    // Wir speichern die aktuelle Aktivität
    var cur_akt = "";
    
    console.log("Rohdaten:", data)

    for (let i = 0; i < data.length; i++) {
      // Prüfen ob 4 Werte gesetzt wurden
        var temp_obj = { akt: '', name: '', gearbeitete_zeit: '', gebuchte_stunden: '' }
        temp_obj.akt = data[i].bezeichnung
        temp_obj.name = data[i].vorname
        temp_obj.gearbeitete_zeit = data[i].gearbeitete_zeit
        //setMainData(oldArray => [...oldArray, temp_obj])
        mainDataNew.push(temp_obj)

        console.log("Temp Object:", temp_obj)
      if (cur_akt !== data[i].bezeichnung) {
        cur_akt = data[i].bezeichnung;
        aktivitäten1.push(cur_akt)
        setOrderedDataX(oldArray => [...oldArray, cur_akt])
        orderedData.push(cur_akt)
      }
      setOrderedDataX(oldArray => [...oldArray, data[i].vorname])
      setOrderedDataX(oldArray => [...oldArray, data[i].gearbeitete_zeit])
      orderedData.push(data[i].vorname)
      orderedData.push(data[i].gearbeitete_zeit)
      
      //setaktivitätenFields([...aktivitätenFields,{ aktivitätsname: '', name: '', istzeit: '', sollzeit: '' }])
    }
    
    //console.log("Main Data New: ", mainDataNew)
    
    setDataIsOrdered(true)
    fetchSollZeit(props.projekt_id)
  }


  // Regular Expression, um zu prüfen ob ein String eine Zahl ist
  let numberReg = new RegExp('[0-9]')

  /* Algorithmus, der die gefetchten Daten der Sollstunden in das georderte Array integriert  **/
  function addSollzeitToOrderedData(data) {
    var j = 0
    let countRows = 0
    console.log("-----", data)
    const loopLength = (data.length + orderedData.length)
    var temp_obj2 = {gebuchte_stunden: ""}
    for (let i = 0; i < loopLength; i++) {
      // Es wird nach jedem Element, welches eine Zahl ist die dazugehörige Sollzeit hinzugefügt 
      if ((orderedData[i]).match(numberReg)) {
        countRows ++;
        console.log("number j:", j)
        // Mit States fkt es nicht !!
        //let cur = {gebuchte_stunden: data[j].gebuchte_stunden}
        //setMainData(oldArray => [...oldArray[j], cur])

        mainDataNew[j].gebuchte_stunden = data[j].gebuchte_stunden
        
        //console.log("Gebuchte Stunde: ", data[1].gebuchte_stunden)
        orderedData.splice(i + 1, 0, data[j].gebuchte_stunden);
        console.log(orderedData)
        i++;
        console.log()
        if (j < data.length) {
          j++;
        }
      }
    }
    setOrderedDataX(orderedData)
    setSollZeitIsAdded(true)
    setAktivitäten(aktivitäten1)
    setRows(countRows)
    console.log("Zeilen:", countRows)
    console.log("AktivitätenListw:", aktivitäten1)
    console.log("Main Data finished: ", mainDataNew)
    setMainData(mainDataNew)
  }

  var x = 1
  var cur_aktivität = ""

  return (
    <div>
      {/*console.log("Ordered data beim Rendern:", orderedDataX)*/}
      {/*console.log("AktivitätenListe", aktivitäten1)*/}
            {
              aktivitäten !== null && sollZeitIsAdded ?
                aktivitäten.map((item) => 
                  <div>
                    {/*console.log(aktivitäten)*/}
                    {/*console.log(orderedDataX)*/}
                    {/*console.log("Main Data mit Index:", mainData[0][0])*/}

                    {(mainData.length > 0) ?
                    console.log("daknflksdds", mainData)
                    : null
                    }
                    {console.log("Main Data:", mainData)}
                    
                    <Typography align="left" variant="h6" style={{paddingBottom:"1rem"}}>{cur_aktivität = item}</Typography>

                    <table class="table table-striped" style={{marginBottom:"2rem"}}>
                      <thead>
                        <tr>
                          <th style={{ color: "#00bcd4", fontSize:"1rem" }}><b>Name</b></th>
                          <th style={{ color: "#00bcd4", fontSize:"1rem" }}><b>Ist-Zeit</b></th>
                          <th style={{ color: "#00bcd4", fontSize:"1rem" }}><b>Soll-Zeit</b></th>
                        </tr>
                      </thead>
                      <tbody>
                        {/* Es müssen pro Durchgang 3 Zeilen erstellt werden */}
                        {
                          (mainData.length > 0) ?
                          mainData.map((item, index) => 
                              item.akt === cur_aktivität ?
                              <tr>
                                <td align="start" style={{fontSize:"1rem"}}>{item.name}</td>
                                <td align="start" style={{fontSize:"1rem"}}>{item.gearbeitete_zeit}</td>
                                <td align="start" style={{fontSize:"1rem"}}>{item.gebuchte_stunden}</td>
                              </tr>
                              : null
                          )
                          :  null
                        }
                      </tbody>
                    </table>
                  </div>

                
                )
                : null
            }
    </div>
  )
}
