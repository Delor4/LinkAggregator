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
<style scoped>
body {
    color: #e8eaed;
    direction: ltr;
    font-family: 'Roboto',arial,sans-serif;
    font-size: 15px;
}
body {
    background-color: #202124;
    box-sizing: border-box;
    display: -webkit-box;
    display: -moz-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    flex-direction: column;
    height: -moz-calc(100% - 64px);
    height: calc(100% - 64px);
    min-height: auto;
    overflow: hidden;
    padding-top: 8px;
    position: fixed;
    top: 64px;
    transition-duration: 150ms;
    transition-property: width,box-shadow,border-radius;
    transition-timing-function: cubic-bezier(0.4,0.0,0.2,1);
    width: 280px;
    z-index: 985;
}
</style>