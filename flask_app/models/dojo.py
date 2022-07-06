# models.dojo

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Create a list to store all the ninjas associated with the instance of
        # A particular dojo
        self.ninjas = []

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

    @classmethod
    def get_dojo_and_all_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        # Result will be a list of ninjas assigned to a particular dojo
        dojo = cls(results[0])
        for row_in_db in results:
            # Create instance of ninjas to add to list
            ninja_data = {
                'id': row_in_db['ninjas.id'],
                'first_name': row_in_db['first_name'],
                'last_name': row_in_db['last_name'],
                'age': row_in_db['age'],
                'created_at': row_in_db['ninjas.created_at'],
                'updated_at': row_in_db['ninjas.updated_at'],
                'dojo_id': row_in_db['dojo_id']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        print(dojo)
        return dojo

