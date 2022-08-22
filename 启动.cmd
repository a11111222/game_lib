chcp 65001
@echo off
git add .
set/p option=分支名字输入:
git commit -m "%option%"