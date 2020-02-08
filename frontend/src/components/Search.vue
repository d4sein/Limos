<template>
  <div id="search">
    <input type="search" @keyup.enter="submitItem" v-model="search" placeholder="Pesquisar..">
    <button type="submit" @click="submitItem">Adicionar</button>
    <ul id="autocomplete">
      <li v-for="(key, value) in arrayAutocomplete" :key=key @click="onClickAutocomplete(key, value)">{{ value }}</li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import debounce from 'lodash.debounce'

export default Vue.extend({
  name: 'search',
  data () {
    return {
      search: '',
      arrayAutocomplete: [],
      tempArrayAutocomplete: []
    }
  },
  methods: {
    submitItem: function (this: any): void {
      this.$emit('searchItem', this.tempArrayAutocomplete[this.search])
      this.search = ''
    },
    onClickAutocomplete: function (id: number, search: string): void {
      this.search = search
    },
    getAnswer: debounce(function (this: any, search: string): void {
      if (search.length === 0) {
        this.arrayAutocomplete = []
        return
      }

      this.axios
        .get(`food?search=${search}`)
        .then((response: any) => (this.arrayAutocomplete = response.data))
        .then(() => {
          if (typeof this.arrayAutocomplete[search] !== 'undefined') {
            // `tempArrayAutocomplete` is a shadow of `arrayAutocomplete`
            // that holds its later values.
            this.tempArrayAutocomplete = this.arrayAutocomplete
            this.arrayAutocomplete = []
          }
        })
        .catch(console.error)
    }, 300)
  },
  watch: {
    search: function (newSearch: string, oldSearch: string): void {
      this.getAnswer(newSearch)
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
