import pandas as pd
with open("C:/mecab/user-dic/nnp.csv", 'a', encoding='utf-8-sig') as f:
    
    while True:
        a = input('단어입력, 오타 잘 확인해주세요! 종료하려면 Ctrl+C: ')
        if type(a) == str :
            f.write(a+',,,,NNP,*,F,'+a+',*,*,*,*,*\n')
        else:
            break
    f.close()