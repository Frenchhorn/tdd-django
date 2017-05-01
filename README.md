## 环境
Python 3.5.3
Django 1.11

## django相关的命令
### 启动服务器
`manage.py runserver`

### 进行所有测试
`manage.py test`

### 进行功能测试
~~python manage.py functional_tests.py~~
`manage.py test functional_tests`

### 测试某一应用
`manage.py test [appname]`

### 记录models.py的改动
`manage.py makemigrations`

### 将改动作用到数据库
`manage.py migrate`
`manage.py migrate --noinput`

### 收集静态文件
`manage.py collectstatic`
>相关设置在settings.py下的STATIC_URL与STATIC_ROOT

## 部署相关
### 添加用户
`sudo useradd -m -s /bin/bash elspeth`
>用户名为elspeth, -m表示创建家目录, -s表示默认能用bash
### 添加权限
`sudo usermod -a -G sudo elspeth`
>把elspeth添加到sudo用户组
### 设置密码
`sudo passwd elspeth`
### 切换当前用户
`su - elspeth`

### 安装Nginx
`sudo apt-get install nginx`
### 开启Nginx服务器
`sudo service nginx start`



## 备注
* 使用LESS定制Bootstrap
* 使用{% static %}模板标签
* 客户端打包工具，例如bower