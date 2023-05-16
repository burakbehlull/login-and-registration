import React,{useEffect, useState} from 'react'
import Login from './components/Auth/Login'
import axios from 'axios'
import './main.scss'


function App() {
  const [data, setData] = useState([])
  useEffect(()=>{
    const getFunc = async () =>{
      const getData = await axios.get('http://localhost:8000')
      setData(getData.data)
    }
    getFunc()
  })
  
  return (
    <div className="App">
      <h1>BLOG</h1>
      {JSON.stringify(data)}

      <Login />

    </div>
  )
}

export default App
