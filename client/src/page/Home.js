import React, { useState } from "react";
import { useHistory } from "react-router-dom"
import imageCompression from "browser-image-compression";
import StyleCard from "./components/StyleCard";
import styleInfo from "../styleInfo";
import empty from "./img/empty_image.PNG";
import "./Home.css";
import "./components/Button.css";

const Home = () => {
  const [inputImage, setInputImage] = useState(null);
  const [style, setStyle] = useState("");
  const [inputImagePreviewUrl, setInputImagePreviewUrl] = useState(empty);
  const history = useHistory();

  const onStyleChange = (e) => {
    setStyle(e.target.value);
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
      imageCompression.getDataUrlFromFile(compressedFile).then((result) => {
        setInputImagePreviewUrl(result);
      });
    } catch (error) {
      console.log(error);
    }
  };

  const resultPageClickHandler = (e) => {
    history.push({
      pathname: "/result",
      state: {
        inputImage: inputImage,
        inputStyle: style
      }
    })
  };

  return (
    <div id="Home-wrapper">
      <h1>Convert your images to Styles of Artists!</h1>
      <h3>Image to Image transition utilizing GAN : Cartoons, Artworks, and more</h3>
      <h2>1. Upload your image(.png, .jpg, .jpeg)</h2>
      <div className="box">
        <img src={inputImagePreviewUrl} className="upload-image" htmlFor="file_upload" alt="image preview" />
      </div>
      <div>
        <input
          id="file_upload"
          name="file"
          type="file"
          onChange={handleImageChange}
        />
        <label className="blue_button" htmlFor="file_upload">
          Upload
        </label>
      </div>
      <div id="style-select-wrapper">
        <h2>2. Take your pick! Choose whatever art style you want</h2>
        {styleInfo.map((data, index) => {
          return (
            <StyleCard
              key={index}
              imageSrc={data.imageSrc}
              style={data.style}
              explain={data.explain}
              value={data.value}
              onChangeHandler={onStyleChange}
            ></StyleCard>
          );
        })}
        <br />

        <div id="convert_btn" className="blue_button" onClick={resultPageClickHandler}>
          Convert
        </div>
      </div>
    </div >
  );
};
export default Home;