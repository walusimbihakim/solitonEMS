from contracts.models import Contract
import datetime


def get_contract(contract_id):
    contract = Contract.objects.get(pk=contract_id)
    return contract


def get_all_contracts():
    return Contract.objects.all()


def get_active_contracts():
    return Contract.objects.filter(status="Active")


def get_terminated_contracts():
    return Contract.objects.exclude(status="Active")


def get_employee_contracts(employee):
    return Contract.objects.filter(status="Active", employee=employee)


def is_contract_expired(contract):
    """Check if contract is expired"""
    return contract.expiry_date > datetime.date.today()
