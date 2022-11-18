<template>
  <div>
    <h1>Da uma olhada nos mthods nesta página</h1>
    <input type="text" placeholder="Primeiro atributo" v-model="atributoUm"/>
    <input type="text" placeholder="Segundo atributo" v-model="atributoDois"/>
    <button v-on:click="post">POST</button>
    <input type="text" placeholder="ID para exclusão" v-model="id"/>
    <button v-on:click="deleteAPi">DELETE</button>
  </div>
</template>

<script>

export default {
  name: 'IndexPage',

  data(){
    return{
      atributoUm: '',
      atributoDois: '',
      id: ''
    }
  },

  methods:{

    //POST
    post: function(){

      const body = [
        {
        atributoUm: this.atributoUm,
        atributoDois: this.atributoDois
        },
      ];

      this.$axios.post(this.$store.state.BASE_URL + '/caminhodaurl/', body).then((response) => {

        alert("Voce enviou os dados para api")

      }).catch((error) => {

        console.log(error)

      })

    },

    //Delete
    deleteAPi: function(){

      this.$axios.delete(this.$store.state.BASE_URL + '/caminhodaurl/' + this.id).then((response) => {

        alert("Voce deletou os dados da api")

      }).catch((error) => {

        console.log(error)

      })

    }


  }



}

</script>
