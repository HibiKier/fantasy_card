from pathlib import Path


# 克制关系
# 光 暗 互相克制
# 火木水相互克制 火->木 木->水 水->火
element_dict = {0: "暗", 1: "光", 2: "火", 3: "木", 4: "水"}


# 卡面路径
star_path = Path() / "card" / "star"
# 卡牌源路径（未加工的图片）
source_path = Path() / "card" / "source_card"
# 完成输出路径
out_path = Path() / "card" / "card"
# 元素图片路径
element_path = Path() / "card" / "cry"
# 魔法类型图片路径
magic_path = Path() / "card" / "rightType"
# 存储文件路径
config_path = Path() / "card_config"
