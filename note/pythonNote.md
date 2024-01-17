# python学习笔记

## 前面的零碎知识

~~*有一定的编程基础，就不记的那么详细了*~~

`round(value)`返回四舍五入的值

`a = a.replace('d','b')`将a字符串里的‘d’替换为‘b'

`split()`字符串分割

`join()`字符串合并（仅新建一次对象，在多个字符串合并时效率高于’+‘）

类型转换：

![image-20240117220621931](https://fasfish.oss-cn-guangzhou.aliyuncs.com/typora_img/image-20240117220621931.png)





## 数据结构



### 列表

#### 列表创建

`range([start],end,[step])` 可创建整数列表，当start大于end且step为负数时顺序为从大到小

推导式生成列表如：`b = [x*2 for x in range(100) if x % 7 == 0]`，得到[0, 14, 28, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182, 196]



