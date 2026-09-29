from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
# from pybo import db
# from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
  return "Hello Pybo!"

@bp.route('/')
def index():
  return render_template('index.html')
# def index():
#   return redirect(url_for('question._list'))



# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#   question = Question.query.get_or_404(question_id)
#   return render_template('question/question_detail.html', question=question)



#@bp.route('/list')
# def book_list():
#   # 도서 번호(bookid) 오름차순으로 전체 도서 조회
#   books = Book.query.order_by(Book.bookid.asc()).all()
#
#   # 템플릿으로 데이터 전달
#   return render_template('/book_list.html', books=books)