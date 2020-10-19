<template>
  <b-modal
    id="la-card-dialog-modal"
    @backdrop="$emit('submit-edit-card', card)"
    @ok="$emit('submit-edit-card', card)"
    @hide="$emit('hide-card-modal', $event)"
  >
    <form>
      Title: <input v-model="card.title" />
      Content:<input v-model="card.content" />
    </form>
  </b-modal>
</template>

<script>
export default {
  data: function () {
    return {};
  },
  computed: {
    modalTitle() {
      return `${this.mode} Card`;
    },
    formVisible: {
      get: function () {
        return this.visible;
      },
      set: function () {
        //console.log("dialog: ", val)
        // this.visible = value
      },
    },
  },
  methods: {},
  mounted() {},
  props: ["title", "loading", "visible", "mode", "card"],
};
</script>

<style scoped>
</style>