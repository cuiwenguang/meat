
# 销售情况分析：一段时间内的销售数量统计，
order_analysis_sql = '''
SELECT date(create_at) as dt, sum(number) as number, name FROM
(SELECT storage_orderdetail.number, storage_product.name, product_id,
order_id, storage_order.create_at, storage_order.customer_id, storage_product.price
from storage_orderdetail
INNER JOIN storage_product ON storage_orderdetail.product_id = storage_product.id
INNER JOIN storage_order On storage_orderdetail.order_id = storage_order.id
where create_at BETWEEN '{0}' AND '{1}' AND product_id in ({2})
)
GROUP BY dt, name;
'''