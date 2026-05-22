from app.clients.linkedin_client import LinkedInClient
from app.clients.adzuna_client import AdzunaClient
from app.clients.indeed_client import IndeedClient 

class JobsService:
    def __init__(self):
        pass

    def fetch_jobs(self, source, keyword, country, location="", page=1, per_page=20):
        # 从不同的数据源中获取数据并存入数据库, source可以是不同的数据源标识，如1 LinkedIn、2 Adzuna、3 Indeed等
        client = None
        if source == 1:
            client = LinkedInClient()
        elif source == 2:
            client = AdzunaClient()
        elif source == 3:
            client = IndeedClient()
        pass
        jobs = client.get_list(keyword=keyword, country=country, location=location, page=page, per_page=per_page)
        return jobs
    

    def deduplicate_jobs(self):
        # 数据去重
        pass