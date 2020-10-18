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
      cards: {
        1: {
          links: {
            id: 3,
            url: "",
          },
        },
      },
      tags: {
        1: {
          id: 1,
          name: "TestowyTag",
          uri: "http_smth_uri",
        },
      },
    };
  },
  methods: {
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
    replaceAllCards: function (cards) {
      for (var card_id in cards) {
        var id = cards[card_id].id;
        cards[card_id].loading = false;
        this.$set(this.cards, id, cards[card_id]);
      }
      // TODO: remove cards when card.loading == true
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
