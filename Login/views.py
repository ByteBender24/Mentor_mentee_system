import string
import random
from django.shortcuts import render, redirect
import csv
import threading
from imports import check_tree_object
# Create your views here.


def csv_writer(file_name, word1, word2):
    """
    Function to write data to a CSV file.

    Parameters:
        file_name (str): The name of the CSV file.
        word1 (str): The first word to write to the CSV file.
        word2 (str): The second word to write to the CSV file.
    """
    with open(f"{file_name}", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([word1, word2])
    pass


def logout(request):
    """
    View for logging out the user and clearing session data.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to redirect the user to the login page.
    """
    request.session['mentor'] = None
    request.session['mentee'] = None
    request.session['adminmm'] = None

    return login(request)


def login(request):
    """
    View for handling user login.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the login page or redirect to the corresponding user dashboard.
    """
    if request.method == "GET":
        return render(request, "Login.html")
    if request.method == "POST":
        if request.session.get("isFirst") is None:
            # Create a new thread to check and load the tree object (assuming the implementation of `check_tree_object`)
            t1 = threading.Thread(target=check_tree_object, args=(request,))
            t1.start()
        else:
            request.session["isFirst"] = False

        username = parse_string(request.POST.get("username"))
        password = reverse_parse_string(request.POST.get("password"))

        # Check user credentials and determine the user status
        status = check_credentials(username, password)
        if status != False:
            request.session[f'{status}'] = username
            # Construct the redirect URL based on the user status
            redirect_url = f"/{status}/{status}/"
            return redirect(redirect_url)
        else:
            return render(request, "Login.html", {"error": "Invalid credentials"})


def check_credentials(username, password):
    """
    Function to check user credentials against the stored login details in a CSV file.

    Parameters:
        username (str): The username entered by the user.
        password (str): The password entered by the user.

    Returns:
        str or False: If the credentials match, returns the status (e.g., "mentor", "mentee", "adminmm").
                      If the credentials do not match, returns False.
    """
    with open('logindetails.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            stored_username, stored_password, status = row
            if username.strip() == stored_username.strip() and password.strip() == stored_password.strip():
                return status
    return False


def parse_string(string: str):
    """
    Function to parse a string and replace specific characters with corresponding replacements.

    Parameters:
        string (str): The string to be parsed.

    Returns:
        str: The parsed string with specific characters replaced.
    """
    if "," in string:
        string = string.replace(",", "_")
    if "\n" in string:
        string = string.replace("\n", "->")
    if "\r" in string:
        string = string.replace("\r", "<")

    return string


def reverse_parse_string(string: str):
    """
    Function to reverse parse a string and replace specific replacements with original characters.

    Parameters:
        string (str): The string to be reverse parsed.

    Returns:
        str: The reverse parsed string with specific replacements restored.
    """
    return string.replace("_", ","). replace("->", "\n").replace("<", "\r")


def forgotpassword(request):
    """
    View for rendering the "forgot password" page.

    Parameters:
        request (HttpRequest): The request object sent by the client.

    Returns:
        HttpResponse: A response to render the "forgot password" page.
    """
    return render(request, "forgotpassword.html")


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
