# 当前虚拟环境名：data_project
# 打开当前项目步骤
# 1. 进入当前项目在当前电脑的路径，如：C:\files\python_project\2026_data_project
# 2. 激活当前虚拟环境：conda activate data_project
# 3. 运行项目：uvicorn app.main:app --reload

# 第三方接口
# https://developer.adzuna.com/overview app_id=7df9e5e2, app_key=96e2c01bc2c5f010ddc6b84ce0b6fc11
# http://api.adzuna.com/v1/api/jobs/gb/version?app_id={YOUR API ID}&app_key={YOUR API KEY}&&content-type=application/json


# 2026-05-08
# 今日复习
# 1. conda命令
conda init powershell
conda create -n env名 python=3.11
conda activate env名
# 2.conda虚拟环境下创建文件
New-Item app\main.py
# 3.启动服务的命令
uvicorn app.main:app --reload

# 4.git命令
git init
git add .
git commit -m "first commit"

git config --global user.name "yuyuane"
git config --global user.email "yuyuane@163.com"
# 即可commit

git branch -M main
git remote add origin https://github.com/yuyuane/2026_data_project.git
git push -u origin main
# -u（--set-upstream）：建立本地分支与远程分支的跟踪关系，之后可以直接用 git push/git pull

# 后续修改数据后命令为
git add . # 将修改的数据添加到暂存区
git commit -m "备注" # 提交到本地仓库
git push # 推送所有更改的数据

# 2026-05-11
# 今日学习 - 接口开发
# 1. 导出所需的包至requirement.txt
pip freeze > requirements.txt
# 2. 开发接口API，获取数据

# 现存问题
# 1. postgresql未搭建
# 2. 后续需要考虑一键搭建数据库的脚本
# 3. Docker
# 4. 环境变量的更改，区分线上线下的环境，使用.env
# 5. Alembic 主要用于数据库迁移，与2是一致的

# 2026-05-12
# 今日学习 - PostgreSQL
# 默认端口：5432
# Python中文件名和函数名是小写与下划线
# 文件中类名是大驼峰命名法