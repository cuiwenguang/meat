#查询总数量
stat_enter_sql = '''SELECT product.name,product_id, sum(number) as total_number, sum(number*price) as total_price  from storage_enterstorage
INNER JOIN storage_product product ON storage_enterstorage.Product_id = product.id
WHERE create_at BETWEEN '{0}' AND '{1}'
GROUP BY product_id'''



