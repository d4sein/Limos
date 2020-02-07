<template>
  <div id="selected"></div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'selected'
})
</script>

<style lang="less" scoped>
@import '../assets/static/mixins';

#selected {
  margin-bottom: 10px;
  grid-column-start: 2;
  grid-column-end: 2;
  grid-row-start: 2;
  grid-row-end: 2;
  border: 1px solid @light-green;
}
</style>
