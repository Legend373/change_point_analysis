import axios from "axios";

const API = "http://127.0.0.1:5000/api";

export const fetchPrices = () => axios.get(`${API}/prices`);
export const fetchEvents = () => axios.get(`${API}/events`);
export const fetchChangePoints = () => axios.get(`${API}/changepoints`);
