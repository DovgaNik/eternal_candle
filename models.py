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