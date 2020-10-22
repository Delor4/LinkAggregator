<template>
  <div class="la_main">
    <la-tags-list
      class="la_tags_list"
      :tags="tags"
      v-on:create-tag="onCreateTag($event)"
      v-on:update-tag="onUpdateTag($event)"
      v-on:remove-tag="onRemoveTag($event)"
    ></la-tags-list>
    <la-cards-list
      class="la_cards_list"
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

/* API */
import api from "../api";

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
    /* Cards */
    setCard: function (card) {
      this.$set(this.cards, card.id, card);
    },
    loadAllCards: async function () {
      var cards = await api.getCards();
      for (var card_id in cards) {
        cards[card_id].tags = [];
        this.setCard(cards[card_id]);
      }

      for (var i in this.cards) {
        /* FIX: N+1 problem 
          Need changes on api side
        */
        this.loadCardTags(this.cards[i].id);
      }
    },

    _createCard: async function (card) {
      var _links = [];
      for (var i in card.links) {
        _links.push({ url: card.links[i].url });
      }
      var _resp = await api.createCard({
        title: card.title,
        content: card.content || (card.title ? "" : "<no content>"),
        links: _links,
      });

      /* creating card tags */
      _resp.tags = [];

      this.setCard(_resp); /* card without tags */

      var fires = [];
      for (var ctag_id in card.tags) {
        fires.push(api.createCardTag(_resp.id, card.tags[ctag_id]));
      }
      await Promise.all(fires);

      return this.loadCardTags(_resp.id);
    },
    _updateCard: async function (card) {
      /* Delete links */
      var self = this;
      var fires = [];
      var removed = [...new Set(card.removed)];
      for (var ri in removed) {
        if (removed[ri] != -1) {
          fires.push(api.deleteLink(removed[ri]));
        }
      }
      var _links = [];
      for (var i in card.links) {
        if (card.links[i].id == -1)
          /* Create new links */
          _links.push({ url: card.links[i].url });
        /* Update old links */ else
          fires.push(
            api.updateLink({
              id: card.links[i].id,
              url: card.links[i].url,
              card_id: card.id,
            })
          );
      }
      var _tags_to_delete = this.cards[card.id].tags.filter(function (x) {
        return card.tags.indexOf(x) < 0;
      });
      var _tags_to_create = card.tags.filter(function (x) {
        return self.cards[card.id].tags.indexOf(x) < 0;
      });
      for (var dtag_id in _tags_to_delete) {
        fires.push(api.deleteCardTag(card.id, _tags_to_delete[dtag_id]));
      }
      for (var ctag_id in _tags_to_create) {
        fires.push(api.createCardTag(card.id, _tags_to_create[ctag_id]));
      }

      await Promise.all(fires);

      var _card = await api
        .updateCard({
          id: card.id,
          title: card.title,
          content: card.content || (card.title ? "" : "<no content>"),
          links: _links,
        })
        .then((response) => {
          response.tags = [];
          return response;
        });

      this.setCard(_card);
      return this.loadCardTags(_card.id);
    },
    createCard: async function (card) {
      return await this._createCard(card);
    },
    updateCard: async function (card) {
      return await this._updateCard(card);
    },
    deleteCard: async function (id) {
      await api.deleteCard(id);
      /* remove tag */
      this.$delete(this.cards, id);
    },
    onCreateCard: function (card) {
      this.createCard(card);
    },
    onUpdateCard: function (card) {
      this.updateCard(card);
    },
    onRemoveCard: function (id) {
      this.deleteCard(id);
    },
    /* Tags */
    setTag: function (tag) {
      this.$set(this.tags, tag.id, tag);
    },
    loadAllTags: async function () {
      var _tags = await api.getTags();
      for (var tag_id in _tags) {
        this.setTag(_tags[tag_id]);
      }
    },
    createTag: async function (tag) {
      var _resp = await api.createTag(tag);
      this.setTag(_resp);
    },
    updateTag: async function (tag) {
      var _resp = await api.updateTag(tag);
      this.setTag(_resp);
    },
    deleteTag: async function (id) {
      await api.deleteTag(id);
      /* remove tag from cards */
      for (var cid in this.cards) {
        var ti = this.cards[cid].tags.indexOf(id); /* mark to update card? */
        if (ti >= 0) this.cards[cid].tags.splice(ti, 1);
      }
      /* remove tag */
      this.$delete(this.tags, id);
    },
    onCreateTag: function (tag) {
      this.createTag(tag);
    },
    onUpdateTag: function (tag) {
      this.updateTag(tag);
    },
    onRemoveTag: function (id) {
      this.deleteTag(id);
    },
    /* Card tags */
    loadCardTags: async function (card_id) {
      var tags = await api.getCardTags(card_id).then((_resp) => {
        var _tags = [];
        for (var ti in _resp) {
          _tags.push(_resp[ti].tag_id);
        }
        return _tags;
      });
      this.cards[card_id].tags = tags;
    },
    /* rest */
    loadAll: async function () {
      await this.loadAllTags();
      this.loadAllCards();
    },
  },
  mounted() {
    this.loadAll();
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
.la_cards_list {
  margin: 5px;
}
</style>
