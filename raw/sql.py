#查询总数量
stat_sql = '''select raw_category.name, temp.* from
(select category_id, sum(number),sum(weight), sum(weight*price) from
(select raw_collectinfo.sg_datetime, raw_collectdetail.* from raw_collectdetail
inner join raw_collectinfo on raw_collectdetail.collect_info_id = raw_collectinfo.id) as tab_collect
where sg_datetime between '{0}' and '{1}'
group by category_id) as temp
inner join raw_category on raw_category.id=temp.category_id'''

analyze_sql = '''
SELECT DATE(sg_datetime) as dt, name, sum(number) as total_number, sum(weight) as total_weight,
sum(price*weight) as total_money FROM raw_collectinfo
  INNER JOIN  raw_collectdetail
    ON raw_collectinfo.id = raw_collectdetail.collect_info_id
  INNER JOIN raw_category ON raw_collectdetail.category_id = raw_category.id
  where dt BETWEEN '{0}' AND  '{1}'
GROUP BY dt, name;
'''

get_collect_detail_sql ="""select category.name,m_weight,p_weight,weight,price,number,number*price as money from raw_collectdetail
inner join raw_category category on raw_collectdetail.category_id = category.id
where collect_info_id = '{0}'"""

