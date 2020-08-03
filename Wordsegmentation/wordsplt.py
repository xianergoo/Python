import sys
import jieba
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d = path.dirname(__file__)
stopwords_path = 'stopwords.txt' # 停用词词表

text_path = 'basefile.txt' #设置要分析的文本路径
text = open(path.join(d, text_path), 'r', encoding='UTF-8').read()
font = "C:\\Windows\\Fonts\\STXINGKA.TTF"
wc = WordCloud(font_path = font,
               background_color="white", 
               max_words=2000, 
               max_font_size=100,
               random_state=42,
               width=1000, height=860, margin=2,
               )
def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    # print(liststr)

    f_stop = open(stopwords_path, 'r', encoding='UTF-8')
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

text1 = jiebaclearText(text)
wc.generate(text1)

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# print(text1)
with open('a.txt', 'w') as f: 
    f.write(text1)