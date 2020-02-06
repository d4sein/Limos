<template>
  <div id="search">
    <input type="search" v-model="search" placeholder="Pesquisar..">
    <button type="submit">Adicionar</button>
    <ul id="autocomplete">
      <li v-for="autocomplete in arrayAutocomplete" :key=autocomplete>{{ autocomplete }}</li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import debounce from 'lodash.debounce'

export default Vue.extend({
  name: 'search',
  methods: {
    debouncer: function (newsearch: string) {},
    getAnswer: function (search: string) {
      if (search.length === 0) {
        this.arrayAutocomplete = []
        return
      }

      this.axios
        .get(`food?search=${search}`)
        .then(response => (this.arrayAutocomplete = response.data))
        .catch(e => console.error(e))
    }
  },
  created: function () {
    this.debouncer = debounce(this.getAnswer, 300)
  },
  data () {
    return {
      search: '',
      arrayAutocomplete: []
    }
  },
  watch: {
    search: function (newSearch: string, oldSearch: string) {
      this.debouncer(newSearch)
    }
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/mixins';

#search {
  grid-column-start: 2;
  grid-column-end: 2;
  grid-row-start: 1;
  grid-row-end: 1;
  display: grid;
  grid-template-columns: 1fr 120px;
  justify-content: center;
  align-items: center;
  position: relative;

  input {
    height: 100%;
    padding: 5px;
    color: @dark-green;
    border: 1px solid @green;
  }

  button {
    height: 100%;
    color: @white;
    background: @green;
    border: none;
  }
}

#autocomplete {
  width: 100%;
  top: 30px;
  position: absolute;
  background: @white;

  li {
    padding: 5px;
    color: @dark-green;
    border-left: 1px solid @light-green;
    border-right: 1px solid @light-green;
    font-size: 14px;

    &:hover {
      background: @light-green2;
    }
  }
}
</style>
