from flask import Blueprint, render_template
from pybo import db
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
  question_list = Question.query.order_by(Question.create_date.desc())
  return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
  question = Question.query.get_or_404(question_id)
  return render_template('question/question_detail.html', question=question)



#@bp.route('/list')
# def book_list():
#   # 도서 번호(bookid) 오름차순으로 전체 도서 조회
#   books = Book.query.order_by(Book.bookid.asc()).all()
#
#   # 템플릿으로 데이터 전달
#   return render_template('/book_list.html', books=books)