��������:	
	Python3.7
	Windows

���ļ���˵��:
	bin:
		start.py  ����Ŀ¼
	conf:
		settings.py �����ļ�,���ڱ�����ĿĿ¼���γ̡�ѡ�Ρ��Լ��û����ļ�Ŀ¼
	core:	#��Ҫ�����
		main			������Ŀ¼
		authentication	��¼��֤
		student			ѧ����
		manager			����Ա��
		course			�γ���͹�����
	db:	#���ݴ洢
		course			�γ����ݣ��洢����Ϊpickle
		select_course	ѧ����ѡ�γ���Ϣ���洢����Ϊpickle
		user			�û������Ĵ洢

�������¼:

	conf:
		from conf import settings as cof

	core:
		from  core import main as m		#������
		from core import authentication as au	#��½��֤
		from core import course as co	#������Ϳγ���
		from core import manager as ma	#����Ա��
		from core import student as stu	#ѧ����
			