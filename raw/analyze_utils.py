
def to_table_data(data):
    labels = set([d[0] for d in data])
    fields = set([d[1] for d in data])
    for l in labels:
        for f in fields:
            exits = [d for d in data if d[0] == l and d[1] == f]
            if len(exits)==0:
                data.append((l, f, 0, 0, 0))
    ret = sorted(data, key=lambda row: row[0])
    return ret, list(labels), list(fields)


def to_chart_data(table_data, labels, fields):
    """
    查询结果转化为bar图标需要的格式
    :return values= [
        # 数量数据
        [
            (1, label2, label3),   # 表示分类 1
            (),   # 表示分类 2
            ...   # 分类...
        ],
        [] # 销售额数据
    ]
    """
    number_list = [[] for i in range(len(fields))]
    weight_list = [[] for i in range(len(fields))]
    money_list = [[] for i in range(len(fields))]
    x = 0
    for f in fields:
        for l in labels:
            d1 = [dd for dd in table_data if dd[0]==l and dd[1]==f][0]
            number_list[x].append(d1[2])
            weight_list[x].append(d1[3])
            money_list[x].append(d1[4])
        x += 1

    values = [number_list, weight_list, money_list]
    return values

