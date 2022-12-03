from sql_alchemy import banco

class site():
    __tablename__ = 'sites'
    def __init__(self, site_id, site):
        self.site_id = site_id
        self.site = site
        
    