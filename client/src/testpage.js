import React, { Component } from "react";
class mainpage extends Component {
  render() {
    return (
      <>
          <form id="upload_form" action="http://localhost:5000/image/upload" method="post" encType="multipart/form-data">
            <label for="here_input_file_id" id="file_id">Upload</label>
              <input type="file" id="here_input_file_id" name="file"/>
            <div>
              <h3>Shinkai</h3>
              <label for="here_input_author_id">Shinkai</label>
              <input type="radio" id="here_input_author_id" name="author" value="Shinkai" />
            </div>

            <button type="submit">Convert</button>
          </form>
      </>
    );
  }
}

export default mainpage;
