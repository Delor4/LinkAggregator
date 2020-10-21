<template>
  <b-modal
    id="la-card-dialog-modal"
    :title="title"
    @backdrop="$emit('submit-edit-card', card)"
    @ok="$emit('submit-edit-card', card)"
    @hide="$emit('hide-card-modal', $event)"
  >
    <form>
      <div>Title: <input v-model="card.title" /></div>
      <div>Content: <input v-model="card.content" /></div>
      <div>
        Links:
        <ul>
          <li
            v-for="(link, index) in card.links"
            v-bind:key="index"
            v-bind:id="link.id"
            v-bind:url="link.url"
          >
            <input v-model="link.url" />
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
        <b-form-group label="Card tags">
          <b-form-checkbox
            v-for="option in tags"
            v-model="card.tags"
            :key="option.id"
            :value="option.id"
            name="cardtags"
            inline
          >
            {{ option.name }}
          </b-form-checkbox>
        </b-form-group>
      </div>
    </form>
  </b-modal>
</template>

<script>
export default {
  props: ["title", "loading", "mode", "card", "tags"],
};
</script>
