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
        <BaseTitle
            :classObject="{black:true}"
            v-if="is_auth"
            :text="'Log\u00A0out'"
            route="#log_out"
        />
        <BaseTitle
            :classObject="{black:true}"
            v-if="is_auth"
            :text="'Change\u00A0API'"
            route="#api_key_change"
        />
        <BaseTitle
            :classObject="{black:true}"
            v-if="is_auth"
            class="reg-title"
            :text="'\u00A0\u00A0Account\u00A0\u00A0'"
            :style-object="{
                'color': (!($route.path==='/account')) ? 'white':'#ffd400',
                'border-color': (!($route.path==='/account')) ? 'white':'#ffd400'
              }"
            :route="'/account'"
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
    ...mapActions(['logout']),
    // eslint-disable-next-line no-unused-vars
    onResize(event) {
      if (window.innerWidth > 720) {
        this.is_active = false
      }
    }
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
  margin: 1%;
}

.log-container a, .log-container p {
  width: 180px;
}

.toggle, #menu-checkbox {
  display: none;
}

@media (max-width: 720px) {
  .toggle {
    display: block;
  }

  .navbar-container {
    position: relative;
  }

  .navbar, .log-container {
    position: relative;
    flex-direction: column;
    height: auto;
  }

  .log-container a:first-child {
    margin-bottom: 6%;
  }

  .toggle {
    position: relative;
    z-index: 1;
    height: 60px;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.9);
    overflow: hidden;
    line-height: 60px;
    font-size: 30px;
    color: white;
    transition: color 0.3s, background-color 0.3s;
    cursor: pointer;
  }

  .toggle:hover {
    color: black;
    background-color: #ffd400;
  }

  .zero-height {
    height: 0
  }
}

</style>