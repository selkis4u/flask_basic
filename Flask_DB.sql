-- 1. 질문 테이블용 시퀀스 생성
CREATE SEQUENCE question_seq
  START WITH 1
  INCREMENT BY 1
  NOCACHE
  NOCYCLE;

-- 2. 답변 테이블용 시퀀스 생성 (나중을 위해 미리 생성)
CREATE SEQUENCE answer_seq
  START WITH 1
  INCREMENT BY 1
  NOCACHE
  NOCYCLE;

COMMIT;