<template>
  <div class="main">

    <div class="main__name-block">
      <div class="main__name-label">
        <p>name</p>
      </div>

      <div class="main__name-input-block nomasion_desanid">
        <input
          @click="inputFocus"
          v-model="name"
          type="text"
          class="main__name-input"
        />
      </div>
    </div>

    <div class="main__game-create-block">
      <div class="btn" @click="joinRoom('create')">create</div>
    </div>

    <div class="main__game-join-block">
      <div class="btn" @click="joinRoom('join')">join</div>
<!--      <div class="btn" @click="joinRoom('join')">join</div>-->
    </div>

  </div>
</template>

<script>
import global from "../global";

export default {
  name: "CompAuth",
  props: {
    socket: Object
  },
  data() {
    return {
      name: "",
      id: null,
    };
  },
  created() {
    this.name = this.$cookie.getCookie("name") || this.name;
    this.id = this.$cookie.getCookie("id") || this.id;

    this.socket.on("join_response", () => {
      this.$emit("joinRoom");
    });
  },
  methods: {
    inputFocus: function () {
      this.name = "";
    },
    joinRoom: function (type) {
      if (this.name.length < 1) {
        return;
      }

      this.$cookie.setCookie("name", this.name);

      if (type === "create") {
        this.socket.emit("creating_room", { id: this.id, name: this.name });
      } else {
        this.socket.emit("joining_room", prompt('Room #'), {id: this.id, name: this.name });
      }
    },
  },
};
</script>

<style lang="scss" scoped>
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
    opacity: 0;
    width: 100%;
  }
  50% {
    opacity: 1;
    width: 50%;
  }
  100% {
    opacity: 0;
    width: 100%;
  }
}

.btn {
  -moz-user-select: none;
  -khtml-user-select: none;
  user-select: none;

  cursor: pointer;

  text-align: center;
  font-size: 2.5rem;
  text-transform: uppercase;
  //font-family: "ChargeVectorBlack", Helvetica, Arial, serif;
}

.main {
  width: 100%;
  height: 100%;

  display: flex;
  flex-direction: column;
}
.main > div {
  display: inherit;
}

.main__name-input {
  position: absolute;
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

.main__name-input:focus {
  outline: none;
}

.main__name-input::selection {
  background-color: rgba(255, 255, 255, 0);
}

.main__name-block {
  flex: 1 1 1px;

  flex-direction: column;
}

.main__name-input-block {
  display: flex;
  justify-content: center;
  align-items: center;

  flex: 1 1 1px;
}

.main__name-label {
  display: flex;
  justify-content: center;
  align-items: center;

  font-size: 1.4rem;
  flex: 0 0 20px;

  -moz-user-select: none;
  -khtml-user-select: none;
  user-select: none;
}

.main__game-create-block {
  justify-content: center;
  align-items: center;

  flex: 0 0 120px;
}

.main__game-join-block {
  justify-content: center;
  align-items: center;
  flex: 0 0 120px;
}

// ПК
@media screen and (max-width: 1024px) {
  .main {
    padding: 100px 60px;
  }

  .main__name-block {
  }

  .main__name-label {
    flex: 0 0 80px;
    font-size: 4.4rem;
  }
}
// Планшет
@media screen and (max-width: 800px) {
  .main {
    padding: 200px 60px;
  }
}
// Телефон
@media screen and (max-width: 420px) {
  .main {
    padding: 80px 60px;
  }

  .main__name-label {
    flex: 0 0 80px;
    font-size: 3.4rem;
  }
}
</style>
