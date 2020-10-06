<template>
<div>
    <b-card-group deck>
        <la-card-item
          v-for="(card) in cards"
          v-bind:key="card.id"
          v-bind:id="card.id"
          v-bind:title="card.title"
          v-bind:content="card.content"
          v-bind:uri="card.uri"
          v-bind:links="card.links"
          v-on:remove-card="$emit('remove-card', $event)"
        ></la-card-item>
  </b-card-group>
</div>
</template>

<script>
import LaCardItem from './LaCardItem.vue'

export default {
  components: {
        LaCardItem
    },
    props: ['cards']
};
</script>