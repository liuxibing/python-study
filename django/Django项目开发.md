## Django项目开发实践

### Django概述

Python的Web框架有上百个，比它的关键字还要多。通过这些Web框架，我们可以化繁为简，降低创建、更新、扩展应用程序的工作量。刚才我们说到Python有上百个Web框架，这些框架包括Django、Flask、Tornado、Sanic、Pyramid、Bottle、Web2py、web.py等。

在上述Python的Web框架中，Django、Flask和Tornado无疑是最有代表性的重量级选手。这节主要是实践Django开发，开发者可以基于Django快速的开发可靠的Web应用程序，因为它减少了Web开发中不必要的开销，对常用的设计和开发模式进行了封装，并对MVC架构提供了支持（Django中称之为MTV架构）。许多成功的网站和应用都是基于Django框架构建的，国内比较有代表性的网站包括：知乎、豆瓣网、果壳网、搜狐闪电邮箱、101围棋网、海报时尚网、背书吧、堆糖、手机搜狐网、咕咚、爱福窝、果库等。

### 快速入门

#### 安装Django管理工具
```shell
pip3 install django
django-admin --version
```

默认安装了django最新版本 3.0.4


#### 创建Django项目
```shell
django-admin startproject k12

```

- `manage.py`： 一个让你可以管理Django项目的工具程序。
- `k12/__init__.py`：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
- `k12/settings.py`：Django项目的配置文件。
- `k12/urls.py`：Django项目的URL声明（URL映射），就像是你的网站的“目录”。
- `k12/wsgi.py`：项目运行在WSGI兼容Web服务器上的接口文件。

> 说明：上面使用了Python自带的venv模块完成了虚拟环境的创建，在Windows环境下可以通过"venv/Scripts/activate"执行批处理文件来实现。

```Shell
cd k12
python -m venv venv
venv/Scripts/activate
```

> 说明：在项目中，也可以在不激活的情况下使用venv，只是在每次执行python相关的命令时，指定用venv中的python相关命令执行文件。

在项目环境中，安装Django和mysqlclient包
```Shell
.\venv\Scripts\pip install django mysqlclient
```
> 说明：Django项目中默认通过mysqlclient来访问mysql数据库，所以先要安装mysqlclient，从而避免Django找不到连接MySQL的客户端工具而询问你：“Did you install mysqlclient? ”（你安装了mysqlclient吗？）。

##### 启动Django自带的服务器
```shell
.\venv\Scripts\python manage.py runserver
```

在浏览器中输入<http://127.0.0.1:8000>访问服务器。

> **说明1**：刚刚启动的是Django自带的用于开发和测试的服务器，它是一个用纯Python编写的轻量级Web服务器，但它并不是真正意义上的生产级别的服务器，千万不要将这个服务器用于和生产环境相关的任何地方。
>
> **说明2**：用于开发的服务器在需要的情况下会对每一次的访问请求重新载入一遍Python代码。所以你不需要为了让修改的代码生效而频繁的重新启动服务器。然而，一些动作，比如添加新文件，将不会触发自动重新加载，这时你得自己手动重启服务器。
>
> **说明3**：可以通过`python manage.py help`命令查看可用命令列表；在启动服务器时，也可以通过`python manage.py runserver 127.0.0.1:8000`来指定将服务器运行于哪个IP地址和端口。
>
> **说明4**：可以通过Ctrl+C来终止服务器的运行。

##### 修改项目的配置文件settings.py
1. 语言和时区设置
```Python
# 此处省略上面的内容

# 设置语言代码
LANGUAGE_CODE = 'zh-hans'
# 设置时区
TIME_ZONE = 'Asia/Chongqing'

# 此处省略下面的内容
```

刷新刚才的页面，可以看到修改语言代码和时区之后的结果。 

> 说明：Django是一个支持国际化和本地化的框架，因此刚才我们看到的默认首页也是支持国际化的，我们将默认语言修改为中文，时区设置为东八区。

2. 数据库设置
```Python
# 此处省略上面的代码
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'k12',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '',
    }
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# 此处省略下面的代码
```

新生成的Django项目，默认配置为sqlite。其实，在配置ENGINE属性时，常用的可选值包括：
- `'django.db.backends.sqlite3'`：SQLite嵌入式数据库。
- `'django.db.backends.postgresql'`：BSD许可证下发行的开源关系型数据库产品。
- `'django.db.backends.mysql'`：转手多次目前属于甲骨文公司的经济高效的数据库产品。
- `'django.db.backends.oracle'`：甲骨文公司的关系型数据库旗舰产品。

我选用的是mysql，配置参数有：NAME属性代表数据库的名称，如果使用SQLite它对应着一个文件，在这种情况下NAME的属性值应该是一个绝对路径；使用其他关系型数据库，则要配置对应的HOST（主机）、PORT（端口）、USER（用户名）、PASSWORD（口令）等属性。

