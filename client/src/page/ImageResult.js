import axios from "axios";
import React, { useEffect, useState } from "react";
import "./ImageResult.css";
import empty from "./img/empty_image.PNG";
const ImageResult = (props) => {
  const [filepath, setFilepath] = useState(null);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getimg = async () => {
      try {
        setError(null);
        setLoading(true);
        const res = await axios
          .post("http://localhost/image/result?style=" + props.style, {
            headers: {
              "Content-Type": "application/json",
              Accept: "application/json",
            },
            method: "POST",
            body: props.filename,
          })
          .then((res) => {
            console.log(res.data);
            setFilepath(res.data);
          });
      } catch (e) {
        setError(e);
      }
      setLoading(false);
    };
    getimg();
  }, []);
  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러</div>;

  let $imageResult = <img src={empty} alt="" />;
  if (filepath) {
    $imageResult = <img src={filepath} alt="" />;
  }
  return (
    <div className="ImageResult">
      <div>{$imageResult}</div>
      <h1>Image Result</h1>
    </div>
  );
};

export default ImageResult;
