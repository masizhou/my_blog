# 简单的个人博客开发


# 一、效果展示：

## 1.1 注册页面


![image](https://user-images.githubusercontent.com/56242720/111177978-b116d280-85e5-11eb-8cd5-3539c0ddf4e6.png)



## 1.2 登录页面
![image](https://user-images.githubusercontent.com/56242720/111178263-ecb19c80-85e5-11eb-891e-657a45a88a26.png)


## 1.3 忘记密码页面
![image](https://user-images.githubusercontent.com/56242720/111178363-05ba4d80-85e6-11eb-825f-6fbb7bfc440e.png)


## 1.4 论坛主页
![image](https://user-images.githubusercontent.com/56242720/111178467-2387b280-85e6-11eb-955d-b3c651c50d41.png)



## 1.5 浏览文章及评论页面
![image](https://user-images.githubusercontent.com/56242720/111178548-3ef2bd80-85e6-11eb-9959-bed57bbd7a6d.png)

![image](https://user-images.githubusercontent.com/56242720/111178624-50d46080-85e6-11eb-9924-513af865df8f.png)


## 1.6 个人信息修改页面
![image](https://user-images.githubusercontent.com/56242720/111178708-6184d680-85e6-11eb-8ef6-d91e95347c77.png)



## 1.7 写文章页面
![image](https://user-images.githubusercontent.com/56242720/111178806-75c8d380-85e6-11eb-9958-c323cd4cff91.png)


## 1.8 后台管理页面

![image](https://user-images.githubusercontent.com/56242720/111865620-1a5e6300-89a3-11eb-9e25-efa870c93bb4.png)





# 二、环境配置

**安装以下数据库和包：**

## 2.1 数据库

```bash
mysql5.5

redis3.2.1
```



## 2.2 解释器和包

```python
pip install python==3.6
pip install django==2.0
pip install PyMySQL
pip install django-redis
```



# 三、数据库设置

## 3.1 建表
进入setting.py,将下面的内容改为自己的数据库配置：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 数据库引擎
        'HOST': '127.0.0.1', # 数据库主机
        'PORT': 3306, # 数据库端口
        'USER': 'msz', # 数据库用户名
        'PASSWORD': '123456', # 数据库用户密码
        'NAME': 'msz_blog' # 数据库名字
    },
}
```
然后建立数据库

最后执行进入manage.py所在的目录，执行：
```python
python manage.py makemigrations
python manage.py migrate
```


## 3.2 后台登录密码

手机号：**17393176178**

密码：fec12345