#### 启用Django后台管理
Django框架有自带的后台管理系统来实现对模型的管理。虽然实际应用中，这个后台可能并不能满足我们的需求，但是在学习Django框架时，我们暂时可以利用Django自带的后台管理系统来管理我们的模型，同时也可以了解一个项目的后台管理系统到底需要哪些功能。

##### 激活Django框架本身有自带的数据模型
```Shell
.\venv\Scripts\python .\manage.py migrate
```

##### 创建超级管理员账号。
```Shell
.\venv\Scripts\python manage.py createsuperuser
```

##### 启动Web服务器，登录后台管理系统。
```Shell
.\venv\Scripts\python manage.py runserver
```

访问<http://127.0.0.1:8000/admin>

### 创建项目应用
- 创建名为tiku（题库系统）的应用，一个Django项目可以包含一个或多个应用。
    ```Shell
    .\venv\Scripts\python manage.py startapp hrs
    ```

   执行上面的命令会在当前路径下创建tiku目录，其目录结构如下所示：

   - `__init__.py`：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
   - `admin.py`：可以用来注册模型，用于在Django的管理界面管理模型。
   -  `apps.py`：当前应用的配置文件。
   - `migrations`：存放与模型有关的数据库迁移信息。
     - `__init__.py`：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
   - `models.py`：存放应用的数据模型，即实体类及其之间的关系（MVC/MTV中的M）。
   - `tests.py`：包含测试应用各项功能的测试类和测试函数。
   - `views.py`：处理请求并返回响应的函数（MVC中的C，MTV中的V）。

- 创建模型或反向生成模型类
    在 Django 里写一个数据库驱动的 Web 应用的第一步是定义模型 – 也就是数据库结构设计和附加的其它元数据。 

    但真正做项目时，数据库设计是现行进行的，在创建好数据库和表的基础上，Django提供了inspectdb管理工具在django中反向生成mysql model代码。

    ```Shell
    .\venv\Scripts\python .\manage.py inspectdb table [papers] >tiku/models.py
    ```

    > 说明：inspectdb的项目用法可以查看其帮助说明 (`inspectdb --help`)。

- 激活应用
    Django 应用是“可插拔”的。你可以在多个项目中使用同一个应用。除此之外，你还可以发布自己的应用，因为它们并不会被绑定到当前安装的 Django 上。 为了在我们的工程中包含这个应用，我们需要在配置类 INSTALLED_APPS 中添加设置。因为 TikuConfig 类写在文件 tiku/apps.py 中，所以它的点式路径是 'tiku.apps.TikuConfig'。在文件 k12/settings.py 中 INSTALLED_APPS 子项添加点式路径后，它看起来像这样： 

    ```Python
    INSTALLED_APPS = [  
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # 激活项目应用
        'tiku.apps.TikuConfig',
    ]
   ```

    现在你的 Django 项目会包含 tiku 应用。接着运行下面的命令： 

    ```Shell
    .\venv\Scripts\python .\manage.py makemigrations tiku
    ```

    通过运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次迁移。让我们看看迁移命令会执行哪些 SQL 语句。sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL： 
    ```Shell
    .\venv\Scripts\python .\manage.py sqlmigrate tiku 0001 
    ```

    你将会看到类似下面这样的输出（我把输出重组成了人类可读的格式）：

    ```Sql
    --
    -- Create model Papers
    --
    CREATE TABLE `tiku_papers` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `paper_title` varchar(255) NOT NULL, `paper_url` varchar(255) NOT NULL UNIQUE, `paper_type` varchar(16) NOT NULL, `province` varchar(16) NOT NULL, `grade` varchar(16) NOT NULL, `zujuan_id` bigint NOT NULL, `crawled` integer NOT NULL);
    ``` 

    前面我们是根据已有数据库表反向生成的模型。如果是我们新建的模型或在开发过程中修改了模型，除了用makemigrations和sqlmigrate查看修改及数据库迁移sql外，还可以用migrate把项目中没有执行过的迁移同步到数据库中。

    ```Shell
    .\venv\Scripts\python .\manage.py migrate 
    ```
    
- 注册模型类并加入Django后台管理(tiku\admin.py)
    ```Python
    # Register your models here.
    from tiku.models import Papers, Questions, PagerQuestions

    class PapersAdmin(admin.ModelAdmin):
        list_display = ('id', 'paper_title', 'paper_url', 'paper_type')

    class QuestionsAdmin(admin.ModelAdmin):
        list_display = ('id', 'question_name', 'question_url', 'question_type')

    admin.site.register(Papers, PapersAdmin)
    admin.site.register(Questions, QuestionsAdmin)
    admin.site.register(PagerQuestions)
   ```

   注册模型类后，就可以在后台管理系统中看到它们。

#### 添加前端页面展示
