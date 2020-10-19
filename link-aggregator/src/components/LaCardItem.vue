<template>
  <div>
    <b-card>
      <b-card-title>
        {{ title }}
        <b-icon-x-circle
          role="button"
          class="close"
          v-on:click="$emit('remove-card', id)"
        ></b-icon-x-circle>
      </b-card-title>
      <b-card-sub-title>
        <b-icon-wrench
          role="button"
          class="close"
          v-on:click="$emit('edit-card', id)"
        ></b-icon-wrench>
      </b-card-sub-title>
      <b-card-text>{{ content }}</b-card-text>
      <la-card-item-link
        v-for="link in links"
        v-bind:key="link.id"
        v-bind:id="link.id"
        v-bind:url="link.url"
      ></la-card-item-link>
      <b-link :href="uri" class="card-link">res</b-link>
      <template v-slot:footer>
        <em>Footer Slot</em>
        <div
          class="alert alert-success alert-dismissible fade show"
          role="alert"
        >
          tag
          <button
            type="button"
            class="close"
            data-dismiss="alert"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
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
  props: ["title", "content", "uri", "links", "id"],
};
</script>
