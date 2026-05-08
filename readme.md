2026-05-08
当前虚拟环境改为data_project
今日复习
1. conda命令
conda init powershell
conda create -n env名 python=3.11
conda activate env名
2.conda虚拟环境下创建文件
New-Item app\main.py
3.启动服务的命令
uvicorn app.main:app --reload
