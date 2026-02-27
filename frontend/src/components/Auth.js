import React, { useState } from 'react';
import api from '../api';

function Auth({ setIsAdmin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [token, setToken] = useState('');

  const handleLogin = async () => {
    try {
      const form = new FormData();
      form.append('username', username);
      form.append('password', password);
      const res = await api.post('/admin/token', form);
      setToken(res.data.access_token);
      setIsAdmin(true);
      localStorage.setItem('admin_token', res.data.access_token);
    } catch {
      alert('Invalid credentials');
    }
  };

  return (
    <div>
      {!token ? (
        <div className="flex gap-2">
          <input type="text" placeholder="Admin Username" value={username} onChange={e => setUsername(e.target.value)} className="border p-1 rounded" />
          <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} className="border p-1 rounded" />
          <button onClick={handleLogin} className="bg-green-600 text-white px-3 py-1 rounded">Login</button>
        </div>
      ) : (
        <span className="text-green-700 font-semibold">Admin</span>
      )}
    </div>
  );
}

export default Auth;
