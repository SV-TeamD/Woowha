import './RPcss.css';
import img from './img/empty_image.PNG';
import facebook from './img/facebookicon.PNG';
import twitter from './img/twittericon.PNG';
import instagram from './img/instagramicon.PNG';
function App() {
  const sns_img_style ={
    marginRight: "50px"
  }
  const ov_img_style ={
    width: "80px",
    heigh: "80px",
    marginRight: "10px"
  }
  
  return (
    <div>
    <header>
      <ul>
        <li>
          <a className="active" href="#home">
            Woowha
          </a>
        </li>
        <li>
          <a href="#image">Image</a>
        </li>
        <li>
          <a href="#overview">Overveiw</a>
        </li>
        <li>
          <a href="#about">About</a>
        </li>
      </ul>
    </header>
    <div className="result">
      <h2>Image Result</h2>
      <img src={img} alt="empty_image"/> 
      <img src={img} alt="empty_image"/>
      <br/><br/>
      <button style={sns_img_style}>Save</button>
      <button>Retry</button>
      <br/><br/><br/>
    </div>
    <div className="sns">
      <br/><br/>
      <img src={twitter} alt="empty_image" style={sns_img_style}/>
      <img src={facebook} alt="empty_image" style={sns_img_style}/>
      <img src={instagram} alt="empty_image" style={sns_img_style}/>
      <br/><br/>
      <button>Convert</button>      
    </div>
    <div className="overview">
      <h2>Overveiw</h2><br/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/><br/><br/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/><br/><br/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/><br/><br/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/>
      <img src={img} alt="empty_image" style={ov_img_style}/><br/><br/>

    </div>

    <div className="about">
      <h2>About</h2>
      <p>Thank you!</p>
    </div>
    </div>
  );
}

export default App;
