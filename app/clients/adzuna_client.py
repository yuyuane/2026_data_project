import requests
class AdzunaClient:
    Base_url = "https://api.adzuna.com/v1/api/jobs"
    APP_ID = "7df9e5e2"
    APP_KEY = "96e2c01bc2c5f010ddc6b84ce0b6fc11"
    # 路径：http://api.adzuna.com/v1/api/jobs/gb/version?app_id={YOUR API ID}&app_key={YOUR API KEY}&&content-type=application/json
    """
    response:
    {
    "__CLASS__": "Adzuna::API::Response::Version",
    "api_version": 1,
    "software_version": "2013111200"
    }
    """
    def get_list(self, keyword, country, location, page, per_page):
        # 这里是获取数据的逻辑，使用requests库发送HTTP请求
        # 这个用到的app_id及key应写到配置文件中 *********
        url = f"{self.Base_url}/{country}/search/{page}"
        params={
            "app_id": self.APP_ID,
            "app_key": self.APP_KEY,
            "results_per_page": per_page,
            "what": keyword
        }
        if location:
            params["where"] = location

        print(f"Fetching data from Adzuna API with params: {params}")
        print(f"Request URL: {url}")
        response = requests.get(url, params)
        # 解析返回的数据，并将其存储到数据库中
        if response.status_code == 200:
            return response.json()
            data = response.json()
            # 这里可以根据实际情况进行数据处理和存储, 数据不在当前类做处理，放置于service去处理
            # print(data)
            # 假设返回的数据中有一个"results"字段包含职位列表
        else:
            # 错误的话，应将日志打印出来，方便调试
            print(f"Failed to fetch data: {response.status_code}")
        pass