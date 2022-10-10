##### **1 数据预处理**

图3为初步预处理后的数据，由于我使用的pyecharts的代码样例中数据的形式为图4格式，所以需要进一步处理。

![img](file:///C:\Users\1\AppData\Local\Temp\ksohtml22724\wps1.jpg) ![img](file:///C:\Users\1\AppData\Local\Temp\ksohtml22724\wps2.jpg)

图 3 test1.csv截图              图 4 pyecharts代码模板截图

 

 

首先将test1.csv中数据name和type两列数据保存为test2.csv。然后执行process_date1.py处理数据得到每天全国的治愈人数总和以及每天每个省治愈人数占全国总治愈人数的比例，将结果保存至out.csv。

![img](file:///C:\Users\1\AppData\Local\Temp\ksohtml22724\wps3.jpg)         ![img](file:///C:\Users\1\AppData\Local\Temp\ksohtml22724\wps4.jpg)

图 5 test2.csv截图                  图 6 out.csv截图

 

接下来将out.csv中的数据合并到test1.csv得到test3.csv。然后执行process_date2.py文件在控制台输入test3.csv即可得到图4格式的数据形式的数据。

   ![img](file:///C:\Users\1\AppData\Local\Temp\ksohtml22724\wps5.jpg)				图 7 执行process_date2.py文件输出结果

​     ![img](file:///C:\Users\1\AppData\Local\Temp\ksohtml22724\wps6.jpg)

图 8 更换main.py文件中数据

#### **2.利用pyecharts实现数据可视化**

（1）运行main.py文件，得到输出的china_covid19_heal_number.html文件。

![img](file:///C:\Users\1\AppData\Local\Temp\ksohtml22724\wps7.jpg) 

图 9 运行main.py文件得到输出的html文件

（2）进入china_covid19_heal_number.html，点击右上角的浏览器图标跳转到可视化界面。

![img](file:///C:\Users\1\AppData\Local\Temp\ksohtml22724\wps8.jpg) 

图 10 点击右上角的浏览器图标

![img](file:///C:\Users\1\AppData\Local\Temp\ksohtml22724\wps9.jpg) 

图 11 运行结果截图