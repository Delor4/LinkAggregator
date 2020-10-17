<template>
<div>
    <b-card-group deck>
      <b-card header="Card with list group">
        <la-tag-item
          v-for="tag in tags"
          v-bind:key="tag.id"
          v-bind:id="tag.id"
          v-bind:name="tag.name"
          v-bind:uri="tag.uri"
          v-on:remove-tag="$emit('remove-tag', $event)"
        ></la-tag-item>
      </b-card>
    </b-card-group>
</div>
</template>

<script>
import LaTagItem from '@/components/LaTagItem.vue'

export default {
  components: {
        LaTagItem
    },
    props: ['tags']
};
</script>