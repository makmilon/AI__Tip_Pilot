import axios from 'axios';

const api = axios.create({
  baseURL: 'https://ai-tip-pilot.onrender.com',
});

export default api;
