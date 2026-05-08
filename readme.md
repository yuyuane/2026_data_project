# 2026-05-08
# 当前虚拟环境改为data_project
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