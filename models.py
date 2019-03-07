from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Workspace(db.Model):
    __tablename__="workspace"
    id=db.Column(db.Integer,primary_key=True)
    workspaceName=db.Column(db.String,nullable=False)
    subgroups=db.relationship("subGroup",backref="workspace",lazy=True)

    def addsubgroup(self,name):
        newGroup=subGroup(name=name,groupID=self.id)
        db.session.add(newGroup)
        db.session.commit()

class subGroup(db.Model):
    __tablename__="subgroup"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    messages=db.relationship("message",backref="subgroup",lazy=True)
    groupID=db.Column(db.Integer,db.ForeignKey('workspace.id'),nullable=False)

    def addMessage(self,message):
        newMessage=message(message=message,message_id=self.id)
        db.session.add(newMessage)
        db.session.commit()

class message(db.Model):
    __tablename__="message"
    id=db.Column(db.Integer,primary_key=True)
    message=db.Column(db.String,nullable=False)
    message_id=db.Column(db.Integer, db.ForeignKey('subgroup.id'),nullable=False)
