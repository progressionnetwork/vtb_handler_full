<template>
  <div class="popup-container"
       @click="back"
       style="background-color: rgba(0,0,0,0);">
    <div class="popup-container"></div>
    <div class="reg-container"
         @mousedown="isInBoxDown=true"
         @mouseup="isInBoxUp=true"
    >
      <form>
        <div class="title-container">
          <BaseTitle
              class="reg-title"
              v-if="routeHashCheck('sign_up')||routeHashCheck('sign_in')"
              :text="'\u00A0\u00A0Sign in\u00A0\u00A0'"
              :style-object="{
                'color': (routeHashCheck('sign_up')) ? 'white':'#ffd400',
                'border-color': (routeHashCheck('sign_up')) ? 'white':'#ffd400'
              }"
              :route="'#sign_in'"
          />
          <BaseTitle
              class="reg-title"
              v-if="routeHashCheck('sign_in')||routeHashCheck('sign_up')"
              :text="'\u00A0\u00A0Sign up\u00A0\u00A0'"
              :style-object="{
                'color': (routeHashCheck('sign_in')) ? 'white':'#ffd400',
                'border-color': (routeHashCheck('sign_in')) ? 'white':'#ffd400'
              }"
              :route="'#sign_up'"
          />
        </div>
        <BaseTitle
            class="reg-title"
            v-if="routeHashCheck('account_activation')"
            text="Account activation"
            :style-object="{'color':'white'}"
        />
        <BaseTitle
            class="reg-title"
            v-if="routeHashCheck('reset_password')"
            text="Reset Password"
            :style-object="{'color':'white'}"
        />
        <BaseTitle
            class="reg-title"
            v-if="routeHashCheck('reset_password_confirmation')"
            text="Reset Password"
            :style-object="{'color':'white'}"
        />
        <BaseTitle
            class="reg-title"
            v-if="$route.hash==='#log_out'"
            text="log out"
            :style-object="{'color':'white'}"
        />
        <BaseInput
            v-if="routeHashCheck('email')"
            :placeholder="placeholders.email"
            :type="`text`"
            :theme="theme.email"
            :value="form.email"
            :img="`${require('../../static/icons/email-input.svg')}`"
            @inputValue="form.email=$event
            errors.email=false"
        />
        <BaseInput
            v-if="routeHashCheck('password')"
            :placeholder="placeholders.password"
            :type="`password`"
            :theme="theme.password"
            :value="form.password"
            :img="`${require('../../static/icons/password-input.svg')}`"
            @inputValue="form.password=$event
            errors.password=false"
        />
        <BaseInput
            v-if="routeHashCheck('passwordRepeat')"
            :placeholder="placeholders.passwordRepeat"
            :type="`password`"
            :theme="theme.passwordRepeat"
            :img="`${require('../../static/icons/password-input.svg')}`"
            @inputValue="form.passwordRepeat=$event
            errors.passwordRepeat=false"
        />
        <BaseCheckbox
            v-if="routeHashCheck('confidentiality')"
            :text="'Agree to the privacy policy'"
            :is_error="Boolean(errors.confidentiality)"
            @checkBoxValue="form.confidentiality=$event"
        />
        <BaseCheckbox
            v-if="routeHashCheck('email_notification')"
            :text="'Email notification'"
            @checkBoxValue="form.email_notification=$event"
        />
        <BaseCheckbox
            v-if="routeHashCheck('log_out')"
            :text="'Forget password'"
            @checkBoxValue="form.forget_password=$event"
        />

        <div class="log-in-row" v-if="routeHashCheck('sign_in')">
          <BaseParagraph
              :text="`Forgot your password?`"
              :route="'#reset_password'"
              :style-object="{'color': 'white'}"
          />
          <BaseButton
              class="button-container"
              :class-object="{'white-border':true}"
              :text="`sign in`"
              @buttonClick="checkForm"
          />
        </div>
        <div class="log-up-column" v-if="routeHashCheck('sign_up')">
          <BaseButton
              class="button-container"
              :class-object="{'white-border':true}"
              :text="`sign up`"
              @buttonClick="checkForm"
          />
        </div>
        <div class="log-up-column"
             v-if="routeHashCheck('reset_password') && !timerCheck('password_reset_email_confirm_waiting')">
          <BaseButton
              class="button-container"
              :class-object="{'white-border':true}"
              :text="`Send message`"
              @buttonClick="checkForm"
          />
        </div>
        <div class="log-up-column"
             v-if="routeHashCheck('reset_password') && timerCheck('password_reset_email_confirm_waiting')">
          <BaseTitle
              :text="`Send email confirmation again after\u00A0`+ String(actual_password_reset_email_confirm_waiting+'\u00A0s')"
              :style-object="{'color':'white'}"
              :key="updateKey+1"
          />
        </div>

        <div class="log-up-column" v-if="routeHashCheck('reset_password_confirmation')">
          <BaseButton
              class="button-container"
              :class-object="{'white-border':true}"
              :text="`Confirm`"
              @buttonClick="checkForm"
          />
        </div>
        <div class="log-up-column" v-if="routeHashCheck('log_out')">
          <BaseButton
              class="button-container"
              :class-object="{'white-border':true}"
              :text="`Confirm`"
              @buttonClick="logoutFunction"
          />
        </div>
        <div class="log-up-column"
             v-if="routeHashCheck('account_activation') && !timerCheck('email_confirm_waiting')">
          <BaseButton
              class="button-container"
              :class-object="{'white-border':true}"
              :text="`Send again`"
              @buttonClick="resendActivationEmailFunction"
              :key="updateKey"
          />
        </div>
        <div class="log-up-column"
             v-if="routeHashCheck('account_activation') && timerCheck('email_confirm_waiting')">
          <BaseTitle
              :text="`Send email confirmation again after\u00A0`+ String(actual_email_confirm_waiting+'\u00A0s')"
              :style-object="{'color':'white'}"
              :key="updateKey+1"
          />
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import BaseInput from "@/components/base/BaseInput";
import BaseParagraph from "@/components/base/base_text/BaseParagraph";
import BaseButton from "@/components/base/BaseButton";
import BaseTitle from "@/components/base/base_text/BaseTitle";
import {mapGetters, mapActions} from "vuex";
import BaseCheckbox from "@/components/base/BaseCheckbox";

