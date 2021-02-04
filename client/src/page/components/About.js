import React from "react";
import Typography from '@material-ui/core/Typography';
import { Box } from "@material-ui/core";

const About = () => {

  return (
    <Box m="2rem">
      <Typography variant="h4" align="center" noWrap>About</Typography>
      <Typography variant="body2" color="textSecondary" align="center">
        {'Copyright © '}
          This website was created by
          <a href="https://github.com/Jivvon">Jivvon</a>,
          <a href="https://github.com/ByeongdoChoi">ByeongdoChoi</a>,
          <a href="https://github.com/genius-jo">genius-jo</a>,
          <a href="https://github.com/iSuddenly">iSuddenly</a>
          <br />
          It uses Deep Learning model CartoonGAN and CycleGAN to translate images.
          <br />
          Thank you!
          <br />
        {new Date().getFullYear()}
        {'.'}
      </Typography>
    </Box>
    );
};

export default About;
