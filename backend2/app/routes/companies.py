from app import db
from app.models.company import Company
from flask import Blueprint, jsonify, request

from app.utils.fail import fail
from app.utils.validate_user import validate_user

company_bp = Blueprint("company", __name__, url_prefix="/api/companies")

@company_bp.route("/dev-get", methods=["GET"])
def get_companies_dev():
    companies = Company.query.all()

    data = []

    for company in companies:
        data.append({
            "company_id": company.id,
            "company_name": company.name,
            "company_reg_no": company.reg_no,
            "company_address": company.address,
            "company_tel": company.phone,
            "company_tax": company.tax_id,
            "company_size": company.size
        })

    return data
    


@company_bp.route("", methods=["POST"])
def get_company():
    payload = request.get_json()
    company_reg_no = payload.get('company_reg_no')
    user_id = payload.get("user_id")
    
    # Validation
    if not validate_user(company_reg_no=company_reg_no, user_id=user_id):
        return fail(details="Invalid request from unknown user")

    company = Company.query.filter_by(reg_no = company_reg_no).first()

    data = {
        "company_name": company.name,
        "company_reg_no": company.reg_no,
        "company_address": company.address,
        "company_tel": company.phone,
        "company_tax": company.tax_id,
        "company_size": company.size,
        "company_threshold": company.threshold,
        "company_report_time_period": company.time_period
    }

    return data