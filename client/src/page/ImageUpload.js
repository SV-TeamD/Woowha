import React, { useState } from "react";
import imageCompression from "browser-image-compression";
import axios from "axios";
import { Link } from "react-router-dom";
import "./ImageUpload.css";
import ImageResult from "./ImageResult";
import empty from "./img/empty_image.PNG";
import hosoda_example from "./img/hosoda_example.PNG";
import hayao_example from "./img/hayao_example.PNG";
import paprika_example from "./img/paprika_example.PNG";
import shinkai_example from "./img/shinkai_example.PNG";
import cezanne_example from "./img/Cezanne_example.png";
import monet_example from "./img/Monet_example.png";
import pelissero_example from "./img/Pelissero_example.jpg";
import vangogh_example from "./img/Vangogh_example.jpg";
import ukiyoe_example from "./img/Ukiyoe_example.png";

const ImageUpload = () => {
  const [inputImage, setInputImage] = useState(null);
  const [style, setStyle] = useState("");
  const [inputImagePreviewUrl, setInputImagePreviewUrl] = useState(empty);
  const [isDone, setIsDone] = useState(false);

  const st_img_style = {
    width: "256px",
    height: "256px",
  };

  const onStyleChange = (e) => {
    const styleinfo = e.target.value;
    setStyle(styleinfo);
  };

  const handleImageChange = async (e) => {
    e.preventDefault();
    const options = {
      maxSizeMB: 2,
      maxWidthOrHeight: 500,
    };
    let imgfile = e.target.files[0];
    setInputImage(imgfile);
    try {
      const compressedFile = await imageCompression(imgfile, options);

      setInputImage(compressedFile);
      const promise = imageCompression.getDataUrlFromFile(compressedFile);
      promise.then((result) => {
        setInputImagePreviewUrl(result);
      });
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="upload">
      <h1>Image Upload</h1>
      <div><img src={inputImagePreviewUrl} alt="image preview" /></div>
      <br />
      <br />
      <label id="file">
        <input id="file" type="file" onChange={handleImageChange} />
        Upload
      </label>
      <br />
      <br />
      <br />
      <div className="select">
        <br />
        <br />
        <div className="author">
          <img src={hayao_example} alt="empty_image" style={st_img_style} />
          <h3>Hayao</h3>
          <p>Explain</p>
          <input
            type="radio"
            name="author"
            value="cartoongan_hayao.pth"
            onChange={onStyleChange}
          />
        </div>

        <div className="author">
          <img src={shinkai_example} alt="empty_image" style={st_img_style} />
          <h3>Shinkai</h3>
          <p>Explain</p>
          <input
            type="radio"
            name="author"
            value="cartoongan_shinkai.pth"
            onChange={onStyleChange}
          />
        </div>

        <div className="author">
          <img src={hosoda_example} alt="empty_image" style={st_img_style} />
          <h3>Hosoda</h3>
          <p>Explain</p>
          <input
            type="radio"
            name="author"
            value="cartoongan_hosoda.pth"
            onChange={onStyleChange}
          />
        </div>

        <div className="author">
          <img src={paprika_example} alt="empty_image" style={st_img_style} />
          <h3>Paprika</h3>
          <p>Explain</p>
          <input
            type="radio"
            name="author"
            value="cartoongan_paprika.pth"
            onChange={onStyleChange}
          />
        </div>

        <br />
        <br />
        <br />

        <div className="author">
          <img src={monet_example} alt="empty_image" />
          <h3>Monet</h3>
          <p>Explain</p>
          <input
            type="radio"
            name="author"
            value="cyclegan_monet.pth"
            onChange={onStyleChange}
          />
        </div>

        <div className="author">
          <img src={vangogh_example} alt="empty_image" />
          <h3>VanGogh</h3>
          <p>Explain</p>
          <input
            type="radio"
            name="author"
            value="cyclegan_vangogh.pth"
            onChange={onStyleChange}
          />
        </div>

        <div className="author">
          <img src={ukiyoe_example} alt="empty_image" />
          <h3>Ukiyoe</h3>
          <p>Explain</p>
          <input
            type="radio"
            name="author"
            value="cyclegan_ukiyoe.pth"
            onChange={onStyleChange}
          />
        </div>

        <div className="author">
          <img src={pelissero_example} alt="empty_image" />
          <h3>Pelissero</h3>
          <p>Explain</p>
          <input
            type="radio"
            name="author"
            value="cartoongan2_pelissero.ckpt"
            onChange={onStyleChange}
          />
        </div>

        <br />
        <br />
        <br />
        <Link to="/resultpage" onClick={()=>{setIsDone(true)}}>
          <ImageResult inputImage={inputImage} inputStyle={style} isDone={isDone}/>
          <button className="blue_button">Convert</button>
        </Link>
      </div>
    </div>
  );
};
export default ImageUpload;
