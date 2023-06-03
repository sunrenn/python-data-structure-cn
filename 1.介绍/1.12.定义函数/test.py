import random
def random_sentence(length=28):
    letters = "abcdefghijklmnopqrstuvwxyz "
    newsentence = ""
    for ii in range(length):
        newsentence += letters[random.randint(0,len(letters)-1)]
    print(newsentence)

def compare2str(aaa:str,bbb:str):
    score = 0
    
    if len(aaa)==len(bbb):     # 两个字符串长度必须一致
        wordsa = aaa.split()
        wordsb = bbb.split()
        if len(wordsa)==len(wordsb):    # 单词数量必须一致！
            # 计分规则：单词数正确与否，
            # 和每个单词的正确与否，判断总数去整除100分，
            # 商为单词正确得分，商加余数为单词数量正确得分。
            score_perword = 100//(len(wordsb)+1)
            score_num = score_perword + 100%(len(wordsb)+1)
            score += score_num
            print("单词数量正确！")
            for ii in range(len(wordsa)):
                if wordsa[ii]==wordsb[ii]:
                    score += score_perword
    
    return score
                    
print(compare2str("b ba","a aa"))