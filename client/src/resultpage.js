import React, { Component } from "react";
import { Link } from "react-router-dom";
import "./resultpage.css";
import ov_1 from "./overviewimg/ov_1.jpg";
import ol_1 from "./overlayimg/ol_1.png";
import img from "./img/empty_image.PNG";
import facebook from "./img/facebookicon.PNG";
import twitter from "./img/twittericon.PNG";
import instagram from "./img/instagramicon.PNG";
import axios from "axios";

class resultpage extends Component {
  constructor(props) {
    super(props);
    this.state = { url: null };
  }

  scrollToTop = (event) => {
    window.scrollTo(0, 0);
  };
  scrollToAbout = (event) => {
    window.scrollTo(0, 1000);
  };
  scrollToOverview = (event) => {
    window.scrollTo(0, 810);
  };

  componentDidMount() {}

  render() {
    const sns_img_style = {
      marginRight: "50px",
    };
    const ov_img_style = {
      display: "block",
      width: "263px",
      height: "220px",
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

        <h2>Overveiw</h2>
        <br />

        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>
        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>
        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>
        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>
        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>
        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>
        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>

        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>

        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>

        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>

        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>

        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>

        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>

        <div className="overview">
          <img src={ov_1} alt="empty_image" style={ov_img_style} />
          <div className="overlay">
            <img className="olimg" alt="" src={ol_1} />
          </div>
        </div>

        <br />
        <br />
        <br />
        <br />

        <div className="about">
          <h2>About</h2>
          <p>Thank you!</p>
        </div>
      </div>
    );
  }
}
export default resultpage;
