import sqlalchemy
import pymysql

class User():
    def __init__(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    def user_count(self):
        '''Get number of rows in users table'''
        #syntax: engine = create_engine("mysql://USER:PASSWORD@HOST/DATABASE")
        engine = sqlalchemy.create_engine("mysql+pymysql://sebasalvarez13:BlueYeti27@localhost/anode_coating")

        #Query to add Id column 
        query = '''SELECT count(*) FROM users;'''

        #Create sql connection
        connection = engine.connect()
        #Execute query
        result = connection.execute(query)

        #Fetch count value
        user_count = result.fetchall()[0][0]

        return(user_count)

        
    def register_user(self):
        '''Add new user to database if user does not exist'''
        user_count = self.user_count()
        print('this is user count: {}'.format(user_count))

        #syntax: engine = create_engine("mysql://USER:PASSWORD@HOST/DATABASE")
        engine = sqlalchemy.create_engine("mysql+pymysql://sebasalvarez13:BlueYeti27@localhost/anode_coating")

        #Create sql connection
        connection = engine.connect()
        
        #Check if this is the first user. If so, id = 1
        if user_count == 0:
            id = 1
            query = '''INSERT INTO users VALUES (%s, %s, %s, %s, %s);'''
            #Execute query
            result = connection.execute(query, [id, self.name, self.last_name, self.email, self.password])
        else:
            query = '''INSERT INTO users (name, last_name, email, password) VALUES (%s, %s, %s, %s);'''
            #Execute query
            result = connection.execute(query, [self.name, self.last_name, self.email, self.password])


if __name__ == "__main__":
    user = User('Sebas', 'Alvarez', 'sebas@pena.com', '1234')
    user.register_user()
