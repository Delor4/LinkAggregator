<template>
  <div>
    <b-card-group deck>
      <span
        role="button"
        @click="onCreateCard"
        :class="{ 'd-none': dialogFormVisible != false }"
      >
        <b-icon-plus-circle></b-icon-plus-circle>
        New
      </span>
      <la-card-item
        v-for="card in cards"
        v-bind:key="card.id"
        v-bind:id="card.id"
        v-bind:title="card.title"
        v-bind:content="card.content"
        v-bind:uri="card.uri"
        v-bind:links="card.links"
        v-on:edit-card="onEditCard($event)"
        v-on:remove-card="$emit('remove-card', $event)"
      ></la-card-item>
    </b-card-group>
    <la-card-dialog
      :title="modalTitle"
      :loading="loading"
      :visible="dialogFormVisible"
      :mode="mode"
      :card="formModel"
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
    onHideModal() {
      this.resetCardDialog();
    },
    cloneCard(_card) {
      var _out = {
        id: _card.id,
        title: _card.title,
        content: _card.content,
        links: [],
        removed: [],
      };
      for (var link in _card.links) {
        var _link = {
          id: _card.links[link].id,
          url: _card.links[link].url,
        };
        _out.links[link] = _link;
      }
      return _out;
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
      this.formModel = {
        title: "",
        content: "",
        links: [],
        removed: [],
      };
    },
  },
  mounted() {
    this.resetCardDialog();
  },
  props: ["cards"],
};
</script>