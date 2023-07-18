from django.shortcuts import render, redirect
from Tree import *
from queue_meeting import *
from Hashmap import *
from imports import all_meeting_requests, mentor_meeting_history, tree, queue, announcements_list

# Create your views here.
def mentee_home(request):
    mentee = request.session.get("mentee")
    mentee_node = tree.find_node_by_name(mentee)
    return render(request, "mentee_home.html", {"mentee": mentee})

def request_meeting(request):
    """
    View for the mentee request page.
    """
    mentee = request.session.get("mentee")
    mentee_node = tree.find_node_by_name(mentee)
    mentor = mentee_node.parent
    mentor_name = mentor.name
    print (mentor_name)
    if request.method == 'POST':
        print (mentee)
        date = request.POST.get('date')
        text = request.POST.get('text')
        request_obj = MeetingRequest(mentee_name=mentee, date=date, text=text)
        queue = all_meeting_requests.get_meeting_request_queue(mentor_name)
        print (request_obj)
        if queue is None:
            all_meeting_requests.add_meeting_request(mentor_name, request_obj)
            queue = all_meeting_requests.get_meeting_request_queue(mentor_name)
        queue.enqueue(request_obj)
        print (queue)
        all_meeting_requests.add_meeting_request(mentor, queue)
        return render(request, 'mentee_home.html' , {"mentee" : mentee})
    return render(request, 'request_meeting_mentee.html', {"mentee" : mentee})

def announcement_mentee(request):
    # Retrieve the announcements from the data structure where mentor stored them
    # Replace 'announcements_list' with the appropriate variable containing the announcements
    announcements = announcements_list
    today = request.session.get("today_date")   
    print (announcement_mentee)
    return render(request, 'announcement_mentee.html', {'announcements': announcements, "date": today})

def mentor_profile(request):
    mentee = request.session.get("mentee")
    mentee_node = tree.find_node_by_name(mentee)
    mentor_node = mentee_node.parent    
    mentor = mentor_node.name

    return render(request, "mentor_profile.html", {"mentor" : mentor_node})

def show_mentee_details(request):
    mentee = request.session.get("mentee")
    mentee_node = tree.find_node_by_name(mentee)
    return render(request, "mentee_details.html", {"mentee" : mentee_node, "readonly": "readonly"})