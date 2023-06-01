import {useState, useEffect} from 'react'
import axios from 'axios'
function Register(){

    const [form, setForm] = useState({username: '', password: '', email: ''})
    const [error, setError] = useState('')
    const [data, setData] = useState('');

    const handleSubmit = () => {
        axios.post('http://localhost:8000/register/', form)
        .then(response => {
            console.log(response.data)
            setData(response.data)
        })
        .catch(error => setError(error));
    }

    const inputChange = (e)=>{
        setForm({...form, [e.target.name]: e.target.value})
    }

    return(
        <>
            <h1>REGİSTER</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Username" name="username" value={form.username} onChange={inputChange} />
                <input type="password" placeholder="Password" name="password" value={form.password} onChange={inputChange} />
                <input type="email" placeholder="Email" name="email" value={form.email} onChange={inputChange} />
                <button type="submit">Login</button>
            </form>
        </>
    )
}

export default Register