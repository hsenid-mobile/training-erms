from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

def addCVs(request):
    page_parameters = {}
    if request.method == "GET":
        if request.GET.get('firstName') and request.GET.get('secondName'):
            start_date = request.GET['firstName']
            end_date = request.GET['secondName']
            init_request = "false"
            print("#")
            print("#")
            print(start_date)
            print(end_date)
            print("#")
            print("#")
        else:
            init_request = "true"
        page_parameters = {"init_request": init_request}
    return render_to_response("erms/add_cv_form.html", page_parameters, context_instance=RequestContext(request))





# @login_required
# def addCVs(request):
#     return render_to_response("erms/add_cv_form.html", context_instance=RequestContext(request))
