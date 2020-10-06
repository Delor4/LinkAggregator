<template>
  <b-link :href="url" class="card-link">link {{ id }}</b-link>
</template>

<script>
module.exports = {
    data: function () {
        return {
        }
    },
    components: {
    },
    props: ['id', 'url']
}
</script>
