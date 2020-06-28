> 当前项目所使用环境：Python2.7，Django1.11.0

# 项目介绍
##### 1. 后端语言：Python + Django
##### 2. 前端语言：HTML + JavaScript + Bootstrap
##### 3. 数据库：MySQL + Redis

# 实现功能
##### 1. 未使用Django-admin，自己手写的管理后台, 用于文章、友链和背景音乐等的在线管理
##### 2. 实现文章按年月，分类归档
##### 3. 实现文章标签云功能
##### 4. 实现标签云功能
##### 5. 后台引入wangEditor富文本编辑器和editor.md Markdown编辑器，前端使用prism.js进行代码高亮
##### 6. Celery + Redis + Supervisor进行异步任务和定时任务的启动和进程管理
##### 7. 接入[七牛云存储](https://www.qiniu.com/)，文章中的图片通过接口上传到七牛云

# 项目部署
> 本项目的部署是在CentOS 7.2的系统上，其他CentOS发行版本或者类Unix系统的部署中可能有不同，请知悉。
      

1. 首先更新系统环境到最新，使其得到更好的兼容
```bash
yum -y update  # 检查是否有可用更新
yum -y upgrade  # 应用更新
```    
2. 克隆项目
```bash
git clone https://github.com/runtaojiao/my-site.git
```    
3. 在项目根目录下创建项目所需要的文件夹
```bash
mkdir logs  # 用来存储项目日志
```    
4. 新建`local_settings.py`用来覆盖`settings.py`里面的数据库配置
```bash
cp -r my_site/local_settings.py.template local_settings.py
```
5. 进入数据库创建数据库
```bash
CREATE DATABASE `my-site` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
```
6. 同步数据库
```bash
python manage.py migrate
```
7. 安装项目所需要的包
```bash
pip install -r requirements.txt
```
8. 因为本项目使用了Redis，所以需要安装redis-server
```bash
yum -y install redis-server  # 安装
redis-server &  # 启动Redis-server
```
9. 运行项目
```bash
python manage.py runserver
```
10. 创建管理员
```bash
python manage.py createsuperuser
```
正常情况下，经过以下步骤，就可以通过 `127.0.0.1:8000` 来访问博客首页了，通过  `127.0.0.1:8000/manager` 访问管理端

# 注意事项
1. 本文档可能尚有遗漏或者不当之处，如遇问题，如造成困惑请尽量自行处理或者联系作者，敬请谅解。
2. 项目中涉及到的配置文件，如七牛云的 `access_key` 和 `secret_key`账号的配置，烦请自行注册账号修改，否则侵权必究。

# 联系我
1. 邮箱：heavycross@163.com
2. QQ: 962069483

**本人博客地址:** [我的博客](http://runtao.sndz.top)
