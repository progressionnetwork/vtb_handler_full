import {HTTP} from './common'

// eslint-disable-next-line no-unused-vars
function createHTTP(url) {
    return {
        async post(config) {
            return HTTP.post(`${url}`, config).then(response => {
                console.log(response)
                return response.data
            })
        },
        async get(id) {
            return HTTP.get(`${url}${id}/`)
        },
        async patch(element) {
            console.log(element)
            return HTTP.patch(`${url}${element.id}/`, element).then(response => {
                console.log(response)
                return response.data
            })
        },
        async delete(id) {
            HTTP.delete(`${url}${id}/`)
            return id
        },
        async list(queryParams = '') {
            return HTTP.get(`${url}${queryParams}`).then(response => {
                return response.data
            })
        }
    }
}

export const Files = createHTTP('/processed-files/')

export const MyProfile = {
    async get() {
        return HTTP.get(`/auth/users/me/`)
    },
}

export const CreateUser = {
    async post(config) {
        return HTTP.post('/auth/users/', config).then(response =>{
            // console.log(response)
            return response.data
        })
    }
}
export const ApiKeyCheck = {
    async post(config) {
        return HTTP.post('/api_key_check/', config).then(response =>{
            // console.log(response)
            return response.status
        })
    }
}
export const ApiKeyChange = {
    async post(config) {
        return HTTP.post('/api_key_change/', config).then(response =>{
            // console.log(response)
            return response.status
        })
    }
}

export const ResetPasswordEmail = {
    async post(config) {
        return HTTP.post('/auth/users/reset_password/', config).then(response =>{
            // console.log(response)
            return response.status
        })
    }
}
export const ResetPasswordEmailConfirmation = {
    async post(config) {
        return HTTP.post('/auth/users/reset_password_confirm/', config).then(response =>{
            // console.log(response)
            return response.status
        })
    }
}

export const Auth = {
    async post(config) {
        return HTTP.post(`/auth/jwt/create/`, config).then(response => {
            // console.log(response)
            return response.data
        })
    },
}
export const Activation = {
    async post(config) {
        return HTTP.post(`/auth/users/activation/`, config).then(response => {
            // console.log(response)
            return response.data
        })
    },
}
export const ResendActivationEmail = {
    async post(config) {
        return HTTP.post(`/auth/users/resend_activation/`, config).then(response => {
            // console.log(response)
            return response.data
        })
    },
}
export const VerifyToken = {
    async post(config) {
        return HTTP.post(`/auth/jwt/verify`, config).then(response => {
            // console.log(response)
            return response.status
        })
    },
}

