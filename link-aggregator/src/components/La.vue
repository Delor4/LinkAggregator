<template>
  <div class="la_main">
    <la-tags-list
      :tags="tags"
      v-on:create-tag="onCreateTag($event)"
      v-on:update-tag="onUpdateTag($event)"
      v-on:remove-tag="onRemoveTag($event)"
    ></la-tags-list>
    <la-cards-list
      :cards="cards"
      :tags="tags"
      v-on:create-card="onCreateCard($event)"
      v-on:update-card="onUpdateCard($event)"
      v-on:remove-card="onRemoveCard($event)"
    ></la-cards-list>
  </div>
</template>

<script>
import LaCardsList from "@/components/LaCardsList.vue";
import LaTagsList from "@/components/LaTagsList.vue";

const axios = require("axios").default;

export default {
  data: function () {
    return {
      info: null,
      loading: true,
      errored: false,
      cards: {},
      tags: {},
    };
  },
  methods: {
    /* Links */
    apiDeleteLink: function (id) {
      axios
        .delete("/api/links/" + id)
        .then((response) => {
          response.done = true;
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    apiCreateLink: function (link, card_id) {
      axios
        .post("/api/links", {
          url: link.url,
          card_id: card_id,
        })
        .then((response) => {
          response.done = true;
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    apiUpdateLink: function (link, card_id) {
      axios
        .put("/api/links/" + link.id, {
          url: link.url,
          card_id: card_id,
        })
        .then((response) => {
          response.done = true;
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    /* Cards */
    apiGetCards: function () {
      var self = this;
      for (var id in this.cards) {
        this.cards[id].loading = true;
      }
      axios
        .get("/api/cards")
        .then((response) => {
          self.replaceAllCards(response.data);
          for(var i in response.data){
            self.apiGetCardTags(response.data[i].id);
          }
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    apiDeleteCard: function (id) {
      this.cards[id].loading = true;
      axios
        .delete("/api/cards/" + id)
        .then((response) => {
          response.done = true;
          this.$delete(this.cards, id);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    apiCreateCard: function (card) {
      var _links = [];
      for (var i in card.links) {
        _links.push({ url: card.links[i].url });
      }
      axios
        .post("/api/cards", {
          title: card.title,
          content: card.content,
          links: _links,
        })
        .then((response) => {
          response.done = true;
          response.data.tags = []
          this.$set(this.cards, response.data.id, response.data);
          this.apiGetCardTags(response.data.id);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    apiUpdateCard: function (card) {
      /* Delete links */
      var self = this
      var removed = [...new Set(card.removed)];
      for (var ri in removed) {
        if (removed[ri] != -1) {
          this.apiDeleteLink(removed[ri]);
        }
      }
      var _links = [];
      for (var i in card.links) {
        if (card.links[i].id == -1)
          /* Create new links */
          _links.push({ url: card.links[i].url });
        /* Update old links */ else
          this.apiUpdateLink(
            {
              id: card.links[i].id,
              url: card.links[i].url,
            },
            card.id
          );
      }
      var _tags_to_delete = this.cards[card.id].tags.filter(function(x) { return card.tags.indexOf(x) < 0 })
      var _tags_to_create = card.tags.filter(function(x) { return self.cards[card.id].tags.indexOf(x) < 0 })
      for(var dtag_id in _tags_to_delete){
        this.apiDeleteCardTag(card.id, _tags_to_delete[dtag_id])
      }
      for(var ctag_id in _tags_to_create){
        this.apiCreateCardTag(card.id, _tags_to_create[ctag_id])
      }
      axios
        .put("/api/cards/" + card.id, {
          title: card.title,
          content: card.content,
          links: _links,
        })
        .then((response) => {
          response.done = true;
          response.data.tags = []
          this.$set(this.cards, response.data.id, response.data);
          this.apiGetCardTags(response.data.id);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    replaceAllCards: function (cards) {
      for (var card_id in cards) {
        var id = cards[card_id].id;
        cards[card_id].loading = false;
        cards[card_id].tags = [];
        this.$set(this.cards, id, cards[card_id]);
      }
      // TODO: remove cards still having card.loading == true
    },
    onCreateCard: function (card) {
      this.apiCreateCard(card);
    },
    onUpdateCard: function (card) {
      this.apiUpdateCard(card);
    },
    onRemoveCard: function (id) {
      this.apiDeleteCard(id);
    },
    /* Tags */
    apiGetTags: function () {
      var self = this;
      for (var id in this.tags) {
        this.tags[id].loading = true;
      }
      axios
        .get("/api/tags")
        .then((response) => {
          self.replaceAllTags(response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    apiDeleteTag: function (id) {
      this.tags[id].loading = true;
      axios
        .delete("/api/tags/" + id)
        .then((response) => {
          response.done = true;
          this.$delete(this.tags, id);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    apiCreateTag: function (tag) {
      axios
        .post("/api/tags", {
          name: tag.name,
        })
        .then((response) => {
          response.done = true;
          this.$set(this.tags, response.data.id, response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    apiUpdateTag: function (tag) {
      axios
        .put("/api/tags/" + tag.id, {
          name: tag.name,
        })
        .then((response) => {
          response.done = true;
          this.$set(this.tags, response.data.id, response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    replaceAllTags: function (tags) {
      for (var tag_id in tags) {
        var id = tags[tag_id].id;
        tags[tag_id].loading = false;
        this.$set(this.tags, id, tags[tag_id]);
      }
      // TODO: remove cards when card.loading == true
    },
    onCreateTag: function (tag) {
      this.apiCreateTag(tag);
    },
    onUpdateTag: function (tag) {
      this.apiUpdateTag(tag);
    },
    onRemoveTag: function (id) {
      this.apiDeleteTag(id);
    },
    /* Card tags */
    apiGetCardTags: function (card_id) {
      var self = this;
      for (var id in this.tags) {
        this.tags[id].loading = true;
      }
      axios
        .get("/api/cards/" + card_id + "/tags")
        .then((response) => {
          self.replaceCardTags(card_id, response.data);
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    apiDeleteCardTag: function (card_id, tag_id) {
      axios
        .delete("/api/cards/" + card_id + "/tags/" + tag_id)
        .then((response) => {
          response.done = true;
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    apiCreateCardTag: function (card_id, tag_id) {
      axios
        .post("/api/cards/" + card_id + "/tags", {
          tag_id: tag_id
        })
        .then((response) => {
          response.done = true;
        })
        .catch((error) => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },
    replaceCardTags: function (card_id, cardtags) {
      this.cards[card_id].tags.length = 0
      for (var i in cardtags) {
        var id = cardtags[i].tag_id;
        this.cards[card_id].tags.push(id)
      }
    },
  },
  mounted() {
    this.apiGetTags();
    this.apiGetCards();
  },
  components: {
    "la-cards-list": LaCardsList,
    "la-tags-list": LaTagsList,
  },
};
</script>
<style scoped>
.la_main {
  display: -webkit-box;
  display: -moz-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  flex-direction: row;
  height: -moz-calc(100% - 64px);
  height: calc(100% - 64px);
}
</style>

// TODO: check-circle icon
