import React, { useEffect, useState } from "react";
import imageCompression from "browser-image-compression";
import { Link } from "react-router-dom";
import StyleCard from "./components/StyleCard";
import "./ImageUpload.css";
import ImageResult from "./ImageResult";
import styleInfo from "../styleInfo";
import empty from "./img/empty_image.PNG";

const ImageUpload = () => {
  const [inputImage, setInputImage] = useState(null);
  const [style, setStyle] = useState("");
  const [inputImagePreviewUrl, setInputImagePreviewUrl] = useState(empty);
  const [isDone, setIsDone] = useState(false);

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
    setIsDone(true);
  };

  return (
    <div className="upload">
      <h1>Image Upload</h1>
      <div>
        <img src={inputImagePreviewUrl} alt="image preview" />
      </div>
      <label className="blue_button" htmlFor="file_upload">
        <input
          id="file_upload"
          name="file"
          type="file"
          onChange={handleImageChange}
        />
        Upload
      </label>
      <div id="style-select-wrapper">
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
        <button className="blue_button" onClick={resultPageClickHandler}>
          click
        </button>
        <div>
          {isDone && <ImageResult inputImage={inputImage} inputStyle={style} />}
        </div>
      </div>
    </div>
  );
};
export default ImageUpload;
