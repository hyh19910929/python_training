# 目錄
- [程式碼編排](#程式碼編排)
- [import](#import)

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
    import os
    import sys
    ```
    不要寫成：
    ```python
    import sys, os
    ```
    但是這種情況是可以的：
    ```python
    from subprocess import Popen, PIPE
    ```
- import 順序 
    1. 標準程式庫的import
    2. 相關第三方程式庫的import
    3. 己方應用程式/程式庫特定的import
- 每組import 之間應該以一個空白行分隔，將任何相關的__all__細述放在import 之下
- 極不鼓勵package 之間使用相對import

[TOP](#目錄)
