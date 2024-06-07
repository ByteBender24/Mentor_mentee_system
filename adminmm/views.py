import string
import random
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
    """
    View for rendering the admin's home page.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the admin's home page.
    """
    return render(request, "admin_home.html")


def csv_writer(file_name, word1, word2, word3):
    """
    Utility function for writing data to a CSV file.

    Parameters:
        file_name (str): The name of the CSV file.
        word1 (str): The first word to be written to the CSV file.
        word2 (str): The second word to be written to the CSV file.
        word3 (str): The third word to be written to the CSV file.

    Returns:
        None
    """
    with open(f"{file_name}", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([word1, word2, word3])


def add_mentor(request):
    """
    View for adding a new mentor to the system.

    Parameters:
        request (HttpRequest): The request object sent by the client, containing mentor details.

    Returns:
        HttpResponse: A response to render the admin's home page after adding the new mentor.
    """
    mentor_name = request.POST.get("mentor-name")
    mentor_department = request.POST.get("mentor-department")

    # Add the mentor to the tree
    tree.add_mentor(mentor_name, mentor_department)

    # Write mentor details to the logindetails.csv file
    csv_writer("logindetails.csv", mentor_name, "9900", "mentor")

    return render(request, "admin_home.html")


def overall_report(request):
    """
    View for generating an overall report of mentors and their associated mentees.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the overall_report.html template with the generated report.
    """
    # Get the mentors and their associated mentees in an inorder traversal
    traversal_result = tree.inorder_traversal(tree.getroot())

    # Create a list to store the mentor-mentee data
    mentor_mentee_data = []

    # Iterate over the traversal result and populate the mentor_mentee_data list
    for mentor, mentees in traversal_result:
        mentor_name = mentor.get_name()
        mentor_department = mentor.get_department()
        mentee_names = [mentee.get_name()
                        for mentee, _ in mentees]  # Extract mentee names
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
    """
    View for updating mentor details.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to indicate the success of mentor details update.
    """
    mentor = request.session.get('mentor')
    mentor_node = tree.find_node_by_name(mentor)

    if request.method == "GET":
        """
        Handle the GET request for updating mentor details.
        This renders the 'mentordetails.html' template with the existing mentor details.

        Returns:
            HttpResponse: A response to render the 'mentordetails.html' template with the existing mentor details.
        """
        print(mentor)
        print(mentor_node)
        return render(request, 'mentordetails.html', {"mentor": mentor_node})
    elif request.method == "POST":
        """
        Handle the POST request for updating mentor details.
        This updates the mentor details based on the data received from the form.

        Returns:
            HttpResponse: A response to indicate the success of mentor details update.
        """
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

        # Education
        part_education = request.POST.getlist('education[]')
        institution = request.POST.getlist("institution[]")
        education = dict(zip(institution, part_education))

        # Achievements
        part_achievement = request.POST.getlist('achievements[]')
        year = request.POST.getlist("year[]")
        achievements = dict(zip(year, part_achievement))

        # availability & contact info
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
    """
    View for displaying mentor details.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the mentor details on the 'display_mentor.html' template.
    """
    print(request.method)
    mentor = request.POST.get("mentor-search")

    if request.method == "GET":
        """
        Handle the GET request for displaying mentor details.
        This renders the 'display_mentor.html' template with the mentor's details.

        Returns:
            HttpResponse: A response to render the 'display_mentor.html' template with the mentor's details.
        """
        print(mentor)
        mentor_node = tree.find_node_by_name(mentor)
        return render(request, "display_mentor.html", {"mentor": mentor_node})

    if request.method == "POST":
        """
        Handle the POST request for displaying mentor details.
        This retrieves the mentor's details, meeting history, and generates a line graph of the mentee's marks (if available).
        Then, it renders the 'display_mentor.html' template with the mentor's details, meeting history, and graph.

        Returns:
            HttpResponse: A response to render the 'display_mentor.html' template with the mentor's details, meeting history, and graph.
        """
        print(mentor)
        mentor_node = tree.find_node_by_name(mentor)

        if mentor_node is None:
            return admin_home(request)

        print(mentor_node.name)
        mentor_graph = mentor_meeting_history.generate_meeting_graph(mentor)
        meeting_details = mentor_meeting_history.get_meeting_records(mentor)

        return render(request, "display_mentor.html", {"mentor": mentor_node, "meeting_details": meeting_details, "mentor_graph": mentor_graph})

    return render(request, "display_mentor.html")


def view_mentee_details(request):
    """
    View for displaying mentee details and marks.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the mentee details and marks on the 'mentee.html' template.
    """
    print(request.method)
    mentee = request.POST.get("mentee-search")

    if request.method == "GET":
        """
        Handle the GET request for displaying mentee details and marks.
        This renders the 'mentee.html' template with the mentee's details.

        Returns:
            HttpResponse: A response to render the 'mentee.html' template with the mentee's details.
        """
        print(mentee)
        mentee_node = tree.find_node_by_name(mentee)
        return render(request, "mentee.html", {"mentee": mentee_node})

    if request.method == "POST":
        """
        Handle the POST request for displaying mentee details and marks.
        This retrieves the mentee's marks, generates a line graph, and renders the 'mentee.html' template with the mentee's details and graph.

        Returns:
            HttpResponse: A response to render the 'mentee.html' template with the mentee's details and graph.
        """
        print(mentee)
        mentee_node = tree.find_node_by_name(mentee)
        print(mentee_node.name)
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
                {"mentee": mentee_node, "mentee_marks": mentee_marks,
                    "image_base64": image_base64},
            )

        return render(request, "mentee.html", {"mentee": mentee_node})

    return render(request, "mentee.html")


def delete_mentor(request):
    """
    View for deleting a mentor and reassigning mentees.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to indicate the successful deletion of the mentor and the unassigned mentees (if any).
    """
    if request.method == "POST":
        mentor_name = request.POST.get("mentor-name")
        mentor_node = tree.find_node_by_name(mentor_name)

        if mentor_node is None:
            return render(request, "admin_home.html", {"messages": ["No mentor available"]})

        unassigned_mentees = tree.remove_mentor(mentor_name)
        return render(request, "admin_home.html", {"unassigned_mentees": unassigned_mentees, "messages": ["Mentor deleted!"]})


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
