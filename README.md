# Recursive-Picture-Cutout
明日方舟报菜名截图快捷小程序（自存）

- 需下载Pillow （run "pip install Pillow" in the Terminal window）
- 需手动测量（单位：pixel）-
  - 干员头像大小 
  - 左侧边框间距 
  - 干员头像间距 

将代码(crop.py)和截图放在同一目录下，如图所示于双引号中填入截图文件名以及对应的数据（均先宽后高），保存后就可以run了

<img width="491" alt="instruction" src="https://github.com/user-attachments/assets/c3195a0d-61d5-48f6-9ae9-b48cfc9db7c2">

![Ganyuan](https://github.com/user-attachments/assets/7c0a13ee-4693-44db-b855-70983cc7cd81)

参数调整tips：
- 每张截图需重新测量一次左侧边框间距(紫色部分)，同设备同等大小的截图无需更改官员头像大小（绿色部分）和间距（浅蓝色部分）
- 若截出来的头像逐渐开始往右偏就是侧边间距（浅蓝组第一个数字）取小了，若往左偏就是取大了
- 若第一张头像截出来就没居中则需要调整左侧边框间距（紫色组）


