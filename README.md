## 环境
Python 3.5.3
Django 1.11
Selenium 3.4.0
Gunicorn 19.7.1

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

## 添加用户
`sudo useradd -m -s /bin/bash elspeth`
>用户名为elspeth, -m表示创建家目录, -s表示默认能用bash
### 添加权限
`sudo usermod -a -G sudo elspeth`
>把elspeth添加到sudo用户组
### 设置密码
`sudo passwd elspeth`
### 切换当前用户
`su - elspeth`

## 安装Nginx
`sudo apt-get install nginx`
### 设置Nginx
>在etc/ngnix下设置conf      
### 开启Nginx服务器
`sudo service nginx start`
### 关闭Nginx服务器
`sudo service nginx stop`

### 安装Python, Git, pip
`sudo apt-get install git python3 python3-pip`


## virtualenv的使用
### 安装virtualenv
`sudo pip3 install virtualenv`
### 创建一个独立的Python运行环境
`virtualenv venv`
>该命令会新建一个文件夹venv,文件夹中是自成一体的Python环境
### 进入该环境
>Linux      
`source venv/bin/activate`      
>Window下是运行venv/Scripts下的activate
`cd venv/Scripts`
`activate`
### 在该环境下安装需要的包如:
`pip install django==1.11`
### 保存环境
`pip freeze | requirments.txt`
### 在新环境安装这些包
`pip install -r requirments.txt`
### 退出环境
`deactivate`

## Gunicorn的使用
### 在venv环境安装gunicorn
`pip install gunicorn`
### 启动，如：
`gunicorn superlists.wsgi:application`
### 让Nginx伺服静态文件
>在etc/ngnix下设置conf
### 编写upstart
>在etc/init/gunicorn-tdd-django

## Fabric的使用
### 安装fabric
`pip install fabric`    
>仅支持Python2.5-2.7
### 编写部署脚本
`fab <function_name>,host=SERVER_ADDRESS`


## 备注
* 使用LESS定制Bootstrap
* 使用{% static %}模板标签
* 客户端打包工具，例如bower
* 其它部署工具:Absible, Vagrant, Chef, Puppet, Salt, Juju