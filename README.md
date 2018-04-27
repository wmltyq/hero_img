# hero_img 

进入王者荣耀的官网首页（http://pvp.qq.com/），通过开发人员工具可以获取到herolist.json的json数据。其中就包含了英雄编号、英雄名和英雄皮肤等信息。点击“游戏资料”标签即可进入英雄介绍页面，再通过对其中任何一个英雄详细页面的数据进行分析可以得知相关规律，再结合之前获取的json数据进行URL构造，即可下载所有的英雄头像和皮肤。实际的运行效果如下图所示：

![运行效果](https://github.com/wmltyq/hero_img/blob/master/img/run.jpg)

下载好的所有英雄皮肤（保存在项目根目录下的skin文件夹中），当壁纸使用很棒：

![英雄皮肤](https://github.com/wmltyq/hero_img/blob/master/img/skin.jpg)

下载好的所有英雄头像（保存在项目根目录下的avatar文件夹中），当QQ、微信或者其他什么账号的头像使用很不错：

![英雄头像](https://github.com/wmltyq/hero_img/blob/master/img/avatar.jpg)