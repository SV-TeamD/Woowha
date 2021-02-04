import { Grid, Card, CardMedia } from "@material-ui/core"
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  cardGrid: {
    paddingTop: theme.spacing(8),
    paddingBottom: theme.spacing(8),
  },
  card: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
  },
  cardMedia: {
    paddingTop: '100%'
  },
  cardContent: {
    flexGrow: 1,
  },
}));

const OverviewImage = ({ index }) => {
  const requireOverViewImages = require.context('../overviewimg/', true, /\.(png|jpe?g)$/)
  const requireOverlayImages = require.context('../overlayimg/', true, /\.(png|jpe?g)$/)
  const classes = useStyles();

  return (
    <Grid item xs={4} sm={3} md={3}>
      <Card className={classes.card}>
        <CardMedia
          className={classes.cardMedia}
          image={requireOverlayImages(`./ol_${index}.png`).default}
          // image={requireOverViewImages(`./ov_${index}.jpg`).default}
        />
      </Card>
    </Grid>
  )
}

export default OverviewImage
