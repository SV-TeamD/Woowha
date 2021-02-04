import React from "react";
import OverviewImage from "./OverviewImage"
import { Container, Typography, Grid, Box } from "@material-ui/core"
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  }
}));

const Overview = () => {
  const classes = useStyles();
  return (
      <Box m="2rem">
        <Typography variant="h3" align="center" noWrap>Overview</Typography>
        <Container className={classes.cardGrid}>
              <Grid container spacing={3}>
                {[...Array(16).keys()].map((index) => {
                  return (
                    <OverviewImage key={index} index={index+1}></OverviewImage>
                  );
                })}
              </Grid>
        </Container>
      </Box>
  );
};

export default Overview;
