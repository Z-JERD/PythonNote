# 远程仓库：
## git clone

    克隆远程仓库, 名称自定义为origin, 并在本地创建master分支

    git clone url

    EX：
        git clone https://github.com/schacon/ticgit

## git clone -b

    克隆指定的分支：git clone -b 分支名 仓库地址

    EX:
        git clone -b dev https://github.com/schacon/ticgit
   
    克隆某分支到本地目录，然后在该目录下push时，对应的就是push到远端的对应分支。


## 查看远程仓库：

        git remote

    查看远程仓库及对应的地址:
        
        git remote -v

    添加远程仓库：

        git remote add <shortname> <url>

        ex:
        
            git remote add pb https://github.com/paulboone/ticgit

    移出远程仓库:

        git remote remove <shortname>

        EX:
            git remote remove pb

# 查看本地分支及追踪的分支：

    ex：
        [root@localhost gitdemo]# git branch -vv
            dev20210508  d8c2f58 [origin/dev] update m_demo
            iss20210508  9f6f384 调整顺序
            * master       9f6f384 [origin/master] 调整顺序
            test20210508 ba0e01a branch test modify m1_demo

    master       分支跟踪   origin/master

    dev20210508  分支跟踪   origin/dev

    在master分支下创建新分支, 分支中的内容和master中的一致

    在dev20210508分支下创建新分支, 分支中的内容和dev20210508中的一致

    删除master下建的分支, 需先切换到master分支下
    删除dev20210508r下建的分支, 需先切换到dev20210508r分支下


# git pull，git pull --rebase 之间的区别

    参考文档：https://www.cnblogs.com/kevingrace/p/5896706.html

## git pull 和 git fetch 关系:

    git fetch: 拉取代码到本地
   
    git pull = git fetch + git merge
   
    git pull --rebase = git fetch + git rebase

## git pull

    git pull 命令默认包含了一个 --merge 参数, 执行 git pull 后，代码会自动 merge 到本地的分支中

    merge 会创建一个新的 commit，如果合并时遇到了冲突，需要解决冲突后重新 commit

## git pull --rebase

    rebase 会将两个分支进行合并，同时合并之前的 commit 历史。如果出现冲突，不用执行git-commit，
    解决冲突后执行以下命令即可:
    
    git add
    
    git rebase --continue   

    git rebase --abort           终止rebase的行动

## 两者的选择

    如果想要一个干净的，没有 merge commit 的线性历史树，那么你应该选择 git rebase
    
    如果想保留完整的历史记录，并且想要避免重写 commit history 的风险，你应该选择使用 git merge

# git push

    git pull <远程主机名> <远程分支名>:<本地分支名>

    git push <远程主机名> <本地分支名>:<远程分支名>


## git push origin master

    本地的master分支推送到origin主机的master分支。如果master不存在，则会被新建

## git push origin

    如果当前分支与远程分支之间存在追踪关系，则本地分支和远程分支都可以省略

    EX: 
        
        * master       9f6f384 [origin/master]

        本地master分支与远程master分支相对应, 在master分支下执行此命令, 则直接推送到远程仓库

## git push

    当前分支只有一个追踪分支，那么主机名都可以省略

    使用 git branch -vv 查看追踪分支的个数

## git push -u origin master
    
    如果当前分支与多个主机存在追踪关系，则可以使用-u选项指定一个默认主机

    将本地的master分支推送到origin主机，同时指定origin为默认主机，后面就可以不加任何参数使用git push

## git push origin --delete master

    删除远程仓库中的master分支

# 分支操作（branch）

## 查看分支：

### 1. git branch

    列出本地已经存在的分支，并且在当前分支的前面用*标记

    ex：
        [root@localhost gitdemo]# git branch
            dev20210508
            * master

### 2. git branch -a
    
    查看所有分支列表，包括本地和远程，远程分支一般会用红色字体标记出来

    ex: remotes开头的都是远程分支

        root@localhost gitdemo]# git branch -a
            dev20210508
            * master
            remotes/origin/HEAD -> origin/master
            remotes/origin/dev
            remotes/origin/master

## 创建/切换分支

    默认创建的分支是和远程仓库中的master分支关联

### 1. 本地创建分支
    
    git branch xxx

    ex:
        git branch test20210508

    查看：
        [root@localhost gitdemo]# git branch
            dev20210508
            * master
            test2021050

### 2. 切换分支：
    
    git checkout  xxx

    ex:
        git checkout test20210508

    查看:
        [root@localhost gitdemo]# git branch
            dev20210508
            master
            * test20210508

### 3. 创建并切换分支：

    git checkout -b xxx

    ex：
        git checkout -b test202105081432

        等同于：
            
            git branch test202105081432

            git checkout test202105081432

### 4. 删除分支

    git branch -d xxx

    ex:

        git branch -d  test202105081432

## git切换到指定远程分支

    应用场景：拉取远程仓库中的其他分支例（dev分支）, 在本地创建devlocal分支, 修改后
             推送到远程仓库

### 新建分支并切换到指定分支
    
    git checkout -b 本地分支名 origin/远程分支名


### 将本地分支推送到远程
    
    git push <远程主机名> <本地分支名>:<远程分支名>

### ex：

    查看所有分支:

        [root@localhost gitdemo]# git branch -a
            dev20210508
            * master
            test20210508
            remotes/origin/HEAD -> origin/master
            remotes/origin/dev
            remotes/origin/master

：
    1. 新建分支
        git checkout -b iss20210430 origin/dev

    2. 修改文件

        vim m_demo.py

    3. 提交
        
        git add m_demo.py

        git commit -m 'update m_demo'

    4. 推送到远程仓库：

        git push -u origin iss20210430:dev

## 分支合并

    1. 本地创建新的分支

        git checkout -b  test

    2. 修改文件

        vim m1_demo.py

    3. 提交

        git add m1_demo.py
        git commit -m 'branch test modify m1_demo'
    
    4. 切换到master分支
        
        git checkout master

    5. 合并test分支
        
        git merge test

        自动merge失败, 需要手动解决冲突，修改代码后, 需要重新 add 和 commit

    6. 拉取远程仓库最新代码

        git pull origin master

    7. 推送到远程仓库
        
        git push origin master
