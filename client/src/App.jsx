import React,{useEffect, useState} from 'react'
import Login from './components/Auth/Login'
import Register from './components/Auth/Register'
import {useParams} from 'react-router-dom'
import axios from 'axios'


function App() {
  const { username } = useParams();
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
      <h1>Login and Registration</h1>
      {JSON.stringify(data)}

      <Login />
      <Register />

      username: {username ? "var" : "yok"}



    </div>
  )
}

export default App
