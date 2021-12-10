<template>
  <div class="navbar-container">
    <div class="navbar"
         v-bind:class="{'zero-height':!is_active}"
    >
      <div class="log-container">
        <BaseTitle
            :classObject="{black:true}"
            v-if="!is_auth"
            text="sign in"
            route="#sign_in"
        />
        <BaseTitle
            :classObject="{black:true}"
            v-if="!is_auth"
            text="sign up"
            route="#sign_up"
        />
<!--        <input-->
<!--            type="file"-->
<!--            id="file"-->
<!--            name="file"-->
<!--            placeholder="Загрузить XML"-->
<!--            @change="postFile"-->
<!--            v-if="is_auth"-->
<!--        />-->
        <div class="input__wrapper"
             v-if="is_auth">
          <input name="file" type="file"  id="input__file" class="input input__file" multiple
                 @change="postFile"
          >
          <label for="input__file" class="input__file-button">
<!--            <span class="input__file-icon-wrapper"><img class="input__file-icon" src="./img/add.svg" alt="Выбрать файл" width="25"></span>-->
            <span class="input__file-button-text">Выберите файл</span>
          </label>
        </div>
        <BaseTitle
            :classObject="{black:true}"
            v-if="is_auth"
            :text="'Log\u00A0out'"
            route="#log_out"
        />
      </div>
    </div>
    <span class="toggle"
          @click="is_active=!is_active"
    >☰</span>
  </div>
</template>

<script>
import BaseTitle from "@/components/base/base_text/BaseTitle";
import {mapActions} from "vuex";
import {BASE_URL, HTTP} from "../../api/common";

export default {
  name: "Navbar",
  props: [
    'is_auth'
  ],
  components: {
    BaseTitle
  },

  data() {
    return {
      is_active: false
    }
  },
  methods: {
    ...mapActions(['logout','setFiles','setUser']),
    // eslint-disable-next-line no-unused-vars
    onResize(event) {
      if (window.innerWidth > 720) {
        this.is_active = false
      }
    },
    postFile: function (event){
      const file = event.target.files[0]
      let formData = new FormData()
      formData.append("file_object", file)
      let setFiles = this.setFiles
      let setUser =this.setUser
      HTTP({
        method: "post",
        url: BASE_URL + "/processed-files/",
        data: formData,
      })
          .then(async function (response) {
            //handle success
            await setFiles('?ordering=-created_at')
            await setUser()
            console.log(response);
          })
          .catch(function (response) {
            //handle error
            console.log(response);
          })
    },
  },
  mounted() {
    window.addEventListener('resize', this.onResize)
    this.onResize()
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  },


}
</script>

<style scoped>
.navbar {
  height: 40px;
  width: 100%;
  background-color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  align-content: center;
}

.navbar a, .navbar button {
  color: white;
  margin: 1%;
  transition: all 0.3s
}

.navbar-container{
  overflow: hidden
}

.navbar button {
  padding-right: 25px;
}

.log-container {
  display: flex;
  flex-direction: row;
  align-content: center;

}

.log-container a, .log-container p {
  width: 180px;
}

.toggle, #menu-checkbox {
  display: none;
}



.input__wrapper {
  /*width: 100%;*/
  position: relative;
  /*margin: 15px 0;*/
  text-align: center;
}

.input__file {
  opacity: 0;
  visibility: hidden;
  position: absolute;
}

.input__file-icon-wrapper {
  height: 60px;
  width: 60px;
  margin-right: 15px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  border-right: 1px solid #fff;
}

.input__file-button-text {
  line-height: 1;
  margin-top: 1px;
}

.input__file-button {
  width: 100%;
  max-width: 290px;
  /*height: 60px;*/
  background-color: #28a745;
  color: #fff;
  /*font-size: 1.125rem;*/
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: start;
  -ms-flex-pack: start;
  justify-content: flex-start;
  border-radius: 3px;
  cursor: pointer;
  margin: 0 auto;
}
</style>