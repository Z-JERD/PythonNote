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
      


# Git提交代码

    #########################################git 提交代码步骤：########################################################
    
    1. git clone https://github.com/Z-JERD/demo.git
       
       默认获取主分支的代码
       
       获取dev分支的代码： 
            
            git clone -b dev https://github.com/Z-JERD/demo.git
    
    2. git status
            查看文件状态, 如果显示的有.idea目录, 手动删除.idea目录

    3. git add -A 
        
        提交变更的文件
        
        git add demo.py     指定跟踪的文件
        
        git add .           提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件
        
        git add -u          提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)
        
        git add -A          提交所有被删除、被修改和新增的文件到数据暂存区
        
    4. 再次检测 git status
    
    5. git commit -m "modify"
        
        将修改从暂存区提交到本地版本库
        
    6. git pull origin master
        
        从远程获取最新版本并merge到本地
    
    7. git push origin master
        
        将本地版本库的分支推送到远程服务器上对应的分支

# .gitignore
    ####################################定义.gitignore文件####################################################
    
    忽略文件, 在Windows下进行开发, Windows会自动在有图片的目录下生成隐藏的缩略图文件，如果有自定义目录，目录下就会有Desktop.ini文件，因此需要忽略Windows自动生成的垃圾文件：

    在使用IDE进行开发时, 会生成.dea文件, 因此需要定义哪些文件需要忽略掉


    定义一个完整的.gitignore文件，内容如下：
		# Windows:
		Thumbs.db
		ehthumbs.db
		Desktop.ini

		# Python: Python工具需要忽略的文件
		*.py[cod]
		*.so
		*.egg
		*.egg-info
		dist
		build
		.idea

		# My configurations:
		db.ini
		deploy_key_rsa

    如果添加的文件在忽略文件名单里, 但确实想添加该文件，可以用-f强制添加到Git：

    $ git add -f App.class

    ####################################解决提交的文件中的.idea####################################################

    查看当前目录下所有的文件(包括隐藏文件)：ls -a

    1. 若idea目录已提交到远程仓库中 git删除远程.idea目录

        1. git rm 删除：

            1.删除缓存区.idea
                    
                    $ git rm -r .idea
            
            2.将.idea从源代码仓库中删除
                    
                    $ git commit -m "commit and remove .idea"
            
            3.推送到远程端
                    
                    $ git push origin master

        2. 在文件夹中删除

            1. rm  -r .idea

            2. git add .idea

            3. git commit -m "commit and remove .idea"

            4. git push origin master

    2. 将 .idea 将入忽略文件中：

        1. 创建.gitignore
            
            $ touch .gitignore

        2.  编辑.gitignore 
            
            $ vim .gitignore
            添加： .idea

        3. git add .gitignore    提交到暂存区
        
        4. git commit -m 'add gitignore file'
        
        5. git push 
            
# Git rm

    rm     文件

    rm -r  文件夹

## rm 文件

    作用：删除工作区的文件

    1. rm test.txt

    2. git add test.txt

    3. git commit -m "delete test"

    4. git push origin master

    结果： 删除了工作区和版本库的文件

## git rm 文件

    作用： 删除工作区文件，并且将这次删除放入暂存区
    
    注意： 要删除的文件是没有修改过的

    1. git rm test.txt

    2. git commit -m "delete test"

    3. git push origin master

    结果： 删除了工作区和版本库的文件

    git rm -f: 要删除的文件已经修改过

## git rm --cached 文件

    作用：删除暂存区文件，但保留工作区的文件，并且将这次删除放入暂存区

    1. git rm --cached test.txt

    2. git commit -m "delete test"

    3. git push origin master

    结果：删除了暂存区和版本库的文件，但保留了工作区的文件


# Git Tag

    Git 可以给历史中的某一个提交打上标签，以示重要
    使用这个功能来标记发布结点（v1.0 等等）

    拉取指定的版本:
       
       git clone -b v0.1 https://github.com/Z-JERD/demo.git 
        

