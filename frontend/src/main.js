import { createApp } from "vue";
import { VueCookieNext } from "vue-cookie-next";

import App from "./App.vue";

import "./assets/main.css";

const app = createApp(App);
app.use(VueCookieNext);
app.mount("#app");

// set default config
VueCookieNext.config({
  expire: "1m",
  path: "/",
  domain: "",
  secure: "",
  sameSite: "",
});

// set global cookie
VueCookieNext.setCookie("theme", "dark");
