from sql_alchemy import banco

class SiteModel(banco.Model):
    #especifica a tabela no banco de dados a partir do modelo do banco
    __tablename__ = 'sites'
    site_id = banco.Column(banco.Integer, primary_key=True)
    url = banco.Column(banco.String(256))
    hoteis = banco.relationship('HotelModel') # Lista de objetos hoteis
    
    def __init__(self, url):
        self.url = url
    
    def json(self):
        return {
            'site_id': self.site_id,
            'url': self.url,
            'hoteis': [hotel.json() for hotel in self.hoteis]
        }

    @classmethod
    def find_by_id(cls, site_id):
        site = cls.query.filter_by(site_id=site_id).first() 
        if site:
            return site
        return None
    
    @classmethod
    def find_site(cls, url):
        site = cls.query.filter_by(url=url).first() 
        if site:
            return site
        return None

    def save_site(self):
        banco.session.add(self)
        banco.session.commit() 
        
    def update_site(self, url):
        self.url = nome
    
    def delete_site(self):
        #deletando todos os hoteis associados ao site
        [hotel.delete_hotel() for hotel in self.hoteis]
        #deletando site propriamente dido
        banco.session.delete(self)
        banco.session.commit()