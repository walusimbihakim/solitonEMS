from leave.selectors import get_all_non_expired_leave_plan_applications
from leave.services import expire_leave_plan_application


def expire_leave_plan_applications():
    non_expired_leave_plan_applications = get_all_non_expired_leave_plan_applications()
    for leave_plan_application in non_expired_leave_plan_applications:
        expire_leave_plan_application(leave_plan_application, 10)
    return True
