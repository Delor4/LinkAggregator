<template>
  <b-list-group-item>
    <span role="button" @click.prevent="$emit('edit-tag', id)">
      <h4>
        <b-badge variant="dark">
          <b-icon-caret-right></b-icon-caret-right>
          {{ name }}
        </b-badge>
      </h4>
    </span>
  </b-list-group-item>
</template>

<script>
export default {
  components: {},
  props: ["name", "uri", "id"],
};
</script>
