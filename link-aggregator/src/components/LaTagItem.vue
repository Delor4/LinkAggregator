<template>
    <b-list-group-item :href="uri">
        <b-icon-caret-right></b-icon-caret-right>
        {{name}}
    </b-list-group-item>
</template>

<script>

export default {
    components: {
    },
    props: ['name', 'uri', 'id'],
}
</script>
