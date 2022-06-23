import json

from config import *
from utils.image_utils import BuildImage
from utils.utils import cn2py

# ------------------卡牌生成参数----------------------
# 所属卡组，为空则使用默认的 default_card.json
# 同卡组相同pid将覆盖
card_set = "来自幻想"
# 图片pid，即为图片的名称
pid: str = "54213197"
# 角色名称，没有则留空
name: str = "歌姬"
# 图片标题
title: str = "崩壊王国の歌姫"
# 卡牌星级，[1, 2, 3, 4, 5, 6]
star: int = 6
# 卡牌元素
# 0: 暗
# 1: 光
# 2: 火
# 3: 木
# 4: 水
element: int = 0
# 左边距，即可向右移动 x 个像素，为负数时向上移动
x: int = 20
# 上边距，即向下移动 y 个像素，为负数时向上移动
y: int = -40
# 压缩比例，某些图片太大时需要等比压缩
ratio: float = 0.65
# ------------------卡牌生成参数----------------------
# --------------------卡牌属性-----------------------
# 不同星级采用属性点数总值，即以下四种属性，任意分配，该值未来将会乘以基数
# 1星卡牌总值：10
# 2星卡牌总值： 13
# 3星卡牌总值： 17
# 4星卡牌总值： 24
# 5行卡牌总值： 33
# 6星卡牌总值： 45

# 攻击，即攻击力
ATK: int = 5
# 防御，即防御力
DEF: int = 10
# 血量，即血量值
HP: int = 13
# 特殊点，技能特效加成与此值相关
UPS: int = 18

# 注册方法
# 咕咕咕

# --------------------卡牌属性-----------------------

# --------------------卡牌生成-----------------------
card_set_file = config_path / f'{cn2py(card_set or "default")}.json'
if card_set_file.exists():
    with open(card_set_file, 'r', encoding='utf8') as f:
        data = json.load(f)
else:
    data = {"card_set": card_set or "default", "card": {}}
# 将属性转为拼音方便获取图片
_element = cn2py(element_dict[element])
file = source_path / str(star) / f"{pid}.png"
file.parent.mkdir(parents=True, exist_ok=True)
# png和jpg都行
if not file.exists():
    file = source_path / str(star) / f"{pid}.jpg"
# 输入图片路径
out_file = out_path / str(star) / f"{pid}.png"
out_file.parent.mkdir(parents=True, exist_ok=True)

bk = BuildImage(0, 0, background=star_path / f"{star}.png")
card = BuildImage(0, 0, background=file, ratio=ratio,
                  font="SweiSpringCJKtc-Bold.ttf", font_size=20)
card.paste(bk, (int(card.w / 2 - bk.w / 2) + x, int(card.h / 2 - bk.h / 2) + y), alpha=True)
x1 = int(card.w / 2 - bk.w / 2) + x
y1 = int(card.h / 2 - bk.h / 2) + y
x2 = int(card.w / 2 + bk.w / 2) + x
y2 = int(card.h / 2 + bk.h / 2) + y
card.crop((x1, y1, x2, y2))
card.text((0, 482), name, (255, 255, 255), center_type='by_width')
card.paste(
    BuildImage(0, 0, plain_text=title, font_size=27, font_color=(255, 255, 255), font="SweiSpringCJKtc-Bold.ttf"),
    (0, 514),
    True,
    "by_width")
cry = BuildImage(0, 0, background=element_path / f"{_element}.png")
card.paste(cry, (10, 10), True)
card.save(out_file)
data["card"][pid] = {
    "name": name,
    "title": title,
    "star": star,
    "element": element_dict[element],
    "config": {
        "x": x,
        "y": y,
        "ratio": ratio
    },
    "attr": {
        "ATK": ATK,
        "DEF": DEF,
        "HP": HP,
        "UPS": UPS
    }
}
with open(card_set_file, 'w', encoding='utf8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
card.show()
