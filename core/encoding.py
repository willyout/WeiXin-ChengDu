# -*- coding: utf-8 -*-
# http://www.cnblogs.com/huxi/archive/2010/12/05/1897271.html

# UCS(Unicode Character Set)还仅仅是字符对应码位的一张表而已，比如"汉"这个字的码位是6C49。
# 字符具体如何传输和储存则是由UTF(UCS Transformation Format)来负责。
# 也是就是说unicode不是编码格式，只是一个码字集合，而utf-8/utf-16才是具体的编码格式。

# str和unicode都是basestring的子类。严格意义上说，str其实是字节串，
# 它是unicode经过编码后的字节组成的序列。

# 对UTF-8编码的str'汉'使用len()函数时，结果是3，因为实际上，
# UTF-8编码的'汉' == '\xE6\xB1\x89'。

strhan = '汉'
print(len(strhan))
# python根据文件指定的编码格式或者没有指定则使用系统的默认编码。
print(repr(strhan))

# unicode才是真正意义上的字符串，对字节串str使用正确的字符编码进行解码后获得，
# 并且len(u'汉') == 1。

unihan = u'汉'
print(len(unihan))
print(repr(unihan))

# encode()和decode()两个basestring的实例方法，理解了str和unicode的区别后，
# 这两个方法就不会再混淆了。

u = u'汉'
print(repr(u))
s = u.encode('utf-8')
print(repr(s))
u2 = s.decode('utf-8')
print(repr(u2))

# 对unicode进行解码是错误的
# s2 = u.decode('UTF-8')
# 同样，对str进行编码也是错误的
# u2 = s.encode('UTF-8')

# 需要注意的是，虽然对str调用encode()方法是错误的，但实际上Python不会抛出异常，
# 而是返回另外一个相同内容但不同id的str；对unicode调用decode()方法也是这样。


# 源代码文件中，如果有用到非ASCII字符，则需要在文件头部进行字符编码的声明，如下：
    
#-*- coding: UTF-8 -*-

# 实际上Python只检查#、coding和编码字符串，其他的字符都是为了美观加上的。
# 另外，Python中可用的字符编码有很多，并且还有许多别名，还不区分大小写，比如UTF-8可以写成u8。
# 参见http://docs.python.org/library/codecs.html#standard-encodings。

# 另外需要注意的是声明的编码必须与文件实际保存时用的编码一致，否则很大几率会出现代码解析异常。
# 现在的IDE一般会自动处理这种情况，改变声明后同时换成声明的编码保存，但文本编辑器控们需要小心。

# 内置的open()方法打开文件时，read()读取的是str，读取后需要使用正确的编码格式进行decode()。
# write()写入时，如果参数是unicode，则需要使用你希望写入的编码进行encode()，
# 如果是其他编码格式的str，则需要先用该str的编码进行decode()，转成unicode后再使用写入的编码进行encode()。
# 如果直接将unicode作为参数传入write()方法，Python将先使用源代码文件声明的字符编码进行编码然后写入。

# with open('../data/citycode', 'r') as cityfile:
    # for line in cityfile.readlines():
    #   print(type(line))
    #   print(line.decode('utf-8'))

s = u'Was ever feather so lightly blown to and fro as this multitude?'
print(s.find('Was'))