# 目錄
- [程式碼編排](#程式碼編排)
- [import](#import)
- [空白](#空白)
- [註解](#註解)
- [文件字串](#文件字串)
- [版本紀錄](#版本紀錄)

### 程式碼編排
- 絕對不要混用tab和空白。
- 每行最大長度限制在79個字元之內。
- 斷行的方式運用括號，有時用反斜線會更好。
- 將最高層級的function和class定義以兩個空白行分隔，class內的mothod定義之間以一個空白行分隔。
- python 核心發行應該使用ASCII、UTF-8，使用ASCII(UTF-8)不該使用編碼指示，應該只用在註解或docstring提到作者的名字需要時，否則建議在字串常量中使用\x, \u, \U等轉譯字符來表示非ASCII資料。([PEP 263](https://www.python.org/dev/peps/pep-0263/) [PEP 3120](https://www.python.org/dev/peps/pep-3120/))

[TOP](#目錄)

### import 
- import 通常要分成不同行。例如：
    ```python
    # O
    import os
    import sys
    # X
    import sys, os
    # O
    from subprocess import Popen, PIPE
    ```
- import 順序 
    1. 標準程式庫的import
    2. 相關第三方程式庫的import
    3. 己方應用程式/程式庫特定的import
- 每組import 之間應該以一個空白行分隔，將任何相關的__all__細述放在import 之下
- 極不鼓勵package 之間使用相對import

[TOP](#目錄)

### 空白
- 以下情況避免使用額外的空白：
    - 緊連在括號之內
    ```python
    spam(ham[1], {eggs: 2})         # O
    spam( ham[ 1 ], { eggs: 2 })    # x
    ```
    - 逗號、分號、冒號前
    ```python
    if x == 4: print x, y; x, y = y, x          # O
    if x == 4 : print x , y ; x , y = y , x     # X
    ```
    - 函式呼叫的參數傳遞左括號前
    ```python 
    spam(1)     # O
    spam (1)    # X
    ```
    - 索引和slice的左括號前
    ```python
    dict['key'] = list[index]       # O
    dict ['key'] = list [index]     # X
    ```
    - 在賦值(或其他)運算子前後用一個以上的空白，只為了和另一個對齊
    ```python
    # O
    x = 1
    y = 2
    long_variable = 3 
    # X
    x               = 1
    y               = 2
    long_variable   = 3
    ```
    - 永遠在二元運算子前後加上一個空白：=, *, +=, ==, <, >=, in, is, and等
    - 當'='符號是用在關鍵字參數，或預設參數時，不要加空白
    ```python
    # O
    def complex(real, imag=0.0):
        return magic(r=real, i=imag)
    # X
    def complex(real, image = 0.0):
        return magic(r = real, i = imag)
    ```
    - 複合statement 通常不鼓勵使用
    ```python
    # O
    if foo == 'blah':
        do_blah_thing()
    do_one()
    do_two()
    do_three
    # X
    if foo == 'blah': do_blah_thing()
    do_one(); do_two(); do_three()
    ```
    - 雖然有時if/for/while的主體短，可以整個放在同一行，但絕對不要在多子句時這麼做，也要避免摺疊這類長行
    ```python
    # X
    if foo == 'blah': do_blah_thing()
    for x in list: total += x
    while t < 10: t = delay()
    ```
    ```python
    # XXXXX
    if foo == 'blah': do_blah_thing()
    else: do_non_blah_thing()

    try: something()
    finally: cleanup()

    do_one(); do_two(); do three(long, argument,
                                 list, like, this)

    if foo == 'blah': one(); two(); three()
    ```

[TOP](#目錄)

### 註解
- 更改程式碼之後，永遠將更新註解列為優先事項。
- 註解應該是完整的句子。第一個單字應該是大寫，除非是一個小寫開頭的識別字。
- 區塊註解通常包含由完整句子組成的一個或多個段落
- 每個句子的句點後應該加兩個空白。
- 非英語系的程式設計師，請用英文寫註解，除非120%確定不會有不懂你語言的人閱讀你的程式碼
- 有節制的使用行內註解；若只陳述明顯事實，是不必要且造成干擾的。
```python
# X
x = x + 1       # Increasement x
# Sometimes O
x = x + 1       # Compensate for border 補償邊界
```

[TOP](#目錄)

### 文件字串
- 好的文件字串(docstring)，撰寫慣例載於 [PEP 257](https://www.python.org/dev/peps/pep-0257/)
- 所有public的module、function、class、method都該寫文件字串，非public的method不需要寫文件字串，但應用註解詳述作用。這註解應該放在def行之下。
- 多行文件字串結尾的"""應該自己獨立一行，而且前面最好加一個空白行
```python
"""Return a foobang

Optional plotz says tp frobnicate the bizbaz first.

"""
```

[TOP](#目錄)

### 版本紀錄
- 如果需要在原始檔加進Subversion、CVS或RCS的資料
```python
__version__ = "$Revision: 60919 $"
# $Source$
```
- 這幾行應該放在module的docstring之下，其他程式碼之前，並在上下各以一個空白行分隔

[TOP](#目錄)

