import axios from "axios";
import React, { useEffect, useState } from "react";
import "./ImageResult.css";
import empty from "./img/empty_image.PNG";

const ImageResult = ({ inputImage, inputStyle }) => {
  const [inputImagePath, setInputImagePath] = useState("");
  const [outputImagePath, setOutputImagePath] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [filename, setFilename] = useState("");
  const baseInputImage = "assets/image_input/"
  const baseOutputImage = "assets/image_output/"

  useEffect(() => {
    console.log("=== useEffect ===");
    (async () => {
      try {
        const fd = new FormData();
        fd.append("file", inputImage, inputImage.name);
        fd.append("author", inputStyle);

        console.log(inputImage);
        console.log(inputStyle);
        for (var key of fd.keys()) {
          console.log(key);
        }
        for (var value of fd.values()) {
          console.log(value);
        }

        // 1. image upload
        const res1 = await axios
          .post("http://127.0.0.1:8000/image/upload", fd, {
            headers: {
              "content-type": "multipart/form-data",
            },
          })
          .then((res) => {
            console.log(res.data["filename"]);
            setFilename(res.data["filename"]);
            // setInputImagePath('assets/image_input/e26ae327a16505f6.jpg')
            setInputImagePath(baseInputImage + res.data["filename"])
            console.log(
              `filename (image/upload의 응답) : ${res.data["filename"]}`
            );
            console.log(`filename (image/upload의 응답) : ${filename}`);
          });

    } catch (e) {
      console.error(e);
      setError(e);
    } finally {
      setLoading(false);
    }})()
  }, [inputImage]);

  useEffect(() => {
    // 2. image result
    (async () => {
      console.log('filename 바뀜: ' + filename)
      if (!filename) return; // filename이 비어있으면 그냥 return
        const res2 = await axios
          .post(
            "http://127.0.0.1:8000/image/result",
            JSON.stringify({ filename: filename, style: inputStyle }),
            {
              headers: {
                "Content-Type": "application/json",
                Accept: "application/json",
              },
              method: "POST",
            }
          )
          .then((res) => {
            // setInputImagePath(baseInputImage + res.data["filename"])
            setOutputImagePath(baseOutputImage + res.data['filename']);
            console.log(`outputImagePath (image/result의 응답) : ${res.data['filename']}`)
          });

        console.log(`inputImage : ${inputImage}`);
        console.log(`outputImagePath : ${outputImagePath}`);
    })()
  }, [filename])


  return (
    <div className="ImageResult">
      <h1>Image Result</h1>
      {loading && <h3>로딩중</h3>}
      {error && <h3>에러</h3>}
      {/* 매개변수의 앞에 .이 들어가면 안 된다. 여기서 붙여주어야 한다. webpack 때문임. */}
      {inputImagePath && <img src={require('.././' + inputImagePath).default} />}
      {outputImagePath && <img src={require('.././' + outputImagePath).default} />}
    </div>
  );
};

export default ImageResult;
