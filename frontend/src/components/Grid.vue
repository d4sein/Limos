<template>
  <div id="grid">
    <search @searchItem="updateSearchItem"/>
    <options/>
    <selected :searchItem="searchItem"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

import Search from './Search.vue'
import Options from './Options.vue'
import Selected from './Selected.vue'

export default Vue.extend({
  name: 'grid',
  components: {
    Search,
    Options,
    Selected
  },
  data () {
    return {
      searchItem: 0
    }
  },
  methods: {
    updateSearchItem (searchItem: number): void {
      this.searchItem = searchItem
    }
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/mixins';

#grid {
  width: 80%;
  margin: 100px auto;
  display: grid;
  grid-gap: 15px;
  grid-template-columns: 1fr 3fr;
  grid-template-rows: 30px 1fr;
}
</style>
