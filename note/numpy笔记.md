# numpy笔记

## array的创建和操作函数


```python
import numpy as np
```


```python
a = np.array([1, 2, 3, 4])
a
```




    array([1, 2, 3, 4])




```python
b = np.array([
    [1, 2],
    [3.4, 4]
])
b
```




    array([[1. , 2. ],
           [3.4, 4. ]])




```python
a.shape
```




    (4,)




```python
b.shape
```




    (2, 2)




```python
a.dtype
```




    dtype('int32')




```python
b.dtype
```




    dtype('float64')




```python
c = np.zeros(10)
c.dtype
```




    dtype('float64')




```python
np.zeros_like(b)
```




    array([[0., 0.],
           [0., 0.]])




```python
np.random.randn(4,3,4,3)
```




    array([[[[ 1.72041688, -0.91299684,  0.46512922],
             [-1.29518178,  1.65813104, -0.236573  ],
             [ 1.01384781, -1.05015072, -1.70989919],
             [ 0.62311922,  0.35815947,  1.89942449]],
    
            [[ 0.28747543,  0.95027404, -0.66253569],
             [ 0.8869993 , -1.81589861, -0.69415687],
             [ 0.61311662, -1.1767259 , -0.27352199],
             [-0.51918212,  1.18299232,  1.02556522]],
    
            [[ 0.31037163, -0.47122767, -0.95715135],
             [-1.49682792,  1.36012172, -0.37846191],
             [ 0.45528709,  1.7834118 , -0.04508502],
             [ 0.85505302, -0.11948856,  0.48587434]]],
    
    
           [[[ 1.09231411, -1.27236532,  0.61857549],
             [ 0.23918785,  0.68351942,  0.99833055],
             [-0.30982041, -0.68247781,  0.43441756],
             [-1.48445483, -1.79327766, -0.42490938]],
    
            [[-0.14867102,  0.10161794, -1.59923881],
             [ 0.33111303,  0.39254407, -0.11678835],
             [-0.28621321, -0.24793773, -0.87898474],
             [-0.40777833, -1.19413986,  1.7483662 ]],
    
            [[-0.07597973,  0.36189613, -0.2579356 ],
             [ 0.1841482 ,  2.95544587,  2.37785823],
             [ 0.78404732,  0.92741319,  0.09910353],
             [ 0.3036828 , -0.8223359 ,  1.49953507]]],
    
    
           [[[ 0.9412732 ,  0.83063908,  0.44856895],
             [-0.28119957, -0.85516015, -2.45460828],
             [ 0.22149407, -0.8144238 ,  1.29108771],
             [-0.03619167, -1.07130361, -0.59144603]],
    
            [[ 1.72116209,  0.88803281,  0.78489317],
             [ 0.44949865,  0.31540188, -0.64053844],
             [ 0.14269961, -0.73868923, -1.90715623],
             [-0.48287958, -0.65662367, -1.60289753]],
    
            [[ 0.17220048,  1.6530191 ,  0.16205254],
             [-0.71225557, -0.27075269,  1.69982539],
             [ 1.50439169,  0.41273281,  0.59524339],
             [ 1.14703637, -0.64547863,  0.18883458]]],
    
    
           [[[ 0.03015213,  0.07918801,  0.19105997],
             [ 1.3089969 ,  0.65677204, -0.54396436],
             [-0.26298851,  0.38603135,  0.93951084],
             [-2.15581848, -2.11243132, -2.95157642]],
    
            [[-0.37772621,  0.77821361,  0.39910062],
             [ 0.41092422,  0.19113319,  1.08539097],
             [ 2.58590631,  0.74956815,  0.9755997 ],
             [-0.12206023,  1.21268777, -1.16930178]],
    
            [[ 1.23670217, -0.66532798,  0.20021953],
             [ 1.20674016, -0.01808711,  0.42301618],
             [-0.49017651,  0.40839918,  0.93163966],
             [ 0.11181634,  0.28745047,  1.08186076]]]])



## array的索引


```python
a = np.arange(10)
a
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
b = np.arange(60).reshape(3, 4, 5)
b
```




    array([[[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 18, 19]],
    
           [[20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29],
            [30, 31, 32, 33, 34],
            [35, 36, 37, 38, 39]],
    
           [[40, 41, 42, 43, 44],
            [45, 46, 47, 48, 49],
            [50, 51, 52, 53, 54],
            [55, 56, 57, 58, 59]]])



### 基础索引（传入数字或切片）


```python
b[1, 2, 3]
```




    33




```python
b[1, 2]
```




    array([30, 31, 32, 33, 34])




```python
b[1]
```




    array([[20, 21, 22, 23, 24],
           [25, 26, 27, 28, 29],
           [30, 31, 32, 33, 34],
           [35, 36, 37, 38, 39]])




```python
b[:, :, 0]
```




    array([[ 0,  5, 10, 15],
           [20, 25, 30, 35],
           [40, 45, 50, 55]])



### 神奇索引（传入数组）


```python
b[[0, 1, 2], [0, 1, 2]] #按（0，0），（1，1），（2，2）来看
```




    array([[ 0,  1,  2,  3,  4],
           [25, 26, 27, 28, 29],
           [50, 51, 52, 53, 54]])




```python
b[[[0, 0, 0], [1, 1, 1], [2, 2, 2]],
 [[0, 0, 0], [1, 1, 1], [2, 2, 2]]]
```




    array([[[ 0,  1,  2,  3,  4],
            [ 0,  1,  2,  3,  4],
            [ 0,  1,  2,  3,  4]],
    
           [[25, 26, 27, 28, 29],
            [25, 26, 27, 28, 29],
            [25, 26, 27, 28, 29]],
    
           [[50, 51, 52, 53, 54],
            [50, 51, 52, 53, 54],
            [50, 51, 52, 53, 54]]])



### 布尔索引（传入条件）


```python
b > 5
```




    array([[[False, False, False, False, False],
            [False,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True]],
    
           [[ True,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True]],
    
           [[ True,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True]]])




```python
b[b > 5]
```




    array([ 6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
           23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
           40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
           57, 58, 59])




```python
b[b > 5] = 111
b
```




    array([[[  0,   1,   2,   3,   4],
            [  5, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111]],
    
           [[111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111]],
    
           [[111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111]]])




```python
b[~(b == 111)] = 111
b
```




    array([[[111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111]],
    
           [[111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111]],
    
           [[111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111],
            [111, 111, 111, 111, 111]]])



与（&），或（|），非（~）


