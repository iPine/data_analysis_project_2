### 项目概述
利用 Python 探索与三大美国城市，芝加哥、纽约和华盛顿特区
的自行车共享系统相关的数据

### 项目功能
1. 通过计算描述性统计数据回答有趣的问题
2. 接受原始输入并在终端中创建交互式体验

### 数据集
三座城市 2017 年上半年的数据
包含相同的核心六 (6)列：
- 起始时间 Start Time（例如 2017-01-01 00:07:57）
- 结束时间 End Time（例如 2017-01-01 00:20:53）
- 骑行时长 Trip Duration（例如 776 秒）
- 起始车站 Start Station（例如百老汇街和巴里大道）
- 结束车站 End Station（例如塞奇威克街和北大道）
- 用户类型 User Type（订阅者 Subscriber/Registered 或客户Customer/Casual）

芝加哥和纽约市文件还包含以下两列：
- 性别 Gender
- 出生年份 Birth Year

### 函数功能说明
- `get_filters` 获取用户的输入，作为过滤条件
- `load_data` 根据过滤条件，加载相应数据
- `time_stats` 显示骑行时间最频繁的统计信息，包括哪个月份，一周的哪天，每天的哪个时段
- `trip_duration_stats` 显示总骑行的时间的统计信息，包括总时长和平均时长
- `station_stats` 显示骑行站点的统计信息，包括最热门的起始站和终点站，以及最热门的行程
- `user_stats` 显示骑行用户的统计信息，包括每类用户的人数，每个性别的人数和关于用户年龄的统计信息（前提是有相关数据）

### 文件说明
- `bikeshare_R1.py`  第一次提交的项目文件
- `bikeshare_R2.py`  修改后，第二次提交的项目文件
- `bikeshare_R3.py`  再次优化，目前最新版本的项目文件

