from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
from random import choice

# Create your views here.
def team_list(request):
    
    team_list = Team.objects.all()
    group = list()
    groups = list()
    country = list() 
    teams = []
    for team in team_list:
        teams.append(team) 
    
    #it will iterate for 8 groups
    while len(groups) < 8:
        group = []
        country = list()
        # this loop will add 4 teams to each group 
        while len(group) < 4:
            team = choice(teams)        
            # condition for first team to be og domestic 
            if team.isRed == True and len(group) == 0:
                
                group.append(team)
                country.append(team.country)
                teams.remove(team)
            

            if team.isRed == False and len(group) > 0:
                if team.country not in country:
                    group.append(team)
                    country.append(team.country)
                    teams.remove(team)
        groups.append(group)
        context = {
            "list1" : groups[:4],
            "list2" : groups[4:]
        }

    return render(request, 'team.html',context)
    


    
