<template>
  <div class="game">
    <div class="game__score-block">
      <div
        class="game__score"
        :style="{ color: player.color || 'white' }"
        v-for="player in players"
      >
        {{ player.name }} {{ player.score }}
      </div>
    </div>

    <div class="game__input-block">
      <div class="game__name-input-block !nomasion_desanid">
        <input
          autofocus
          @keyup.enter="wordSend"
          v-model="word"
          type="text"
          class="game__name-input"
        />
      </div>
    </div>

    <div class="game__words-block">
      <div
        class="game__last-word"
        :style="{ color: 'white' }"
      >
        {{ this.lastWord }}
      </div>

      <div class="game__words-overflow">
        <div
          class="game__words"
          :style="{ color: row.color || 'white' }"
          v-for="row in sortedWords"
        >
          {{ row.lvl }} -> {{ row.word }}
        </div>
      </div>
    </div>

    <button class="exit-button" @click="leaveRoom">exit</button>
  </div>
</template>

<script>
import io from "socket.io-client";
import global from "../global";

export default {
  name: "CompGame",
  props: {
    socket: Object,
    roomId: Number,
    startInfoAboutGame: Object,
  },
  data() {
    return {
      word: "месяц",
      players: [],
      words: [],
      lastWord: "",
    };
  },
  computed: {
    sortedWords: function () {
      return this.words.sort((a, b) => a.lvl - b.lvl);
    }
  },
  created() {
    window.addEventListener("beforeunload", ()=> {this.socket.emit("leaveRoom", 0, { id: 0, name: this.name })});

    this.socket.on("fin", (winner) => {
      console.log(winner)
    });

    this.socket.on("send_words", (words) => {
      this.words = words;
    });

    this.socket.on("send_players", (players) => {
      this.players = players
    });
  },
  beforeUnmount() {
    console.log("exit");
    this.socket.emit("leaveRoom", 0, { id: 0, name: this.name });
  },
  methods: {
    leaveRoom: function () {
      this.$emit("changeComp", "Auth");
    },
    wordSend: function () {
      this.lastWord = this.word;
      this.socket.emit("word2back", this.word);
      this.word = "";
    },
  },
};
</script>

<style lang="scss" scoped>
.game {
  width: 100%;
  height: 100%;

  display: flex;
  flex-direction: column;
}

.game__score-block {
  flex: 0 0 100px;
  //background-color: #57e30d;

  column-count: 2;
  column-gap: 4%;

  padding: 10px 22px;

  overflow: auto;
}

.game__input-block {
  flex: 0 0 auto;
  //background-color: #0d3fe3;
}

.game__words-block {
  flex: 1 1 1px;

  display: flex;
  flex-direction: column;

  justify-content: flex-start;
  align-items: center;
  //background-color: #e30d2d;
  font-size: 2rem;
  overflow: auto;
}

.game__words-overflow {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;

  width: 100%;
  height: 100%;
  overflow: auto;
}

.game__last-word {
  margin: 50px 0;
}

.game__words {
  flex: 1 1 auto;
}

// ПК
@media screen and (max-width: 1024px) {
}
// Планшет
@media screen and (max-width: 800px) {
}
// Телефон
@media screen and (max-width: 420px) {
  .game__score-block {
    flex: 0 0 170px;
  }
  .game__input-block {
    flex: 0 0 100px;
  }
}

.game__score {
  font-size: 1.5rem;
}

.game__name-input-block {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;

  border: 1px solid white;
}

.nomasion_desanid:after {
  content: "";
  position: absolute;
  z-index: -2;
  left: 0;
  top: 0;
  width: 100%;
  height: 200px;
  right: 0;
  bottom: 0;
  margin: auto;
  opacity: 1;
  border-radius: 60px;
  filter: blur(60px);
  transform: translate3d(0, 0, 0);
  background: linear-gradient(-134deg, #0083ff 0, #d582ff 100%);
  animation: glow 3s infinite;
}
@keyframes glow {
  0% {
    opacity: 1;
    width: 100%;
  }
  50% {
    opacity: 0.85;
    width: 100%;
  }
  100% {
    opacity: 1;
    width: 100%;
  }
}

.game__name-input {
  width: 100vw;

  border: none;
  //border-radius: 7px;

  background-color: var(--color-background);
  caret-color: transparent;
  color: white;

  font-size: 3.8rem;
  //font-family: "ChargeVectorBlack", Helvetica, Arial, serif;

  text-align: center;
}

.game__name-input:focus {
  outline: none;
}

.game__name-input::selection {
  background-color: rgba(255, 255, 255, 0);
}

.exit-button {
  position: absolute;
  right: 0;
  width: 50px;
  height: 50px;
}
</style>
