<template>
    <tr :class="{ complete: complete }">
        <td>{{ title }}</td>
        <td>{{ formatDate(created_at) }}</td>
        <td><input @click="toggleTaskComplete(index)" type="checkbox" :checked="complete"></td>
        <td><button @click="deleteTask(task, index)">Delete</button></td>
    </tr>
</template>

<script>
import moment from 'moment';
import { api } from '../axios-api'

export default {
    name: "ItemRow",
    data() {
        return {
            complete: this.task.complete,
            title: this.task.title,
            created_at: this.task.created_at,
            id: this.task.id,
        }
    },
    props: {
        task: {
            type: Object,
            required: true,
        },
        index: {
            type: Number,
            required: true,
        }
    },
    methods: {
        async toggleTaskComplete(index) {
            const response = await api.patch(`tasks/${this.id}/`, { complete: !this.complete })
            const complete = await response.data.complete
            this.complete = complete
            this.$emit('complete', index, complete)
        },
        async deleteTask(task, index) {
            const apiDelete = await api.delete(`tasks/${task.id}/`)
            if (apiDelete.status == 204 ) {
                this.$emit('deleted', index)
            }
        },
        formatDate(date) {
            return moment(date).calendar();
        },
    }
}
</script>

<style lang="scss" scoped>
tr {
    &.complete {
       background-color: rgba(0, 0, 0, .25); 
    }

    td {
        width: 150px;
        text-align: center;
        padding: 10px 0;

        button {
            border: 0;
            background-color: hsl(348, 100%, 61%);
            color: #fff;
            height: 25px;
            cursor: pointer;

            &:hover {
                background-color: hsl(348, 100%, 46%);
            }
        }
    }
}
</style>