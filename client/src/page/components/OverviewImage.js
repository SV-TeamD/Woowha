const OverviewImage = ({ index }) => {
  const requireOverViewImages = require.context('../overviewimg/', true, /\.(png|jpe?g)$/)
  const requireOverlayImages = require.context('../overlayimg/', true, /\.(png|jpe?g)$/)

  const overlay_img_style = {
    display: "block",
    width: "250px",
    height: "220px",
  };
  return (
    <>
      <div className="overview">
        <img src={requireOverViewImages(`./ov_${index}.jpg`).default} alt="overview image" style={overlay_img_style} />
        <div className="overlay">
          <img className="olimg" alt="overlay image" src={requireOverlayImages(`./ol_${index}.png`).default} />
        </div>
      </div>
    </>
  )
}

export default OverviewImage
