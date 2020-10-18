<template>
  <div :class="{ 'd-none': visible == false }">
    <form>
      <input v-model="tag.name" />
    </form>
    <span slot="footer">
      <button type="info" @click="$emit('cancel-edit-tag')">Cancel</button>
      <button
        type="primary"
        :loading="loading"
        @click="$emit('submit-edit-tag', tag)"
      >
        {{ mode }}
      </button>
    </span>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      dialogFormVisible: false,
    };
  },
  computed: {
    modalTitle() {
      return `${this.mode} Tag`;
    },
  },
  methods: {},
  mounted() {},
  props: ["title", "loading", "visible", "mode", "tag"],
};
</script>

<style scoped>
</style>