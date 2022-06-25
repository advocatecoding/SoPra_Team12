import React, { Component } from 'react';
import PropTypes from 'prop-types';
import CircularProgress from '@mui/material/CircularProgress';


/**
 * Shows a loading progress, if the show prop is true.
 */
class LoadingProgress extends Component {

  /** Renders the component */
  render() {
    const { show } = this.props;

    return (
      show ?
        <div>
          < CircularProgress/>
        </div>
        : null
    );
  }
}



/** PropTypes */
LoadingProgress.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** If true, the loading progress is rendered */
  show: PropTypes.bool.isRequired,
}

export default LoadingProgress;
