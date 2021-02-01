import axios from "axios";
import React, { useEffect, useState } from "react";
import "./ImageResult.css";
import empty from "./img/empty_image.PNG";

const ImageResult = ({ inputImage, inputStyle }) => {
  const [filepath, setFilepath] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [origin, setOrigin] = useState("");
  const [filename, setFilename] = useState("");

  useEffect(() => {
    console.log("=== useEffect ===");

    const getFilename = async () => {
      const fd = new FormData();
      fd.append("file", inputImage);
      fd.append("author", inputStyle);
      console.log(inputImage);
      console.log(inputStyle);
      for (var key of fd.keys()) {
        console.log(key);
      }
      for (var value of fd.values()) {
        console.log(value);
      }

      const res = await axios
        .post("http://127.0.0.1:8000/image/upload", fd, {
          headers: {
            "content-type": "multipart/form-data",
          },
        })
        .then((res) => {
          console.log("call getFilename");
          setFilename(res.data.filename);
        });
    };

    const getimg = async () => {
      try {
        const result = await axios
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
            console.log("call getimg");
            console.log("res.data: ", res.data);
            setFilepath(res.data);
          });
      } catch (e) {
        setError(e);
      } finally {
        setLoading(false);
      }
    };

    try {
      getFilename().then((res) => {
        getimg();
      });
      setOrigin("input/" + inputImage);
      console.log(inputImage);
      console.log(origin);
    } catch (e) {
      setError(e);
    } finally {
      setLoading(false);
    }
  }, []);

  return (
    <div className="ImageResult">
      <h1>Image Result</h1>
      {loading && <h3>로딩중</h3>}
      {error && <h3>에러</h3>}
      {filepath && <img src={filepath} />}
      {origin && <img src={origin} />}
    </div>
  );
};

export default ImageResult;
