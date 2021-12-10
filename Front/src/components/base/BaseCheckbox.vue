<template>
  <div class="input"
  >
    <div
        v-bind:class="classObject"
        class="check-box"
        @click="check =!check; $emit('checkBoxValue',check)"
    >
      <img
          v-if="check"
          src="../../static/icons/check-marker.svg"
          alt=""
      >
    </div>
    <div class="input-text">
      <div class="input-link">
        <BaseParagraph
            style="display: block"
            :text="text"
            :style-object="{color:`white`}"
        />
      </div>
    </div>
  </div>

</template>

<script>
import BaseParagraph from "@/components/base/base_text/BaseParagraph";

export default {
  name: "BaseCheckbox",
  components:{
    BaseParagraph
  },
  props: {
    value: {
      type: Boolean,
      default: false
    },
    text: {
      type: String,
      default: null
    },
    is_error: {
      type: Boolean,
      default: false
    },
  },
  data() {
    return {
      check: false
    }
  },
  computed: {
    classObject: function () {
      return {
        'default': !this.check,
        'right': this.check,
        'error': this.is_error,
      }
    },
  },
}
</script>

<style scoped>
.input {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  margin-top: 2%;
}

.input input {
  margin-right: 4%;
}

.input-link {
  color: white;
  transition: all 0.3s;
}

.input-text {
  width: 100%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  text-align: left;
  justify-content: left;
}
.input:hover a p {
  text-decoration: underline;
}

.check-box {
  border: 1px solid white;
  box-sizing: border-box;
  border-radius: 2px;
  transition: all 0.3s;
  height: 24px;
  width: 24px;
  display: flex;
  margin-right: 4%;
}

.check-box img {
  width: 90%;
  margin: auto;
}

.default {
  text-decoration: underline;
  border: 1px solid rgba(255, 255, 255, 0.7);
}
.error {
  border: 1px solid #FF0808CD;
}
.right {
  border-color: #00FFC2;
}

</style>