开发环境:	
	Python3.7
	Windows

各文件夹说明:
	bin:
		start.py  启动目录
	conf:
		settings.py 配置文件,用于保存项目目录、课程、选课、以及用户等文件目录
	core:	#主要代码块
		main			主程序目录
		authentication	登录认证
		student			学生类
		manager			管理员类
		course			课程类和公共类
	db:	#数据存储
		course			课程数据，存储类型为pickle
		select_course	学生已选课程信息，存储类型为pickle
		user			用户表，明文存储

导入包记录:

	conf:
		from conf import settings as cof

	core:
		from  core import main as m		#主程序
		from core import authentication as au	#登陆认证
		from core import course as co	#公共类和课程类
		from core import manager as ma	#管理员类
		from core import student as stu	#学生类
			