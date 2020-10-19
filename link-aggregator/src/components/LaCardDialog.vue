<template>
  <b-modal
    id="la-card-dialog-modal"
    :title="title"
    @backdrop="$emit('submit-edit-card', card)"
    @ok="$emit('submit-edit-card', card)"
    @hide="$emit('hide-card-modal', $event)"
  >
    <form>
      Title: <input v-model="card.title" /> Content:<input
        v-model="card.content"
      />
      <ul>
        <li
          v-for="(link, index) in card.links"
          v-bind:key="index"
          v-bind:id="link.id"
          v-bind:url="link.url"
        >
          Link: <input v-model="link.url" />
          <b-icon-x-circle
            role="button"
            class="close"
            v-on:click="
              card.removed.push(link.id);
              card.links.splice(index, 1);
            "
          ></b-icon-x-circle>
        </li>
        <li>
          <span
            role="button"
            @click="
              card.links.push({
                id: -1,
                url: 'http://',
              })
            "
          >
            <b-icon-plus-circle></b-icon-plus-circle>
            New
          </span>
        </li>
      </ul>
    </form>
  </b-modal>
</template>

<script>
export default {
  data: function () {
    return {};
  },
  computed: {
    formVisible: {
      get: function () {
        return this.visible;
      },
      set: function () {},
    },
  },

  props: ["title", "loading", "visible", "mode", "card"],
};
</script>

