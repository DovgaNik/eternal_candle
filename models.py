class Question():
    def __init__(self, question_id, question_body, question_explanation):
        self.question_id = question_id
        self.question_body = question_body
        self.question_explanation = question_explanation

    question_id: str
    question_body: str
    question_explanation: str

    def to_dict(self):
        return {
            "question_id": self.question_id,
            "question_body": self.question_body,
            "question_explanation": self.question_explanation,
        }

class QuestionResponse(Question):
    def __init__(self, question_id, question_body, question_explanation, question_timestamp, response_iubita, response_iubitul, response_iubita_ts, response_iubitul_ts):
        self.question_id = question_id
        self.question_body = question_body
        self.question_explanation = question_explanation
        self.question_timestamp = question_timestamp
        self.response_iubita = response_iubita
        self.response_iubitul = response_iubitul
        self.response_iubita_ts = response_iubita_ts
        self.response_iubitul_ts = response_iubitul_ts

    def to_dict(self):
        return {
            "question_id": self.question_id,
            "question_body": self.question_body,
            "question_explanation": self.question_explanation,
            "question_timestamp": self.question_timestamp,
            "response_iubita": self.response_iubita,
            "response_iubitul": self.response_iubitul,
            "response_iubita_ts": self.response_iubita_ts,
            "response_iubitul_ts": self.response_iubitul_ts,
        }