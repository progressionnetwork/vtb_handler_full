<template>
  <a v-bind:class="classObject" v-bind:style="styleObject" v-if="link" :href="link" target="_blank">
    {{ text }}
  </a>
  <router-link v-bind:class="classObject" v-bind:style="styleObject" v-else-if="route" :to="route" tag="a">
    {{ text }}
  </router-link>
  <p  v-bind:style="styleObject" v-else>
    {{ text }}
  </p>
</template>


<script>
export default {
  name: "BaseSubTitle",
  props: {
    text: {
      type: String,
      default: null
    },
    link: {
      type: String,
      default: null
    },
    route: {
      type: String,
      default: null
    },
    classObject: {
      type: Object,
      default: function () {
        return {
        }
      }
    },
    styleObject: {
      type: Object,
      default: function () {
        return {
        }
      }
    },
  },
}
</script>

<style scoped>
p,a {
  font-family: Roboto;
  font-style: normal;
  font-weight: bold;
  font-size: 25px;
  line-height: 143%;
  transition: color 0.3s

}
a {
  text-decoration: none;
  transition: color 0.3s
}
a:hover{
  color: #ffd400 !important;
}

.white-border{
  border:1px solid white;
  border-radius: 5px;
  transition: border 0.3s;
  cursor: pointer;
}

.white-border:hover{
  border:1px solid #ffd400;
}

</style>
