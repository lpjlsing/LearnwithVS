#-*- coding:utf-8 -*-

# __filename__ = "string_matching.py"
# __author__ = "薯条社区"
# __date__ = "2019-07-30"


def pattern_match_in_string(master_string, pattern_string):
    '''
    :param master_string: 主字符串
    :param pattern_string: 模式字符串
    :return: 返回模式字符串在主字符串中的索引
    '''

    length_of_master = len(master_string)
    length_of_pattern = len(pattern_string)

    # 最多只进行length_of_master - length_of_pattern+1轮比较
    # 这是一个很简单的数学计算问题，读者可以自行举个特例来进行理解

    for index in range(0, length_of_master - length_of_pattern+1):
        for master_character_index, master_character in enumerate(master_string[index:]):

            # 在字符比较过程中，只要不匹配就退出当前循环，继续下一轮的比较
            if master_character != pattern_string[master_character_index]:
                break

            '''
            如果master_character_index与模式字符串的末尾字符的索引相等,
            说明已经完成了所有字符的比较
            '''
            if master_character_index == length_of_pattern-1:
                return index

    return -1


def KMP_algorithm(master_string, pattern_string):
    '''
    :param master_string: 主字符串
    :param pattern_string: 模式字符串
    :return: 返回模式字符串在主字符串中的索引
    '''

    length_of_master = len(master_string)
    length_of_pattern = len(pattern_string)

    # 定义master_string_index 用来保存在主串中的移动位置
    master_string_index = 0
    # 执行build_pattern_string_lookup_table来构建模式子串的索引位置查找表
    # 通过模式子串的索引位置查找表，可以计算主串的最大移动距离

    lookup_table = build_pattern_string_lookup_table(pattern_string)

    # 最多进行  length_of_master - length_of_pattern+1次比较
    while master_string_index <= length_of_master - length_of_pattern:
        for pattern_string_index in range(length_of_pattern):
            if master_string[pattern_string_index + master_string_index] != \
                    pattern_string[pattern_string_index]:

                '''
                    如果主串的当前字符与模式子串的当前字符不相等，则主串的索引往前移动
                    已匹配的字符串的长度-模式子串前缀与后缀的交集集合中长度最宽的字符串的长度
                '''
                master_string_index += max(pattern_string_index - lookup_table[pattern_string_index - 1], 1)
                break
        else:
            '''
            如果正常退出for循环,表示已经完成了所有模式子串字符的匹配，
            当前的master_string_index的值就为模式字符串在主字符串中的索引
            '''
            return master_string_index

    return -1


def build_pattern_string_lookup_table(pattern_string):
    '''
    :param pattern_string:
    :return: 返回构建好的模式子串中的前缀集合与后缀集合
    '''

    string_prefixes = set()
    lookup_table = [0]
    length_of_pattern = len(pattern_string)

    for index in range(1, length_of_pattern):
        # 将模式字符串的所有字符串前缀添加进字符串前缀集合 ***
        string_prefixes.add(pattern_string[:index])
        string_suffixes = {pattern_string[suffix_index:index + 1]
                           for suffix_index in range(1, index + 1)}

        # 计算字符串前缀集合与后缀集合的交集
        intersection_set = string_prefixes & string_suffixes

        # 计算交集集合中共有的最长的字符串的长度
        max_length_of_common_string = len((intersection_set or {''}).pop() )
        for string in intersection_set:
            max_length_of_common_string = len(string) if len(string) > \
                                                         max_length_of_common_string else max_length_of_common_string

        lookup_table.append(max_length_of_common_string)

    return lookup_table


if __name__ == "__main__":
    index = KMP_algorithm("人生苦短,我爱pytho", "python")
    print("pattern string in master's index is {}".format(index))