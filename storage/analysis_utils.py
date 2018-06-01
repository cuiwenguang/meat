



def to_bar_chart_data(table_data):
    """查询结果转化为bar图标需要的格式"""
    labels = [td[0] for td in table_data["rows"]]
    fields = table_data["fields"][1:]
    values = [[] for i in range(len(fields))] # [[],[],[],[]]
    for row in table_data["rows"]:
        for i in range(len(fields)):
            values[i].append(row[i+1])

    return {
        "labels": labels,
        "fields": fields,
        "values": values
    }

def to_table_data(data):
    """
    转成表格数据
    [(日期， 分类， v1, v2, 。。。。)]
    """
    fields = ['日期'] + [f for f in set([d[2] for d in data])]
    labels = set([d[0] for d in data])
    values = []
    x = 0
    for lab in labels:
        d1 = [dx for dx in data if dx[0] == lab]
        values.append([])
        y = 0
        values[x].append(lab)
        for p in fields[1:]:
            d2 = [dy[1] for dy in d1 if dy[2] == p]
            if len(d2) == 0:
                values[x].append(0)
            else:
                values[x].append(d2[0])
            y += 1
        x += 1
    return {
        "fields": fields,
        "rows": values
    }

