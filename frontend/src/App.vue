<template>
  <component @joinRoom="joinRoom" :is="activeComp" :socket="socket" :roomId="roomId" :startInfoAboutGame="startInfoAboutGame"></component>
</template>

<script>
import global from "./global";
import CompAuth from "./components/CompAuth.vue";
import CompGame from "./components/CompGame.vue";
import io from "socket.io-client";

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
      socket: null,
      roomId: null,
      startInfoAboutGame: null,
    };
  },
  beforeCreate() {
    // (async () => {
    //   this.list = await (await fetch(global.back_ip + "/get_list")).json();
    // })();
  },
  created() {
    this.socket = io.connect(global.back_ip);

    this.socket.on("connect", () => {
      console.log("success connected to backend", this.socket);
    });

    this.socket.on("update_players", () => {
      console.log("success connected to backend", this.socket);
    });

    this.socket.on("update_words", () => {
      console.log("success connected to backend", this.socket);
    });


    this.socket.on("message", (data) => {
      console.log("log is: ", data);
    });
  },
  methods: {
    joinRoom: function (roomId) {
      this.roomId = roomId;
      // this.startInfoAboutGame = {words: joinInfo.words, players: joinInfo.players}

      this.changeComp("Game")
    },
    changeComp: function (compName) {
      this.activeComp = this.comps["Comp" + compName] || this.activeComp;
    },
    send: function () {
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
