from vanna.base import VannaBase
from vanna.google import GoogleGeminiChat
from sqlalchemy import create_engine

import pandas as pd
import ssl

class IrisVectorDB(VannaBase):
  def add_ddl(self, ddl: str, **kwargs) -> str:
     # Implement here

  def add_documentation(self, doc: str, **kwargs) -> str:
     # Implement here

  def add_question_sql(self, question: str, sql: str, **kwargs) -> str:
     # Implement here

  def get_related_ddl(self, question: str, **kwargs) -> list:
     # Implement here

  def get_related_documentation(self, question: str, **kwargs) -> list:
     # Implement here

  def get_similar_question_sql(self, question: str, **kwargs) -> list:
     # Implement here

  def get_training_data(self, **kwargs) -> pd.DataFrame:
     # Implement here

  def remove_training_data(id: str, **kwargs) -> bool:
     # Implement here


class MyVanna(MyCustomVectorDB, GoogleGeminiChat):
    def __init__(self, config=None):
        MyCustomVectorDB.__init__(self, config=config)
        GoogleGeminiChat.__init__(self, config={'api_key': GEMINI_API_KEY, 'model': GEMINI_MODEL})

vn = MyVanna()
