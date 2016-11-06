from collections import defaultdict
import itertools
import operator

# can: candidate
# freq: frequent
# trans: transaction


class Apriori:
    def __init__(self, dataset, min_sup=0.01):
        self.data = dataset
        self.min_sup_val = (min_sup * len(self.data))

    def apriori(self, display_num):
        freq_set = self.find_frequent_1_itemsets()
        all_freq_set = freq_set

        while freq_set != []:
            can_set = self.apriori_gen(freq_set)
            can_dic = {}
            for trans in self.data:
                for item in can_set:
                    if set(item) <= set(trans):
                        if tuple(item) in can_dic:
                            can_dic[tuple(item)] += 1
                        else:
                            can_dic[tuple(item)] = 1

            curr_freq_set = []
            for item in can_dic:
                if can_dic[item] >= self.min_sup_val:
                    curr_freq_set.append(list(item))

            freq_dic = {}
            if curr_freq_set != []:
                for item in curr_freq_set:
                    freq_dic[tuple(item)] = can_dic[tuple(item)]
                if len(curr_freq_set[0]) == display_num:
                    sort_freq=sorted(freq_dic.items(), key=operator.itemgetter(1))
                    for x in sort_freq:
                        print('{0}   {1}'.format(x[0],x[1]))

            freq_set = curr_freq_set
            all_freq_set += curr_freq_set
        return all_freq_set

    def find_frequent_1_itemsets(self):
        can_set = defaultdict(int)
        for trans in self.data:
            for item in trans:
                    can_set[item] += 1

        freq_set = []
        for item in can_set:
            if can_set[item] >= self.min_sup_val:
                freq_set.append([item])
        return freq_set

    def apriori_gen(self, freq_set):
        can_set = []
        k = len(freq_set[0])+1
        for item1 in freq_set:
            for item2 in freq_set:
                flag = False
                for i in range(k-2):
                    if item1[i] != item2[i]:
                        flag = True
                        break
                if flag: continue
                if item1[k-2] < item2[k-2]:
                    c = item1 + [item2[k-2]]
                else:
                    continue
                if self.has_infrequent_subset(c, freq_set, k):
                    continue
                else:
                    can_set.append(c)
        return can_set

    def has_infrequent_subset(self, can_set, freq_set, k):
        subsets = list(itertools.combinations(can_set, k-1))
        for item in subsets:
            item = list(item)
            if item not in freq_set:
                return True
        return False


if __name__ == '__main__':
    path = 'ssq.TXT'
    dataList = [line.strip().split('\t') for line in open(path)]
    D = [data[2:8] for data in dataList[1:]]
    test = Apriori(D, 0.002)
    test.apriori(5)