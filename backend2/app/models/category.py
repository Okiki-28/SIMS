from app import db
from app.models.product import Product

class Category(db.Model):

    __tablename__ = "category"

    # Category table having columns id, name, number_of_items and company_reg_no

    id = db.Column(
        db.Integer,
        autoincrement = True,
        primary_key = True
    )
    name = db.Column(
        db.String("30"),
        nullable = False
    )
    company_reg_no = db.Column(
        db.String(10),
        db.ForeignKey("company.reg_no", ondelete="CASCADE"),
        nullable=False
    )

    # Relationships
    company = db.relationship("Company", foreign_keys=[company_reg_no], backref="categories")

    @property
    def number_of_items(self):
        return Product.query.filter_by(category_id=self.id).count()