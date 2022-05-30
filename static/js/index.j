
const MyNum={
    
        template:
        `<div>
        <span class="input-group-text">$</span>
        <input type="number" class="form-control" aria-label="Amount (to the nearest dollar)" min="min" max="mix"
               v-model="current_val" v-on:input="Validate"/>
        <span class="input-group-text">.00</span>
        </div>`,
        props:['min_val','max_val'],
        data()
        {
            return{
                current_val:this.min_val,
            };
        },
        methods:{
            Validate(){
                console.log('current='+this.current_val+' range='+this.min_val+'-'+this.max_val)
                if(this.current_val<this.min_val)
                {
                    this.current_val=this.min_val
                    console.log('under')
                }
                else if(this.current_val>this.max_val)
                {
                    this.current_val=this.max_val
                    console.log('over')
                }
                else
                {
                    console.log('ok')
                }
                console.log('current='+this.current_val)
            }
        },

};



Vue.createApp({
    components:{
        'my-num':MyNum,        
    },
    data()
    {
        return{
            message:'hello',
            btn_enable:true,
            prices:Array(5).fill(1),
            min:0,
            max:10,
            image:{'none':'0x00'},
        }
    },
    methods:{
        Validate:function(){
            if(this.prices[0]<this.min)
            {
                this.prices[0]=this.min
            }
            else if(this.prices[0]>this.max)
            {
                this.prices[0]=this.max
            }
            
        },
        ///ローカルの画像をPythonで読み込んでbase64にエンコードしたデータを、Vueのデータに入れる
        GetPicture:function(e){
            let self = this//let self=this　は、どうやら定石のようだ
            $.ajax({
                type:'POST',
                url:'/ajax',
            })
            .done(function(data){
                self.image=data
            })
            .fail(function(){
                console.log('error')
            })
        }
    },

    beforeCreate:function(){
        console.log('beforeCreate');
    },
    created:function(){
        console.log('created');
    },
    mounted:function(){
        console.log('mounted🤩');
        console.log(this.prices)
    },
    updated:function(){
        console.log('updated🆙');
    },
    unmouted:function(){
        console.log('UNMOUNTED!🆓')
    },
}).mount('#app');

// setTimeout(function(){
//     //3秒後に消える
//     app.unmount();
// },3000);
