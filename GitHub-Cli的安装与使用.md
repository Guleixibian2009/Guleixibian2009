# GitHub-Cli 的安装与使用  

## 零.综述  
**Take GitHub to the command line!**  
![GitHub-Cli](https://raw.githubusercontent.com/Guleixibian2009/Guleixibian2009/GitHub-Drive/Cli1.png)  
想必`GitHub`大家都不陌生。一开始我也只是偶尔上去安装个软件啥的，但是自从几个月前我接触到用`GitHub`作为服务器和二级域名来做网站后，我访问`GitHub`也就更加频繁了。每天都要重复登陆、收验证码实在是有些浪费时间了，再加上这么慢的网速，于是我开始使用`Git+Hexo`本地生成+上传的模式。可用了一段时间后，我却发现有比`Git`更快、更强、更高大上的终端命令行——**`GitHub-Cli`**(以下也简称gh）。

## 一.Gh简介
`GitHub-Cli`,也就是`GitHub`*最新推出的命令行终端*，具有快速、高效等特性，给万千码农带来了极大的福利—— <u>更快地访问、克隆仓库，更快的提交更新，更高效的处理`issue`和`PR`。</u> 曾经必须要到`GitHub`网页端才能修改的元信息，现在在`CMD`上就可以操作。  
十几天前`gh`已经推出了最新的`2.4.0`版本。这款终端使用`GoLang`编写，配合一定的批处理文件就可以完成一切任务。最新数据显示该仓库已经有了**2万6千个Star**。  
[项目官网](https://cli.github.com/)  [项目源码地址](https://github.com/cli/cli/)

## 二.Gh的安装
安装其实很简单，毕竟它不是`GUI`，只是一个类似`Bash`的东东嘛。下面以*Windows*为例：

### 1. 安装包安装（通用）
访问[这个链接](https://github.com/cli/cli/releases/tag/v2.4.0)，找到`Assets`。然后你会找到**很多很多的安装包**，在比较下面的地方有一个`gh_2.4.0_windows_amd64.msi`的安装文件（*貌似是64位的*）。尝试下载它……
	下载下来以后，直接运行安装即可。安装完成后，打开`CMD`运行：
  ```bash
  $ gh --version
  ```


