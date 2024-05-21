from sqlalchemy import Integer, DateTime, Column, String
from model.entity.base import Base


class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer, primary_key=True, autoincrement=True)
    card_number = Column(Integer, nullable=False)
    dateTime = Column(DateTime.now, nullable=False)
    transaction_type = Column(String(20), nullable=False)
    description = Column(String(20), nullable=False)

    def __init__(self, id, dateTime, card_number, transaction_type, description):
        self.id = id
        self.dateTime = None
        self.transaction_type = transaction_type
        self.card_number = card_number
        self.description = description

    def Transaction_type(self, transaction_type):
        if isinstance(transaction_type, str) and transaction_type.lower() in ("income", "outcome"):
            self.transaction_type = transaction_type.lower()
        elif isinstance(transaction_type, int) and transaction_type in (1, -1):
            self.transaction_type = "income" if transaction_type == 1 else "out come"
        else:
            raise ValueError("invalid:transaction_type")
