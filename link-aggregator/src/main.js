import Vue from 'vue'
//import App from './App.vue'
//import router from './router'
//import store from './store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
/*
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
*/
Vue.component('la-card-item-link', {
    template: '\
  <b-link :href="url" class="card-link">link {{ id }}</b-link>\
',
  props: ['url', 'id']
})

Vue.component('la-card-item', {
  template: '\
  <b-card :title="title" sub-title="Card subtitle">\
    <b-card-text>{{ content }}</b-card-text>\
    <b-link\
          is="la-card-item-link"\
          v-for="link in links"\
          v-bind:key="link.id"\
          v-bind:id="link.id"\
          v-bind:url="link.url"></b-link>\
    <b-link :href="uri" class="card-link">res</b-link>\
    <template v-slot:footer>\
        <em>Footer Slot</em>\
        <div class="alert alert-success alert-dismissible fade show" role="alert">\
  tag\
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">\
    <span aria-hidden="true">&times;</span>\
  </button>\
</div>\
      </template>\
      <div class="title">{{ uri }}</div>\
      <button v-on:click="$emit(\'remove\')">Remove</button>\
       </b-card>\
  ',
  props: ['title', 'content', 'uri', 'links']
})
const axios = require('axios').default;

new Vue({
  el: '#la-cards-list',
  data () {
    return {
      info: null,
      loading: true,
      errored: false,
    cards: {},
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
      var self = this;
      for(var id in this.cards) {
        this.cards[id].loading = true
      }
      axios
      .get('http://localhost:44343/api/cards')
      .then(response => {
        self.replaceAllCards(response.data)
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
      .delete('http://localhost:44343/api/cards/'+id)
      .then(response => {
        response.done = true
        this.$delete(this.cards, id)
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
            var id = cards[card_id].id
            console.log(card_id, id);
            console.log(cards[card_id]);
            cards[card_id].loading = false
            this.$set(this.cards, id, cards[card_id])
        }
        console.log(this.cards)
        // TODO: remove cards when card.loading == true
    },
    onRemoveCard: function(id) {
        console.log("remove card ", id)
        console.log(this.cards)
        console.log(this.cards[id])
        this.apiDeleteCard(id)
    }
  },
  mounted () {
    this.apiGetCards()
  }
})