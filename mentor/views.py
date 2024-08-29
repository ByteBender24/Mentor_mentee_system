from django.shortcuts import redirect, render, HttpResponse
from Tree import *
from Hashmap import *
from queue_meeting import *
from imports import all_meeting_requests, mentor_meeting_history, tree, queue, announcements_list
from datetime import date
import csv


def mentor_home(request):
    """
    Renders the mentor's home page.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered mentorhome.html template with the mentor's name passed as a context variable.
    """
    mentor = request.session.get('mentor')
    return render(request, 'mentorhome.html', {"mentor": mentor})


def csv_writer(file_name, word1, word2, word3):
    """
    Writes data to a CSV file.

    Args:
        file_name (str): The name of the CSV file.
        word1 (str): The first word to write.
        word2 (str): The second word to write.
        word3 (str): The third word to write.
    """
    with open(f"{file_name}", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([word1, word2, word3])
    pass


def add_mentee(request):
    """
    Adds a mentee to the mentor's list of mentees.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is GET, renders the add_mentee.html template.
        If the request method is POST, adds the mentee to the mentor's list of mentees and redirects to the mentor's home page.
    """
    mentor = request.session.get("mentor")
    if request.method == "GET":
        return render(request, "add_mentee.html")
    if request.method == "POST":
        mentee_name = request.POST.get("mentee_name")
        mentee_department = request.POST.get("mentee_department")

        csv_writer("logindetails.csv", mentee_name, "0099", "mentee")

        tree.add_mentee(mentor, mentee_name, mentee_department)
        print(tree)
        return redirect("/mentor/mentor")


def show_mentor_details(request):
    """
    Displays the details of the mentor.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is GET, renders the mentordetails.html template with the mentor's details passed as context variables.
        If the request method is not GET, returns an HTTP response indicating that no mentor is available.
    """
    if request.method == "GET":
        mentor = request.session.get('mentor')
        mentor_node = tree.find_node_by_name(mentor)
        mentor_node.skills = {"Programming Language": "Python"}
        mentor_node.education = {
            "Secondary Education": "HC school", "UG B.Tech": "SSLV College"}
        mentor_node.achievements = {"Project management": "HSV certified"}
        print(mentor)
        print(mentor_node)
        print(mentor_node.name)
        print("MENTOR")

        return render(request, 'mentordetails.html',
                      {"mentor": mentor_node,
                       "skills": mentor_node.skills.items(),
                       "education": mentor_node.education.items(),
                       "achievements": mentor_node.achievements.items(),
                       "readonly_state": True})
    return HttpResponse("No mentor available")


def show_mentee_details(request):
    """
    Displays the details of the mentee.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is GET, renders the menteedetails.html template with the mentee's details passed as context variables.
        If the request method is not GET, returns an HTTP response indicating that no mentee is available.
    """
    if request.method == "GET":
        mentee = request.session.get('mentee')
        print(mentee)
        mentee_node = tree.find_node_by_name(mentee)
        mentee_node.skills = {"Programming Language": "Python"}
        mentee_node.education = {"Secondary Education": "Holy Cross school"}
        mentee_node.achievements = {"Spelling Bee": "Top 3 in ISB"}

        print(mentee)
        print(mentee_node)
        print(mentee_node.name)

        return render(request, 'menteedetails.html',
                      {"mentee": mentee_node,
                       "skills": mentee_node.skills.items(),
                       "education": mentee_node.education.items(),
                       "achievements": mentee_node.achievements.items(),
                       "readonly_state": True})
    return HttpResponse("No mentee available")


def show_mentee_marks(request):
    """
    View for rendering the mentee's marks page in read-only mode.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the mentee's marks page with marks details in read-only mode.
    """
    if request.method == "GET":
        mentee = request.GET.get('name')
        mentee_node = tree.find_node_by_name(mentee)
        return render(request, 'marks.html', {"mentee": mentee_node, "readonly_state": True})
    return HttpResponse("None")


def update_mentee_marks(request):
    """
    View for rendering the mentee's marks page in edit mode and handling the updates to the marks.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the mentee's marks page with marks details in edit mode or
        a response after handling the updates to the marks.
    """
    if request.method == "GET":
        mentee = request.GET.get('name')
        request.session['mentee'] = mentee
        mentee_node = tree.find_node_by_name(mentee)
        return render(request, 'marks.html', {"mentee": mentee_node, "readonly_state": False})
    if request.method == "POST":
        CAT1 = request.POST.get("CAT1")
        CAT2 = request.POST.get("CAT2")
        SAT = request.POST.get("SAT")
        End_sem = request.POST.get("End_sem")
        mentee = request.session.get('mentee')
        mentee_node = tree.find_node_by_name(mentee)
        m = Marks(CAT1=CAT1, CAT2=CAT2, SAT=SAT, End_sem=End_sem)
        mentee_node.marks = m
        return render(request, 'marks.html', {"mentee": mentee_node, "readonly_state": True})


def update_mentee_details(request):
    """
    Updates the details of the mentee.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is GET, renders the menteedetails.html template in editable mode with the mentee's details passed as context variables.
        If the request method is POST, updates the mentee's details and redirects to the mentor's home page.
    """
    if request.method == "GET":
        mentee = request.GET.get('name')
        mentee_node = tree.find_node_by_name(mentee)
        mentee_node.skills = {"Programming Language": "Python"}
        mentee_node.education = {"Secondary Education": "Holy Cross school"}
        mentee_node.achievements = {"Spelling Bee": "Top 3 in ISB"}

        return render(request, 'menteedetails.html',
                      {"mentee": mentee_node,
                       "skills": mentee_node.skills.items(),
                       "education": mentee_node.education.items(),
                       "achievements": mentee_node.achievements.items(),
                       "readonly_state": False})
    elif request.method == "POST":

        # Name, photo, dept, exp, description
        name = request.POST.get('name')
        profile_picture = request.POST.get('profile_picture')
        department = request.POST.get('department')
        description = request.POST.get('description')

        # Skills
        dep_skill = request.POST.getlist('department[]')
        part_skill = request.POST.getlist("skill[]")
        skills = dict(zip(dep_skill, part_skill))
        print(skills)
        # Education
        part_education = request.POST.getlist('education[]')
        institution = request.POST.getlist("institution[]")
        education = dict(zip(institution, part_education))
        print(education)
        # Achievements
        part_achievement = request.POST.getlist('achievements[]')
        year = request.POST.getlist("year[]")
        achievements = dict(zip(year, part_achievement))
        print(achievements)
        # availability & contact info
        contact_info = request.POST.get('contact-info')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        nationality = request.POST.get('Nationality')
        religion = request.POST.get('religion')
        community = request.POST.get('Community')
        remarks = request.POST.get('remarks')
        mentee = tree.find_node_by_name(name)

        fields = {
            "name": name,
            "department": department,
            "profile_picture": profile_picture,
            "skills": skills,
            "description": description,
            "contact_info": contact_info,
            "education": education,
            "achievements": achievements,
            "dob": dob,
            "gender": gender,
            "nationality": nationality,
            "religion": religion,
            "community": community,
            "remarks": remarks
        }

        for field_name, field_value in fields.items():
            update_method = getattr(mentee, f"update_{field_name}", None)
            if update_method is not None:
                update_method(field_value)
            else:
                setattr(mentee, field_name, field_value)
            print(getattr(mentee, field_name))

        return redirect("mentor_home")


def update_mentor_details(request):
    """
    Updates the details of the mentor.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is GET, renders the mentordetails.html template in editable mode with the mentor's details passed as context variables.
        If the request method is POST, updates the mentor's details and redirects to the mentor's home page.
    """
    if request.method == "GET":
        mentor = request.session.get('mentor')
        mentor_node = tree.find_node_by_name(mentor)
        mentor_node.skills = {"Programming Language": "Python"}
        mentor_node.education = {
            "Secondary Education": "HC school", "UG B.Tech": "SSLV College"}
        mentor_node.achievements = {"Project management": "HSV certified"}
        print("MENTOR")

        return render(request, 'mentordetails.html',
                      {"mentor": mentor_node,
                       "skills": mentor_node.skills.items(),
                       "education": mentor_node.education.items(),
                       "achievements": mentor_node.achievements.items(),
                       "readonly_state": False})
    elif request.method == "POST":

        # Name, photo, dept, exp, description
        name = request.POST.get('name')
        profile_picture = request.POST.get('profile_picture')
        department = request.POST.get('department')
        experience = request.POST.get('experience')
        description = request.POST.get('description')

        # Skills
        dep_skill = request.POST.getlist('department[]')
        part_skill = request.POST.getlist("skill[]")
        skills = dict(zip(dep_skill, part_skill))
        print(skills)
        # Education
        part_education = request.POST.getlist('education[]')
        institution = request.POST.getlist("institution[]")
        education = dict(zip(institution, part_education))
        print(education)
        # Achievements
        part_achievement = request.POST.getlist('achievements[]')
        year = request.POST.getlist("year[]")
        achievements = dict(zip(year, part_achievement))
        print(achievements)
        # Availability & contact info
        availability = request.POST.get('availability')
        contact_info = request.POST.get('contact-info')

        mentor = tree.find_node_by_name(name)

        fields = {
            "name": name,
            "department": department,
            "profile_picture": profile_picture,
            "experience": experience,
            "description": description,
            "skills": skills,
            "education": education,
            "achievements": achievements,
            "availability": availability,
            "contact_info": contact_info
        }

        for field_name, field_value in fields.items():
            update_method = getattr(mentor, f"update_{field_name}", None)
            if update_method is not None:
                update_method(field_value)
            else:
                setattr(mentor, field_name, field_value)
            print(getattr(mentor, field_name))
        print(mentor)

        return redirect("mentor_home")


def search_mentee(request):
    """
    Searches for a mentee.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is GET, renders the search_mentee.html template.
        If the request method is POST, searches for the mentee and renders the display_mentee.html template with the mentee's details passed as context variables.
    """
    mentor = request.session.get("mentor")
    if request.method == "GET":
        return render(request, "search_mentee.html")
    if request.method == "POST":
        mentee_name = request.POST.get("mentee_name")
        request.session["mentee"] = mentee_name
        print(mentee_name)
        mentee = request.session.get("mentee")
        print(tree.get_mentees(mentor))
        if mentee in tree.get_mentees(mentor):
            mentee_node = tree.find_node_by_name(mentee)
            print(mentee)
            print(mentee_node.name)
            return render(request, "display_mentee.html", {"mentee": mentee_node})
    return render(request, "display_mentee.html")

def remove_duplicates_from_dict(meeting_dict):
    """
    Removes duplicates from the lists of meetings for each mentor in the dictionary.
    
    Args:
        meeting_dict (dict): A dictionary with mentor names as keys and lists of Meeting objects as values.
    
    Returns:
        dict: A dictionary with duplicates removed from the lists of meetings.
    """
    for mentor, meetings in meeting_dict.items():
        # Use a set to track seen meetings and ensure uniqueness
        seen = set()
        unique_meetings = []
        for meeting in meetings:
            if meeting not in seen:
                seen.add(meeting)
                unique_meetings.append(meeting)
        # Update the list with unique meetings
        meeting_dict[mentor] = unique_meetings
    return meeting_dict

def add_meeting(request):
    """
    Adds a meeting.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is GET, renders the meeting_history.html template with the mentor's meetings and meeting history passed as context variables.
        If the request method is POST, adds the meeting to the mentor's meeting history and redirects to the meeting history page.
    """
    mentor_name = request.session.get('mentor')
    
    # Initialize mentor_meeting_history if it is not yet instantiated
    if 'mentor_meeting_history' not in globals():
        global mentor_meeting_history
        mentor_meeting_history = MentorMeetingHistory()

    # Retrieve meeting records
    meetings = mentor_meeting_history.get_meeting_records(mentor_name)
    mentor = tree.find_node_by_name(mentor_name)

    if request.method == "POST":
        date = request.POST.get('date')
        link = request.POST.get('link')
        details = request.POST.get('details')
        participants = request.POST.getlist('participants')

        meeting = Meeting(date=date, link=link, details=details, participants=participants)
        meetings.append(meeting)
        mentor_meeting_history.add_meeting_record(mentor_name, meeting)
        
        # Remove duplicates
        mentor_meeting_history.meeting_history.put(mentor_name, remove_duplicates_from_dict({
            mentor_name: meetings
        }).get(mentor_name))

        print (mentor_meeting_history.meeting_history)
        return render(request, 'meeting_history.html', {
            'meetings': meetings,
            'mentor': mentor,
            'mentor_meeting_history': mentor_meeting_history
        })

    return render(request, 'meeting_history.html', {
        'meetings': meetings,
        'mentor': mentor,
        'mentor_meeting_history': mentor_meeting_history
    })



def list_of_mentees(request):
    """
    Renders the list of mentees page.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered list_of_all_mentees.html template with the mentor's name and list of mentees passed as context variables.
    """
    mentor = request.session.get('mentor')
    print(mentor)
    mentor_node = tree.find_node_by_name(mentor)
    mentor_children = mentor_node.children

    return render(request, "list_of_all_mentees.html", {"mentor": mentor, "mentees": mentor_children})


def search_meeting(request):
    """
    Searches for a meeting.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is GET, renders the meeting_search_edit.html template.
        If the request method is POST and a meeting is found, updates the meeting's details and renders the meeting_search_edit.html template with the updated meeting details.
        If the request method is POST and no meeting is found, renders the meeting_search_edit.html template.
    """
    mentor_name = request.session.get("mentor")
    meeting_info = mentor_meeting_history.get_meeting_records(mentor_name)
    meeting_searched = None

    if request.method == "POST":
        meeting_date = request.POST.get("meeting-search")
        print("POST")
        for meeting in meeting_info:
            print(meeting)
            print(meeting_date)
            print(".", meeting.date)
            if meeting_date == meeting.date:
                print("dasdasd", meeting_date)
                print(".", meeting.date)

                meeting_searched = meeting
                break

    if request.method == "GET" or not meeting_searched:

        return render(request, "meeting_search_edit.html")

    if request.method == "POST" and meeting_searched:
        meeting_searched.date = request.POST.get("date")
        meeting_searched.link = request.POST.get("link")
        meeting_searched.details = request.POST.get("details")
        meeting_searched.participants = request.POST.get("participants")
        print("participantssssss:", meeting_searched.participants)
        return render(request, "meeting_search_edit.html", {"meeting": meeting_searched})

    return render(request, "meeting_search_edit.html", {"meeting": meeting_searched})


def mentor_meeting_request(request):
    """
    Displays the meeting requests for the mentor.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered request_meeting.html template with the mentor's meeting requests passed as a context variable.
    """
    mentor = request.session.get("mentor")
    mentor_meeting_requests_queue = all_meeting_requests.get_meeting_request_queue(
        mentor)
    print(mentor_meeting_requests_queue)
    meeting_requests = mentor_meeting_requests_queue.list()
    return render(request, 'request_meeting.html', {'meeting_requests': meeting_requests})


def delete_mentee(request):
    """
    Deletes a mentee from the mentor's list of mentees.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is GET, renders the deletementee.html template.
        If the request method is POST, removes the mentee from the mentor's list of mentees and renders the mentor's home page.
    """
    if request.method == "GET":
        return render(request, "deletementee.html")
    if request.method == "POST":
        mentee = request.POST.get("name")
        mentor = request.session.get("mentor")
        tree.remove_mentee(mentor, mentee)
        return render(request, "mentorhome.html")


def announcement_mentor(request):
    """
    Adds an announcement made by the mentor.

    Args:
        request: The HTTP request object.

    Returns:
        If the request method is POST, adds the announcement to the list of announcements and redirects back to the mentor announcement page.
        If the request method is not POST, renders the announcement_mentor.html template.
    """
    if request.method == 'POST':
        announcement = request.POST.get('announcement')
        announcements_list.append(announcement)
        request.session["today_date"] = date.today().isoformat()
        print(announcements_list)
        # Redirect back to the mentor announcement page
        return redirect('announcement_mentor')

    return render(request, 'announcement_mentor.html')
