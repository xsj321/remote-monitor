基于树莓派实现的远程监控环境监控系统
=============

使用树莓派作为服务器来实现对网页的支持.同时利用树莓派的摄像头实现对监控的支持，所以打开网页就实现了监控的获取，且可以查看环境温度湿度，空气状况。

> 摄像头的图像的的转发使用mjpg-streame


使用方式
=====

前置环境（Linux）：Python3

运行 ：

    remote monitor/www/auto_run.sh

主要文件
=====

1. auto_run.sh：bash脚本文件，启动GetPage.py，启动net.sh
2. GetPage.py：python脚本获取串口数据，刷新网页部件
3. main.html：网页主框架负责规划组件位置
4. fire.html：视频显示组件，负责将视频串流显示到页面，嵌套在main.html
5. shuju.html:数据显示组件，负责将数据显示到页面，嵌套在main.html


 
