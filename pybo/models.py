from pybo import db
from sqlalchemy import Sequence
from flask_sqlalchemy import SQLAlchemy

class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer,db.Sequence('question_seq', start=1, increment=1), primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    __tablename__ = 'answer'

    id = db.Column(db.Integer, db.Sequence('answer_seq', start=1, increment=1), primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete ='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# class Book(db.Model):
#     __tablename__ = 'BOOK'
#
#     bookid = db.Column(db.Integer, primary_key=True)
#     bookname = db.Column(db.String(40), nullable=False)
#     publisher = db.Column(db.String(40))
#     price = db.Column(db.Integer)
#
#
# class Customer(db.Model):
#   __tablename__ = 'CUSTOMER'
#
#   custid = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(40), nullable=False)
#   address = db.Column(db.String(50))
#   phone = db.Column(db.String(20))
#
#
# class Orders(db.Model):
#   __tablename__ = 'ORDERS'
#
#   orderid = db.Column(db.Integer, primary_key=True)
#   custid = db.Column(db.Integer, db.ForeignKey('CUSTOMER.custid'))
#   bookid = db.Column(db.Integer, db.ForeignKey('BOOK.bookid'))
#   saleprice = db.Column(db.Integer)
#   orderdate = db.Column(db.Date)
#
#   customer = db.relationship('Customer', backref=db.backref('order_set'))
#   book = db.relationship('Book', backref=db.backref('order_set'))
#
#
#   class ImportedBook(db.Model):
#       __tablename__ = 'IMPORTED_BOOK'
#
#       bookid = db.Column(db.Integer, primary_key=True)
#       bookname = db.Column(db.String(40), nullable=False)
#       publisher = db.Column(db.String(40))
#       price = db.Column(db.Integer)
#
#   class NewBook(db.Model):
#       __tablename__ = 'NEWBOOK'
#
#       bookid = db.Column(db.Integer, primary_key=True)
#       bookname = db.Column(db.String(40), nullable=False)
#       publisher = db.Column(db.String(40))
#       price = db.Column(db.Integer)