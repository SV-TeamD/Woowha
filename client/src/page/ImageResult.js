import axios from "axios";
import React, { useEffect, useState } from "react";
import "./ImageResult.css";
import empty from "./img/empty_image.PNG";

const ImageResult = (props) => {
  const [filepath, setFilepath] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [origin, setOrigin] = useState("");
  useEffect(() => {
    const getimg = async () => {
      try {
        setError(null);
        setLoading(true);
        const res = await axios
          .post("http://localhost/image/result?style=" + props.inputstyle, {
            headers: {
              "Content-Type": "application/json",
              Accept: "application/json",
            },
            method: "POST",
            body: props.inputname,
          })
          .then((res) => {
            const filepath = res.data;
            setFilepath(filepath);
          }, []);
      } catch (e) {
        setError(e);
      }
      setLoading(false);
    };
    getimg();
    setOrigin("input/" + props.filename);
  }, [props.inputstyle]);

  return (
    <div className="ImageResult">
      <h1>Image Result</h1>
      {loading && <h3>로딩중</h3>}
      {error && <h3>에러</h3>}
      {props.filepath && <img src={filepath} />}
      {origin && <img src={origin} />}
    </div>
  );
};

export default ImageResult;
