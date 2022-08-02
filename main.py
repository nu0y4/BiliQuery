# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import re

import requests


def main():
    inputStr = input("请输入b站分享链接：")
    url = inputStr
    r = requests.get(url,headers={"Content-Type":"application/json"})
    reditList = r.history#可以看出获取的是一个地址序列
    urlContext = (f'{reditList[len(reditList)-1].headers["location"]}')#解析后的链接
    urlContextList = urlContext.split("=")
    urlContextList = (urlContextList[1])[:-2]
    print('UID：'+urlContextList)

if __name__=='__main__':
    main()


#print(urlContext)


#html = requests.get(url)
#print(html.text)
