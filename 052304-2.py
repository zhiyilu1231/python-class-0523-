with open('speech.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    words = jieba.cut(content)
    for w in words:
        print(w)