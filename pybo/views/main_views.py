from flask import Blueprint, render_template
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
  question_list = Question.query.order_by(Question.create_date.desc())
  return render_template('question/question_list.html', question_list=question_list)

# @bp.route('/hello')
# def hello_pybo():
#     return 'Physical AI 서비스 개발 테스트 페이지입니다.!!'

#@bp.route('/list')
# def book_list():
#   # 도서 번호(bookid) 오름차순으로 전체 도서 조회
#   books = Book.query.order_by(Book.bookid.asc()).all()
#
#   # 템플릿으로 데이터 전달
#   return render_template('/book_list.html', books=books)

