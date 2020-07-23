from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from ems_admin.selectors import get_user, get_user_from_employee


def send_hr_mail_on_contract_expiry(approvers, contract, domain=None):
    approver_emails = []
    for approver in approvers:
        approver_emails.append(approver.email)

    context = {
        "applicant_name": contract.applicant,
        "server_url": domain
    }

    subject, from_email, to = 'Contract Expiry', None, approver_emails,
    html_content = get_template("email/hr_contract_expiry_reminder.html").render(context)
    msg = EmailMultiAlternatives(subject, None, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def send_remainder_on_contract_expiry(contract):
    employee = contract.employee
    user = get_user_from_employee(employee)
