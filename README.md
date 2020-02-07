# pymonitor工具
当编写python程序时，调试阶段需要多次重新启动程序。使用pymonitor工具，监测工程目录下的.py文件，如果python源程序文件出现变化，自动重新启动程序，从而提高开发效率.
## 使用方法
python环境自行准备，既然编写python程序，环境应该是准备好了的。
1. 安装watchdog: `pip install -i https://mirrors.aliyun.com/pypi/simple/ watchdog`，这是从国内阿里云镜像安装的方法，速度更快。
2. 拷贝`pymonitor.py`文件到你的工程目录下.
3. 命令格式：`>python pymonitor.py your.file.py [-p path]`
* 参数说明：
* `your.file.py`: 你要调试的程序，一般是工程的入口文件，诸如`app.py1`, `main.py`等文件名.
* `-p path`: [可选]，指定要监测的目录，可以是绝对目录，也可以是相对目录.
## 说明
这是在学廖雪峰的python教程过程中，看到有这么一个小工具，然后给它增加了一些命令行参数的内容.
