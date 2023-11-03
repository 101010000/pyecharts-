#导包，导入Line功能构建折线图对象
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
#得到折线图对象
line = Line()
#添加X轴数据
line.add_xaxis(["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"])
#添加Y轴数据
line.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
line.add_yaxis("商家B", [6, 25, 40, 8, 60, 80])
#设置全局配置项set_global_opts来设置
line.set_global_opts(
    title_opts = TitleOpts(title ="商家商品折线图展示",pos_left = "center",pos_bottom= "1%"),
    legend_opts = LegendOpts(is_show = True),
    toolbox_opts = ToolboxOpts(is_show = True),
    visualmap_opts = VisualMapOpts(is_show = True)
)

#生成图表render
line.render('折线图.html')