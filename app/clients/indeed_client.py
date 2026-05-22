import requests
class IndeedClient:
    Base_url = "https://www.indeed.com/jobs"

    def get_list(self, keyword, country, location, page, per_page):
        # 模拟请求，实际需要使用requests库发送HTTP请求
        jobs = requests.get(self.Base_url, params={
            "q": keyword,
            "l": location,
            "start": (page - 1) * per_page,
            "limit": per_page
        })
        return jobs.json()  # 假设返回的是JSON格式的数据
        # 解析返回的HTML或JSON数据，提取职位信息
