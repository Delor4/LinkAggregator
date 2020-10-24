<template>
  <div>
    <b-card style="max-width: 20rem; margin-bottom: 5px">
      <b-card-title role="button" v-on:click="$emit('edit-card', card.id)">
        {{ card.title }}
      </b-card-title>
      <b-card-text role="button" v-on:click="$emit('edit-card', card.id)">
        {{ card.content }}
      </b-card-text>
      <b-list-group>
        <la-card-item-link
          v-for="link in card.links"
          v-bind:key="link.id"
          v-bind:id="link.id"
          v-bind:url="link.url"
        ></la-card-item-link>
      </b-list-group>
      <template v-slot:footer>
        <b-badge
          role="button"
          variant="dark"
          v-for="(tag_id, index) in card.tags"
          v-bind:key="index"
          v-bind:tags="tags"
          style="margin-right: 0.5em"
          v-on:click="$emit('edit-card', card.id)"
        >
          {{ tags[tag_id].name }}
        </b-badge>
      </template>
    </b-card>
  </div>
</template>

<script>
import LaCardItemLink from "@/components/LaCardItemLink.vue";

export default {
  components: {
    "la-card-item-link": LaCardItemLink,
  },
  props: ["title", "content", "uri", "links", "id", "card", "tags"],
};
</script>
