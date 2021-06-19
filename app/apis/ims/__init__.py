"""
app.apis.ims.init
-------------------

"""
from flask_restful import Api

from apis.ims import caliper, rest, lti_11, lti_13, cim, assignment_grades, deep_link, proctoring, names_roles, groups, jwks, outcomes, health


def evaluate_url(url, prefix_url):
    """

    :param url:
    :param prefix_url:
    :return:
    """
    return (prefix_url if prefix_url else '') + url


def init_app(api: Api, prefix_url=None):
    """
    :param prefix_url:
    :param api:
    :return:
    """

    api.add_resource(caliper.Send, evaluate_url('/caliper/send', prefix_url))
    api.add_resource(caliper.Register, evaluate_url('/caliper/register', prefix_url))
    api.add_resource(caliper.Caliper, evaluate_url('/caliper', prefix_url))

    api.add_resource(rest.Auth, evaluate_url('/rest/auth', prefix_url))
    api.add_resource(rest.User, evaluate_url('/rest/user', prefix_url))
    api.add_resource(rest.Course, evaluate_url('/rest/course', prefix_url))

    api.add_resource(outcomes.Outcomes, evaluate_url('/lti/outcomes', prefix_url))
    api.add_resource(outcomes.SendOutcomes, evaluate_url('/lti/send_outcomes', prefix_url))
    api.add_resource(outcomes.GetOutcomes, evaluate_url('/lti/get_outcomes', prefix_url))

    api.add_resource(lti_11.Membership, evaluate_url('/lti/membership', prefix_url))
    api.add_resource(lti_11.Lti, evaluate_url('/lti/11/launch', prefix_url))

    api.add_resource(cim.CIMRequest, evaluate_url('/contentItem/request', prefix_url))
    api.add_resource(cim.ContentItemData, evaluate_url('/contentItem/data', prefix_url))

    api.add_resource(lti_13.Lti13Launch, evaluate_url('/lti/13/launch', prefix_url))
    api.add_resource(lti_13.JWTPayloadData, evaluate_url('/lti/13/payloadData', prefix_url))
    api.add_resource(lti_13.Login, evaluate_url('/lti/13/login', prefix_url))

    api.add_resource(deep_link.DeepLinkingPayloadData, evaluate_url('/deepLink/payloadData', prefix_url))
    api.add_resource(deep_link.DeepLinkingContent, evaluate_url('/deepLink/content', prefix_url))
    api.add_resource(deep_link.CustomDeepLinkingContentTypes, evaluate_url('/deepLink/content/custom/contentTypes', prefix_url))
    api.add_resource(deep_link.DeepLinkingOptions, evaluate_url('/deepLink/options', prefix_url))
    api.add_resource(deep_link.DeepLinkingFrame, evaluate_url('/deepLink/frame', prefix_url))

    api.add_resource(proctoring.ProctoringPayloadData, evaluate_url('/proctoring/payloadData', prefix_url))
    api.add_resource(proctoring.BuildProctoringStartReturnPayload,
                     evaluate_url('/buildProctoringStartReturnPayload', prefix_url))
    api.add_resource(proctoring.BuildProctoringEndReturnPayload,
                     evaluate_url('/buildProctoringEndReturnPayload', prefix_url))

    api.add_resource(names_roles.NamesAndRoles, evaluate_url('/namesAndRoles', prefix_url))
    api.add_resource(names_roles.NamesAndRoles2, evaluate_url('/namesAndRoles2', prefix_url))
    api.add_resource(names_roles.NamesRolesPayloadData, evaluate_url('/namesAndRoles/payloadData', prefix_url))

    api.add_resource(groups.Groups, evaluate_url('/groups', prefix_url), evaluate_url('/getgroups', prefix_url))
    api.add_resource(groups.GroupsPayloadData, evaluate_url('/groups/payloadData', prefix_url))
    api.add_resource(groups.GroupSets, evaluate_url('/groups/sets', prefix_url))
    api.add_resource(groups.GroupSetsPayloadData, evaluate_url('/groups/sets/payloadData', prefix_url))

    api.add_resource(assignment_grades.AssignmentAndGrades, evaluate_url('/assignAndGrades', prefix_url))
    api.add_resource(assignment_grades.ReadColumn, evaluate_url('/agsReadCols', prefix_url))
    api.add_resource(assignment_grades.AddColumn, evaluate_url('/agsAddcol', prefix_url))
    api.add_resource(assignment_grades.DeleteColumn, evaluate_url('/agsDeleteCol', prefix_url))
    api.add_resource(assignment_grades.Results, evaluate_url('/agsResults', prefix_url))
    api.add_resource(assignment_grades.Scores, evaluate_url('/agsScores', prefix_url))
    api.add_resource(assignment_grades.ClearScores, evaluate_url('/agsClearScores', prefix_url))
    api.add_resource(assignment_grades.SubmitAttempt, evaluate_url('/agsSubmitAttempt', prefix_url))
    api.add_resource(assignment_grades.AssignmentGradesPayloadData, evaluate_url('/agPayloadData', prefix_url))

    api.add_resource(jwks.WellKnownJWKS, evaluate_url('/jwks', prefix_url))
    api.add_resource(health.HealthCheck, evaluate_url('/healthCheck', prefix_url))
