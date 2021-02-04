import { Grid, Radio, FormControlLabel, Card, CardMedia, CardContent } from "@material-ui/core"
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

const StyleCard = ({ imageSrc, style, explain, value }) => {
  const classes = useStyles();

  return (
    <Grid item xs={6} sm={4} md={3}>
      <Card className={classes.card}>
        <CardMedia
          className={classes.cardMedia}
          image={imageSrc}
          title={style}
        />
        <CardContent className={classes.cardContent}>
            <FormControlLabel value={value} name="author" control={<Radio />} label={style}/>
        </CardContent>
      </Card>
    </Grid>
  )
}

export default StyleCard;
