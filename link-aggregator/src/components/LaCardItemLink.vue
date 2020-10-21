<template>
  <b-list-group-item>
    <b-link
      target="_blank"
      rel="noopener noreferrer"
      :href="url"
      class="card-link"
      >{{ showUrl }}</b-link
    >
  </b-list-group-item>
</template>

<script>
module.exports = {
  computed: {
    showUrl() {
      if (this.url.length > 30) {
        return this.url.slice(0, 28) + "...";
      }
      return this.url;
    },
  },
  props: ["id", "url"],
};
</script>
