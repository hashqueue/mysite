## 学习Django官网投票项目的Demo
### 如何运行项目
* clone此项目到本地
    ```bash
    https://github.com/passerby223/mysite.git
    ```
* 创建一个Python虚拟环境并激活虚拟环境，然后安装项目所需依赖包
    ```bash
    python3 -m venv ~/.virtualenvs/mysite
    source ~/.virtualenvs/mysite1/bin/activate
    cd PycharmProjects/mysite/
    pip3 install -i https://pypi.douban.com/simple -r requirements.txt
    ```
* 项目根目录下进行数据迁移
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
* 项目根目录下运行项目
    ```bash
    python3 manage.py runserver
    ```
* 浏览器中
    * [http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/) 访问项目首页
    * [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) 访问项目管理后台，要访问管理后台前需要先创建一个超级管理员账号，可通过`python3 manage.py createsuperuser`命令来创建超级管理员,然后通过这个管理员账号登录后台即可。
