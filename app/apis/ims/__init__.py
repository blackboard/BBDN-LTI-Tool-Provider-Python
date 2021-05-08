"""
app.apis.ims.init
-------------------

"""
from flask_restful import Api

from apis.ims import caliper, rest, lti_11, lti_13, cim, assignment_grades, deep_link, proctoring, names_roles, groups, jwks


def init_app(api: Api):
    """
    :param api:
    :return:
    """
    # app.register_blueprint(internal, url_prefix="/internal")

    api.add_resource(caliper.Send, '/caliper/send')
    api.add_resource(caliper.Register, '/caliper/register')
    api.add_resource(caliper.Caliper, '/caliper')

    api.add_resource(rest.Auth, '/rest/auth')
    api.add_resource(rest.User, '/rest/user')
    api.add_resource(rest.Course, '/rest/course')

    api.add_resource(lti_11.Outcomes, '/ims/outcomes')
    api.add_resource(lti_11.SendOutcomes, '/ims/send_outcomes')
    api.add_resource(lti_11.GetOutcomes, '/ims/get_outcomes')
    api.add_resource(lti_11.Membership, '/ims/membership')
    api.add_resource(lti_11.Lti, '/ims')

    api.add_resource(cim.CIMRequest, '/CIMRequest')
    api.add_resource(cim.ContentItemData, '/contentitemdata')

    api.add_resource(lti_13.Lti13, '/lti13')
    api.add_resource(lti_13.JWTPayloadData, '/jwtPayloadData')
    api.add_resource(lti_13.Login, '/login')

    api.add_resource(deep_link.DeepLinkingPayloadData, '/dlPayloadData')
    api.add_resource(deep_link.DeepLinkingContent, '/deepLinkContent')

    api.add_resource(proctoring.ProctoringPayloadData, '/getProctoringPayloadData')
    api.add_resource(proctoring.BuildProctoringStartReturnPayload, '/buildProctoringStartReturnPayload')
    api.add_resource(proctoring.BuildProctoringEndReturnPayload, '/buildProctoringEndReturnPayload')

    api.add_resource(names_roles.NamesAndRoles, '/namesAndRoles')
    api.add_resource(names_roles.NamesAndRoles2, '/namesAndRoles2')
    api.add_resource(names_roles.NamesRolesPayloadData, '/nrPayloadData')

    api.add_resource(groups.Groups, '/groups', '/getgroups')
    api.add_resource(groups.GroupsPayloadData, '/groupsPayloadData')
    api.add_resource(groups.GroupSets, '/groupsets')
    api.add_resource(groups.GroupSetsPayloadData, '/groupSetsPayloadData')

    api.add_resource(assignment_grades.AssignmentAndGrades, '/assignAndGrades')
    api.add_resource(assignment_grades.ReadColumn, '/agsReadCols')
    api.add_resource(assignment_grades.AddColumn, '/agsAddcol')
    api.add_resource(assignment_grades.DeleteColumn, '/agsDeleteCol')
    api.add_resource(assignment_grades.Results, '/agsResults')
    api.add_resource(assignment_grades.Scores, '/agsScores')
    api.add_resource(assignment_grades.ClearScores, '/agsClearScores')
    api.add_resource(assignment_grades.SubmitAttempt, '/agsSubmitAttempt')
    api.add_resource(assignment_grades.AssignmentGradesPayloadData, '/agPayloadData')

    api.add_resource(jwks.WellKnownJWKS, '/.well-known/jwks.json')
