from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts

#创建Bar构建对象
bar1 = Bar()
bar2 = Bar()
bar3 = Bar()
#添加X轴数据
bar1.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar2.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar3.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
#添加Y轴数据
bar1.add_yaxis("商家A", [5, 20, 36, 10, 75, 90],label_opts=LabelOpts(position="right"))
bar2.add_yaxis("商家A", [15, 6, 45, 20, 35, 66],label_opts=LabelOpts(position="right"))
bar3.add_yaxis("商家A", [10, 10, 35, 20, 45, 76],label_opts=LabelOpts(position="right"))
#设置全局配置项set_global_opts来设置
#设置xy轴反转
bar1.reversal_axis()
bar2.reversal_axis()
bar3.reversal_axis()
#构建时间线对象
timeline = Timeline({'theme':'dark'})
#在时间线上添加点
timeline.add(bar1, "bar1")
timeline.add(bar2, "bar2")
timeline.add(bar3, "bar3")
#设置自动播放
timeline.add_schema(
    play_interval = 1000,   #自动播放的时间间隔，单位毫秒
    is_timeline_show=True,  #是否显示时间轴
    is_auto_play=True,      #是否自动播放
    is_loop_play=True       #是否循环播放
)
#生成图表render
timeline.render('柱状图.html')