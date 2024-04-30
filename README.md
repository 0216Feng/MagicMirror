# 香橙派魔镜 Magic Mirror

基于香橙派Zero3和Python进行开发的智能镜，具有时间，天气，课程表，日程表，备忘录，新闻，个人护理产品保质期，相册组件，使用红外模块实现自动亮屏息屏，支持网页端开关UI显示组件和修改组件内容，并且集成一定程度的语音助手（暂时只能对组件进行开关和新增删除内容 ~~不够预算调实时语音转写API~~）由于本项目是我们的人机交互课项目，工期要求短而且有其他事务，且该项目只是作为期末报告的demo，美观性和功能性均有不足 ~~（十分拉胯）~~，支持自行修改完善作为自己的项目。

# 硬件配置

* 开发板：本项目使用的开发板为香橙派Zero3（Orange Pi Zero3）1G内存版本 ~~（问就是没钱，而且能用就行）~~，安装系统为定制版的Ubuntu，关于如何烧录系统，可参考开发板的用户手册进行操作：[官网地址](http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-Zero-3.html)
* 屏幕：京东方（BOE）液晶模组NT116WHM-N21, 面板尺寸为11.6英寸，分辨率为1366x768,具体可参考屏库数据：[屏库](http://www.orangepi.cn/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-Zero-3.html)
* 驱动板：拼多多购买（确保有HDMI输入并且匹配屏幕供电针脚数和电压即可）
* 红外模块：SR501，淘宝自行购买（需要双母头的杜邦线连接开发板GPIO口），接线教程可自行搜索
* 镜子：亚克力单面透镜
* 支架：拼多多购买，尺寸适合屏幕和镜子即可

# 软件

## 系统配置

* 键鼠：开发板配备1个USB接口，可连接键盘，同时支持蓝牙，可连接蓝牙鼠标

* 中文输入法安装：可参考网络教程，如果想实现shift切换中英文，进入左上方所有应用程序--设置--Fcitx5配置--全局选项中设置切换输入法快捷键

* 开发环境：大部分组件都在个人电脑上的VS Code进行开发，电脑上正常运行的镜子测试一般也没有问题。唯一需要在镜子上开发的组件是自动亮屏息屏，涉及红外模块信号的读取和屏幕电源的控制。安装好的定制版Ubuntu自带编辑器Geany，且已经预装Python 3.10.12。
* 竖屏显示：所有应用程序--设置--显示--旋转
* 终端和文件管理：均可在所有应用程序中找到

 ## 组件介绍

* UI：使用PyQt5，组件单独编写，最后根据需要添加到主窗口布局中，从数据库中动态读取数据并定期刷新

* 天气：IP归属地 -> 城市 -> 心知天气API获取当地天气和生活指数（[心知天气API申请，有免费版，可用数据有限](https://www.seniverse.com/)），PyQt5标签组件label显示
* 新闻：聚合数据API（[API申请，免费版每日可调用50次](https://www.juhe.cn/docs/api/id/235)），使用PyQt5标签组件label显示
* 课程表，日程表，个人护理产品保质期：PyQt5表格组件QTableWidget, 从数据库中动态读取数据并定期刷新
* 备忘录：标题内容和创建时间，使用PyQt5标签组件QLabel显示，从数据库中动态读取数据并定期刷新
* 相册：调用 https://github.com/PyQt5/PyQt/tree/master/QPropertyAnimation/Lib 实现多图滚动，使用PyQt5标签组件QPixmap显示
* 网页端后台：使用fastapi作为后端服务器，前端使用响应式设计，可以开关组件和新增修改内容
* 语音助手：调用pyaudio和wave库把录音打包为.wave文件（设置了录音的音量阈值）-> 讯飞语音文件转写（[API申请，可领取50小时免费额度](https://www.xfyun.cn/services/lfasr#anchor4503211)） -> 讯飞星火大模型匹配用户指令对应的数据库操作（[API申请，可领取200万tocken免费额度](https://xinghuo.xfyun.cn/sparkapi)）
* 自动亮屏息屏：查阅screen.py中的注释和开发板手册中的引脚信息进行跳线，至少需要五条跳线，其中三条双母头线用于连接红外模块，一条双母头线用于检测屏幕是否亮屏（一端连接到驱动板上给屏幕供电的引脚），一条公母线用于控制驱动板的电源实现屏幕亮灭

### 运行

* 打开Ubuntu终端，安装pip

  ```
  sudo apt update
  sudo apt install python3-pip
  ```

  

* 安装项目所需的库（注：OPi为开发板自带；PyQt5无法通过pip install安装，会卡死，需另外安装。特别感谢：https://www.ppmy.cn/news/19014.html?action=onClick ，PyQt5装了半天终于找到正解）

  ```
  pip install -r requirements.txt
  ```

  ```
  sudo apt install pyqt5*
  ```

  

* 启动desktop.py（全屏显示，切回原页面Alt+Tab）

  ```
  python desktop.py
  ```

  

* 若需要网页端后台管理页，启动server.py(需要pip install uvicorn)

  host参数保证同一局域网内可跨设备配置，镜子启动server并查询本机ip，电脑端在浏览器进入镜子ip:8000即可进入后台管理页

  ```
  uvicorn server:app --host '0.0.0.0' --reload
  ```

  

* 若需要语音助手（暂不稳定 ~~大模型有时会叛逆~~），启动command.py(请先填写appid和api信息，可在科大讯飞控制台查看)

  ```python
  # command.py
  # 填写语音文件转写API信息
  api = RequestApi(appid="", secret_key="", upload_file_path=r"output.wav")
  ```

  ```python
  # ./assistant/config.json
  # 填写星火大模型API信息
  "spark_info": {
        "app_id": "",
        "api_secret": "",
        "api_key": ""
  ```

  ```
  python command.py
  ```

  

  修改角色和提示词

  ```python
  # ./assistant/config.json
  "spark_info": {
        ''''''
        "character": '''此处填写角色''',
        "prompt": '''此处填写提示词'''
  ```

  

  同时启动UI

  ```
  python desktop.py & command.py
  ```

  

* 若需要自动亮屏息屏（同时启动如上，&作为连接符）（红外信号波动较大，暂时不会调优，只能作为试验性功能）

  ```
  python screen.py
  ```

  

* 若正常运行，可以通过网页端后台页面或语音助手开关组件或新增删除内容，UI会刷新页面（语音助手反馈较慢，因为语音文件转写较为耗时，有时还需要排队 ~~得加钱~~）



* 若第一次运行报错，可以尝试再次运行，一般是urllib错误
