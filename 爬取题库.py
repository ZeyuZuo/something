import requests
import parsel # 数据解析模块 第三方模块 pip install parsel
import os # 文件操作模块
import re # 正则表达式模块
import csv
import re

sum=0
pattern = re.compile(r'<[^>]+>',re.S)
# result = pattern.sub('', html)
# print(result)
headers = {
    'Connection': 'keep-alive',
    'Cookie': 'wsess=jherigsq0nnbda036cf4p639l1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 '
}
filename = 'D:\\选择题.md' #还有选择题
# 本来用csv，感觉不好看，改成了md
with open(file=filename,mode='w',newline='',encoding='utf-8-sig') as file:
    # writer = csv.writer(file)
    # writer.writerow(['序号','问题','A','B','C','D','答案'])
    for page in range(223,373):
        url = f'http://172.27.66.73/redir.php?catalog_id=6&cmd=learning&tikubh=516700&page={page}'
        response = requests.get(url,headers=headers)
        # print(response.text)
        response.encoding = 'utf-8'
        response.encoding=response.apparent_encoding
        selector = parsel.Selector(response.text)
        i = 1
        print(page)
        while(i<10):
            question_selector = f'body > div.w-990 > div.main-content > div.shiti-content > div:nth-child({i}) > h3'
            answer_selector = f'body > div.w-990 > div.main-content > div.shiti-content > span:nth-child({i+1})'
            a_selector = f'body > div.w-990 > div.main-content > div.shiti-content > div:nth-child({i}) > ul > li:nth-child(1) > label'
            b_selector = f'body > div.w-990 > div.main-content > div.shiti-content > div:nth-child({i}) > ul > li:nth-child(2) > label'
            c_selector = f'body > div.w-990 > div.main-content > div.shiti-content > div:nth-child({i}) > ul > li:nth-child(3) > label'
            d_selector = f'body > div.w-990 > div.main-content > div.shiti-content > div:nth-child({i}) > ul > li:nth-child(4) > label'
            question = selector.css(question_selector).get()
            answer = selector.css(answer_selector).get()
            a = selector.css(a_selector).get()
            b = selector.css(b_selector).get()
            c = selector.css(c_selector).get()
            d = selector.css(d_selector).get()

            question = pattern.sub('',question)
            a = pattern.sub('',a) if a else ''
            b = pattern.sub('',b) if b else ''
            c = pattern.sub('',c) if c else ''
            d = pattern.sub('',d) if d else ''
            answer = pattern.sub('',answer)
            answer = re.sub('）','',answer)
            answer = re.sub('（','',answer)
            tmp = question.split('、')
            id = tmp[0]
            q = re.sub('^\d+、', '', question)
            answer = answer.replace(' ','')
            # file.write('#### '+ id + '\n')
            file.write('**'+question+'**'+'\n')
            if a != '':
                file.write(a+'\n')
            if b != '':
                file.write(b+'\n')
            if c != '':
                file.write(c+'\n')
            if d != '':
                file.write(d+'\n')

            file.write('**'+answer+'**'+'\n\n\n')
            # writer.writerow([id,q,a,b,c,d,answer])
            i=i+2
            sum=sum+1
            print(sum)