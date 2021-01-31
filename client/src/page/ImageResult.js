import axios from "axios";
import React, { useEffect, useState } from "react";
import "./ImageResult.css";
import empty from "./img/empty_image.PNG";

const ImageResult = (props) => {
  const [filepath, setFilepath] = useState(null);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [origin, setOrigin] = useState("");

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
  setOrigin("input/" + props.filename);
  console.log(origin);
  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러</div>;

  let $imageResult = <img src={empty} alt="" />;
  let $origin = <img src={empty} alt="" />;
  if (filepath) {
    $imageResult = <img src={filepath} alt="" />;
    $origin = <img src={origin} alt="" />;
  }
  return (
    <div className="ImageResult">
      <h1>Image Result</h1>
      <div>{$origin}</div>
      <div>{$imageResult}</div>
    </div>
  );
};

export default ImageResult;
