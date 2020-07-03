from survey.models import Question

def SurveyCount(request):
    count = Question.objects.count()
    return {"survey_count": count}