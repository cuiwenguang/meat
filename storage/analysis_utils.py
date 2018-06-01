import json


def to_bar_chart_data(data):
    """查询结果转化为图标可以使用的数据结构"""
    labels = set([d[0] for d in data])
    products = set([d[2] for d in data])
    values = []
    x = 0
    for lab in labels:
        d1 = [dx for dx in data if dx[0] == lab]
        values.append([])
        y = 0
        for p in products:
            d2 = [dy[1] for dy in d1 if dy[2] == p]
            if len(d2) == 0:
                values[x].append(0)
            else:
                values[x].append(d2[0])
            y += 1
        x += 1

    result = {
        "labels": list(labels),
        "fields": list(products),
        "values": values
    }
    return json.dumps(result)