export default {
  name: "RegPopup",
  components: {
    BaseInput, BaseParagraph, BaseButton, BaseTitle, BaseCheckbox
  },
  props: ['auth'],
  data() {
    return {
      updateKey: 0,
      email_confirm_waiting: {},
      password_reset_email_confirm_waiting: {},
      actual_email_confirm_waiting: 0,
      actual_password_reset_email_confirm_waiting: 0,
      defaultPlaceholders: {
        email: 'Enter e-mail',
        password: 'Enter password',
        passwordRepeat: 'Confirm password',
      },
      placeholders: {
        email: 'Enter e-mail',
        password: 'Enter password',
        passwordRepeat: 'Confirm password',
      },
      form: {
        email: '',
        password: '',
        passwordRepeat: '',
        confidentiality: false,
        email_notification: false,
        forget_password: false
      },
      errors: {
        email: false,
        password: false,
        passwordRepeat: false,
        confidentiality: false,
      },
    }
  },
  methods: {
    ...mapActions(['createUser','clearStore','activation', 'authorization', 'setUser', 'logout',
      'resetPasswordEmail', 'resetPasswordEmailConfirmation', 'resendActivationEmail']),
    clearFormat: function () {
      for (let key of Object.keys(this.errors)) {
        this.errors[key] = false
      }
      this.placeholders = JSON.parse(JSON.stringify(this.defaultPlaceholders))
    },
    back: function () {
      if (!this.isInBoxDown && !this.isInBoxUp) {
        document.getElementsByTagName('body')[0].style.overflow = 'visible'
        this.$router.push(this.$route.path)
      } else {
        this.isInBoxDown = false
        this.isInBoxUp = false
      }
      this.isInBoxDown = false
      this.isInBoxUp = false
    },
    closePopupListener: function (event) {
      if (event.key === 'Escape') {
        this.back()
      }
    },

    checkForm: async function () {
      this.clearFormat()
      if (this.$route.hash !== '#reset_password_confirmation') {
        if (!this.validEmail(this.form.email)) {
          this.errors.email = true
          this.placeholders.email = 'E-mail entered incorrectly'
        }
        if (!this.form.email) {
          this.errors.email = true
          this.placeholders.email = 'Enter e-mail'
        }
      }

      if (this.$route.hash !== '#reset_password') {
        if (!this.form.password) {
          this.errors.password = true
        }
        let passwordCheck = this.validPassword(this.form.password)
        if (passwordCheck) {
          this.errors.password = true
          this.placeholders.password = passwordCheck
        }
      }

      if ((this.$route.hash === '#sign_up' || this.$route.hash === '#reset_password_confirmation')) {
        if (!this.form.passwordRepeat) {
          this.errors.passwordRepeat = true
        }
        if (this.form.passwordRepeat !== this.form.password) {
          this.placeholders.passwordRepeat = 'Password mismatch'
          this.errors.passwordRepeat = true
        }
      }

      if (this.$route.hash === '#sign_up') {
        if (!this.form.confidentiality) {
          this.errors.confidentiality = true
        }
      }

      for (let error in this.errors) {
        if (this.errors[error]) {
          return false
        }
      }

      if (this.$route.hash === '#sign_in') {
        await this.authFunction()
      }

      if (this.$route.hash === '#sign_up') {
        await this.createUserFunction()
      }

      if (this.$route.hash === '#reset_password') {
        this.resetPasswordEmailFunction()
      }

      if (this.$route.hash === '#reset_password_confirmation') {
        await this.resetPasswordEmailConfirmationFunction()
      }

      for (let error in this.errors) {
        if (this.errors[error]) {
          return false
        }
      }

      localStorage.setItem('email', this.form.email)
      localStorage.setItem('password', this.form.password)
      // let path = this.$route.path.split('/')

      if (!(['#reset_password','#sign_up'].includes(this.$route.hash))) {
        this.back()
      }
      // if (path[2] === 'reset_password') {
      //   await this.$router.push('/portfolio')
      // }
      //
      // if (this.$route.hash==='#sign_up') {
      //   await this.$router.push('#account_activation')
      // }

    },
    timerCheck: function (timeName) {
      if (this[timeName][this.form.email]) {
        return !!this[timeName][this.form.email]['timer'];
      } else {
        return false
      }
    },
    createUserFunction: async function () {
      let email = this.form.email
      let password = this.form.password
      let email_notification = this.form.email_notification
      let json = {
        'email': email,
        'password': password,
        'email_notification': email_notification,
      }
      // eslint-disable-next-line no-unused-vars
      await this.createUser(json).then(resp => {
        if (!this.getAuth.errors.createUserError) {
          this.back()
        } else {
          this.errors.email = true
          this.placeholders.email = 'E-mail already exist'
        }
      })
    },
    authFunction: async function () {
      let json = {
        email: this.form.email,
        password: this.form.password
      }
      // eslint-disable-next-line no-unused-vars
      await this.authorization(json).then(resp => {
        if (this.getAuth.errors.authError) {
          this.errors.email = true
          this.errors.password = true
          this.placeholders.email = 'Invalid e-mail or password'
          this.placeholders.password = 'Invalid e-mail or password'
        }
        // eslint-disable-next-line no-unused-vars
      }).then(resp => {
        if (!this.getAuth.errors.authError) {
          this.setUser()
        }
      })
    },
    logoutFunction: function () {
      if (this.form.forget_password) {
        localStorage.setItem('password', '')
      }
      this.logout()
      this.clearStore()
      this.back()
    },
    resetPasswordEmailConfirmationFunction: async function () {
      let json = {
        uid: this.$route.params.uid,
        token: this.$route.params.token,
        new_password: this.form.password,
        // re_new_password: this.form.passwordRepeat,
      }
      // eslint-disable-next-line no-unused-vars
      await this.resetPasswordEmailConfirmation(json).then(resp => {
        if (this.getAuth.errors.resetPasswordEmailConfirmationError) {
          this.errors.password = true
          this.errors.passwordRepeat = true
          this.placeholders.password = 'Send new email'
          this.placeholders.passwordRepeat = 'Send new email'
        }
        // eslint-disable-next-line no-unused-vars
      }).then(resp => {
        if (!this.getAuth.errors.resetPasswordEmailConfirmationError)
        this.authorization({
          email: this.form.email,
          password: this.form.password
          // eslint-disable-next-line no-unused-vars
        }).then(resp => {
          this.setUser()
        })
      })
      if (this.getAuth.errors.resetPasswordEmailConfirmationError) {
        this.errors.password = true
        this.errors.passwordRepeat = true
        this.placeholders.password = 'Send new email'
        this.placeholders.passwordRepeat = 'Send new email'
      }
    },
    resendActivationEmailFunction: function () {
      let json = {
        email: this.form.email,
      }
      // eslint-disable-next-line no-unused-vars
      this.resendActivationEmail(json)
      if (this.email_confirm_waiting[this.form.email]) {
        this.email_confirm_waiting[this.form.email]['timer'] = 300
      } else {
        this.email_confirm_waiting[this.form.email] = {'timer': 300, 'time': Date.now()}
      }
      this.actual_email_confirm_waiting = this.email_confirm_waiting[this.form.email]['timer']
      this.startWaiting('email_confirm_waiting')
    },
    resetPasswordEmailFunction: function () {
      let json = {
        email: this.form.email,
      }
      // eslint-disable-next-line no-unused-vars
      this.resetPasswordEmail(json).then(resp => {
        if (this.getAuth.errors.resetPasswordEmailError) {
          this.errors.email = true
          this.placeholders.email = 'E-mail does not exist'
        }
      })
      if (this.password_reset_email_confirm_waiting[this.form.email]) {
        this.password_reset_email_confirm_waiting[this.form.email]['timer'] = 300
      } else {
        this.password_reset_email_confirm_waiting[this.form.email] = {'timer': 300, 'time': Date.now()}
      }
      this.actual_password_reset_email_confirm_waiting = this.password_reset_email_confirm_waiting[this.form.email]['timer']
      this.startWaiting('password_reset_email_confirm_waiting')
    },
    startWaiting: function (timeName) {
      setInterval(() => {
        if (this[timeName][this.form.email]['timer'] === 0) {
          return
        }
        this[`actual_${timeName}`]--
        this[timeName][this.form.email]['timer']--
      }, 1000)
    },
    routeHashCheck: function (active_name) {
      let routeHash = this.$route.hash
      let active_fields = []
      if (routeHash === '#sign_up') {
        active_fields = ['sign_up', 'email', 'password', 'passwordRepeat',
          'confidentiality', 'email_notification']
      }
      if (routeHash === '#sign_in') {
        active_fields = ['sign_in', 'email', 'password',]
      }
      if (routeHash === '#reset_password') {
        if (this.password_reset_email_confirm_waiting[this.form.email]) {
          if (this.password_reset_email_confirm_waiting[this.form.email]['timer']) {
            active_fields = ['reset_password']
          } else {
            active_fields = ['reset_password', 'email']
          }
        } else {
          active_fields = ['reset_password', 'email']
        }
      }
      if (routeHash === '#reset_password_confirmation') {
        active_fields = ['reset_password_confirmation', 'password', 'passwordRepeat']
      }
      if (routeHash === '#log_out') {
        active_fields = ['log_out',]
      }
      if (routeHash === '#account_activation') {
        active_fields = ['account_activation',]
      }
      return active_fields.includes(active_name)
    },
    validPassword: function () {
      if (this.form.password.length <= 8) {
        return 'Password length less than 8 characters'
      }
      if (!/\d/.test(this.form.password)) {
        return 'The password must contain number'
      }
      if (/[а-яА-Я]/.test(this.form.password)) {
        return 'Password must not contain non-English letters'
      }
      if (!/[A-Z]/.test(this.form.password)) {
        return 'The password must contain capital letters'
      }
      if (!/[a-z]/.test(this.form.password)) {
        return 'Password must contain the lower case letter'
      } else {
        return false
      }
    },
    validEmail: function (email) {
      let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    validApi: function (api, api_name) {
      if (!/[a-zA-Z0-9]/.test(api)) {
        return `${api_name.capitalize()} must contain English letters or numbers`
      }
      if (api.length !== 64) {
        return `Length ${api_name} must be 64 characters`
      } else {
        return false
      }
    },
    takeTimers: function () {
      let email_confirm_waiting = JSON.parse(localStorage.getItem('email_confirm_waiting'))
      let password_reset_email_confirm_waiting = JSON.parse(localStorage.getItem('password_reset_email_confirm_waiting'))
      if (!email_confirm_waiting) {
        email_confirm_waiting = {}
      }
      if (!password_reset_email_confirm_waiting) {
        password_reset_email_confirm_waiting = {}
      }
      this.email_confirm_waiting = email_confirm_waiting
      this.password_reset_email_confirm_waiting = password_reset_email_confirm_waiting
      let actual_password_reset_email_confirm_waiting = password_reset_email_confirm_waiting[this.form.email]
      let actual_email_confirm_waiting = email_confirm_waiting[this.form.email]
      if (actual_password_reset_email_confirm_waiting) {
        let now_time = Date.now()
        let difference = Math.round(actual_password_reset_email_confirm_waiting['timer'] - (now_time - actual_password_reset_email_confirm_waiting['time']) / 1000)
        if (difference <= 0) {
          this.password_reset_email_confirm_waiting[this.form.email]['timer'] = 0
        } else {
          this.password_reset_email_confirm_waiting[this.form.email]['timer'] = difference
          this.actual_password_reset_email_confirm_waiting = difference
          this.startWaiting('password_reset_email_confirm_waiting')
        }
      }
      if (actual_email_confirm_waiting) {
        let now_time = Date.now()
        let difference = Math.round(actual_email_confirm_waiting['timer'] - (now_time - actual_email_confirm_waiting['time']) / 1000)
        if (difference <= 0) {
          this.email_confirm_waiting[this.form.email]['timer'] = 0
        } else {
          this.email_confirm_waiting[this.form.email]['timer'] = difference
          this.actual_email_confirm_waiting = difference
          this.startWaiting('email_confirm_waiting')
        }
      }
    }
  },
  computed: {
    ...mapGetters(['getAuth']),
    actual_email: function () {
      return this.form.email
    },
    theme: function () {
      let form = this.form
      let errors = this.errors
      let placeholders = this.placeholders
      let validEmail = this.validEmail
      let validPassword = this.validPassword
      return {
        email: function () {
          if (errors.email) {
            return 'error'
          }
          if (!form.email) {
            placeholders.email = 'Enter your e-mail'
            return 'default'
          }
          if (!validEmail(form.email)) {
            placeholders.email = 'E-mail entered incorrectly'
            return 'error'
          } else {
            placeholders.email = 'Correct e-mail'
            return 'right'
          }
        }(),
        password: function () {
          if (errors.password) {
            return 'error'
          }
          if (!form.password) {
            placeholders.password = 'Enter password'
            return 'default'
          }
          let passwordPlaceholder = validPassword()
          if (passwordPlaceholder) {
            placeholders.password = passwordPlaceholder
            return 'error'
          } else {
            placeholders.password = 'Correct password'
            return 'right'
          }
        }(),
        passwordRepeat: function () {
          if (errors.passwordRepeat) {
            return 'error'
          }
          if (!form.passwordRepeat) {
            placeholders.passwordRepeat = 'Confirm password'
            return 'default'
          }
          if (form.password !== form.passwordRepeat) {
            placeholders.passwordRepeat = 'Password mismatch'
            return 'error'
          } else {
            placeholders.passwordRepeat = 'Passwords match'
            return 'right'
          }
        }(),
      }
    },
  },
  created() {
    let localStorageEmail = localStorage.getItem('email')
    let localStoragePassword = localStorage.getItem('password')
    if (localStorageEmail && localStoragePassword) {
      this.form.email = localStorageEmail
      this.form.password = localStoragePassword
    }
    this.takeTimers()
    document.getElementsByTagName('body')[0].style.overflow = 'hidden'
  },
  beforeDestroy() {
    document.removeEventListener('keydown', this.closePopupListener)
  },
  beforeMount() {
    document.addEventListener('keydown', this.closePopupListener)
  },
  updated() {
    document.getElementsByTagName('body')[0].style.overflow = 'visible'
  },
  watch: {
    // eslint-disable-next-line no-unused-vars
    actual_email_confirm_waiting(newVal, oldVal) {
      let email_confirm_waiting = JSON.parse(localStorage.getItem('email_confirm_waiting'))
      if (!email_confirm_waiting) {
        email_confirm_waiting = {}
      }
      email_confirm_waiting[this.form.email] = {
        'timer': this.actual_email_confirm_waiting,
        'time': Date.now()
      }
      localStorage.setItem('email_confirm_waiting', JSON.stringify(email_confirm_waiting))

    },
    // eslint-disable-next-line no-unused-vars
    actual_password_reset_email_confirm_waiting(newVal, oldVal) {
      let password_reset_email_confirm_waiting = JSON.parse(localStorage.getItem('password_reset_email_confirm_waiting'))
      if (!password_reset_email_confirm_waiting) {
        password_reset_email_confirm_waiting = {}
      }
      password_reset_email_confirm_waiting[this.form.email] = {
        'timer': this.actual_password_reset_email_confirm_waiting,
        'time': Date.now()
      }
      localStorage.setItem('password_reset_email_confirm_waiting', JSON.stringify(password_reset_email_confirm_waiting))
    },
    // eslint-disable-next-line no-unused-vars
    actual_email(newVal, oldVal) {
      this.actual_password_reset_email_confirm_waiting = 0
      this.actual_email_confirm_waiting = 0
      this.takeTimers()
    }
  }
}
</script>

<style scoped>
.popup-container {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.25);
  display: flex;
  cursor: pointer;
  transition: all 0.1s;
}

