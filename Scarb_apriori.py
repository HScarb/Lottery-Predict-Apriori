# read lottery.txt
import sys
import copy


# try:
#     dataList = []
#     f = open('lottery.txt', 'r')
#     f.readline()        # 读第一行
#     # 读剩下的数据
#     i = 0
#     for line in f.readlines():
#         data = []
#         line = line.strip()
#         line = line.split('\t')
#         data.append(line[2])
#         data.append(line[3])
#         data.append(line[4])
#         data.append(line[5])
#         data.append(line[6])
#         data.append(line[7])
#
#         dataList.append(data)
#         i = i + 1
#         if i > 2:
#             break
# except:
#     print('open file error')
# finally:
#     if f:
#         f.close()

#####################################
from collections import defaultdict


def init_pass(T):
    C = {}  #C为字典
    for t in T:
        for i in t:

            if i in C.keys():
                C[i] += 1
            else:
                C[i] = 1
    return C

def generate(F):
    C = []
    k = len(F[0]) + 1
    for f1 in F:
        for f2 in F:
            if f1[k-2] < f2[k-2]:
                c = copy.copy(f1)
                c.append(f2[k-2])
                flag = True
                for i in range(0,k-1):
                    s = copy.copy(c)
                    s.pop(i)
                    if s not in F:
                        flag = False
                        break
                if flag and c not in C:
                    C.append(c)
    return C

def compareList(A,B):
    if len(A) <= len(B):
        for a in A:
            if a not in B:
                return False
    else:
        for b in B:
            if b not in A:
                return False
    return True

def apriori(T,minSupport):
    D=[]
    C=init_pass(T)
    keys=C.keys();#.keys()方法，求出字典中的索引
    keys = sorted(keys)
    D.append(keys)#加入D集中
    F=[[]]
    for f in D[0]:
        if C[f]>=minSupport:
            F[0].append([f])
    k=1

    while F[k-1]!=[]:
        D.append(generate(F[k-1]))
        F.append([])
        for c in D[k]:
            count = 0;
            for t in T:
                if compareList(c,t):
                    count += 1
            if count>= minSupport:
                F[k].append(c)
        k += 1

    U = []
    for f in F:
        for x in f:
            U.append(x)
    return U

#z = apriori(dataList, 1)

# print(z)

class Apriori(object):
    def __init__(self, data, min_sup=2):
        self.data = data
        self.min_sup_val = min_sup

    def apriori(self):
        None


    def find_frequent_1_itemsets(self):
        """
        查找频繁1项集
        """
        freq_cnt = defaultdict(int)         # 带默认值的dict
        for list in self.data:
            for item in list:
                freq_cnt[item] += 1

        freq_list = []
        for item in freq_cnt:
            if freq_cnt[item] >= self.min_sup_val:
                freq_list.append([item])
        return freq_list

    def apriori_gen(self):
        None

    def has_infrequent_subset(self):
        None

if __name__ == '__main__':
    filePath = 'ssq.TXT'
    dataList = [line.strip().split('\t') for line in open(filePath)]
    data = [data[2:8] for data in dataList[1:]]
    t = Apriori(data, 2)
    t.find_frequent_1_itemsets()
