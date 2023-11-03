from pyecharts.charts import Map
from pyecharts.options import TitleOpts,VisualMapOpts
#准备一个地图对象
map = Map()
#准备数据
data = [
    ('河南省', 100),
    ('湖北省', 120),
    ('贵州省', 200),
    ('山西省', 150),
    ('甘肃省', 80),
    ('上海市', 90),
    ('北京市', 70),
]
#添加数据
map.add('测试地图',data,'china')
#设置全局配置项set_global_opts来设置
map.set_global_opts(
    title_opts = TitleOpts(title = '测试地图',pos_left ='center',pos_bottom='1%'),
    visualmap_opts = VisualMapOpts(
        is_show = True,
        is_piecewise=True,
        pieces=[
            {'min': 0, 'max': 49, 'label': '0-49', 'color': '#ff7f50'},
            {'min': 50, 'max': 99, 'label': '50-99','color': '#87cefa'},
            {'min': 100, 'max': 149, 'label': '100-149','color': '#da70d6'},
            {'min': 150, 'max': 199, 'label': '150-199','color': '#32cd32'},
            {'min': 200, 'max': 249, 'label': '200-249','color': '#6495ed'},
        ]
        )
)
#绘制地图
map.render('地图.html')
