from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment, Teacher

from .schema import AssignmentSchema, AssignmentGradeSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_all_assignments(p):
  """List all submitted or graded assignments"""
  submitted_or_graded = Assignment.get_submitted_or_gradded()
  submitted_or_graded_dump = AssignmentSchema().dump(submitted_or_graded, many=True)
  
  return APIResponse.respond(data=submitted_or_graded_dump)


@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_all_teachers(p):
  """List all teachers"""
  teachers = Teacher.get_teachers()
  teachers_dump = AssignmentSchema().dump(teachers, many=True)
  
  return APIResponse.respond(data=teachers_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def regrade_assigment(p, incoming_payload):
    """Regrade an assignment graded by a teacher"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)

