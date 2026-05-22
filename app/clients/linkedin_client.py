import requests
class LinkedInClient:
    Base_url = "https://api.linkedin.com/v2/jobs"

    def get_list(self, keyword, country, location, page, per_page):
        # 模拟请求，实际需要使用requests库发送HTTP请求
        jobs = requests.get(self.Base_url, params={
            "keywords": keyword,
            "location": location,
            "start": (page - 1) * per_page,
            "count": per_page
        })
        return jobs.json()  # 假设返回的是JSON格式的数据
        # 解析返回的HTML或JSON数据，提取职位信息