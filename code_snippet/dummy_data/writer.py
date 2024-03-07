from random import randint, choice
from datetime import datetime, timedelta

from md_parser import parse_document
from model.AnswerQuery import AnswerQuery


class QuestionQuery:
    member_id_list = [60, 1, 2, 3, 16, 17, 64, 65, 66, 67]

    def __init__(self, start_datetime, end_datetime, id_input, question):
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._random_member_id = choice(self.member_id_list)
        self._random_datetime = self.random_datetime()
        self._id_input = id_input
        self._question = question

    def __str__(self):
        return "INSERT INTO `kernel_square`.`question`" + \
               " (`closed_status`,`created_date`,`id`,`member_id`,`modified_date`,`view_count`,`content`,`image_url`,`title`) VALUES " + \
               f"(0,'{self._random_datetime}',{self._id_input},{self._random_member_id},'{self._random_datetime}',0,'{self._question}',NULL,'{self._question}');\n"

    def get_question_id(self):
        return self._id_input

    def get_question_author_id(self):
        return self._random_member_id

    def get_question_datetime(self):
        return self._random_datetime

    def random_datetime(self):
        """
        Generate a random datetime between start and end
        :param start: starting datetime (string format 'YYYY-MM-DD HH:MM:SS')
        :param end: ending datetime (string format 'YYYY-MM-DD HH:MM:SS')
        :return: random datetime string in the format 'YYYY-MM-DD HH:MM:SS'
        """
        start_dt = datetime.strptime(self._start_datetime, '%Y-%m-%d %H:%M:%S')
        end_dt = datetime.strptime(self._end_datetime, '%Y-%m-%d %H:%M:%S')
        delta = end_dt - start_dt
        random_second = randint(0, delta.total_seconds())
        return (start_dt + timedelta(seconds=random_second)).strftime('%Y-%m-%d %H:%M:%S')


with open("README.md", "r", encoding="utf-8") as rf:
    readme_md = rf.read()

start_datetime_question = "2024-02-01 00:00:00"
end_datetime_question = "2024-02-28 23:59:59"

start_datetime_answer = "2024-03-01 00:00:00"
end_datetime_answer = "2024-03-07 23:59:59"

qw = open("question.sql", "w", encoding="utf-8")
aw = open("answer.sql", "w", encoding="utf-8")

details_data_result = parse_document(readme_md)
for index, (summary, text_below_details) in enumerate(details_data_result):

    question = QuestionQuery(start_datetime_question, end_datetime_question, index + 168, summary)
    qw.write(str(question))
    if text_below_details == "<p></p>":
        continue

    answer = AnswerQuery(start_datetime_answer, end_datetime_answer, index + 110, text_below_details, question.get_question_author_id(), question.get_question_id())
    aw.write(str(answer).replace("\n", "") + "\n")
