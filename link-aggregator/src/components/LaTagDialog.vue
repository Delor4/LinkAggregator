<template>
  <b-modal
    id="la-tag-dialog-modal"
    :title="title"
    @backdrop="$emit('submit-edit-tag', tag)"
    @ok="$emit('submit-edit-tag', tag)"
    @hide="$emit('hide-tag-modal', $event)"
  >
    <form v-on:submit.prevent="ok()">
      Tag text: <input v-model="tag.name" />
    </form>
    <template #modal-footer="{ ok, cancel, hide }">
      <b-button
        :hidden="tag.id == -1"
        variant="danger"
        @click="
          $emit('remove-tag', tag.id);
          hide();
        "
      >
        Delete
      </b-button>
      <b-button variant="secondary" @click="cancel()"> Cancel </b-button>
      <b-button variant="success" @click="ok()">
        {{ mode == "Edit" ? "Save" : "Create" }}
      </b-button>
    </template>
  </b-modal>
</template>

<script>
export default {
  methods: {
    ok() {
      this.$emit('submit-edit-tag', this.tag)
      this.$bvModal.hide("la-tag-dialog-modal");
    },
  },
  props: ["title", "mode", "tag"],
};
</script>

<style scoped>
</style>