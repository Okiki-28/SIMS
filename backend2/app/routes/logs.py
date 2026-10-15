from app import db
from app.models.log import Log
from flask import Blueprint, jsonify, request

from app.utils.ok import ok
from app.utils.convert_to_decimals import convert_decimals

log_bp = Blueprint("log", __name__, url_prefix="/api/logs")

def add_log(user_id, action, message, company_reg_no, **kwargs):

    log = Log(
        company_reg_no = company_reg_no,
        user_id = user_id,
        action = action,
        message = message,
        info = convert_decimals(kwargs)
    )

    db.session.add(log)
    db.session.commit()

@log_bp.route("/get", methods=["POST"])
def get_company_logs():
    payload = request.get_json()
    company_reg_no = payload.get("company_reg_no")
    user_id = payload.get("user_id")

    logs = Log.query.filter_by(company_reg_no = company_reg_no).all()
    
    data = [
        {
            "company_reg_no": l.company_reg_no,
            "timestamp": l.time,
            "user": l.user.first_name + " " + l.user.last_name,
            "user_id": l.user_id,
            "action": l.action,
            "message": l.message,
            "info": l.info or None
        } for l in logs ]
    
    add_log (
        action="VIEW",
        message=f"Admin user viewed company logs",
        company_reg_no=company_reg_no,
        user_id=user_id
    )

    return jsonify(data)