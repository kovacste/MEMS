
function login() {
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    post('/login', { username: username, password: password }).then(response => {
        console.log('user data send to login', response)
    })
}

function post(url, data) {
    return fetch(url, {
        method: "POST",
        body: JSON.stringify(data)
    })
}

var Login = { template:
            '<div> <div>' +
                '<label> Felhasználónév </label>' +
                '<v-text-field label="Felhasználónév" v-model="username"> </v-text-field>'+
            '</div>'+
            '<div>'+
                 '<label> Jelszó </label>'+
                ' <input type="text" v-model="password">'+
            '</div>'+
            '<div>'+
               ' <input type="button" @click=login() value="Belépés">'+
            '</div> </div>',

           data() {
                return {
                    username: 'admin',
                    password: null
                }
           },

           methods: {
                login() {
                    console.log('kamubejelentkezés')
                    this.$router.push('/home')
                }
           }
}

const Home = {
    template: '<div><h1> Otthona állapota </h1> <widget label="Aktuális hőmérséklet" suffix="C°" :value="temp"> </widget> <widget label="Aktuális páratartalom" suffix="%" :value="hum"></widget></div>',
    data() {
        return {
            temp: 0,
            hum: 0,
            timer: null
            REFRESH_INTERVAL_MILLISEC: 5000
        }
    },

    created() {
        this.timer = setInterval(this.refreshData, this.REFRESH_INTERVAL_MILLISEC)
    },

    methods: {
        refreshData() {
            console.log('data refreshed')
            axios.get("/homeData").then(response => {
                console.log(response.data.temp)
                this.temp = response.data.temp
                this.hum = response.data.hum
            })
        }
    },

    beforeDestroy() {
        clearInterval(this.timer)
    }
}

const Beállítások = {
    template : ''
}

const routes = [
  { path: '/', component: Login },
  { path: '/home', component: Home }
]

const router = new VueRouter({
  routes // short for `routes: routes`
})

const Widget = {
    template: '<v-layout row wrap justify-start> <v-flex md5 xs5> {{label}} </v-flex> <v-flex md4 xs4> {{value}} {{suffix}} </v-flex> </v-layout>',
    props: ['label', 'value', 'suffix']
}

Vue.component('widget', Widget)


var app = new Vue({
  el: '#app',
  router,
  data: {
    message: 'Hello Vue!',
    username: '',
    password: ''
  }
})