<template>
  <div>
    <b-card-group deck>
      <b-card style="min-width: 14rem">
        <b-card-title>Tags </b-card-title>
        <b-card-sub-title>
          <span
            role="button"
            @click="onCreateTag"
            :class="{ 'd-none': dialogFormVisible != false }"
          >
            <b-icon-plus-circle></b-icon-plus-circle>
            New
          </span>
        </b-card-sub-title>
        <la-tag-dialog
          :title="modalTitle"
          :mode="mode"
          :tag="formModel"
          v-on:cancel-edit-tag="onCancelEditTag()"
          v-on:submit-edit-tag="onSubmitEditTag($event)"
          v-on:hide-tag-modal="resetTagDialog()"
        ></la-tag-dialog>
        <la-tag-item
          v-for="tag in tags"
          v-bind:key="tag.id"
          v-bind:id="tag.id"
          v-bind:name="tag.name"
          v-bind:uri="tag.uri"
          v-on:remove-tag="$emit('remove-tag', $event)"
          v-on:edit-tag="onEditTag($event)"
        ></la-tag-item>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
import LaTagItem from "@/components/LaTagItem.vue";
import LaTagDialog from "@/components/LaTagDialog.vue";

export default {
  components: {
    LaTagItem,
    LaTagDialog,
  },
  data: function () {
    return {
      mode: "",
      dialogFormVisible: false,
      loading: false,
      formModel: {},
    };
  },
  computed: {
    modalTitle() {
      return `${this.mode} tag`;
    },
  },
  methods: {
    _newTag() {
      return {
        id: -1,
        name: "",
      }
    },
    cloneTag(tag) {
      var _tag = this._newTag()
      _tag.id = tag.id
      _tag.name = tag.name
      return _tag;
    },
    onCreateTag() {
      this.mode = "Create";
      this.dialogFormVisible = true;
      this.$bvModal.show("la-tag-dialog-modal");
    },
    onEditTag(tag_id) {
      this.mode = "Edit";
      this.formModel = this.cloneTag(this.tags[tag_id]);
      this.dialogFormVisible = true;
      this.$bvModal.show("la-tag-dialog-modal");
    },
    onCancelEditTag() {
      this.resetTagDialog();
    },
    onSubmitEditTag(tag) {
      if (this.mode == "Edit") this.updateTag(tag);
      else this.saveTag(tag);
      this.resetTagDialog();
    },
    saveTag(tag) {
      this.$emit("create-tag", tag);
    },
    updateTag(tag) {
      this.$emit("update-tag", tag);
    },
    resetTagDialog() {
      this.mode = "";
      this.dialogFormVisible = false;
      this.loading = false;
      this.formModel = {
        name: "",
      };
    },
    mounted() {
      this.resetTagDialog();
    },
  },

  props: ["tags"],
};
</script>
<style scoped>
body {
  color: #e8eaed;
  direction: ltr;
  font-family: "Roboto", arial, sans-serif;
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
  transition-property: width, box-shadow, border-radius;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  width: 280px;
  z-index: 985;
}
</style>