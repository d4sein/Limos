<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="less">
@import 'assets/static/mixins';

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: @white;
}

a {
  text-decoration: none;
}

li {
  list-style-type: none;
}
</style>