.popup-container:hover {
  background-color: rgba(0, 0, 0, 0.4);
}

.reg-container {
  position: relative;
  width: 448px;
  cursor: default;
  z-index: 10000;
  background: black;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  border-radius: 4px;
  margin: auto;
  padding-top: 1%;
  padding-bottom: 1%;
  display: flex;
}

form {
  width: 90%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  margin: auto;
}

.choice-row {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding-top: 8%;
  padding-bottom: 8%;
}

.choice {
  transition: all 0.3s;
  opacity: 0.7;
}

.choice:hover {
  opacity: 1;
}

.active-choice {
  padding-left: 2%;
  padding-right: 2%;
  border-bottom: 1px solid #FFFFFF;
  opacity: 1;
}

.pseudo-input {
  margin-bottom: 4%;
}

.log-in-row {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  margin-top: 6%;
  margin-bottom: 6%;
}

.log-in-row .button-container {
  width: 40%;
  margin-left: 10%;
}

.log-in-row a p {
  opacity: 0.7;
  transition: all 0.3s;
}

.log-in-row a:hover p {
  opacity: 1;
}

.log-up-column .button-container {
  width: 50%;
  margin-top: 5%;
  margin-bottom: 5%;
  margin-left: auto;
  margin-right: auto;
}

.reg-title {
  margin-bottom: 3%;
  border-bottom: 1px solid white;
}

.title-container {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
</style>
