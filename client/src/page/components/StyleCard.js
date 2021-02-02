const StyleCard = ({ imageSrc, style, explain, value, onChangeHandler }) => {
  const cardStyle = {
    width: "256px",
    height: "256px",
  };

  return (
    <div className="author">
      <img src={imageSrc} alt={explain} style={cardStyle} />
      <div className="radio-wrap">
        <input
          id={`radio-id-${style}`}
          type="radio"
          name="author"
          value={value}
          onChange={onChangeHandler}
        />
        <label htmlFor={`radio-id-${style}`}><h3>{style}</h3></label>
      </div>
    </div>
  )
}

export default StyleCard;