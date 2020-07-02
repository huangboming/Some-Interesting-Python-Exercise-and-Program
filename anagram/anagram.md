## Anagram(同字母异形词)

同字母异形词，指的是相同字母不同排序的词，比如abroad和aboard。

《Think Python》第十二章练习二要求从word.txt中找出所有同字母异形词，储存在列表中，并按照同结构的同字母异形词的多少进行倒序排序。

anagram.py是我个人对这道题的解法。因为word.txt中的单词较多，需要很长时间来运行。

get_txt.py是从《Think Python》官网中下载word.txt的脚本，需要requests和bs4模块。

word.txt中一共有113809个在填字游戏中合法的词（其实和常用词差不多），详见[Think Python Chapter 9](http://greenteapress.com/thinkpython2/html/thinkpython2010.html), [Wikipedia](https://en.wikipedia.org/wiki/Moby_Project)。