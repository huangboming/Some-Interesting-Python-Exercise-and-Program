# Think Python Chapter 12 Exercise 2
# 1. Write a program that reads a word list from a file (see Section 9.1)
# and prints all the sets of words that are anagrams.
# 2. Modify the previous program so that it prints the longest list of anagrams first, 
# followed by the second longest, and so on.

# The Author of Think Python has an answer at http://thinkpython2.com/code/anagram_sets.py

def get_char_dict(word):
    """
    功能: 输出单词的字母构成和它们出现的次数，输出数据类型为字典，字母为key，对应出现次数为value
    
    参数: word -- str
    
    返回值: char_dict -- dict 
    
    example:  get_char_dict("hello") -- returns: {'h': 1, 'e': 1, 'o': 1, 'l': 2}
    """
    
    char_dict = dict()
    for char in word:
        char_dict[char] = char_dict.get(char, 1) + 1
    return char_dict


def built_dict_keys(word):
    """
    功能: 以字母-字母出现频率形式（经过排序）构造字典的key
    
    参数: word -- str
    
    返回值: char_freq_string -- str
    
    example: built_dict_keys("hello") -- returns: 1E 1H 2L 1O
    """
    char_dict = get_char_dict(word)
    char_freq_string = ""
    for char, freq in zip(char_dict.keys(), char_dict.values()):
        char_freq_string += f"{freq}{char.upper()} "
        
    char_freq_list = char_freq_string.rstrip().split()
    char_freq_list.sort()
    char_freq_string = " ".join(char_freq_list)
    return char_freq_string

def have_same_dict(word1, word2):
    """
    功能: 判断两个单词是否拥有相同的结构（字母及其出现次数是否一样）
    
    参数: word1, word2 -- str
    
    返回值: bool
    
    example: have_same_dict("hello", "lloeh") -- returns: True
             have_same_dict("hello", "looeh") -- returns: False
    """
    return get_char_dict(word1) == get_char_dict(word2)

def sorted_by_values_length(anagram_dict):
    """
    功能: 以值（列表）的长度倒序排列字典的值
    
    参数: anagram_dict -- dict
    
    返回值: scatter_list -- (nested) list
    
    """
    dict_values = sorted(anagram_dict.values())
    length_list = []
    for item in dict_values:
        length_list.append(len(item))
        
    sorted_list = sorted(tuple(zip(length_list, dict_values)), reverse = True) ## 按照长度倒序排序，但还包含列表对应长度，需要进一步提取
    scatter_list = []
    
    for i in range(len(sorted_list)):
        scatter_list.append(sorted_list[i][1])
    
    return  scatter_list


def main():
    
    """
    功能: 1.找出word.txt中所有同字母异序词 2.按照词的多少进行排序
    """
    
    with open('word.txt', 'r') as f:
        word_list = f.readlines()
        anagram_dict = dict()
        for i in range(len(word_list)):
            word1 = word_list[i]
            if built_dict_keys(word1) in anagram_dict.keys(): ## 如果这个词已经存在，就直接检测下一个词
                continue
            
            anagram_list = [word1.strip()] 
            for j in range(i+1, len(word_list)): ## 从这个词的下一个词开始检索，提高效率
                word2 = word_list[j]
                if have_same_dict(word1.strip(), word2.strip()):
                    anagram_list.append(word2.strip())
                    
            if len(anagram_list) > 1:
                key = built_dict_keys(word1.strip())
                anagram_dict[key] = anagram_list
            
        print(anagram_dict, sorted_by_values_length(anagram_dict), sep = '\n\n')
        
if __name__ == "__main__":
    main()