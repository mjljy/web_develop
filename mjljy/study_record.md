#*chapter1*
1、Q1:为什么使用python开发web Q2:python2 or python3 >> python3
* 至少熟悉一种Python Web-框架                                       >0分
* 熟悉Python 语法。                                                >6分
* 熟悉数据库、缓存、消息队列等技术的使用场景、使用方法等。             >5分
* 日常能使用Linux 或Mac 系统丁＿作。                                >6分
* 有性能叫优经验， 能快速定位问题。                                  >5分
* 对HTML/CSS/JavaScript 有一定了解，有使用经验。                     >5分
#chapter2 web开发前的准备
##1、* 环境准备 VirtualBox  Vagrant Docker 提供Ubuntu环境 运行书中例子
*Vagrant    是个什么东西？
1、Vagrant是一个简单易用的部署工具，它能帮助开发人员迅速的构建一个开发环境，帮助测试人员构建测试环境
通过读取配置文件，获知用户需要的环境的操作系统、网络配置、基础软件等信息；
2、调用虚拟化管理软件的API（VMWare Fusion，Oracle VirtualBox, AWS, OpenStack等）为用户创建好基础环境；
3、调用用户定义的安装脚本（shell，puppet，chef）安装好相应的服务和软件包；
vagrant 是一个操作虚拟机的丁具，它会很快地完成一套开发环境的部署，也解决了
各个开发环境不一致的问题，减少了重复配置环境而造成的时间和精力上的浪费
举个例子， 在没有用Vagrant 之前，新员丁加入后常常需要一到两天的时间搭建完
整的开发环境、而有了Vagrant. 直接启动就好了
Docker
提供Ubuntu 环境*
##2、步骤如下
**1、安装 VirtualBox 6.1 ：支持新建不同系统的虚拟电脑机
 Docker 和  Vagrant 环境都需要使用它作为宿主机到**
2、RubyGems 是 Ruby 的一个包管理器，它提供一个分发 Ruby 程序和库的标准格式，还提供一个管理程序包安装的工具。
RubyGems 旨在方便地管理 gem 安装的工具，以及用于分发 gem 的服务器。这类似于 Ubuntu 下的apt-get, Centos 的 yum，Python 的 pip。
RubyGems大约创建于2003年11月，从Ruby 1.9版起成为Ruby标准库的一部分。

##下载作者box环境
得到一个ubuntu用户目录下为空的linux虚拟机
用户密码都是 Ubuntu
设置root密码：Ubuntu

###linux环境下的 python第三方库安装？
*更换安装的源
####管理第三方库工具
*pip easy_install
*yum emerge apt-get
*python setup.py install

在Python 发展史上出现了很多创建和发布包的工具
####entry_points 
要将python模块转变为命令行工具只用在 setup.py 文件中添加参数entry_points
如果你经常学习开源的代码，对这个东西应该不会陌生，它经常出现在setup.py文件中，那么它是起什么作用的呢？
假设有这样一个场景，你自己用python写了一个工具脚本，这个脚本可以初始化数据库,脚本名字叫hibiscus.py ,很不错的小工具，
但是很快你发现，每次运行它都需要执行命令python hibisucs.py，这还是在你切
换到脚本所在目录的情况下。那么能不能像执行系统命令那样去执行这个脚本呢？
答案是可以的，我们在setup.py脚本里配置entry_points就可以实现这个目标

执行命令 python setup.py install
安装好以后，可以在任意目录下执行下面的命令
hibiscus initdb --dbname=testdb
输出结果为init testdb  

####创建pyhotn虚拟的环境好处？
实现环境的相互独立 互不干扰
*创建 virtualenv venv 
*激活 source venv / bin/activate
####虚拟环境的创建



#chapter3 Flask web开发
Flask 主要依赖＝个库J
* Jinja2: 默认的模板引擎。
* Werkzeug : 一个包含WSGI 、路巾、调试的T具集。
* Itsdangerous: 基千Django 签名校块( http://bit.ly/28QV7Fb ) 的签名实现



#*chapter9* 进阶 