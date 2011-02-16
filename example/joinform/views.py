# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from example.joinform.forms import JoinForm

def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = 'Title: ' + cd['title']+'\n'
            message = message + '\n First Name: ' + cd['firstname'] +'\n'
            message = message + '\n Last Name: ' + cd['lastname'] +'\n'
            message = message + '\n Birthday Date: ' +'\n'
            message = message + ' Month: ' + cd['bdateMonth']
            message = message + ' Day: ' + cd['bdateDay']
            message = message + ' Year: ' + cd['bdateYear']+'\n'
            message = message + '\n Marital Status: ' + cd['marital']+'\n'
            message = message + '\n Occupation: ' + cd['occupation']+'\n'
            message = message + '\n Firm/Business Name & Address: ' + cd['firm']+'\n'
            message = message + '\n Business Phone #: ' + cd['bphone']+'\n'
            message = message + '\n Home Phone #: ' + cd['hphone']+'\n'
            message = message + '\n Pager #: ' + cd['pager']+'\n'
            message = message + '\n Email Address: ' + cd['email']+'\n'
            message = message + '\n Religious Background: ' + cd['religion']+'\n'
            message = message + '\n Please check all that apply: '+'\n'
            message = message + cd['previousjewish'].replace("u'","")+'\n'
            message = message + '\n Can you: '+'\n'
            message = message + cd['previousexp'].replace("u'","")+'\n'
            message = message + '\n Do you have an interest in any of the following \n committees/activities: '+'\n'
            message = message + cd['activity'].replace("u'","")+'\n'
            message = message + '\n Yahrzeits   I/We observe \n'
            if cd['hebrewdate'] == True:
                message = message + 'Hebrew Date \n'
            if cd['englishdate'] == True:
                message = message + 'English Date \n'
            message = message + '\n Name of Deceased Relative--Relationship--Date of Death'
            message = message + '\n' + cd['nameofdeceased1'] +'--'+ cd['relationship1'] +'--'+ cd['dateofdeath1']
            message = message + '\n' + cd['nameofdeceased2'] +'--'+ cd['relationship2'] + '--'+cd['dateofdeath2']
            message = message + '\n' + cd['nameofdeceased3'] +'--'+ cd['relationship3'] + '--'+cd['dateofdeath3']+'\n'
            message = message + '\n Number of Children: ' + cd['numofchild']
            message = message + '\n Name--Age--Gender--Grade--Name of School/College--Bar/Bat Mitzvah & Year--Use Photo'
            message = message + '\n' + cd['nameofchild1'] +'--'+ cd['ageofchild1'] +'--'+ cd['genderofchild1']+'--'+cd['nameofschool1']+'--'+cd['barmitzvah1']+'--'+str(cd['usephoto1'])
            message = message + '\n' + cd['nameofchild2'] +'--'+ cd['ageofchild2'] +'--'+ cd['genderofchild2']+'--'+cd['nameofschool2']+'--'+cd['barmitzvah2']+'--'+str(cd['usephoto2'])
            message = message + '\n'+ cd['nameofchild3'] +'--'+ cd['ageofchild3'] +'--'+ cd['genderofchild3']+'--'+cd['nameofschool3']+'--'+cd['barmitzvah3']+'--'+str(cd['usephoto3'])
            message = message + '\n' + cd['nameofchild4'] +'--'+ cd['ageofchild4'] +'--'+ cd['genderofchild4']+'--'+cd['nameofschool4']+'--'+cd['barmitzvah4']+'--'+str(cd['usephoto4'])
            message = message + '\n' + cd['nameofchild5'] +'--'+ cd['ageofchild5'] +'--'+ cd['genderofchild5']+'--'+cd['nameofschool5']+'--'+cd['barmitzvah5']+'--'+str(cd['usephoto5']) +'\n'
            message = message + '\n Special Talents or Skills: \n' + cd['specialtalent']+'\n'
            message = message + '\n Reasons for joining Temple Bat Yahm: \n' + cd['reasonsforjoin']+'\n'
            send_mail(
                cd['firstname'] + cd['lastname'],
                message,
                cd.get('email', 'noreply@example.com'),
                ['jointemplebatyahm@gmail.com'],
            )
            return HttpResponse(cd['title']+'\n'+ cd['activity'])
    else:
        form = JoinForm()
    return render_to_response('join_form.html', {'form': form})
