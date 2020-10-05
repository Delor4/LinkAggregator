import Vue from 'vue'
//import App from './App.vue'
//import router from './router'
//import store from './store'

Vue.config.productionTip = false
/*
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
*/

Vue.component('la-card-item', {
  template: '\
    <li>\
      <div class="title">{{ title }}</div>\
      <div class="title">{{ content }}</div>\
      <div class="title">{{ uri }}</div>\
      <button v-on:click="$emit(\'remove\')">Remove</button>\
    </li>\
  ',
  props: ['title', 'content', 'uri']
})
const axios = require('axios').default;

new Vue({
  el: '#la-cards-list',
  data () {
    return {
      info: null,
      loading: true,
      errored: false,
      newTodoText: '',
    cards: {
      1: {
        id: 1,
        title: 'Do the new dishes',
        content: 'content',
        links: [],
        uri: "",
        loading: false,
      },
      2: {
        id: 2,
        title: 'Take out the trash',
        loading: false,
        uri: "",
        links: [],
      },
      3: {
        id: 3,
        title: 'Mow the lawn',
        links: [],
        uri: "",
        loading: false,
      }
    },
    nextTodoId: 4
    }
  },
  methods: {
    addNewTodo: function () {
      this.cards.push({
        id: this.nextTodoId++,
        title: this.newTodoText
      })
      this.newTodoText = ''
    },
    apiGetCards: function () {
      for(var id in this.cards) {
        this.cards[id].loading = true
      }
      axios
      .get('http://localhost:44343/api/cards')
      .then(response => {
        this.replaceAllCards(response.data)
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading = false)
    },
    apiDeleteCard: function (id) {
        this.cards[id].loading = true
      axios
      .delete('http://localhost:44343/api/card/'+id)
      .then(response => {
        response.done = true
        delete this.cards[id]
        //console.log(response)
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading =false)
    },
    replaceAllCards: function (cards) {
        for(var card_id in cards) {
            //console.log(cards[card_id]);
            cards[card_id].loading = false
            this.cards[card_id] = cards[card_id]
        }
        // TODO: remove cards when card.loading == true
    },
    onRemoveCard: function(id) {
        console.log("remove card ", id)
        this.apiDeleteCard(id)
    }
  },

  mounted () {
    this.apiGetCards()
  }
})