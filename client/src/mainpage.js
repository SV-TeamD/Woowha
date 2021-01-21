import React, { Component } from "react";
import "./mainpage.css";
import img from "./img/empty_image.PNG";

class mainpage extends Component {
  render() {
    const st_img_style = {
      width: "220px",
      height: "267px",
      marginRight: "40px",
    };
    const ov_img_style = {
      width: "80px",
      heigh: "80px",
      marginRight: "10px",
    };
    return (
      <div>
        <br />
        <br />
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
        <div className="upload">
          <h2>Image Upload</h2>
          <img src={img} alt="empty_image" /> <br />
          <br />
          <br />
          <button>Upload</button>
          <br />
          <br />
          <br />
          <br />
        </div>
        <div className="select">
          <br />
          <br />
          <img src={img} alt="empty_image" style={st_img_style} />
          <img src={img} alt="empty_image" style={st_img_style} />
          <img src={img} alt="empty_image" style={st_img_style} />
          <img src={img} alt="empty_image" style={st_img_style} />
          <br />
          <br />
          <button>Convert</button>
        </div>
        <div className="overview">
          <h2>Overveiw</h2>
          <br />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <br />
          <br />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <br />
          <br />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <br />
          <br />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <img src={img} alt="empty_image" style={ov_img_style} />
          <br />
          <br />
        </div>

        <div className="about">
          <h2>About</h2>
          <p>Thank you!</p>
        </div>
      </div>
    );
  }
}

export default mainpage;
