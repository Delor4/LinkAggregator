<template>
    <b-list-group-item>
        <a :href="uri">
            <b-icon-caret-right></b-icon-caret-right>
            {{name}}
        </a>
        <b-icon-x-circle class="pull-right" role="button" v-on:click="$emit('remove-tag', id)"></b-icon-x-circle>
    </b-list-group-item>
</template>

<script>

export default {
    components: {
    },
    props: ['name', 'uri', 'id'],
}
</script>
