from random import randint, choice
from datetime import datetime, timedelta


class AnswerQuery:
    member_id_list = [60, 1, 2, 3, 16, 17, 64, 65, 66, 67]

    def __init__(self, start_datetime, end_datetime, id_input, answer, question_author_id, question_id_input):
        self.answer_member_id_list = [value for value in self.member_id_list if value != question_author_id]

        self._start_datetime = start_datetime
        self._end_datetime = end_datetime
        self._random_member_id = choice(self.answer_member_id_list)
        self._random_datetime = self.random_datetime()
        self._id_input = id_input
        self._question_id_input = question_id_input
        self._answer = answer

    def __str__(self):
        return "INSERT INTO `kernel_square`.`answer`" + \
               "(`created_date`,`id`,`member_id`,`modified_date`,`question_id`,`rank_id`,`vote_count`,`content`,`image_url`) VALUES " + \
               f"('{self._random_datetime}',{self._id_input},{self._random_member_id},'{self._random_datetime}','{self._question_id_input}',NULL,0,'{self._answer}',NULL);\n"

    def get_question_id(self):
        return self._id_input

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
