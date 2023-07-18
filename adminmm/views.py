from django.http import HttpResponse
from django.shortcuts import redirect, render
from Tree import *
from django.contrib import messages
from imports import all_meeting_requests, mentor_meeting_history, tree, queue
import csv
import matplotlib.pyplot as plt
import io
import urllib

# Create your views here.
def admin_home(request):
    return render(request, "admin_home.html")

def csv_writer(file_name, word1, word2, word3):
    with open(f"{file_name}", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([word1, word2, word3])
    pass

def add_mentor(request):
    mentor_name = request.POST.get("mentor-name")
    mentor_department = request.POST.get("mentor-department")

    # Add the mentor to the tree
    tree.add_mentor(mentor_name, mentor_department)
    csv_writer("logindetails.csv", mentor_name, "9900", "mentor")
    return render(request, "admin_home.html")

def overall_report(request):
    # Get the mentors and their associated mentees in an inorder traversal
    traversal_result = tree.inorder_traversal(tree.getroot())

    # Create a list to store the mentor-mentee data
    mentor_mentee_data = []

    # Iterate over the traversal result and populate the mentor_mentee_data list
    for mentor, mentees in traversal_result:
        mentor_name = mentor.get_name()
        mentor_department = mentor.get_department()
        mentee_names = [mentee.get_name() for mentee, _ in mentees]  # Extract mentee names
        mentor_nodes = tree.admin.children
        mentor_mentee_data.append({
            'mentor_name': mentor_name,
            'mentor_department': mentor_department,
            'mentees': mentee_names
        })

        total_mentees = 0

        for mentor in mentor_nodes:
            for mentee in mentor.children:
                total_mentees += 1

    # Prepare any additional data for the report

    # Pass the data to the template for rendering
    context = {
        'mentor_mentee_data': mentor_nodes,
        'total_mentees': total_mentees
    }

    return render(request, 'overall_report.html', context)

def update_mentor_details(request):
    mentor = request.session.get('mentor')
    mentor_node = tree.find_node_by_name(mentor)
    if request.method == "GET":
        print (mentor)
        print(mentor_node)
        return render(request, 'mentordetails.html', {"mentor" : mentor_node})
    elif request.method == "POST":

        #Name, photo, dept, exp, description
        name = request.POST.get('name')
        profile_picture = request.POST.get('profile_picture')
        department = request.POST.get('department')
        experience = request.POST.get('experience')
        description = request.POST.get('description')

        # Skills
        dep_skill = request.POST.getlist('department[]')
        part_skill = request.POST.getlist("skill[]")
        skills = dict(zip(dep_skill, part_skill))

        # Education
        part_education = request.POST.getlist('education[]')
        institution = request.POST.getlist("institution[]")
        education = dict(zip(institution, part_education))

        # Achievements
        part_achievement = request.POST.getlist('achievements[]')
        year = request.POST.getlist("year[]")
        achievements = dict(zip(year, part_achievement))

        #availability & contact info
        availability = request.POST.get('availability')
        contact_info = request.POST.get('contact-info')

        # Update mentor details
        mentor_node.update_name(name)
        mentor_node.update_department(department)
        mentor_node.update_profile_image(profile_picture)
        mentor_node.update_experience(experience)
        mentor_node.update_skills(skills)
        mentor_node.update_description(description)
        mentor_node.update_availability(availability)
        mentor_node.update_contact_info(contact_info)
        mentor_node.update_education(education)
        mentor_node.update_achievements(achievements)

        # Update mentor details in the tree structure
        # You can add your implementation here

        return HttpResponse("Mentor details updated successfully!")
    
def show_mentor_details(request):
    print (request.method)
    mentor = request.POST.get("mentor-search")
    if request.method == "GET":
        print (mentor)
        mentor_node = tree.find_node_by_name(mentor)
        return render(request, "display_mentor.html", {"mentor" : mentor_node})
    if request.method == "POST":
        print (mentor)
        mentor_node = tree.find_node_by_name(mentor)
        if mentor_node is None:
            return admin_home(request)
        print (mentor_node.name)
        mentor_graph = mentor_meeting_history.generate_meeting_graph(mentor) 
        meeting_details = mentor_meeting_history.get_meeting_records(mentor)
        return render(request, "display_mentor.html", {"mentor" : mentor_node, "meeting_details" : meeting_details, "mentor_graph" : mentor_graph})
    return render(request, "display_mentor.html")

def view_mentee_details(request):
    print (request.method)
    mentee = request.POST.get("mentee-search")
    if request.method == "GET":
        print (mentee)
        mentee_node = tree.find_node_by_name(mentee)
        return render(request, "mentee.html", {"mentee" : mentee_node})
    if request.method == "POST":
        print (mentee)
        mentee_node = tree.find_node_by_name(mentee)
        print (mentee_node.name)
        marks = mentee_node.marks
        if marks is not None:
            mentee_marks = {
                "CAT1": marks.CAT1,
                "CAT2": marks.CAT2,
                "SAT": marks.SAT,
                "End_sem": marks.End_sem,
            }

            # Generate the line graph using Matplotlib
            fig, ax = plt.subplots()
            ax.plot(
                mentee_marks.keys(),
                mentee_marks.values(),
                marker='o',
                linestyle='-',
                color='b',
            )
            ax.set_xlabel('Exams')
            ax.set_ylabel('Marks')
            ax.set_title('Mentee Marks')

            # Save the graph to a bytes buffer
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)

            # Encode the graph image to base64
            image_base64 = urllib.parse.quote(buffer.read())

            # Close the Matplotlib plot
            plt.close()
            
            return render(
                request,
                "mentee.html",
                {"mentee": mentee_node, "mentee_marks": mentee_marks, "image_base64": image_base64},
            )
        return render(request, "mentee.html", {"mentee" : mentee_node})
        
    return render(request, "mentee.html")

def delete_mentor(request):
    if request.method == "POST":
        mentor_name = request.POST.get("mentor-name")
        mentor_node = tree.find_node_by_name(mentor_name)
        if mentor_node is None:
            return render(request, "admin_home.html", {"messages" : ["No mentor available"]})
        unassigned_mentees = tree.remove_mentor(mentor_name)
        return render(request, "admin_home.html", {"unassigned_mentees" : unassigned_mentees, "messages":["Mentor deleted!"]})
