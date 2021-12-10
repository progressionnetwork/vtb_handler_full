import {
    Files,
} from '@/api/elements'
import {
    SET_FILES,SET_FILE,CLEAR_STORE
} from '../mutation-types'


// Геттеры
export default {
    state: {
        files:[],
        file:{}
    },
    getters: {
        getFiles(state) {
            return state.files
        },
        getFile(state) {
            return state.file
        },
        getFilesCount(state) {
            return state.files_count
        },

    },
// Мутации
    mutations: {
        [SET_FILES](state, files) {
            state.files = files.results
            state.files_count = files.count
        },
        [SET_FILE](state, files) {
            state.file = files.data
        },
        [CLEAR_STORE](state){
            state.files = []
            state.file = {}
        }
    },
// Действия
    actions: {
        async setFiles({commit}, queryParams) {
            await Files.list(queryParams)
                .then(files => {
                    commit(SET_FILES, files)
                    console.log(files)
                }).catch((error) => {
                    console.log(error)
                })
        },
        async setFile({commit}, id) {
            await Files.get(id)
                .then(file => {
                    commit(SET_FILE, file)
                    console.log(file)
                }).catch((error) => {
                    console.log(error)
                })
        },
        clearStore({commit}) {
            commit(CLEAR_STORE)
        },
    },
}
