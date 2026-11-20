import uuid
from datetime import datetime


class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.tracking_code = str(uuid.uuid4())
        self.created_at = datetime.now()
