<template>
  <div>
    <la-cards-list
        :cards="cards"
        v-on:remove-card="onRemoveCard($event)"
    ></la-cards-list>
  </div>
</template>

<script>
import LaCardsList from '@/components/LaCardsList.vue'
const axios = require('axios').default;

export default {
   data: function() {
        return {
            info: null,
            loading: true,
            errored: false,
            cards: {
                1: {
                    links: {
                        id: 3,
                        url: ""
                    }
                }
            },
        }
    },
  methods: {
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
            cards[card_id].loading = false
            this.$set(this.cards, id, cards[card_id])
        }
        // TODO: remove cards when card.loading == true
    },
    onRemoveCard: function(id) {
        this.apiDeleteCard(id)
    }
  },
  mounted () {
    this.apiGetCards()
  },
  components: {
    'la-cards-list': LaCardsList
  },
};
</script>