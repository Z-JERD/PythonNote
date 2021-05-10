import time
import datetime
from flask import Flask, make_response


application = Flask(__name__)


@application.route("/secondary/<int:task_id>")
def index(task_id):
    print("================:", datetime.datetime.now())

    return "绫罗飘起遮住日落西，奏一回断肠的古曲"


@application.route("/secondary/get/<int:task_id>")
def get(task_id):
    print("---------------:", datetime.datetime.now())
    time.sleep(1)

    return "清明上河图"


@app.route('/cache_file')
def file_download():

    """
    在缓存中生成文件并返回
    :return:
    """

    import io
    import csv
    import xlwt
    import urllib.parse

    info = [
        ['序号', '影院编码', '影院名称', '所属院线', '省份', '城市', '影片名称', '影片排次号', '放映日期', '放映时间', '放映影厅', '影厅座位数', '总人数', '观影单位'],
        [1, 43014301, '长沙岳麓横店电影城', '横店', '湖南', '长沙', '哪吒之魔童降世', '001c04352019', '2020-07-24', '19:40:00', '5号厅',
         110, 41, '长沙市岳麓区洋湖街道社区卫生服务中心'],
        [2, 43011311, '长沙横店IMAX影城', '横店', '湖南省', '长沙', '大鱼海棠', '001c04422016', '2020-07-24', '19:30:00', '5号厅', 177,
         20, '中心医院'],
        [3, 44032201, '汕头横店电影城', '横店', '广东省', '汕头', '大话西游之大圣娶亲', '001100361994', '2020-07-24', '17:00:00', '2号厅',
         95, 25, '汕头第十二中学']
    ]

    # 缓存中生成csv文件

    filename = "活动场报表.csv"
    writer_file = io.StringIO()

    writer = csv.writer(writer_file, dialect='excel', delimiter=',')

    writer.writerows(info)

    response = make_response(writer_file.getvalue())

    # 缓存中生成Excel文件

    # filename = "活动场报表.xlsx"
    #
    # writer_file = io.BytesIO()
    #
    # workbook = xlwt.Workbook(encoding='utf-8')
    # sheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
    #
    # for i in range(0, len(info)):
    #     for j in range(0, len(info[i])):
    #         sheet.write(i, j, info[i][j])
    #
    # workbook.save(writer_file)
    #
    # response = make_response(writer_file.getvalue())

    filename = urllib.parse.quote(filename.encode('utf-8'))

    response.headers["Content-Type"] = "application/force-download"
    response.headers["Content-Disposition"] = "attachment; filename* = UTF-8''" + filename
    response.headers["Location"] = filename
    response.headers["Access-Control-Expose-Headers"] = "location"

    return response

if __name__ == '__main__':
    application.run("0.0.0.0", 8088, debug=True)

