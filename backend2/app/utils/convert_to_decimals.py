from decimal import Decimal

def convert_decimals(obj):
    if isinstance(obj, dict):
        return {a: convert_decimals(b) for a, b in obj.items()}
    elif isinstance(obj, list):
        return [convert_decimals(a) for a in obj]
    elif isinstance(obj, Decimal):
        return float(obj)
    return obj