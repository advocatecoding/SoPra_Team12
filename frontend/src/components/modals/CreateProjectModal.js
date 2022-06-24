import '../../index.css';
import React, { useState, useEffect, useRef, useCallback } from 'react';
import { CSSTransition } from 'react-transition-group';
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
import UsersProject from '../UsersProject'
import Header from '../header/Header';


export default function CreateProjectModal(props) {

    useEffect(() => {
        setModalOpen(true)
        iDerhalten(props.id)
    }, [])


    const [mitarbeiterProjekte, setMitarbeiterProjekte] = useState([]);
    const dropdownRef = useRef(null);
    const [loadingInProgress, setLoading] = useState(true);


    // Usestates für Post Projekt
    const [projektname, setProjektname] = useState("");
    const [auftraggeber, setAuftraggeber] = useState("");
    const [projektleiter, setProjekleiter] = useState("");
    const [modalOpen, setModalOpen] = useState(true);
    const [aktivitaetenErstellen, setAktivitaetenErstellen] = useState(false);
    const [teamErstellen, setTeamErstellen] = useState(false);




    // UseStates für Mitarbeiter in Projekt
    const [mitarbeiter, setMitarbeiter] = useState("");
    // projekt entspricht hier projektId
    const [projekt, setProjektId] = useState("");

    const getSettedProjektId = useCallback((projId) => {
        setProjektId((prevData) => {
            if (prevData.includes(projId)) {
                return prevData.filter(image => image !== projId);
            }
            return prevData;
        });
    }, []);
   

    function postProjekt(id) {
        getSettedProjektId()
        console.log({ projektleiter }, "ayk projektleiter wird gesetzt")
        const url = `/zeit/projekte`;
        axios.post(url, {
            id,
            projektname,
            auftraggeber,
            projektleiter
        }).then((response) => {
            console.log(response)
            const data = response.data;
            console.log(data)
            console.log("Die ProjektId soll ab hier gespeichert werden:",  data.id)
            setProjektId(data.id)
            console.log("Projekt wurde gepostet", projekt)
        }).catch(err => { console.log(err) })
    };


    function postAktivitäten(aktivitaetname, dauer, kapazität, id) {
        getSettedProjektId()
        const projektname = projekt
        const url = `/zeit/aktivitaten`;
        axios.post(url, {
            id,
            aktivitaetname, 
            projektname, 
            dauer, 
            kapazität
        }).then((response) => {
            console.log(response)
            const data = response.data;
            console.log("Die ProjektId soll ab hier AUCH gespeichert werden:",  data.id)
        }).catch(err => { console.log(err) })
    }

    function postTeam(mitarbeiter, verkaufte_stunden) {
        getSettedProjektId();
        console.log("ProjektId in postTeam:", projekt)
        const url = `/zeit/mitarbeiter_in_projekt`;
        axios.post(url, {
            mitarbeiter,
            projekt,
            verkaufte_stunden
        }).then((response) => {
            const data = response.data
        }).catch(err => console.log(err))
    };

    const handleClose = (e) => {
        e.preventDefault();
        setModalOpen(false);
        setAktivitaetenErstellen(false);
        setTeamErstellen(false)

        {/** Post-Requests */ }
        postProjekt(1211);
        getSettedProjektId()
        teamFields.map((data) => {
            postTeam(data.mitarbeiter_id, data.verkaufte_stunden);
        }
        )
        aktivitätenFields.map((data) => {
            postAktivitäten(data.aktivitätsname, data.dauer, data.kapazität, 1211);
        })
    };

    const changeProjektname = (event) => {
        setProjektname(event.target.value)
    }
    const changeAuftraggeber = (event) => {
        setAuftraggeber(event.target.value)
    }


    const handleCloseEmpty = (e) => {
        e.preventDefault();
        setModalOpen(true);
        setaktivitätenFields([
            { id: uuidv4(), aktivitätsname: '', dauer: '', kapazität: '' },
        ])
        setTeamFields([
            { id: uuidv4(), mitarbeiter_id: '', verkaufte_stunden: '', },
        ])
        setAktivitaetenErstellen(false);
        setTeamErstellen(false);
        props.setOpenModal(false)
    };



    const showAktivitaetenErstellen = (e) => {
        e.preventDefault();
        setAktivitaetenErstellen(true)
    };

    const showTeamErstellen = (e) => {
        e.preventDefault();
        setTeamErstellen(true);
    }

    const zurück1 = (e) => {
        e.preventDefault();
        setAktivitaetenErstellen(false);
    }

    const zurück2 = (e) => {
        e.preventDefault();
        setTeamErstellen(false);
    }

    const iDerhalten = (id) => {
        setProjekleiter(id)
        setMitarbeiter(id)
        console.log({ projektleiter }, "ayk projektleiter wird gesetzt")
    }


    {/** Für dynamische Felder des Modals */ }

    const [aktivitätenFields, setaktivitätenFields] = useState([
        { id: uuidv4(), aktivitätsname: '', dauer: '', kapazität: '' },
    ]);

    const addAktivitätenFields = () => {
        setaktivitätenFields([...aktivitätenFields, { id: uuidv4(), aktivitätsname: '', dauer: '', kapazität: '' }])
        console.log(aktivitätenFields)
    }

    const removeAktivitätenFields = id => {
        console.log(id)
        if (id !== 1) {
            const values = [...aktivitätenFields];
            values.splice(values.findIndex(value => value.id === id), 1);
            setaktivitätenFields(values);
        }
    }

    const [teamFields, setTeamFields] = useState([
        { id: uuidv4(), mitarbeiter_id: '', verkaufte_stunden: '' },
    ]);

    const addTeamFields = () => {
        setTeamFields([...teamFields, { id: uuidv4(), mitarbeiter_id: '', verkaufte_stunden: '' }])
        console.log(teamFields)
    }

    const removeTeamFields = id => {
        console.log(id)
        if (id !== 1) {
            const values = [...teamFields];
            values.splice(values.findIndex(value => value.id === id), 1);
            setTeamFields(values);
        }
    }

    {/** Funktionen, die dafür sorgen, dass die Werte der Inputs sich aktualisieren */ }

    const setAktivitätInput = (id, event) => {
        const newaktivitätenFields = aktivitätenFields.map(i => {
            if (id === i.id) {
                i[event.target.name] = event.target.value
            }
            return i;
        })
        setaktivitätenFields(newaktivitätenFields);
    }


    const setTeamInput = (id, event) => {
        //console.log(event.value)
        const newTeamFields = teamFields.map(i => {
            //console.log(event.value)
            if (id === i.id) {
                try {
                    i[event.target.name] = event.target.value
                } catch (TypeError) {
                    i["mitarbeiter_id"] = event
                }

            }
            return i;
        })
        setTeamFields(newTeamFields)
        console.log(teamFields)
    }


    return (
        <div>
            <Dialog open={props.showModal}
                PaperProps={{
                    sx: {
                        minHeight: 300,
                        minWidth: 740,
                        maxHeight: 700
                    }
                }}>
                <DialogTitle sx={{ m: 0, p: 2 }}>Projekt anlegen <Button startIcon={<CloseIcon />} onClick={() => {
                    props.setOpenModal(false);
                }}
                    sx={{
                        right: 0,
                        marginLeft: "auto",
                    }} ></Button>
                </DialogTitle>
                <DialogContent dividers>
                    <Typography>Geben Sie den Namen und Auftraggeber des Projektes an.</Typography>
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
                    <Button onClick={showAktivitaetenErstellen}>Weiter</Button>

                </DialogActions>

            </Dialog>

            <Dialog open={aktivitaetenErstellen}
                PaperProps={{
                    sx: {
                        minHeight: 300,
                        minWidth: 740,
                        maxHeight: 700
                    }
                }}>
                <DialogTitle sx={{ m: 0, p: 2 }}>Projekt anlegen <Button startIcon={<CloseIcon />} onClick={handleCloseEmpty}
                    sx={{
                        right: 0,
                        marginLeft: "auto",
                    }} ></Button>
                </DialogTitle>

                <DialogContent dividers>
                    <Typography>Fügen Sie die Aktivitäten, deren Dauer und Kapazität hinzu.</Typography>

                    {/** Es werden dynamisch pro Slot 3 Felder erzeugt */}

                    {
                        aktivitätenFields.map(inputField => (

                            <Box sx={{ display: 'flex', flexWrap: 'wrap' }} key={inputField.id}>


                                <FormControl sx={{ m: 1, width: '25ch' }} variant="outlined">
                                    <Typography style={{ marginBottom: "0.5rem" }}>Aktivitätsname</Typography>
                                    <OutlinedInput
                                        name={"aktivitätsname"}
                                        value={inputField.aktivitätsname}
                                        onChange={event => setAktivitätInput(inputField.id, event)}
                                        required
                                    />
                                </FormControl>

                                <FormControl sx={{ m: 1, width: '21ch' }} variant="outlined">
                                    <Typography style={{ marginBottom: "0.5rem" }}>Dauer (Enddatum)</Typography>
                                    <OutlinedInput
                                        name={"dauer"}
                                        value={inputField.dauer}
                                        onChange={event => setAktivitätInput(inputField.id, event)}
                                        type="text"
                                        required
                                        placeholder="Format: JJJJ-MM-TT"
                                    />
                                </FormControl>

                                <FormControl sx={{ m: 1, width: '15ch' }} variant="outlined">
                                    <Typography style={{ marginBottom: "0.5rem" }}>Kapazität</Typography>
                                    <OutlinedInput
                                        name={"kapazität"}
                                        value={inputField.kapazität}
                                        required
                                        onChange={event => setAktivitätInput(inputField.id, event)}
                                        endAdornment={<InputAdornment position="end">h</InputAdornment>}
                                    />
                                </FormControl>

                                {/** Add & Remove Buttons für neue Slots */}
                                <IconButton style={{ display: "inline-block", padding: "0.5rem" }} onClick={addAktivitätenFields}>
                                    <AddCircleOutlineIcon id="add-project-icon" style={{ color: "#00bcd4", transform: "scale(1.3)", cursor: "pointer" }} />
                                </IconButton>

                                <IconButton style={{ display: "inline-block", padding: "0.5rem" }} disabled={aktivitätenFields.length === 1} onClick={() => removeAktivitätenFields(inputField.id)}>
                                    <RemoveCircleOutlineIcon id="add-project-icon" style={{ color: "#00bcd4", transform: "scale(1.3)", cursor: "pointer" }} />
                                </IconButton>
                            </Box>
                        ))
                    }



                </DialogContent>
                <DialogActions>
                    <Button onClick={zurück1} style={{ marginRight: "auto", paddingLeft: "1rem" }}>Zurück</Button>
                    <Button onClick={showTeamErstellen} style={{ paddingRight: "1rem" }}>Weiter</Button>
                </DialogActions>
            </Dialog>

            <Dialog open={teamErstellen}
                PaperProps={{
                    sx: {
                        minHeight: 300,
                        minWidth: 740,
                        maxHeight: 700
                    }
                }}>
                <DialogTitle sx={{ m: 0, p: 2 }}>Projekt anlegen <Button startIcon={<CloseIcon />} onClick={handleCloseEmpty}
                    sx={{
                        right: 0,
                        marginLeft: "auto",
                    }} ></Button>
                </DialogTitle>

                <DialogContent dividers>
                    <Typography>Weisen Sie dem zu erstellenden Projekt ein Team und deren verkaufte Stunden zu.</Typography>

                    {/** Es werden dynamisch pro Slot 3 Felder erzeugt */}

                    {
                        teamFields.map(inputField => (

                            <Box sx={{ display: 'flex', flexWrap: 'wrap' }} key={inputField.id}>

                                <Typography style={{ position: "absolute" }}>Mitarbeiter</Typography>
                                <div style={{ paddingTop: "2rem" }}>
                                    <UsersProject
                                        name={"mitarbeiter_id"}
                                        value={inputField.mitarbeiter_id}
                                        onChange={event => setTeamInput(inputField.id, event)}
                                    ></UsersProject>
                                </div>



                                <FormControl sx={{ m: 1, width: '22ch' }} variant="outlined">
                                    <Typography style={{ marginBottom: "0.5rem" }}>Verkaufte Stunden</Typography>
                                    <OutlinedInput
                                        name={"verkaufte_stunden"}
                                        value={inputField.verkaufte_stunden}
                                        onChange={event => setTeamInput(inputField.id, event)}
                                        endAdornment={<InputAdornment position="end">h</InputAdornment>}
                                    />
                                </FormControl>



                                {/** Add & Remove Buttons für neue Slots */}
                                <IconButton style={{ display: "inline-block", padding: "1rem" }} onClick={addTeamFields}>
                                    <AddCircleOutlineIcon id="add-project-icon" style={{ color: "#00bcd4", transform: "scale(1.3)", cursor: "pointer" }} />
                                </IconButton>

                                <IconButton style={{ display: "inline-block", padding: "1rem" }} disabled={teamFields.length === 1} onClick={() => removeTeamFields(inputField.id)}>
                                    <RemoveCircleOutlineIcon id="add-project-icon" style={{ color: "#00bcd4", transform: "scale(1.3)", cursor: "pointer" }} />
                                </IconButton>
                            </Box>
                        ))
                    }

                </DialogContent>
                <DialogActions>
                    <Button onClick={zurück2} style={{ marginRight: "auto", paddingLeft: "1rem" }}>Zurück</Button>
                    <Button onClick={handleClose} style={{ paddingRight: "1rem" }}>Speichern</Button>
                </DialogActions>
            </Dialog>
        </div>
    )
}
