import React from 'react'
import { Button, Grid, Box } from '@material-ui/core';
import { styled, ThemeProvider, createTheme } from '@mui/material/styles';
import PropTypes from 'prop-types';
import Divider from '@mui/material/Divider';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Paper from '@mui/material/Paper';
import IconButton from '@mui/material/IconButton';
import Tooltip from '@mui/material/Tooltip';
import ArrowRight from '@mui/icons-material/ArrowRight';
import KeyboardArrowDown from '@mui/icons-material/KeyboardArrowDown';
import Home from '@mui/icons-material/Home';
import AddIcon from '@mui/icons-material/Add';
import PermMedia from '@mui/icons-material/PermMedia';
import PersonenList from './components/PersonenList'
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import ListSubheader from '@mui/material/ListSubheader';
import Collapse from '@mui/material/Collapse';
import InboxIcon from '@mui/icons-material/MoveToInbox';
import DraftsIcon from '@mui/icons-material/Drafts';
import SendIcon from '@mui/icons-material/Send';
import StarBorder from '@mui/icons-material/StarBorder';
import AccountTreeRoundedIcon from '@mui/icons-material/AccountTreeRounded';


const data = [
  { icon: <PermMedia />, label: 'Aktivität A' },
  { icon: <PermMedia />, label: 'Aktivität B' },
  { icon: <PermMedia />, label: 'Aktivität C' },
  { icon: <PermMedia />, label: 'Aktivität D' },
];


const FireNav = styled(List)({
  '& .MuiListItemButton-root': {
    paddingLeft: 24,
    paddingRight: 24,
  },
  '& .MuiListItemIcon-root': {
    minWidth: 0,
    marginRight: 16,
  },
  '& .MuiSvgIcon-root': {
    fontSize: 20,
  },
});

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));

function Start() {
  const [open, setOpen] = React.useState(true);
  
  const handleClick = () => {
    setOpen(!open);
  };
  return (
    <div >

      {/* Abstand */}
      <Box sx={{ mt: 5 }}></Box>
      <Grid container justifyContent='center'>
        <Button variant="outlined" style={{ color: "#00bcd4", borderColor: "#00bcd4", borderWidth: "2px", borderRadius: "50px" }} >
          Projekt anlegen
        </Button>
      </Grid>
      {/* Abstand */}
      <Box sx={{ mt: 5 }}></Box>

      {/* Sidebar -> Projektübersicht */}
      <Grid container spacing={2} justify="center">
        <Grid item xs={3} style={{}}>
          <List
            sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}
            component="nav"
            aria-labelledby="nested-list-subheader"
            subheader={
              <ListSubheader component="div" id="nested-list-subheader">
                Nested List Items
              </ListSubheader>
            }
          >

            <ListItemButton>
              <ListItemIcon>
              <AccountTreeRoundedIcon></AccountTreeRoundedIcon>
              </ListItemIcon>
              <ListItemText primary="Projekt 1" />
            </ListItemButton>

            <ListItemButton onClick={handleClick}>
              <ListItemIcon>
              <AccountTreeRoundedIcon></AccountTreeRoundedIcon>
              </ListItemIcon>
              <ListItemText primary="Projekt 2" />
              {open ? <ExpandLess /> : <ExpandMore />}
            </ListItemButton>

            <Collapse in={open} timeout="auto" unmountOnExit>
              <List component="div" disablePadding>
                <ListItemButton sx={{ pl: 4 }}>
                  <ListItemIcon>
                  <AccountTreeRoundedIcon></AccountTreeRoundedIcon>
                  </ListItemIcon>
                  <ListItemText primary="Aktivität A" />
                </ListItemButton>
                <ListItemButton sx={{ pl: 4 }}>
                  <ListItemIcon>
                  <AccountTreeRoundedIcon></AccountTreeRoundedIcon>
                  </ListItemIcon>
                  <ListItemText primary="Aktivität B" />
                </ListItemButton>
              </List>
            </Collapse>

            <ListItemButton onClick={handleClick}>
              <ListItemIcon>
              <AccountTreeRoundedIcon></AccountTreeRoundedIcon>
              </ListItemIcon>
              <ListItemText primary="Projekt 3" />
              {open ? <ExpandLess /> : <ExpandMore />}
            </ListItemButton>

            <Collapse in={open} timeout="auto" unmountOnExit>
              <List component="div" disablePadding>
                <ListItemButton sx={{ pl: 4 }}>
                  <ListItemIcon>
                  <AccountTreeRoundedIcon></AccountTreeRoundedIcon>
                  </ListItemIcon>
                  <ListItemText primary="Aktivität A" />
                </ListItemButton>
                <ListItemButton sx={{ pl: 4 }}>
                  <ListItemIcon>
                  <AccountTreeRoundedIcon></AccountTreeRoundedIcon>
                  </ListItemIcon>
                  <ListItemText primary="Aktivität B" />
                </ListItemButton>
              </List>
            </Collapse>
          </List>
          
        </Grid>
        <Grid item xs={1}></Grid>
        {/* Personenliste wird angezeigt */}
        <Grid item xs={8} style={{ backgroundColor: "grey", height: "900px" }}>
          <PersonenList></PersonenList>
        </Grid>
      </Grid>
    </div>
  )
}

Start.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default Start