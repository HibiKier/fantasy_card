import pypinyin


def cn2py(word: str) -> str:
    """
    说明：
        将字符串转化为拼音
    参数：
        :param word: 文本
    """
    temp = ""
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        temp += "".join(i)
    return temp


