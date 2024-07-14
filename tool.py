import os


def newDep(name, text):
    file = open(f"{os.getenv('APPDATA')}/{name}.dep", "w+", encoding="utf-8")
    file.write(text)
    file.close()


def addDepTest(name, newText):
    file = open(f"{os.getenv('APPDATA')}/{name}.dep", "a", encoding="utf-8")
    file.write(newText)
    file.close()


def getDepText(name):
    file = open(f"{os.getenv('APPDATA')}/{name}.dep", "r", encoding="utf-8")
    return file.read()


def extract_content_between(s, start_substr, end_substr):
    # 找到第一个起始子字符串和最后一个结束子字符串的索引
    start_index = s.find(start_substr)
    if start_index == -1:
        return None  # 如果没有找到起始子字符串，返回None

    end_index = s.rfind(end_substr)
    if end_index == -1:
        return None  # 如果没有找到结束子字符串，返回None

    # 计算起始子字符串之后和结束子字符串之前的内容的起始和结束索引
    start_content_index = start_index + len(start_substr)
    # 确保结束索引不包括结束子字符串本身
    end_content_index = end_index

    # 截取并返回两个子字符串之间的内容
    return s[start_content_index:end_content_index]


def get_content_from_char(s, char):
    # 找到字符在字符串中的索引，如果字符不存在则返回整个字符串
    index = s.find(char)
    if index == -1:
        return s

    # 从字符后的位置到字符串末尾获取内容，不包含换行符
    content = s[index + 1:]

    # 去除末尾的换行符
    content = content.rstrip('\n')

    return content

