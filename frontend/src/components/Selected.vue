<template>
  <div id="selected">
    <ul>
      <li v-for="item in arrayItems" :key=item.id>{{ item[0].description }}</li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'selected',
  props: {
    searchItem: {
      type: Number
    }
  },
  data () {
    return {
      arrayItems: [] as Array<string>
    }
  },
  watch: {
    searchItem: function () {
      this.axios
        .get(`food/${this.searchItem}`)
        .then(response => (this.arrayItems.push(response.data)))
        .catch(console.error)
    }
  }
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
