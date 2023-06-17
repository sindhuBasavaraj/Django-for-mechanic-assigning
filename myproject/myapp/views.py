from django.shortcuts import render
from .models import Issue, Agents, Mechanic
import random

def new_issue(request):
    if request.method == 'POST':
        # Get the form data from the request
        userID = request.POST.get('userID')
        location = request.POST.get('location')
        problem = request.POST.get('problem')

        # Create a new issue
        issue = Issue.objects.create(userID=userID, location=location, problem=problem)

        # Assign an agent with the least queue if available
        agents = Agents.objects.all().order_by('queue')

        if agents:
            agent = random.choice(agents)  # Assign the agent with the least queue
            agent.queue += 1
            agent.save()

            mechanics = Mechanic.objects.filter(availability=True)[:10]
            if mechanics:
                mechanic = random.choice(mechanics)
                mechanic.availability = True
                mechanic.save()
                issue.status = 'ASSIGNED'
                issue.mechanic = mechanics  # Associate the assigned mechanic with the issue
                issue.save()
            else:
                mechanic = None

            return render(request, 'success.html', {'issue': issue, 'agent':agent,'mechanic': mechanic})

    return render(request, 'new_issue.html')

