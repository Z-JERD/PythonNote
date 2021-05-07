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


if __name__.startswith('uwsgi_file_'):

    application = SecondaryIncome()

