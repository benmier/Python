from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def get_all(self):
    	return self.db.query_db('SELECT * FROM products')

    def get_one(self,id):
    	return self.db.query_db("SELECT * FROM products WHERE id='{}'".format(id))

    def create(self,info):
    	query = "INSERT INTO products (name,description,price) VALUES ('{}','{}','{}',NOW(),NOW()".format(info['name'],info['description'],info['price'])
    	return self.db.query_db(query)

    def update(self,info):
    	query = "UPDATE products SET name='{}',description='{}',price='{}',updated_at=NOW() WHERE id='{}'".format(info['name'],info['description'],info['price'],info['id'])
  		return self.db.query_db(query)

  	def destroy(self,id):
  		return self.db.query_db("DELETE FROM products WHERE id='{}'".format(id))