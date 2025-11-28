import os
import psycopg2
from uuid import uuid4

import models

DB_URL = os.getenv("DATABASE_URL")


def get_connection():
    return psycopg2.connect(DB_URL)


def get_recent_questions(limit: int = 10):
    query = """
            SELECT question_body
            FROM public.questions
            ORDER BY question_timestamp DESC
                LIMIT %s; \
            """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (limit,))
            rows = cur.fetchall()

    return [r[0] for r in rows]


def insert_question(question_body, question_explanation=None):
    query = """
            INSERT INTO public.questions (question_body, question_explanation)
            VALUES (%s, %s) RETURNING question_id; \
            """

    with get_connection() as conn:
        generated_id = None;
        with conn.cursor() as cur:
            cur.execute(query, (question_body, question_explanation))
            generated_id = cur.fetchone()[0]
        conn.commit()
        return generated_id


def get_latest_questions(limit: int = 25, page: int = 1):
    offset = (page - 1) * limit

    query = """
            SELECT *
            FROM questions
            ORDER BY question_timestamp DESC
            LIMIT %s OFFSET %s; 
            """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (limit, offset))
            rows = cur.fetchall()

    questions = []
    for row in rows:
        question_id, body, explanation, timestamp, resp_iubi, resp_iubit, resp_iubi_ts, resp_iubit_ts = row
        questions.append(
            models.QuestionResponse(question_id, body, explanation, timestamp, resp_iubi, resp_iubit, resp_iubi_ts,
                                    resp_iubit_ts))
    return questions
