import React, { Component } from "react";
import { Link } from "react-router-dom";
import "./resultpage.css";
import img from "./img/empty_image.PNG";
import facebook from "./img/facebookicon.PNG";
import twitter from "./img/twittericon.PNG";
import instagram from "./img/instagramicon.PNG";

class resultpage extends Component {
  scrollToTop = (event) => {
    window.scrollTo(0, 0);
  };
  scrollToAbout = (event) => {
    window.scrollTo(0, 1000);
  };
  scrollToOverview = (event) => {
    window.scrollTo(0, 810);
  };
  componentDidMount() {
    fetch("http://locahost:5000/image/result/filename?style=Hayao")
      .then((response) => response.json())
      .then((response) => this.setState({ users: response }));
  }

  _handleImageChange(e) {
    e.preventDefault();

    let reader = new FileReader();
    let file = e.target.files[0];

    reader.onloadend = () => {
      this.setState({
        file: file,
        imagePreviewUrl: reader.result,
      });
    };

    reader.readAsDataURL(file);
  }

  render() {
    const sns_img_style = {
      marginRight: "50px",
    };
    const ov_img_style = {
      width: "200px",
      heigh: "200px",
      marginRight: "10px",
    };

    return (
      <div>
        <br />
        <br />
        <header className="head">
          <ul>
            <li>
              <a href="/">Woowha</a>
            </li>
            <li>
              <a href="#image" onClick={this.scrollToTop}>
                Image
              </a>
            </li>
            <li>
              <a href="#overview" onClick={this.scrollToOverview}>
                Overveiw
              </a>
            </li>
            <li>
              <a href="#about" onClick={this.scrollToAbout}>
                About
              </a>
            </li>
          </ul>
        </header>
        <div className="result">
          <h2>Image Result</h2>
          <img src={img} style={sns_img_style} alt="empty_image" />
          <img src={img} style={sns_img_style} alt="empty_image" />
          <br />
          <br />
          <button style={sns_img_style}>Save</button>
          <Link to="/">
            <button>Retry</button>
          </Link>
          <br />
          <br />
          <br />
        </div>
        <div className="sns">
          <br />
          <br />
          <img src={twitter} alt="empty_image" style={sns_img_style} />
          <img src={facebook} alt="empty_image" style={sns_img_style} />
          <img src={instagram} alt="empty_image" style={sns_img_style} />
          <br />
          <br />
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
export default resultpage;
