# 有想法和建议可以发送issues捏
# fantasy_card（幻想卡牌/来自幻想）
集卡+对战的卡牌游戏，对战玩法类似于游戏王，炉石之类的，特色在于可以通过demo代码使用图片生成卡牌，通过注册卡牌生效方法的方式来对每张牌赋予 __技能/被动/主动__ 进行对战，这部分会与真寻的商店道具注册类似。  
目前卡面框选择的是 __乖离性百万亚瑟王__

## 集卡

与[HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)中pcr集卡插件类型，但是获取难度会更大，卡牌也会更加珍贵，因为是可以通过卡牌对战的，目前获取卡牌的途径是在商店中添加道具幻想卡包，且每天有购买次数限制，因此价格不会定太高。   
![图片](https://user-images.githubusercontent.com/45528451/175210297-38225d38-91b7-4463-92f4-3060a55b2360.png)  
除了商店以外，也可以通过其他方式，例如各种小游戏之类，会提供一个便捷方法，但希望奖励提供的数量不要过多。  
在对战中获取对方的卡牌也是获取卡牌的一种方式。

## 对战（咕）

在群聊中使用自动战斗过程转发消息，以免刷屏困扰  
私聊中可以类似联机大厅，进行bot全局联机，同时可以创建房间，通过指定房间号加入等等  
关于 __段位/天梯__：  
  * 待定

## 卡牌生成

通过demo代码生成的卡牌会将数据保存至本地json，在真寻中在特定目录下会读取并导入所有卡牌至数据库，并生成对应卡牌。  
同时，允许对卡牌进行分类形成卡组，更建议卡组使用json进行区分，即一套卡组使用一份json文件，相同卡组建议提供卡组效果。  
__比如__：两个角色卡在场上时会触发卡组效果，提升 __属性__ 等等。

__规范__：
* 卡牌图片的华丽程度应与星级有关（参考卡牌图鉴
* 更推荐p站上的二次元捏，但三次元也不是不行
* 不可以是恐怖猎奇 ！

## 生效方法

定义完成的卡牌需要通过卡牌名称来指定生效方法，除了json文件存储卡牌生成数据外，还需要编写python进行方法的注册和生效。  
一些通用方法可以通过工具文件中调用，__例如__：攻击角色，提升属性，攻击玩家，前置判断队列等等。

## Web端？

你在想什么？

## 集卡概率
不建议修改！  
![图片](https://user-images.githubusercontent.com/45528451/175213997-e4a63558-b23b-4394-8802-d1f996533a1d.png)

## 卡牌图鉴（2022/1）

半年前的卡牌图鉴
![图片](https://user-images.githubusercontent.com/45528451/175214200-4bc031e1-7967-49a5-a0ec-06eecd60639c.png)
