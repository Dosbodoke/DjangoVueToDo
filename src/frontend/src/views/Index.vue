<template>
    <div id="index">
        <div class="container">
            <div class="card">
                <div class="card-header">
                    <div class="card-header-title">
                        TO-DO
                    </div>
                    <div class="card-header-input">
                        <input type="text" v-model="newTask" @keyup.enter="createTask(newTask)">
                        <button @click="createTask(newTask)">Create</button>
                    </div>
                </div>
                <div class="card-content">
                    <table>
                        <thead>
                            <th @click="reOrder('Title')">Title <span :class="orderedBy == 'Title' ? 'arrow-down': 'arrow-up' "></span></th>
                            <th @click="reOrder('Created At')">Created At <span :class="orderedBy == 'Created At' ? 'arrow-down': 'arrow-up' "></span></th>
                            <th @click="reOrder('Completed')">Completed <span :class="orderedBy == 'Completed' ? 'arrow-down': 'arrow-up' "></span></th>
                            <th>Delete</th>
                        </thead>
                        <tbody>
                            <ItemRow 
                                v-for="(task, index) in APIData"
                                :key="task.id"
                                :task="task"
                                :index="index"
                                @deleted="deleteData"
                                @complete="toggleComplete"
                                class="item-row"
                            />
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { api } from '../axios-api'
import ItemRow from '../components/ItemRow.vue'

export default {
    name: 'index',
    components: {
        ItemRow,
    },
    data() {
        return {
            orderedBy: 'Created At',
            newTask: '',
            APIData: [],
        }
    },
    created() {
        api.get('tasks/',)
          .then(response => {this.APIData = response.data})
    },
    methods: {
        createTask(title) {
            api.post('tasks/', {title: title})
              .then((response) => {
                  this.APIData.unshift(response.data)
                  this.newTask = ''
              })
        },
        deleteData(index) {
            this.APIData.splice(index, 1)
        },
        toggleComplete(index, complete) {
            this.APIData[index].complete = complete  
            if (this.orderedBy === 'Completed') this.reOrder('Completed')
        },
        reOrder(str) {
            this.orderedBy = str;
            switch(str) {
                case 'Title':
                    this.APIData.sort((a, b) => {
                        var titleA = a.title.toUpperCase()
                        var titleB = b.title.toUpperCase()
                        if (titleA < titleB) {
                            return -1;
                        }
                        return 1
                    })
                    break;
                
                case 'Created At':
                    this.APIData.sort((a, b) => {
                        var dateA = a.created_at
                        var dateB = b.created_at
                        if (dateA < dateB) {
                            return -1
                        }
                        return 1
                    })
                    break

                case 'Completed':
                    this.APIData.sort((a, b) => {
                        var checkA = a.complete
                        var checkB = b.complete
                        return (checkA === checkB)? 0 : checkA ? 1 : -1;
                    })
                    break
            }
        },
    }
}
</script>

<style lang="scss" scoped>
.container {
    max-width: 920px;
    margin: 0 auto;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;

    .card {
        box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
        padding: 25px;

        .card-header{

            .card-header-title {
                text-align: center;
            }

            .card-header-input {
                margin: 15px auto;
                display: flex;
                justify-content: center;
                gap: 5px;

                button {
                    background-color: hsl(141, 53%, 53%);
                    border: 0;
                    color: #fff;
                    height: 30px;
                    width: 90px;  
                }
            }
        }

        .card-content {
            table {
                border-collapse: collapse;

                th {
                    width: 150px;
                    text-align: center;

                    .arrow-up, .arrow-down {
                        display: inline-block;
                        width: 0;
                        height: 0;
                        border-left: 5px solid transparent;
                        border-right: 5px solid transparent;
                    }

                    .arrow-up {
                        border-bottom: 5px solid rgba(0, 0, 0, .4);
                    }

                        .arrow-down {
                        border-top: 5px solid hsl(141, 53%, 53%);
                    }
                }
            }
        }
    }
}
</style>