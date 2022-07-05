from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def show_all_dojos(cls):
        """Show all the dojos"""
        query = "SELECT * FROM dojos;"
        dojo_from_db = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for d in dojo_from_db:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def create_dojo(cls,data):
        """Create dojo based on data passed from form"""
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
