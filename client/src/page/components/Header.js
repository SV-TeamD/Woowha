import React from "react";
import { AppBar, Toolbar, Grid, Typography } from '@material-ui/core'

const Header = () => {
<<<<<<< HEAD
  const scrollToTop = () => {
    window.scrollTo(0, 0);
  };
  const scrollToOverview = () => {
    window.scrollTo(0, 1600);
  };
  const scrollToAbout = () => {
    window.scrollTo(0, 1800);
  };
=======
  const scrollTo = (y) => {
    window.scrollTo(0, y);
  }
>>>>>>> eae70a9fb2352ec0dd5f1569da13d536aedf9b63

  return (
    <AppBar position="fixed">
      <Toolbar>
        <Grid container spacing={3}>
          <Grid item xs={4}>
              <a href="#image" onClick={() => scrollTo(0)}>
            <Typography variant="h5" align="center" noWrap>
                UPLOAD
            </Typography>
              </a>
          </Grid>
          <Grid item xs={4}>
            <Typography variant="h5" align="center" noWrap>
              <a href="#overview" onClick={()=>{scrollTo(1800)}}>OVERVIEW</a>
            </Typography>
          </Grid>
          <Grid item xs={4}>
            <Typography variant="h5" align="center" noWrap>
              <a href="#about" onClick={()=>{scrollTo(3000)}}>ABOUT</a>
            </Typography>
          </Grid>
        </Grid>
      </Toolbar>
    </AppBar>
  )

};

export default Header;
