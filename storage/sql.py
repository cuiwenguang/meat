#查询入库总数量
stat_enter_sql = '''SELECT product.name,product_id, sum(number) as total_number, sum(number*price) as total_price  from storage_enterstorage
INNER JOIN storage_product product ON storage_enterstorage.Product_id = product.id
WHERE create_at BETWEEN '{0}' AND '{1}'
GROUP BY product_id'''

# 统计出库数据
stat_out_sql = '''SELECT name, sum(number) as number,money FROM
(SELECT storage_orderdetail.number, storage_product.name, product_id,
order_id, storage_order.create_at,storage_order.money, storage_order.customer_id, storage_product.price
from storage_orderdetail
INNER JOIN storage_product ON storage_orderdetail.product_id = storage_product.id
INNER JOIN storage_order On storage_orderdetail.order_id = storage_order.id
where create_at BETWEEN '{0}' AND '{1}'
)
GROUP BY name;'''



