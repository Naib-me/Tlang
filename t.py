import os
import sys
import tool
from colorama import init, Fore, Back, Style
tab = 0
tab_cun = 0
init(autoreset=True)  # autoreset=True会在每次打印后重置颜色
lines = 0
tool.newDep("path", open("./KLang/w.txt", 'r', encoding="utf-8").read())

shell = sys.argv[1::]
if shell[0] == "v":
    art = """
                         ______________
                        |______________|
                              | |
                              | |
                              | |
                              | |
                              |_|
                              
     Releases: Tlang 0.1.0      Version classification: Beta
    """
    tool.newDep("tio",open("./KLang/tio.js",'r',encoding='utf-8').read())

    print(art)
elif shell[0] == "run":
    filenameall = shell[1]
    filename = shell[1].split(".")[0]
    if "t" != shell[1].split(".")[1]:
        print(Fore.RED + "ERR:错误的文件类型!")
        exit()
    run = open(f"{filename}.js",'w+',encoding="utf-8")
    run.close()
    run = open(f"{filename}.js", 'a', encoding="utf-8")
    # 使用'with'语句来打开文件，这样可以确保文件在操作完成后自动关闭
    with open(filenameall, 'r', encoding='utf-8') as file:
        # 使用for循环逐行读取文件
        for line in file:
            lines += 1
            # 可以使用strip()方法去掉每行末尾的换行符
            stripped_line = line.strip()

            # 检查处理后的行是否为空
            if stripped_line:  # 如果不为空
                x = stripped_line.split(" ")
                if x[0] == "using":
                    """  此处不需要使用s
                    while tab >= 1:
                        run.write("\t")
                        tab -= 1
                    tab = tab_cun
                    """
                    try:
                        run.write(tool.getDepText(x[1]))
                    except:
                        print(Fore.RED + f"ERR:using关键字使用错误!({lines})")
                elif x[0] == "var":   # var name = "name"
                    varName = tool.extract_content_between(stripped_line,"var","=")
                    varText = tool.get_content_from_char(stripped_line,"=")
                    run.write(f"var {varName} = {varText}\n")
                else:
                    run.write(line + "\n")
    run.close()
    os.system(f"node {filename}.js")
    os.remove(f"{filename}.js")
