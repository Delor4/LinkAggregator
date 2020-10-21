<template>
  <b-modal
    id="la-tag-dialog-modal"
    :title="title"
    @backdrop="$emit('submit-edit-tag', tag)"
    @ok="$emit('submit-edit-tag', tag)"
    @hide="$emit('hide-tag-modal', $event)"
  >
    <form>
      Tag text: <input v-model="tag.name" />
    </form>
    <span slot="footer">
      <button type="info" @click="$emit('cancel-edit-tag')">Cancel</button>
      <button
        type="primary"
        @click="$emit('submit-edit-tag', tag)"
      >
        {{ mode }}
      </button>
    </span>
  </b-modal>
</template>

<script>
export default {
  props: ["title", "mode", "tag"],
};
</script>

<style scoped>
</style>