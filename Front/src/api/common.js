import axios from 'axios'

export const BASE_URL = 'http://82.202.161.81:8000/api'

export const HTTP = axios.create({
    baseURL: BASE_URL,
})

HTTP.defaults.headers.post['Content-Type'] = "multipart/form-data"