## 本地创建标签：

    1. 轻量级标签： git tag 标签名称

        EX： git tag v1.4-lw

    2. 附注标签： git tag -a 标签名称 -m 标签描述

        EX：git tag -a v1.4-lw -m 'VERSION1.4'

## 显示本地标签:

    1. 列出所有标签：

        git tag

    2. 查询指定的标签：

        git tag -l 'v1.8.5*'

    3. 查看标签信息：

        git show v1.4-lw

## 删除本地标签

    git tag -d 标签名

    EX:
        git tag -d v0.1.2

## 删除远程仓库的tag：

    git push origin --delete tag 标签名

    EX:

        git push origin --delete tag v0.1.2  

## 拉取远程标签到本地：

    git pull origin --tags 

## Tag推到远程仓库：

    git push origin v0.1.2

    git push origin -–tags        # 将本地所有标签一次性提交到git服务器

    EX:
        
        默认标签是打在最新提交的commit上的

        git add -A

        git commit -m '修改并创建tag'

        git push origin master

        git tag v1.1

        git push origin v1.1

## 补打标签

    如果忘了打标签可以给指定的commit打标签

    找到历史提交的commit id：

        git log --oneline

        git log -10 --oneline                   # 查看前10条提交

        git log --oneline  --since=2.weeks      # 查看最近两周的提交

        EX:
            root@localhost python_linux]# git log --oneline  --since=2.weeks
            95510dd add NginxServer
            d1637f0 Create OpenRestyREAD.md
            2dbdd1a Update README.md

    补打标签：
        
        git tag  v0.1.1 2dbdd1a

    推到远程仓库：

        git push origin v0.1.1

# Git Commit
## 多次commit

    每个commit都会被提交到远程仓库中

    EX: 修改m1_demo和m_demo文件

        1. git status
            
            # On branch master
            # Changes not staged for commit:
            #   (use "git add <file>..." to update what will be committed)
            #   (use "git checkout -- <file>..." to discard changes in working directory)
            #
            #	modified:   m1_demo.py
            #	modified:   m_demo.py

        2. git add m1_demo.py

        3. git commit -m 'update m1_demo'

        4. git add m_demo.py

        5. git commit -m 'update m_demo'

        6. git status
            # On branch master
            # Your branch is ahead of 'origin/master' by 2 commits.
            #   (use "git push" to publish your local commits)

        7. git push origin master

        [root@localhost gitdemo]# git log --oneline
        460cd86 update m_demo
        6a6afd0 update m1_demo


        [root@localhost gitdemo]# git reflog
        460cd86 HEAD@{0}: commit: update m_demo
        6a6afd0 HEAD@{1}: commit: update m1_demo
        c26c4cb HEAD@{2}: commit: update
        44895c8 HEAD@{3}: commit: rm m3_demo.py


## --amend

    会将修改合并到上一次提交，不会产生新的提交

    最后的commit 替换之前的commit, 远程仓库中只有最后一次的commit记录

    EX:

        1. git add m1_demo.py

        2. git commit -m 'insert row in m1_demo'

        3. git add m_demo.py

        4. git commit -m 'insert row in m1_demo m_demo' --amend

            或者：git commit --amend

        5. git push origin master


        [root@localhost gitdemo]#  git log --oneline
        859a55e insert row in m1_demo m_demo
        460cd86 update m_demo
        6a6afd0 update m1_demo
        c26c4cb update
        44895c8 rm m3_demo.py


        [root@localhost gitdemo]#  git reflog
        859a55e HEAD@{0}: commit (amend): insert row in m1_demo m_demo
        a6b3e97 HEAD@{1}: commit: insert row in m1_demo
        460cd86 HEAD@{2}: commit: update m_demo
        6a6afd0 HEAD@{3}: commit: update m1_demo
        c26c4cb HEAD@{4}: commit: update
        44895c8 HEAD@{5}: commit: rm m3_demo.py


# Git Reset

