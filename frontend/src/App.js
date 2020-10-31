import React, {useState} from 'react';
import axios from 'axios';

import logo from './logo.svg';
import './App.css';

function App() {

  const [url, setUrl] = useState(null);
  const [result, setResult] = useState(null);
  const [blackbear, setBlackbear] = useState(0);
  const [grizzlybear, setGrizzly] = useState(0);
  const [teddybear, setTeddy] = useState(0);
  const [viewres, setViewres] = useState(0);
  const [bear, setBear] = useState(null);

  async function sendLink() {
    const result = await axios({
      method: 'post',
      url: 'http://localhost:5000/api/url/bear',
      data: {
      url: url
      }
    });

    setResult(result.data);
    console.log(result);

    var res = result.data['prediction'];

    setBlackbear(res[1]);
    setGrizzly(res[2]);
    setTeddy(res[3]);
    setViewres(1);
    setBear(res[0]);
  }

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Enter a URL!
        </p>



        <form onSubmit={(e) => { e.preventDefault(); sendLink()}}>
          <input type="url" onChange={(e) => { e.preventDefault(); setUrl(e.target.value)}}></input>
          <input type="submit"></input>
        </form>
        <ImagePreview url ={url} />
        <ViewResults
            viewres = {viewres}
            bear = {bear}
            blackbear={blackbear}
            grizzlybear={grizzlybear}
            teddybear={teddybear}
        />
      </header>
    </div>
  );
}

// Component to display the results when user input is send to the model.
const ViewResults = ({viewres,bear,blackbear,grizzlybear,teddybear}) => {
  if (!viewres) return null;
  return (
    <>
    <h4>Results!</h4>
      <p>
        You are a {bear} bear!
      </p>
      <h6>
      Black Bear: {blackbear}
      </h6>
      <h6>
      Grizzly Bear: {grizzlybear}
      </h6>
      <h6>
      Teddy Bear: {teddybear}
      </h6>
    </>
  )
}

// Component that returns the preview of the given image
const ImagePreview = ({url}) => {
  if (!url)
    return null;

  // renders an error gif when an invalid image link is pasted
  const default_URL = "https://media0.giphy.com/media/eNdTUcTWKL7O0UvonE/giphy.gif"
  return (
    <div className = "img-preview" >
      <img src = {url} onError = {(e)=>{e.target.src = default_URL }} height="150px" width="150px" />
    </div>
  )
}
export default App;
