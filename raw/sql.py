#查询总数量
stat_sql = '''select raw_category.name, temp.* from
(select category_id, sum(number),sum(weight), sum(weight*price) from
(select raw_collectinfo.sg_datetime, raw_collectdetail.* from raw_collectdetail
inner join raw_collectinfo on raw_collectdetail.collect_info_id = raw_collectinfo.id) as tab_collect
where sg_datetime between '{0}' and '{1}'
group by category_id) as temp
inner join raw_category on raw_category.id=temp.category_id'''




