import React, { useState } from 'react';
import axios from 'axios';

function Login() {
  const [data, setData] = useState('');
  const [error, setError] = useState('')
  
  const [form, setForm] = useState({username: '', password: ''})

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('http://localhost:8000/login/', form)
      .then(response => {
        console.log(response.data)
        setData(response.data)
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('username', response.data.username);
      })
      .catch(error => setError(error));
  }
  
  const inputChange = (e)=>{
    setForm({...form, [e.target.name]: e.target.value})
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
          {localStorage.getItem('token')}
          {localStorage.getItem('username')}
          
          {form.username & form.password}

          {error}
        <input type="text" placeholder="Username" name="username" value={form.username} onChange={inputChange} />
        <input type="password" placeholder="Password" name="password" value={form.password} onChange={inputChange} />
        <button type="submit">Login</button>
      </form>
      <button onClick={()=> localStorage.removeItem('token') & localStorage.removeItem('username')}>logout</button>
  </>
  );
}

export default Login;
