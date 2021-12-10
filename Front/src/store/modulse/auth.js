import {
    Auth, VerifyToken, CreateUser
} from '@/api/elements'
import {
    AUTH,
    AUTH_ERROR,
    LOG_OUT,
    TOKEN_VERIFY,
    ACTIVATION,
    ACTIVATION_ERROR,
    SET_USER,
    PATCH_USER,
    CREATE_USER,
    CREATE_USER_ERROR,
    TOKEN_VERIFY_ERROR,
    RESET_PASSWORD_EMAIL,
    RESET_PASSWORD_EMAIL_ERROR,
    RESET_PASSWORD_EMAIL_CONFIRMATION,
    RESET_PASSWORD_EMAIL_CONFIRMATION_ERROR,
} from '../mutation-types'
import {HTTP} from "@/api/common";
import {
    Activation, MyProfile, ResendActivationEmail, ResetPasswordEmail, ResetPasswordEmailConfirmation
} from "../../api/elements";

// Геттеры
export default {
    state: {
        token: '',
        user: {},
        is_auth: false,
        errors: {
            createUserError: '',
            authError: '',
            verifyError: '',
            apiKeyError: '',
            resetPasswordEmailError: '',
            resetPasswordEmailConfirmationError: '',
            activationError: '',
            apiKeyChangeError: ''
        },
    },
    getters: {
        getAuth(state) {
            return state
        },
    },
// Мутации
    mutations: {
        [CREATE_USER](state, user) {
            this.state.user = user
            state.errors.createUserError = ''
        },
        [CREATE_USER_ERROR](state, err) {
            state.errors.createUserError = err
        },
        [SET_USER](state, user) {
            state.is_auth = true
            state.user = user
        },
        [PATCH_USER](state, user) {
            state.user = user
        },
        [AUTH](state, token) {
            localStorage.setItem('token', token)
            HTTP.defaults.headers.common['Authorization'] = 'JWT ' + token
            state.token = token
            state.errors.authError = ''
        },
        [AUTH_ERROR](state, err) {
            localStorage.setItem('token', '')
            state.token = ''
            state.errors.authError = err
        },
        [TOKEN_VERIFY](state) {
            state.errors.verifyError = ''
            state.is_auth = true
            HTTP.defaults.headers.common['Authorization'] = localStorage.getItem('token')
            state.token = localStorage.getItem('token')
        },
        [TOKEN_VERIFY_ERROR](state, err) {
            state.errors.verifyError = err
            state.token = ''
            localStorage.setItem('token', '')
        },
        [ACTIVATION](state) {
            state.errors.activationError = ''
        },
        [ACTIVATION_ERROR](state, err) {
            state.errors.activationError = err
        },
        [RESET_PASSWORD_EMAIL](state) {
            state.errors.resetPasswordEmailError = ''
        },
        [RESET_PASSWORD_EMAIL_ERROR](state, err) {
            state.errors.resetPasswordEmailError = err
        },
        [RESET_PASSWORD_EMAIL_CONFIRMATION](state, new_password) {
            state.errors.resetPasswordEmailConfirmationError = ''
            localStorage.setItem('password', new_password)
        },
        [RESET_PASSWORD_EMAIL_CONFIRMATION_ERROR](state, err) {
            state.errors.resetPasswordEmailConfirmationError = err
        },
        [LOG_OUT](state) {
            HTTP.defaults.headers.common['Authorization'] = ''
            localStorage.setItem('token', '')
            state.token = ''
            state.user = {}
            state.is_auth = false
            state.errors = {
                createUserError: '',
                authError: '',
                verifyError: '',
                apiKeyError: '',
                resetPasswordEmailError: '',
                resetPasswordEmailConfirmationError: '',
                apiKeyChangeError: '',
                activationError: '',
            }
        },
    },
// Действия
    actions: {
        async authorization({commit}, authData) {
            await Auth.post(authData).then(resp => {
                commit(AUTH, resp['access'])
            }).catch(err => {
                commit(AUTH_ERROR, err)
            })
        },
        async activation({commit}, activationData) {
            await Activation.post(activationData).then(resp => {
                console.log(activationData)
                commit(ACTIVATION, resp)
            }).catch(err => {
                commit(ACTIVATION_ERROR, err)
            })
        },
        async verifyToken({commit}, authData) {
            await VerifyToken.post(authData).then(resp => {
                commit(TOKEN_VERIFY, resp)
            }).catch(err => {
                commit(TOKEN_VERIFY_ERROR, err)
            })
        },
        async logout({commit}) {
            commit(LOG_OUT)
        },
        async createUser({commit}, userData) {
            await CreateUser.post(userData).then(user => {
                commit(CREATE_USER, user)
            }).catch(err => {
                commit(CREATE_USER_ERROR, err)
            })
        },
        async setUser({commit}) {
            await MyProfile.get().then(user => {
                commit(SET_USER, user.data)
            })
        },
        async resetPasswordEmail({commit}, email) {
            await ResetPasswordEmail.post(email).then(resp => {
                commit(RESET_PASSWORD_EMAIL, resp)
            }).catch(err => {
                commit(RESET_PASSWORD_EMAIL_ERROR, err)
            })
        },
        async resetPasswordEmailConfirmation({commit}, confirmationData) {
            await ResetPasswordEmailConfirmation.post(confirmationData).then(resp => {
                commit(RESET_PASSWORD_EMAIL_CONFIRMATION, resp['new_password'])
            }).catch(err => {
                commit(RESET_PASSWORD_EMAIL_CONFIRMATION_ERROR, err)
            })
        },
        // eslint-disable-next-line no-unused-vars
        async resendActivationEmail({commit}, emailData) {
            await ResendActivationEmail.post(emailData)
        }
    },
}