class Account(db.Model):
    """
    Account model for storing account information and related transactions.
    """
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    account_type = db.Column(db.String(10), nullable=False)
    # Using Numeric for currency to ensure precision (precision=12, scale=2 for example)
    balance = db.Column(db.Numeric(precision=12, scale=2), default=0.00, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationships
    user = db.relationship(
        'User',
        backref=db.backref('accounts', lazy='dynamic'),
        lazy='joined'
    )
    # Transactions where this account is the source (outgoing transactions)
    transactions_sent = db.relationship(
        'Transaction',
        foreign_keys='Transaction.source_account_id',
        backref=db.backref('source_account', lazy='joined'),
        lazy='dynamic'
    )
    # Transactions where this account is the target (incoming transactions)
    transactions_received = db.relationship(
        'Transaction',
        foreign_keys='Transaction.target_account_id',
        backref=db.backref('target_account', lazy='joined'),
        lazy='dynamic'
    )

    def __repr__(self):
        return f"<Account(id={self.id}, account_number='{self.account_number}')>"
