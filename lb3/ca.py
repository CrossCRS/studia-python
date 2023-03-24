#!/usr/bin/python3

rule = 30
predict = ["***", "**_", "*_*", "*__", "_**", "_*_", "__*", "___"]
prerule = ["*" if i == '1' else "_" for i in bin(rule+256)[3::]]
dict = dict([i, j] for i, j in zip(predict, prerule))

print(dict)

