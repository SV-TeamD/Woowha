import React, { Component } from "react";
import "./mainpage.css";
import img from "./img/empty_image.PNG";
import ov_1 from "./overviewimg/ov_1.jpg";
import ol_1 from "./overlayimg/ol_1.png";
import hosoda_example from "./img/hosoda_example.PNG";
import hayao_example from "./img/hayao_example.PNG";
import paprika_example from "./img/paprika_example.PNG";
import shinkai_example from "./img/shinkai_example.PNG";
class mainpage extends Component {
  constructor(props) {
    super(props);
    this.state = { file: "", imagePreviewUrl: "", url: "" };
  }
  scrollToTop = (event) => {
    window.scrollTo(0, 0);
  };
  scrollToAbout = (event) => {
    window.scrollTo(0, 1500);
  };
  scrollToOverview = (event) => {
    window.scrollTo(0, 1250);
  };

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
  componentDidMount() {
    this.handleButton();
  }
  handleButton = () => {
    fetch("http://localhost/image/result", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => {
        res.json();
      })
      .then((data) => {
        this.setState({ url: data });
      });
  };
  render() {
    const st_img_style = {
      width: "220px",
      height: "267px",
    };
    const ov_img_style = {
      display: "block",
      width: "263px",
      height: "220px",
    };

    let { imagePreviewUrl } = this.state;
    let $imagePreview = <img src={img} />;

    if (imagePreviewUrl) {
      $imagePreview = <img src={imagePreviewUrl} />;
    }

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
        <div className="upload">
          <h2>Image Upload</h2>
          <br />
          <div className="imgPreview">{$imagePreview}</div>
          <br />
          <br />
          <form
            id="upload_form"
            action="http://localhost/image/upload"
            method="post"
            encType="multipart/form-data"
          >
            <label id="file">
              Upload
              <input
                type="file"
                name="file"
                onChange={(e) => this._handleImageChange(e)}
              />
            </label>
            <br />
            <br />
            <br />
            <div className="select">
              <br />
              <br />
              <div className="author1">
                <img
                  src={hayao_example}
                  alt="empty_image"
                  style={st_img_style}
                />
                <h3>Hayao</h3>
                <p>Explain</p>
                <label id="author">
                  <input type="radio" name="author" value="Hayao" />
                </label>
              </div>

              <div className="author2">
                <img
                  src={shinkai_example}
                  alt="empty_image"
                  style={st_img_style}
                />
                <h3>Shinkai</h3>
                <p>Explain</p>
                <label id="author">
                  <input type="radio" name="author" value="Shinkai" />
                </label>
              </div>

              <div className="author3">
                <img
                  src={paprika_example}
                  alt="empty_image"
                  style={st_img_style}
                />
                <h3>Paprika</h3>
                <p>Explain</p>
                <label id="author">
                  <input type="radio" name="author" value="Paprika" />
                </label>
              </div>

              <div className="author4">
                <img
                  src={hosoda_example}
                  alt="empty_image"
                  style={st_img_style}
                />
                <h3>Hosoda</h3>
                <p>Explain</p>
                <label id="author">
                  <input type="radio" name="author" value="Hosoda" />
                </label>
              </div>

              <br />
              <br />
              <br />
              <button type="submit">Convert</button>
            </div>
          </form>
        </div>
        <br />
        <br />
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

export default mainpage;
