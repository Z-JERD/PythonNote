import ewsgi
import datetime
import time


class SecondaryIncome(ewsgi.JrWsgiServer):

    def __init__(self ):
    
        super().__init__()

    def url__secondary_income__get_name(self, id: int):

        for i in range(800):

            if i == 1:
                print("========任务：", id)

            if i == 100 or i == 1000:
                print("======%s分割线：%s" % (id, i))

        print("-------------已完成：", id)

        return {"name": "2021", "age": 19}

    def url__secondary_income__get_hobby(self):

        print("=================:", datetime.datetime.now())
        
        time.sleep(2)
        a = {}

        try:
            b = a["name"]
        except Exception as e:
            return self.BadRequest([], '数字制作费缺少标识')

        return {"hobby": "basketball"}

    def url__secondary_income__upload( self, uid:int, catalog:str, file, filename:str=None ) -> dict:
        
        with open("123.jpg", 'a') as f :
            f.write(file)

        return {"upload": "success"}

    def url__secondary_income__get_path(self, api: str):

        print(api)

        return {"file_path": "/stm/{}".format(api)}
    
    def url__secondary_income__cachefile(self):
        """
            在缓存中生成文件返回
        """
        import xlwt
        import csv
        import io

        info = [
            ['序号', '影院编码', '影院名称', '所属院线', '省份', '城市', '影片名称', '影片排次号', '放映日期', '放映时间', '放映影厅', '影厅座位数', '总人数', '观影单位'],
            [1, 43014301, '长沙岳麓横店电影城', '横店', '湖南', '长沙', '哪吒之魔童降世', '001c04352019', '2020-07-24', '19:40:00', '5号厅',
             110, 41, '长沙市岳麓区洋湖街道社区卫生服务中心'],
            [2, 43011311, '长沙横店IMAX影城', '横店', '湖南省', '长沙', '大鱼海棠', '001c04422016', '2020-07-24', '19:30:00', '5号厅', 177,
             20, '中心医院'],
            [3, 44032201, '汕头横店电影城', '横店', '广东省', '汕头', '大话西游之大圣娶亲', '001100361994', '2020-07-24', '17:00:00', '2号厅',
             95, 25, '汕头第十二中学']
        ]

        # 生成Excel缓存文件, 需要使用io.BytesIO

        # writer_file = io.BytesIO()

        # workbook = xlwt.Workbook(encoding='utf-8')
        # sheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
        # 
        # for i in range(0, len(info)):
        #     for j in range(0, len(info[i])):
        #         sheet.write(i, j, info[i][j])
        # 
        # workbook.save(writer_file)
        # 
        # return ewsgi.HttpMemFile("ceshi.xlsx", writer_file.getvalue())
        
        # 生成csv文件

        writer_file = io.StringIO()

        writer = csv.writer(writer_file, dialect='excel', delimiter=',')

        writer.writerows(info)

        return ewsgi.HttpMemFile("ceshi.csv", writer_file.getvalue())


if __name__.startswith('uwsgi_file_'):

    application = SecondaryIncome()

