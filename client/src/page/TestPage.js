import React, { useEffect, useState } from "react";
import axios from "axios";
import Button from "@material-ui/core/Button"

const TestPage = () => {
  const [resultImage, setResultImage] = useState(null);
  const onCliekHandler = () => {
    const url = "http://127.0.0.1:8000/image/result?style=cartoongan_hayao.pth"
    const filename = "8bd7299c705c7a2c.jpg"
    axios.post(url, JSON.stringify({ filename: filename }), {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      method: "POST"
    }).then((res) => {
      console.log(res.data)
      setResultImage(res.data.url)
    })
  }

  return (<>
    <h3>TestPage</h3>
    <Button varient="contained" color="primary">
      @@ Button @@
    </Button>
    {/* <button onClick={onCliekHandler}>
    </button> */}
    {resultImage && <img src={resultImage}></img>}
  </>)
}

export default TestPage
