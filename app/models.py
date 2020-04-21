from app import db

class Data(db.Model):
    nume=db.Column(db.String(30),nullable=False)
    id=db.Column(db.Integer,nullable=False,primary_key=True)

    def __repr__(self):
        return "User("+self.nume+","+str(self.id)+')'
