<template>
  <div>
    <b-card style="max-width: 20rem; margin-bottom: 5px">
      <b-card-title>
        {{ card.title }}
        <b-icon-x-circle
          role="button"
          class="close"
          v-on:click="$emit('remove-card', card.id)"
        ></b-icon-x-circle>
      </b-card-title>
      <b-card-sub-title>
        <b-icon-wrench
          role="button"
          class="close"
          v-on:click="$emit('edit-card', card.id)"
        ></b-icon-wrench>
      </b-card-sub-title>
      <b-card-text>{{ card.content }}</b-card-text>
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
          v-for="(tag_id, index) in card.tags"
          v-bind:key="index"
          v-bind:tags="tags"
          style="margin-right: 0.5em"
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
