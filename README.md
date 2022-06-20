### BuidlerDao FlashBot
- 主讲人: Wiger https://twitter.com/JizhouW
- 代码编写: Wiger https://twitter.com/JizhouW
- 代码编写: Soth https://twitter.com/Soth76267980
- 助教: Niel

### 软件交易模式
1. 正常交易: 市价/限价 买入/卖出
2. 抢新: 抢土狗
3. 多线程模式: n 线程同时启动购买

### 功能
- 价格显示
- 开盘 0 秒进场
- 买入均价获取
- BNB: 市价买入 市价卖出 止盈 止损
- USDT: 市价买入 市价卖出 止盈 止损

### 功能简介
1. 定时开启交易
2. 限价/市价买入
3. 限价/市价卖出
4. 设置每单交易定时: 到指定时间未交易自动取消
5. 设置矿工费: Gas_Price 和  Gas_Limit 越大越先打包, 过小可能交易不成功, 总矿工费: Gas_Price * Gas_Limit, 正常交易: Gas_Price = 10 - 15, 抢新币设置为: Gas_Price = 50 - 100, Gas_Limit 全部设置为 210000 即可
6. 设置滑点百分比: 假定最低买入数目 100, 滑点设置为 5% (仅需输入 5, 无需输入百分号), 则最低买入数目为 95
7. 查询钱包余额
8. 多线程交易
9. 流动性检测, 防止过早盲目交易浪费 Gas 费
10. 增加 config.py 配置文件
11. 增加实时显示价格功能
12. 增加全部卖出/部分卖出功能
13. 增加止损模式

### 用户须填写信息
1. `MY_ADDR`: 钱包地址
2. `PRIV_KEY`: 钱包私钥
3. `ADDR_1`: 起始地址, 例如: WBNB 地址: "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
4. `ADDR_2`: 结束地址, 例如: BAKE 地址: "0xE02dF9e3e622DeBdD69fb838bB799E3F168902c5"
5. `LIQUL_ADDR`: 流动性检测地址, 例如: BAKE_Pancake_Swap 地址: "0x1099C2E6Ed6ebA95099c205b599B409305783E43"
6. `GAS_PRICE`: 矿工费: 抢币设置为 50 - 150
7. `GAS_LIMIT`: 矿工数目: 210000 - 360000
8. `SLIPPAGE_BUY`: 购买滑点, 输入 30 即为 30%, 输入 0 即指定数量不变
9. `SLIPPAGE_SELL`:  出售滑点, 输入 30 即为 30%, 输入 0 即指定数量不变
10. `PER_PRICE`: 限价出售单价, 例如: BAKE:BNB = 0.012
11. `decimal_1`: 一号币小数位数, 例如: BNB = 18
12. `decimal_2`: 二号币小数位数, 例如: BAKE = 18
13. `time_period`: 订单时间, 到时间自动取消, 单位为秒
14. `count_token_1`: 购买总消耗钱数, 例如: BNB = 0.00005
15. `count_token_2`: 出售总消耗钱数, 例如: BAKE = 0.03
16. `sleep_time`: 流动性检测间隔时间

### 抢币模式
- `MODEL_TYPE`: 抢币模式, 根据是否有合约地址, 是否有交易对地址决定, 后续会继续更新
    1. 判断是否有合约地址, 没有合约地址则提示输入
    2. 用合约地址获取交易对地址
    3. 根据交易对地址, 获取池子 代币 和 BNB 数目
    4. 根据 代币 和 BNB 数目判断是否开盘
    5. 开盘后发起交易
    
### 测试结果
- 实际开盘时间: 2021.06.01 23:39:32
- 检测开盘时间: 2021.06.01 23:39:33
- 提交购买时间: 2021.06.01 23:39:33
- 购买成交时间: 2021.06.01 23:39:39
- 检测总耗时间: 1 秒
- 开盘交易总耗时间: 7 秒

### 目前问题
1. 检测交易是否成功: 目前用检测账户余额是否数值变化进行判定, 例如交易前: BAKE 余额 600, 交易后变为: 1666, 则判定为交易成功
2. 检测开盘, 拒绝盲目发起交易烧手续费: 目前通过检测池子余额进行判定开盘, 但无法将两个模式统一, 有两个思路: 1) 通过合约地址查找交易对地址, 然后开启模式 1; 2) 通过合约地址直接检测开盘与否
3. 实时显示价格: 思路可能类似 2-1 通过爬虫获取

### 已解决
1. 检测交易是否成功: 检测账户余额是否数值变化进行判定
2. 检测开盘: 合约地址获取交易对地址 -> 根据交易对地址, 获取池子 代币 和 BNB 数目 -> 根据 代币 和 BNB 数目判断是否开盘
3. 实时显示价格: 借助 getAmountsOut() 获取 1 个 BNB 能换多少 USDT, 并借助池子中 BNB 与 代币数目 的比值计算出最终价格

### 改进计划
1. 核心部分包装为 c++ dll 文件
2. 全部部分写成函数, 抵制顺序执行, 加入主函数 main
3. 代码混淆 + 加壳 + 在线验证 + ...
4. 网页制作
5. 多语言制作
6. 通过 邮箱 + 付款地址 进行付款, 后台根据读取 BSC 链上交易进行 激活码 邮件发送
7. 软件 License 系统
8. Sniper 类封装性不够好，需要花时间维护或重构

### 代码风格修改
1. 增加 Sniper() 类
2. 整合并删除 config.py
3. 变量名称格式化

### 用户界面
1. 雏形已完成
2. 计划完成皮肤优化
3. 打包

### 功能测试
1. 4种模式已测试完成
2. 交易截图已保存
3. GUI 接口数据类型等未测试

### GUI 使用
```
pip install pyqt5 --user

python ./main.py
```

### 完成版问题
1. 不用打印价格, 已经有实时显示功能
2. 购买单价, 购买花费数目, 卖出单价, 卖出花费数目, 参数未成功传递, 仍为 init 初始值
3. 止损模式价格仍然为 init 初始值

### 核心功能测试完毕
- 2021/06/14 00:00:39

### 名称
1. 小火箭 - To The Moon
2. Waltzing
3. FastShot
4. QuickWin
5. Whizzbang

### 通信流程
1. 用户网页下单: 邮箱地址 + 付款地址, 付款
2. woocommerce API + 后端循环扫描: 判定条件 + 收款信息 + 邮箱地址, 发送邮件
3. 第一次打开软件: 向服务端发起: 激活码 + 机器码(CPU + MAC + 激活时间 + ...), 服务器保存, 登记时间
4. 第二次打开软件: 向服务端发起: 检验 激活码 + 机器码

### 环境配置
1. `conda create --name rocket python=3.8.5`
2. `conda activate rocket`
3. `pip install wmi -i https://pypi.tuna.tsinghua.edu.cn/simple`
4. `pip install pypiwin32 -i https://pypi.tuna.tsinghua.edu.cn/simple`
5. 将 `Lib\site-packages\pywin32_system32` 中这两个文件复制到 `C:\Windows\System32` 目录下: `pythoncom38.dll` 和 `pywintypes38.dll`
6. `pip install pycryptodome -i https://pypi.tuna.tsinghua.edu.cn/simple`
7. `pip install tinyaes -i https://pypi.tuna.tsinghua.edu.cn/simple`
8. `pip install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple`
9. `pip install web3 -i https://pypi.tuna.tsinghua.edu.cn/simple`
10. `pip install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple`
11. 打开命令行, 进入文件夹, 放好图标
12. `pyinstaller -F -w --key=wiger --clean --icon=roc.ico main.py`
13. dist 文件夹见
