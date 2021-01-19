import React, { Component } from "react";
import "./mainpage.css";
import img from "./img/empty_image.PNG";
class mainpage extends Component {
  constructor(props) {
    super(props);
    this.state = { file: "", imagePreviewUrl: "" };
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

    let { imagePreviewUrl } = this.state;
    let $imagePreview = <img src={img} />;
    if (imagePreviewUrl) {
      $imagePreview = <img src={imagePreviewUrl} />;
    }

    return (
      <div>
        <br />
        <br />
        <header>
          <ul>
            <li>
              <a classNamde="active" href="#home">
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
          <br />
          <br />
          <div>
            <div className="imgPreview">{$imagePreview}</div>
            <br />
            <br />
            <form action="image_route.py" method="post">
              <label id="upload_file">
                <input
                  type="file"
                  onChange={(e) => this._handleImageChange(e)}
                />
                Upload
              </label>
            </form>
          </div>
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
