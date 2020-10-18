<template>
  <b-list-group-item>
    <span role="button" @click.prevent="$emit('edit-tag', id)">
      <b-icon-caret-right></b-icon-caret-right>
      {{ name }}
    </span>
    <b-icon-x-circle
      class="pull-right"
      role="button"
      v-on:click="$emit('remove-tag', id)"
    ></b-icon-x-circle>
  </b-list-group-item>
</template>

<script>
export default {
  components: {},
  props: ["name", "uri", "id"],
};
</script>