## 整体示意图

    原内容----------------修改过的内容----------------暂存----------------分支
            
        ------------------>自动检测
                         
                         ----------------------->git add
                                    
                                                    --------------->git commit
                                    
                                                <---------- --------git reset --soft 版本号
                   
                    <---------------------git reset head 文件
        
        <-------------git checkout 文件
                    
                    <--------------------=--------------------------git reset --mix 版本号
        
        
        <-----------------------------------------------------------git reset --hard 版本号


## 撤销未commit的操作：

    [root@localhost gitdemo]# tail -n 8 m1_demo.py 
        git push origin master

        git commit 20210514144700

        git commit 20210514150000 m1_demo

    1. 修改m1_demo.py, 添加：git reset test in 2021-05-14 15:15

            [root@localhost gitdemo]# tail -n 8 m1_demo.py 
            git push origin master

            git commit 20210514144700

            git commit 20210514150000 m1_demo

    2.  提交到暂存区：

        git add m1_demo.py

        [root@localhost gitdemo]# git status
        # On branch master
        # Changes to be committed:
        #   (use "git reset HEAD <file>..." to unstage)
        #
        #	modified:   m1_demo.py

### 1. 将文件取消暂存

    git reset HEAD <file>

    EX:

    [root@localhost gitdemo]# git reset HEAD m1_demo.py 
    
    Unstaged changes after reset:
    M	m1_demo.py
    
    [root@localhost gitdemo]# git status
    # On branch master
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #	modified:   m1_demo.py

### 2. 撤销对文件的修改

    git checkout -- <file> 

    EX:

        [root@localhost gitdemo]# git status
            # On branch master
            # Changes not staged for commit:
            #   (use "git add <file>..." to update what will be committed)
            #   (use "git checkout -- <file>..." to discard changes in working directory)
            #
            #	modified:   m1_demo.py
            #
            no changes added to commit (use "git add"and/or "git commit -a")

        [root@localhost gitdemo]# tail -n 8 m1_demo.py 
            git push origin master

            git commit 20210514144700

            git commit 20210514150000 m1_demo

            git reset test in 2021-05-14 15:15

        [root@localhost gitdemo]# git checkout -- m1_demo.py

        [root@localhost gitdemo]# git status
            # On branch master
            nothing to commit, working directory clean
        
        [root@localhost gitdemo]# tail -n 8 m1_demo.py
            git pull origin master

            git push origin master

            git commit 20210514144700

            git commit 20210514150000 m1_demo

## git reset 版本号

    参考文档：https://www.jianshu.com/p/c2ec5f06cf1a

### 1. git reset --hard 版本号

    重置stage区和工作目录

    stage区和工作目录里的内容会被完全重置为和HEAD的新位置相同的内容。换句话说，没有commit的修改会被全部擦掉


### 2. git reset --mixed  版本号

    保留工作目录，并清空暂存区

    工作目录的修改、暂存区的内容以及由 reset 所导致的新的文件差异，都会被放进工作目录

### 3. git reset --soft 版本号  

    保留工作目录和暂存区中的内容，并把因为保留工作目录内容所带来的新的文件差异放进暂存区

# Git Log

    -n      限制日志条目数量

## 1. git log
    
    按时间先后顺序列出所有的提交

    EX:
        # git log
        
        commit 226c419eb9cf63aea71a627e14b62e60f1538225
        Author: zhaoguangfei <zhaoguangfei@example.com>
        Date:   Wed Jan 15 15:23:52 2020 +0800

            更下rsa加密

        commit 3e10d4bcacac54980d95448baf077bd174d21c38
        Author: zhaoguangfei <zhaoguangfei@example.com>
        Date:   Fri Dec 6 11:05:50 2019 +0800

            新增文件处理

## 2. git log -p

    显示每次提交所引入的差异

    EX:

        # git log -p -2
        
        commit 226c419eb9cf63aea71a627e14b62e60f1538225
        Author: zhaoguangfei <zhaoguangfei@example.com>
        Date:   Wed Jan 15 15:23:52 2020 +0800

            更下rsa加密

        diff --git a/rsa_encrypt_decrypt.py b/rsa_encrypt_decrypt.py
        index 89775da..11a1078 100644
        --- a/rsa_encrypt_decrypt.py
        +++ b/rsa_encrypt_decrypt.py
        ..................

