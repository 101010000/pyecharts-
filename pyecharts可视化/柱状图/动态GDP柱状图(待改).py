import json
from pyecharts.charts import Bar,Timeline
from pyecharts.options import ToolboxOpts,AxisOpts
#打开文件
f = open('D:\VS code examples\python\example\pyecharts可视化\柱状图\CountryGDP.json','r',encoding='utf-8-sig')
data = f.read().replace('\n','')
# print(data)
#关闭文件
f.close()
#将json数据转化为python列表
data_list = json.loads(data)
# print(data_list)
#创建柱状图对象
timeline = Timeline({"theme":"dark"})
#添加X轴数据
years = [item['time'] for item in data_list]
sorted_years_list = sorted(years)

for year in sorted_years_list:
    bar = Bar()
    countries = [key for key in data_list[0].keys() if key != 'time']
    for country in countries:
        gdp = [int(item[country]) for item in data_list]
        bar.add_xaxis(country)
        bar.add_yaxis('GDP',gdp)   
        bar.reversal_axis()
    bar.set_global_opts(
        toolbox_opts = ToolboxOpts(is_show = True),
        xaxis_opts = AxisOpts(name = 'GDP',max_=max(gdp)),
        yaxis_opts = AxisOpts(name = 'Country')
    )
    timeline.add(bar,year)

timeline.add_schema(
    play_interval = 100,   #自动播放的时间间隔，单位毫秒
    is_timeline_show=True,  #是否显示时间轴
    is_auto_play=True,      #是否自动播放
    is_loop_play=True       #是否循环播放
)

timeline.render('动态GDP柱状图.html')


