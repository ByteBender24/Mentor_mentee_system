from django.shortcuts import render, redirect
from Tree import *
from queue_meeting import *
from Hashmap import *
from imports import all_meeting_requests, mentor_meeting_history, tree, queue, announcements_list

# Create your views here.


def mentee_home(request):
    """
    View for rendering the mentee home page.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the mentee home page with mentee details.
    """
    mentee = request.session.get("mentee")
    mentee_node = tree.find_node_by_name(mentee)
    return render(request, "mentee_home.html", {"mentee": mentee})


def request_meeting(request):
    """
    View for the mentee request page. Handles the POST request to submit meeting requests.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the mentee home page after submitting the meeting request,
                      or to render the meeting request form.
    """
    mentee = request.session.get("mentee")
    mentee_node = tree.find_node_by_name(mentee)
    mentor = mentee_node.parent
    mentor_name = mentor.name
    if request.method == 'POST':
        date = request.POST.get('date')
        text = request.POST.get('text')
        request_obj = MeetingRequest(mentee_name=mentee, date=date, text=text)
        queue = all_meeting_requests.get_meeting_request_queue(mentor_name)
        if queue is None:
            all_meeting_requests.add_meeting_request(mentor_name, request_obj)
            queue = all_meeting_requests.get_meeting_request_queue(mentor_name)
        queue.enqueue(request_obj)
        all_meeting_requests.add_meeting_request(mentor, queue)
        return render(request, 'mentee_home.html', {"mentee": mentee})
    return render(request, 'request_meeting_mentee.html', {"mentee": mentee})


def announcement_mentee(request):
    """
    View for rendering the announcements page for the mentee.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the announcements page with announcements and today's date.
    """
    # Retrieve the announcements from the data structure where mentor stored them
    # Replace 'announcements_list' with the appropriate variable containing the announcements
    announcements = announcements_list
    today = request.session.get("today_date")
    return render(request, 'announcement_mentee.html', {'announcements': announcements, "date": today})


def mentor_profile(request):
    """
    View for rendering the mentor's profile page for the currently logged-in mentee.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the mentor's profile page with mentor details.
    """
    mentee = request.session.get("mentee")
    mentee_node = tree.find_node_by_name(mentee)
    mentor_node = mentee_node.parent
    mentor = mentor_node.name

    return render(request, "mentor_profile.html", {"mentor": mentor_node})


def show_mentee_details(request):
    """
    View for rendering the mentee's details page for the currently logged-in mentee.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the mentee's details page with mentee details.
    """
    mentee = request.session.get("mentee")
    mentee_node = tree.find_node_by_name(mentee)
    return render(request, "mentee_details.html", {"mentee": mentee_node, "readonly": "readonly"})
import string
import random
import csv

def generate_random_password(length=10):
    """
    Generate a simple random password.

    Parameters:
        length (int, optional): The length of the password to generate. Defaults to 10.

    Returns:
        str: A randomly generated password containing lowercase letters, uppercase letters, and digits.

    Example:
        generate_random_password()
        'Mj5zEg6K7n'
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def change_csv_password(csv_file, username, new_password):
    """
    Change the password for a given username in a CSV file.

    Parameters:
        csv_file (str): The path to the CSV file containing username, password, and status.
        username (str): The username for which the password needs to be changed.
        new_password (str): The new password to set for the given username.

    Returns:
        bool: True if the password was changed successfully, False otherwise.

    Example:
        change_csv_password('logindetails.csv', 'Heisenberg', 'newpassword')
        True
    """
    with open(csv_file, 'r') as file:
        rows = list(csv.reader(file))

    for i, row in enumerate(rows):
        stored_username, _, _ = row
        if stored_username.strip() == username.strip():
            rows[i][1] = new_password
            break
    else:
        return False

    with open(csv_file, 'w', newline='') as file:
        csv.writer(file).writerows(rows)

    return True