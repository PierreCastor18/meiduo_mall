var vm = new Vue({
	el: '#app',
	data: {
		host,
		error_name: false,
		error_password: false,
		error_check_password: false,
		error_phone: false,
		error_allow: false,
		error_image_code: false,
		error_sms_code: false,

		username: '',
		password: '',
		password2: '',
		mobile: '', 
		image_code: '',
		sms_code: '',
		allow: false,

		image_code_id: '',
		image_code_url: '',
		sending_flag: false,
		sms_code_tip: '获取短信验证码',

		error_image_code_message: '请填写图片验证码',
		error_sms_code_message: '请填写短信验证码',
		error_phone_message: '您输入的手机号格式不正确',
		error_name_message: '请输入5-20个字符的用户'
	},
	mounted: function(){

	},
	methods: {
		
		check_username: function (){
			var len = this.username.length;
			if(len<5||len>20) {
				this.error_name = true;
			} else {
                this.error_name_message = '请输入5-20个字符的用户名';
				this.error_name = false;
			}
			// 检查重名
			if (this.error_name == false) {
				axios.get(this.host+'/usernames/' + this.username + '/count/', {
						responseType: 'json'
					})
					.then(response => {
						if (response.data.count > 0) {
							this.error_name_message = '用户名已存在';
							this.error_name = true;
						} else {
							this.error_name = false;
						}
					})
					.catch(error => {
						console.log(error.response.data);
					})
			}
		},
		check_pwd: function (){
			var len = this.password.length;
			if(len<8||len>20){
				this.error_password = true;
			} else {
				this.error_password = false;
			}		
		},
		check_cpwd: function (){
			if(this.password!=this.password2) {
				this.error_check_password = true;
			} else {
				this.error_check_password = false;
			}		
		},
		check_phone: function (){
			var re = /^1[345789]\d{9}$/;
			if(re.test(this.mobile)) {
				this.error_phone = false;
			} else {
                this.error_phone_message = '您输入的手机号格式不正确';
				this.error_phone = true;
			}
			if (this.error_phone == false) {
				axios.get(this.host+'/mobiles/'+ this.mobile + '/count/', {
						responseType: 'json'
					})
					.then(response => {
						if (response.data.count > 0) {
							this.error_phone_message = '手机号已存在';
							this.error_phone = true;
						} else {
							this.error_phone = false;
						}
					})
					.catch(error => {
						console.log(error.response.data);
					})
			}
		},
		check_image_code: function (){
			if(!this.image_code) {
				this.error_image_code = true;
			} else {
				this.error_image_code = false;
			}	
		},
		check_sms_code: function(){
			if(!this.sms_code){
				this.error_sms_code = true;
			} else {
				this.error_sms_code = false;
			}
		},
		check_allow: function(){
			if(!this.allow) {
				this.error_allow = true;
			} else {
				this.error_allow = false;
			}
		},
		// 注册
		on_submit: function(){
			this.check_username();
			this.check_pwd();
			this.check_cpwd();
			this.check_phone();
			this.check_sms_code();
			this.check_allow();


			if(this.error_name == false && this.error_password == false && this.error_check_password == false
				&& this.error_phone == false && this.error_sms_code == false && this.error_allow == false) {
				axios.post(this.host+'/users/', {
						username: this.username,
						password: this.password,
						password2: this.password2,
						mobile: this.mobile,
						sms_code: this.sms_code,
						allow: this.allow.toString()
					}, {
						responseType: 'json'
					})
					.then(response => {
						// 保存后端返回的token数据
						localStorage.token = response.data.token;
						localStorage.username = response.data.username;
						localStorage.user_id = response.data.user_id;

						location.href = '/index.html';
					})
					.catch(error=> {
						if (error.response.status == 400) {
							this.error_sms_code_message = '短信验证码错误';
							this.error_sms_code = true;
						} else {
							console.log(error.response.data);
						}
					})
			}
		},
		// 发送短信验证码
		send_sms_code: function () {
			if (this.sending_flag == true) {
				return;
			}
			this.sending_flag = true;

			// 校验参数，保证输入框有数据填写
			this.check_phone();
			

			if (this.error_phone == true || this.error_image_code == true) {
				this.sending_flag = false;
				return;
			}

			// 向后端接口发送请求，让后端发送短信验证码
			axios.get(this.host+'/sms_codes/' + this.mobile + '/', {
					// 向后端声明，请返回json数据
					responseType: 'json'
				})
				.then(response => {
					// 表示后端发送短信成功
					// 倒计时60秒，60秒后允许用户再次点击发送短信验证码的按钮
					var num = 60;
					// 设置一个计时器
					var t = setInterval(() => {
						if (num == 1) {
							// 如果计时器到最后, 清除计时器对象
							clearInterval(t);
							// 将点击获取验证码的按钮展示的文本回复成原始文本
							this.sms_code_tip = '获取短信验证码';
							// 将点击按钮的onclick事件函数恢复回去
							this.sending_flag = false;
						} else {
							num -= 1;
							// 展示倒计时信息
							this.sms_code_tip = num + '秒';
						}
					}, 1000, 60)
				})
				.catch(error => {
					if (error.response.status == 400) {
	
						this.error_image_code = true;
					} else {
						console.log(error.response.data);
					}
					this.sending_flag = false;
				})
        }

	}
});










