<template>
  <div>
    <div
      role="button"
      @click="onCreateCard"
      :class="{ 'd-none': dialogFormVisible != false }"
    >
      <b-icon-plus-circle></b-icon-plus-circle>
      New card
    </div>
    <b-card-group deck>
      <la-card-item
        v-for="card in cards"
        v-bind:key="card.id"
        :card="card"
        :tags="tags"
        v-on:edit-card="onEditCard($event)"
        v-on:remove-card="$emit('remove-card', $event)"
      ></la-card-item>
    </b-card-group>
    <la-card-dialog
      :title="modalTitle"
      :loading="loading"
      :mode="mode"
      :card="formModel"
      :tags="tags"
      v-on:submit-edit-card="onSubmitEditCard($event)"
      v-on:hide-card-modal="onHideModal($event)"
    ></la-card-dialog>
  </div>
</template>

<script>
import LaCardItem from "@/components/LaCardItem.vue";
import LaCardDialog from "@/components/LaCardDialog.vue";

export default {
  components: {
    LaCardItem,
    LaCardDialog,
  },
  data: function () {
    return {
      mode: "",
      dialogFormVisible: false,
      loading: false,
      formModel: {},
    };
  },
  computed: {
    modalTitle() {
      return `${this.mode} card`;
    },
  },
  methods: {
    _newCard() {
      return {
        id: -1,
        title: "",
        content: "",
        links: [],
        removed: [],
        tags: [],
      };
    },
    cloneCard(_card) {
      var _out = this._newCard();
      _out.id = _card.id;
      _out.title = _card.title;
      _out.content = _card.content;
      for (var link in _card.links) {
        var _link = {
          id: _card.links[link].id,
          url: _card.links[link].url,
        };
        _out.links[link] = _link;
      }
      return _out;
    },
    onHideModal() {
      this.resetCardDialog();
    },
    onCreateCard() {
      this.mode = "Create";
      this.dialogFormVisible = true;
      this.$bvModal.show("la-card-dialog-modal");
    },
    onEditCard(model_id) {
      this.mode = "Edit";
      this.formModel = this.cloneCard(this.cards[model_id]);
      this.dialogFormVisible = true;
      this.$bvModal.show("la-card-dialog-modal");
    },
    onCancelEditCard() {
      this.resetCardDialog();
    },
    onSubmitEditCard(card) {
      if (this.mode == "Edit") this.updateCard(card);
      else this.saveCard(card);
      this.resetCardDialog();
    },
    saveCard(card) {
      this.$emit("create-card", card);
    },
    updateCard(card) {
      this.$emit("update-card", card);
    },
    resetCardDialog() {
      this.mode = "";
      this.dialogFormVisible = false;
      this.loading = false;
      this.formModel = this._newCard();
    },
  },
  mounted() {
    this.resetCardDialog();
  },
  props: ["cards", "tags"],
};
</script>