## 3. git log --stat

    提交的简略统计信息

    EX:
        # git log --stat -2
        
        commit 226c419eb9cf63aea71a627e14b62e60f1538225
        Author: zhaoguangfei <zhaoguangfei@example.com>
        Date:   Wed Jan 15 15:23:52 2020 +0800

            更下rsa加密

        rsa_encrypt_decrypt.py | 330 ++++++++++++++++++++++++++++++++++----------------------------------------------------
        1 file changed, 129 insertions(+), 201 deletions(-)

        commit 3e10d4bcacac54980d95448baf077bd174d21c38
        Author: zhaoguangfei <zhaoguangfei@example.com>
        Date:   Fri Dec 6 11:05:50 2019 +0800

            新增文件处理

        functions_exception.md | 92 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        1 file changed, 92 insertions(+)

## 4. git log --pretty=oneline

    每个提交放在一行显示

    EX:

        # git log --pretty=oneline -2
        
        226c419eb9cf63aea71a627e14b62e60f1538225 更下rsa加密
        3e10d4bcacac54980d95448baf077bd174d21c38 新增文件处理

## 5. git log --oneline

    简写哈希值并将每个提交放在一行显示

    EX:
        # git log --oneline -2
        
        226c419 更下rsa加密
        3e10d4b 新增文件处理

## 6. git log --since

    限制时间

    EX:  列出最近两周的提交
        
        git log --since=2.weeks --oneline

## 7. 展示分支、合并历史
    
    git log --pretty=format:"%h %s" --graph

## 8. 指定样式

    # git log --pretty=format:"%h - %an, %cr : %s" -2
    
    226c419 - zhaoguangfei, 1 year, 4 months ago : 更下rsa加密
    3e10d4b - zhaoguangfei, 1 year, 5 months ago : 新增文件处理

# Git Reflog

    git log: 是显示当前的HEAD和它的祖先的COMMIT, 在远程仓库中的COMMIT都会显示出来

    git reflog: 根本不遍历HEAD的祖先。它是HEAD所指向的一个顺序的提交列表。reflog并不是repo（仓库）的一部分，它单独存储， 它纯属是本地的


    git reflog 可以查看所有分支的所有操作记录（包括已经被删除的 commit 记录和 reset 的操作）

    例如执行 git reset --hard HEAD~1，退回到上一个版本，用git log则是看不出来被删除的commitid，用git reflog则可以看到被删除的commitid，恢复到被删除的那个版本


# Git Config

## Git 工作区：
    
    工作区（Working Directory）：是可以直接编辑的地方。
    
    暂存区（Stage/Index）：数据暂时存放的区域。
    
    版本库（commit History）：存放已经提交的数据。

    
    工作区的文件 git add 后到暂存区，暂存区的文件 git commit 后到版本库

## Git用户配置:

    1. 查看配置信息

        git config --list

    2.设置用户信息：
		
        1.git config  --global user.name "zhaoguangfei"
		
        2.git config  --global user.email "zhaoguangfei@qq.com"

    3. 用户验证

        避免反复的输入用户名和密码登录
        
        1. https：在https中加入账号和密码

            EX:

                git clone https://用户名：密码@github.com/Z-JERD/gitdemo.git

                或：git remote add origin https://用户名：密码@github.com/Z-JERD/demo.git

        2. ssh：公钥私钥认证

            1. 在git命令下输入：ssh-keygen.exe 一直回车

                出现：
                Your identification has been saved in /c/Users/Administrator/.ssh/id_rsa.
                Your public key has been saved in /c/Users/Administrator/.ssh/id_rsa.pub.

            2. 找到ssh文件的打开
                $ ls
                
                id_rsa  id_rsa.pub

            3. 获取公钥
                
                $ cat id_rsa.pub

            4. 打开github放到settings中的ssh keys中

            5. clone的时候使用ssh

                git clone git@github.com:Z-JERD/gitdemo.git

                或：git remote add origin git@github.com:Z-JERD/gitdemo.git
