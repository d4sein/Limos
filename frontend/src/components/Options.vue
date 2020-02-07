<template>
  <div id="options">
    <ul>
        <li v-for="option in getOptions" :key="option">
        <p>{{ option }}</p>
        <input type="checkbox" :name="option">
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import '../assets/static/axios_config'

export default Vue.extend({
  name: 'options',
  data () {
    return {
      arrayOptions: []
    }
  },
  mounted () {
    this.axios
      .get('food/options')
      .then(response => (this.arrayOptions = response.data))
      .catch(e => console.error(e))
  },
  computed: {
    getOptions: function (): Array<string> {
      let result: Array<string> = this.arrayOptions

      if (result.length > 0) {
        let filters: Array<string> = ['index', 'Descrição', 'Categoria']
        result = result.filter(e => !filters.includes(e))
      }

      return result
    }
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/mixins';

#options {
  grid-column-start: 1;
  grid-column-end: 1;
  grid-row-start: 1;
  grid-row-end: 3;

  ul {

    li {
      margin-bottom: 10px;
      padding: 10px;
      display: flex;
      background: @light-green;

    &:nth-child(2n) {
      background: @light-green2;
    }

      p {
        color: @dark-green;
      }

      input {
        margin-left: auto;
      }
    }
  }
}
</style>
