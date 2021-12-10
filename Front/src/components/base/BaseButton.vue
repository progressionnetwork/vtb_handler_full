<template>
  <button
      :type="type"
      v-bind:class="classObject"
      class="button"
      @click="$emit('buttonClick')"
  >
    <BaseParagraph
        v-if="theme==='small'"
        :text="text"
    />
    <BaseTitle
        v-if="theme==='default'"
        :text="text"
    />
  </button>
</template>

<script>
import BaseTitle from "@/components/base/base_text/BaseTitle";
import BaseParagraph from "@/components/base/base_text/BaseParagraph";

export default {
  name: "BaseButton",
  components: {
    BaseTitle,BaseParagraph
  },
  props: {
    text: {
      type: String,
      default: null
    },
    type: {
      type: String,
      default: 'button'
    },
    theme: {
      type: String,
      default: 'default'
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
        return {}
      }
    },
  },
}
</script>

<style scoped>
.button {
  cursor: pointer;
  height: 100%;
  border: none;
  background-color: rgba(0, 0, 0, 0);
  color: white;
}

.button p, button a {
  transition: all 0.3s
}

.button:hover p, button:hover a {
  color: #ffd400;
}
.white-border{
  border:1px solid white;
  border-radius: 5px;
  transition: border 0.3s;
}
.black-button{
  border-radius: 5px;
  background-color: rgba(0, 0, 0, 0.9);
}

.white-border:hover{
  border:1px solid #ffd400;
}

.white-hover:hover p{
  color: white;
}

.gold-button{
  background-color: #ffd400;
}
.gold-button p{
  color: black;
}
.gold-button:hover p{
  color: black;
}

</style>