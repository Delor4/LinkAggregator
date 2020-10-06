<template>
<div>
  <b-card :title="title" sub-title="Card subtitle">
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
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            tag
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
    </template>
    <div class="title">{{ uri }}</div>
    <button v-on:click="$emit('remove-card', id)">Remove</button>
  </b-card>
</div>
</template>

<script>
import LaCardItemLink from '@/components/LaCardItemLink.vue'

export default {
    components: {
        'la-card-item-link': LaCardItemLink
    },
    props: ['title', 'content', 'uri', 'links', 'id'],
}
</script>
