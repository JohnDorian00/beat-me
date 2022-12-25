<template>
  <!--  <div><input style="width: 500px; height: 100px" v-model="input" /></div>-->
  <!--  <div><button style="width: 200px; height: 50px" @click="send"></button></div>-->
  <!--  <div>{{ this.answers }}</div>-->
  <component @changeComp="changeComp" :is="activeComp"></component>
</template>

<script>
import io from "socket.io-client";
import global from "./global";
import CompAuth from "./components/CompAuth.vue";
import CompGame from "./components/CompGame.vue";

export default {
  name: "App",
  data: function () {
    return {
      list: null,
      answers: [],
      input: "",
      activeComp: CompAuth,
      comps: {
        CompAuth: CompAuth,
        CompGame: CompGame,
      },
    };
  },
  beforeCreate() {
    (async () => {
      this.list = await (await fetch(global.back_ip + "/get_list")).json();
      console.log(this.list);
    })();
  },
  created() {},
  methods: {
    changeComp: function (compName) {
      this.activeComp = this.comps["Comp" + compName] || this.activeComp;
    },
    send: function () {
      console.log(this.input);
      if (this.list.includes(this.input)) {
        this.answers.push(
          this.input + " " + (this.list.indexOf(this.input) + 1)
        );
      }
    },
  },
};
</script>

<style lang="scss">
@font-face {
  font-family: "ChargeVectorBlack";
  src: local("ChargeVectorBlack"),
    url("./assets/fonts/Charge Vector Black/ChargeVectorBlack.ttf")
      format("truetype");
}
</style>
