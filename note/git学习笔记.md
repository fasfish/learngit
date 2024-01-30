# git学习笔记



## 创建版本库（仓库）

`mkdir <filename>` 创建一个文件夹（目录），效果和自己去右键新建一样

`cd <filename>` 打开目录

`pwd` 显示工作目录

`git init`命令把这个目录变成Git可以管理的仓库（注意先cd打开目录）

`git add <file> `将文件添加进暂存区（stage）

`git commit -m "explanation"` 一次性把暂存区的所有修改提交到分支

`ls`查看目录下的文件



## 时光机

### 版本回退

`git diff <filename>` 查看工作区和版本库中该文件的差异（该文件未add）

`git log`命令查看版本历史记录

`cat <filename>` 查看文件的文本内容

在Git中，用`HEAD`表示当前版本，也就是最新的提交`1094adb...`（注意我的提交ID和你的肯定不一样），上一个版本就是`HEAD^`，上上一个版本就是`HEAD^^`，当然往上100个版本写100个`^`比较容易数不过来，所以写成`HEAD~100`。



`git reset --hard HEAD^` 回退到上一版本

`git reset --hard <版本号>`  可用于在回退版本后再去更加新的版本（版本号没必要写全，前几位就可以了，Git会自动去找）

`git reflog`查看版本相关的每一次命令（可用于查找版本号）



### 管理修改

第一次修改 -> `git add` -> 第二次修改 -> `git commit`

Git管理的是修改，当你用`git add`命令后，在工作区的第一次修改被放入暂存区，准备提交，但是，在工作区的第二次修改并没有放入暂存区，所以，`git commit`只负责把暂存区的修改提交了，也就是第一次的修改被提交了，第二次的修改不会被提交。

提交后，用`git diff HEAD -- readme.txt`命令可以查看工作区和版本库里面最新版本的区别。



### 撤销修改

场景1：当你改乱了工作区某个文件的内容，未使用add，想直接丢弃工作区的修改时，用命令`git checkout -- <filename>`。

命令`git checkout -- readme.txt`意思就是，把`readme.txt`文件在工作区的修改全部撤销，这里有两种情况：

一种是`readme.txt`自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

一种是`readme.txt`已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

总之，就是让这个文件回到最近一次`git commit`或`git add`时的状态。



场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时（使用了add），想丢弃修改，分两步，第一步用命令`git reset HEAD <file>`，就回到了场景1，第二步按场景1操作。

`git reset`命令既可以回退版本，也可以把暂存区的修改回退到工作区。当我们用`HEAD`时，表示最新的版本。



场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，使用版本回退。



### 删除操作

`rm <file>` 相当于在文件管理器中删除文件(此时还要用`git rm <file>`或`git add<file>`+git commit才能删除版本库中的文件)

`git rm <file>` 然后 git commit 则可以从版本库中删除文件（同时也会删除本地的文件）

如果手动误删文件，使用`git checkout -- test.txt`可以恢复。`git checkout`其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。（即让这个文件回到最近一次`git commit`或`git add`时的状态。）



## 远程仓库

### 添加远程库

`ssh -T git@github.com`可检查与github的连接



`git push -u origin master`把本地库的内容推送到远程，用`git push`命令，实际上是把当前分支`master`推送到远程。

由于远程库是空的，我们第一次推送`master`分支时，加上了`-u`参数，Git不但会把本地的`master`分支内容推送的远程新的`master`分支，还会把本地的`master`分支和远程的`master`分支关联起来，在以后的推送或者拉取时就可以简化命令。

后续用`git push origin master`把本地master分支的最新修改推送至GitHub。



如果添加的时候地址写错了，或者就是想删除远程库，可以用`git remote rm <name>`命令。使用前，建议先用`git remote -v`查看远程库信息：

```
$ git remote -v
origin  git@github.com:michaelliao/learn-git.git (fetch)
origin  git@github.com:michaelliao/learn-git.git (push)
```

然后，根据名字删除，比如删除`origin`：

```
$ git remote rm origin
```

此处的“删除”其实是解除了本地和远程的绑定关系，并不是物理上删除了远程库。远程库本身并没有任何改动。要真正删除远程库，需要登录到GitHub，在后台页面找到删除按钮再删除。



### 从远程库克隆

`git clone git@github.com:<GitHub用户名>/gitskills.git`这样可以克隆远程库到gitskills目录







## 我的小故事

今天是1月16号，但这个故事持续到了17号的一点。

首先，我看了廖雪峰的博客进行学习，但里面讲的太简单了，我一实践便一败涂地。幸好之前师兄还发了另一个博客，从那里我知道了要生成SSH Key并复制到GitHub去，到这里都一切顺利，但是在我兴冲冲地去`ssh -T git@github.com`后，等着我的居然是**Connection closed by 127.0.0.1 port 22**，后面的两个小时让我明白它是我的一大敌人。我先是关了加速器，结果回报我的是超时，更糟糕了不是吗。我只得把加速器开回来，对浏览器丝滑访问GitHub而小小的git却死活连不上百思不得其解。我开始上别的博客查找应对方案，万幸的是也有不少人在用git连GitHub时出过问题，不幸的是和我报错相同的例子寥寥无几（其实只有一个）。为了解决问题，也算是死马当活马医，报错类型不同也没关系，只要有关于连接问题的一丝线索我都不放过。在开关加速器，新增config文件，`git config --global http.proxy`等等一顿操作猛如虎之后，我不得不宣告失败。万念俱灰之际，我来到了一个意想不到的地方——GitHub的官方文档，经过一番查询，一条`ssh -T -p 443 git@ssh.github.com`终于让我人生中第一次在git中看到了fasfish（我的用户名）。这时我简直要跳起来，好不容易终于能连上了！

按理接下来我可以进一步搞我的远程仓库了，但是事情还没完。GitHub文档里提到可以通过覆盖 SSH 设置来强制与 GitHub.com 的任何连接均通过该服务器和端口运行。我当然想以后方便一点，而且这个不用担心网络环境问题看上去也不难，于是又开始作死。我先按GitHub文档里说的操作，结果用`ssh -T git@github.com`验证时又收到了**Connection closed by 127.0.0.1 port 22**。也算是意料之中吧，我开始查看有关的博客，大多的说法是在~\\.ssh\\config目录下创建文本文件，然后输入有关的连接信息，这时候就让我很迷惑，到底是创建一个config.txt，还是创建一个config目录然后在里面放文本，又或是创建一个config格式的文本文件？有的说要修改权限值，还有的说创建的是ssh.config文件，但最终我的一番尝试又以失败告终。今天我的心情也贼差，因而更不想就此罢休。最后的最后，终于在[这个博客]([Windows的.ssh / config文件(git) | 码农家园 (codenong.com)](https://www.codenong.com/26266778/))的一句话受到启发。

![屏幕截图 2024-01-17 020220](https://fasfish.oss-cn-guangzhou.aliyuncs.com/typora_img/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202024-01-17%20020220.png)

我按着路径打开，发现里面有个ssh_config，打开这个文档，里面的英文一句都看不懂（没细看），但是我有看到文档最后有个Host，看着就很符合config文件的风格！

凭借着看过的博客和直觉，我在C:\Program Files\Git\etc\ssh\ssh_config的最下面添加了：

```text
Host github.com
    Hostname ssh.github.com
    Port 443
    User git
```

然后`ssh -T git@github.com`，此时已是1：15，我已经不报过多期望。但是在git bash里看到我的用户名的那一刻，我差点要叫出来。今天真是太累了，作业也没能完成，唉。
