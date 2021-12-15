from flask import Flask, request
from flask_restplus import Api, Resource, fields, reqparse, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

#Message
not_found = {"message": "Not Found"}
success = {"message": "Success"}
failed = {"message": "Failed"}

class StudentModel(db.Model):
	id      =  db.Column (db.Integer, primary_key=True)
	name    =  db.Column (db.String(20), nullable=False)
	surname =  db.Column (db.String(20), nullable=False)
	age     =  db.Column (db.Integer, nullable=False)
	gender  =  db.Column (db.String(20), nullable=False)

def __repr__(self):
	return "Student %s (name, surname, age, gender)"
	


# PUT Arguments f0r student database
student_put_args = reqparse.RequestParser()

student_put_args.add_argument("name", type=str, required=True)

student_put_args.add_argument("surname", type=str, required=True)

student_put_args.add_argument("age", type=int, required=True)

student_put_args.add_argument("gender", type=str, required=True)

# UPDATE Arguments f0r student database
student_update_args = reqparse.RequestParser()

student_update_args.add_argument("name", type=str)

student_update_args.add_argument("surname", type=str)

student_update_args.add_argument("age", type=int)

student_update_args.add_argument("gender", type=str)


# DELETE Arguments f0r student database
student_delete_args = reqparse.RequestParser()

student_delete_args.add_argument("name", type=str)

student_delete_args.add_argument("surname", type=str)

student_delete_args.add_argument("age", type=int)

student_delete_args.add_argument("gender", type=str)


resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'surname': fields.String,
	'age': fields.Integer,
    'gender': fields.String,
}

student = StudentModel(id=student_id, name=args['name'], surname=args['surname'], age=args['age'], gender=args['gender'])


class Students(Resource):
	@marshal_with(resource_fields)

    def get(self):
        """ Get all students """

        return  StudentModel.query.filter_by(id=student_id).first()
        
        

    @marshal_with(resource_fields)
    def post(self):
        """ Add a new student """
        
		args = student_put_args.parse_args()
		result = StudentModel.query.filter_by(id=student_id).first()
		if result:
			failed , 404

		new_student = StudentModel(id=student_id, name=args['name'], surname=args['surname'], age=args['age'], gender=args['gender'])
		
		db.session.add(new_student)
		db.session.commit()
		
		return new_student, 201
		


    @marshal_with(resource_fields)
    def get(self, student_id):
        """ Get a particular student """
        
        if student["student_id"] == student_id:
            return student
            
        return not_found, 404
        
        
        
    @marshal_with(resource_fields)
    def delete(self, student_id):
        """ Delete a particular student """

        for student in StudentModel:
            if student["student_id"] == student_id:
                StudentModel.remove(student)
                
		        db.session.commit()
		
		return  StudentModel, 201
                return success
        return not_found, 404



    @marshal_with(resource_fields)
    def put(self, student_id):
        """ Update a particular student """

        for student in StudentModel:
            if student["student_id"] == student_id:
                new_student_name = api.payload["student_name"]
                student["student_name"] = new_student_name
                return success
        return not_found, 404
        
        

api.add_resource(Student, "/student/<int:student_id>")

if __name__ == '__main__':
    app.run(debug=True)