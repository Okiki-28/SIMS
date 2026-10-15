from app import db

class Supplier(db.Model):

    __tablename__ = "supplier"

    # Supplier table having columns id, name, phone, email, address, company_reg_no

    id = db.Column(
        db.Integer,
        autoincrement = True,
        primary_key = True
    )
    name = db.Column(
        db.String("30"),
        nullable = False
    )
    phone = db.Column(
        db.String(20)
    )
    email = db.Column(
        db.String(100)
    )
    address = db.Column(
        db.String(150)
    )
    company_reg_no = db.Column(
        db.String(10),
        db.ForeignKey("company.reg_no", ondelete="CASCADE"),
        nullable=False
    )
    
    # Relationships
    company = db.relationship("Company", foreign_keys=[company_reg_no], backref="suppliers")