class AdminNode:
    """
    Represents an admin node in a mentor-mentee system.
    """

    def __init__(self, ID, name):
        """
        Initializes an AdminNode object.

        Args:
            ID (int): The ID of the admin.
            name (str): The name of the admin.
        """
        self.id = ID
        self.name = name
        self.parent = None
        self.children = []
        self.department = "Admin"

    def __str__(self):
        """
        Returns a string representation of the AdminNode object.

        Returns:
            str: The string representation of the AdminNode object.
        """
        return f"Admin: {self.name} | Department: {self.department}"


class MentorNode:
    """
    Represents a mentor node in a mentor-mentee system.
    """

    def __init__(self, name, department, profile_picture=None, experience=None, skills=None, description=None,
                 availability=None, contact_info=None, education=None, achievements=None):
        """
        Initializes a MentorNode object.

        Args:
            name (str): The name of the mentor.
            department (str): The department of the mentor.
            profile_picture (str, optional): The URL or path to the mentor's profile picture. Defaults to None.
            experience (str, optional): The experience of the mentor. Defaults to None.
            skills (list, optional): The skills of the mentor. Defaults to None.
            description (str, optional): The description of the mentor. Defaults to None.
            availability (str, optional): The availability of the mentor. Defaults to None.
            contact_info (str, optional): The contact information of the mentor. Defaults to None.
            education (str, optional): The education information of the mentor. Defaults to None.
            achievements (str, optional): The achievements of the mentor. Defaults to None.
        """
        self.name = name
        self.profile_picture = profile_picture
        self.department = department
        self.experience = experience
        self.skills = skills
        self.description = description
        self.availability = availability
        self.contact_info = contact_info
        self.education = education
        self.achievements = achievements
        self.parent = None
        self.children = []

    def update_name(self, name):
        """
        Updates the name of the mentor.

        Args:
            name (str): The new name of the mentor.
        """
        self.name = name

    def update_department(self, department):
        """
        Updates the department of the mentor.

        Args:
            department (str): The new department of the mentor.
        """
        self.department = department

    def update_profile_image(self, img):
        """
        Updates the profile picture of the mentor.

        Args:
            img (str): The URL or path to the mentor's new profile picture.
        """
        self.profile_picture = img

    def update_experience(self, info):
        """
        Updates the experience of the mentor.

        Args:
            info (str): The new experience information of the mentor.
        """
        self.experience = info

    def update_skills(self, skills):
        """
        Updates the skills of the mentor.

        Args:
            skills (list): The new skills of the mentor.
        """
        self.skills = skills

    def update_description(self, description):
        """
        Updates the description of the mentor.

        Args:
            description (str): The new description of the mentor.
        """
        self.description = description

    def update_availability(self, availability):
        """
        Updates the availability of the mentor.

        Args:
            availability (str): The new availability of the mentor.
        """
        self.availability = availability

    def update_contact_info(self, contact_info):
        """
        Updates the contact information of the mentor.

        Args:
            contact_info (str): The new contact information of the mentor.
        """
        self.contact_info = contact_info

    def update_education(self, education):
        """
        Updates the education information of the mentor.

        Args:
            education (str): The new education information of the mentor.
        """
        self.education = education

    def update_achievements(self, achievements):
        """
        Updates the achievements of the mentor.

        Args:
            achievements (str): The new achievements of the mentor.
        """
        self.achievements = achievements

    def __str__(self):
        """
        Get a string representation of the MentorNode.
        :return: String representation of the MentorNode.
        """
        details = [
            f"Name: {self.name}",
            f"Department: {self.department}",
            f"Profile Picture: {self.profile_picture}",
            f"Experience: {self.experience}",
            f"Skills: {self.skills}",
            f"Description: {self.description}",
            f"Availability: {self.availability}",
            f"Contact Info: {self.contact_info}",
            f"Educations: {self.education}",
            f"Achievements: {self.achievements}"
        ]
        return "\n".join(details)

    def get_name(self):
        """
        Returns the name of the mentor.

        Returns:
            str: The name of the mentor.
        """
        return self.name

    def get_department(self):
        """
        Returns the department of the mentor.

        Returns:
            str: The department of the mentor.
        """
        return self.department


class Marks:
    def __init__(self, CAT1=None, CAT2=None, SAT=None, End_sem=None):
        self.CAT1 = CAT1
        self.CAT2 = CAT2
        self.SAT = SAT
        self.End_sem = End_sem

    def update_marks(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return str([self.CAT1, self.CAT2, self.SAT, self.End_sem])


class MenteeNode:
    """
    Represents a mentee node in a mentor-mentee system.
    """

    def __init__(self, name, department, profile_picture=None, experience=None, skills=None, description=None,
                 availability=None, contact_info=None, education=None, achievements=None, dob=None, gender=None,
                 nationality=None, religion=None, community=None, remarks=None, marks=None):
        """
        Initializes a MenteeNode object.

        Args:
            name (str): The name of the mentee.
            department (str): The department of the mentee.
            profile_picture (str, optional): The URL or path to the mentee's profile picture. Defaults to None.
            experience (str, optional): The experience of the mentee. Defaults to None.
            skills (list, optional): The skills of the mentee. Defaults to None.
            description (str, optional): The description of the mentee. Defaults to None.
            availability (str, optional): The availability of the mentee. Defaults to None.
            contact_info (str, optional): The contact information of the mentee. Defaults to None.
            education (str, optional): The education information of the mentee. Defaults to None.
            achievements (str, optional): The achievements of the mentee. Defaults to None.
            dob (str, optional): The date of birth of the mentee. Defaults to None.
            gender (str, optional): The gender of the mentee. Defaults to None.
            nationality (str, optional): The nationality of the mentee. Defaults to None.
            religion (str, optional): The religion of the mentee. Defaults to None.
            community (str, optional): The community of the mentee. Defaults to None.
        """
        self.name = name
        self.profile_picture = profile_picture
        self.department = department
        self.skills = skills
        self.contact_info = contact_info
        self.education = education
        self.achievements = achievements
        self.dob = dob
        self.gender = gender
        self.nationality = nationality
        self.religion = religion
        self.community = community
        self.remarks = remarks
        self.parent = None
        self.children = []
        self.marks = marks

    def update_marks(self, marks):
        """
        Updates the marks of the mentee.

        Args:
            marks (marks): The new marks of the mentee.
        """
        self.marks = marks

    def update_name(self, name):
        """
        Updates the name of the mentee.

        Args:
            name (str): The new name of the mentee.
        """
        self.name = name

    def update_department(self, department):
        """
        Updates the department of the mentee.

        Args:
            department (str): The new department of the mentee.
        """
        self.department = department

    def update_profile_image(self, img):
        """
        Updates the profile picture of the mentee.

        Args:
            img (str): The URL or path to the mentee's new profile picture.
        """
        self.profile_picture = img

    def update_skills(self, skills):
        """
        Updates the skills of the mentee.

        Args:
            skills (list): The new skills of the mentee.
        """
        self.skills = skills

    def update_contact_info(self, contact_info):
        """
        Updates the contact information of the mentee.

        Args:
            contact_info (str): The new contact information of the mentee.
        """
        self.contact_info = contact_info

    def update_education(self, education):
        """
        Updates the education information of the mentee.

        Args:
            education (str): The new education information of the mentee.
        """
        self.education = education

    def update_achievements(self, achievements):
        """
        Updates the achievements of the mentee.

        Args:
            achievements (str): The new achievements of the mentee.
        """
        self.achievements = achievements

    def update_dob(self, dob):
        """
        Updates the date of birth of the mentee.

        Args:
            dob (str): The new date of birth of the mentee.
        """
        self.dob = dob

    def update_details(self, key, value):
        """
        Updates the details of the mentee using key-value pairs.

        Args:
            key (str): The attribute to update.
            value: The new value for the attribute.
        """
        setattr(self, key, value)

    def __str__(self):
        """
        Get a string representation of the MenteeNode.
        :return: String representation of the MenteeNode.
        """
        details = [
            f"Name: {self.name}",
            f"Department: {self.department}",
            f"Profile Picture: {self.profile_picture}",
            f"Skills: {self.skills}",
            f"Contact Info: {self.contact_info}",
            f"Educations: {self.education}",
            f"Achievements: {self.achievements}",
            f"DOB: {self.dob}",
            f"Gender: {self.gender}",
            f"Nationality: {self.nationality}",
            f"Religion: {self.religion}",
            f"Community: {self.community}",
            f"marks: {self.marks}"
        ]
        return "\n".join(details)

    def get_name(self):
        """
        Returns the name of the mentee.

        Returns:
            str: The name of the mentee.
        """
        return self.name

    def get_department(self):
        """
        Returns the department of the mentee.

        Returns:
            str: The department of the mentee.
        """
        return self.department

    def get_profile_picture(self):
        """
        Returns the profile picture of the mentee.

        Returns:
            str: The profile picture of the mentee.
        """
        return self.profile_picture

    def get_skills(self):
        """
        Returns the skills of the mentee.

        Returns:
            list: The skills of the mentee.
        """
        return self.skills

    def get_contact_info(self):
        """
        Returns the contact information of the mentee.

        Returns:
            str: The contact information of the mentee.
        """
        return self.contact_info

    def get_education(self):
        """
        Returns the education information of the mentee.

        Returns:
            str: The education information of the mentee.
        """
        return self.education

    def get_achievements(self):
        """
        Returns the achievements of the mentee.

        Returns:
            str: The achievements of the mentee.
        """
        return self.achievements

    def get_dob(self):
        """
        Returns the date of birth of the mentee.

        Returns:
            str: The date of birth of the mentee.
        """
        return self.dob

    def get_gender(self):
        """
        Returns the gender of the mentee.

        Returns:
            str: The gender of the mentee.
        """
        return self.gender

    def get_nationality(self):
        """
        Returns the nationality of the mentee.

        Returns:
            str: The nationality of the mentee.
        """
        return self.nationality

    def get_religion(self):
        """
        Returns the religion of the mentee.

        Returns:
            str: The religion of the mentee.
        """
        return self.religion

    def get_community(self):
        """
        Returns the community of the mentee.

        Returns:
            str: The community of the mentee.
        """
        return self.community


class Tree:
    """
    The Tree class represents a hierarchical structure of admin, mentors, and mentees.
    It provides methods to add and remove mentors and mentees, update details, and retrieve information.
    """

    def __init__(self, admin):
        """
        Initialize the Tree with an admin node as the root.
        :param admin: The admin node.
        """
        self.admin = admin

    def getroot(self):
        """
        Get the root node of the tree (admin node).
        :return: The root node.
        """
        return self.admin

    def getchildren(self, person):
        """
        Get the children of a person (mentor or admin).
        :param person: The person node.
        :return: List of children nodes.
        """
        if person.children:
            return person.children
        return None

    def add_mentor(self, name, department, profile_picture=None, experience=None, skills=None, description=None,
                   availability=None, contact_info=None, education=None, achievements=None):
        """
        Add a new mentor to the tree.
        :param name: Name of the mentor.
        :param department: Department of the mentor.
        :param profile_picture: Profile picture of the mentor (optional).
        :param experience: Experience of the mentor (optional).
        :param skills: Skills of the mentor (optional).
        :param description: Description of the mentor (optional).
        :param availability: Availability of the mentor (optional).
        :param contact_info: Contact information of the mentor (optional).
        :param education: Education details of the mentor (optional).
        :param achievements: Achievements of the mentor (optional).
        :return: The newly added mentor node.
        """
        mentor = MentorNode(name, department, profile_picture, experience, skills, description, availability,
                            contact_info, education, achievements)
        mentor.parent = self.admin
        self.admin.children.append(mentor)
        return mentor

    def remove_mentor(self, mentor_name):
        """
        Remove a mentor from the tree.
        :param mentor_name: Name of the mentor to remove.
        """
        mentor = self.find_node_by_name(mentor_name, self.admin)
        if mentor:
            unassigned_mentees = mentor.children
            self.admin.children.remove(mentor)
            mentor.parent = None
            print(f"Removed mentor: {mentor_name}")
            return unassigned_mentees
        else:
            print(f"Mentor {mentor_name} not found.")
            return []

    def add_mentee(self, mentor_name, name, department, profile_picture=None, experience=None, skills=None,
                   description=None, availability=None, contact_info=None, education=None, achievements=None,
                   dob=None, gender=None, nationality=None, religion=None, community=None):
        """
        Add a new mentee under a mentor in the tree.
        :param mentor_name: Name of the mentor.
        :param name: Name of the mentee.
        :param department: Department of the mentee.
        :param profile_picture: Profile picture of the mentee (optional).
        :param experience: Experience of the mentee (optional).
        :param skills: Skills of the mentee (optional).
        :param description: Description of the mentee (optional).
        :param availability: Availability of the mentee (optional).
        :param contact_info: Contact information of the mentee (optional).
        :param education: Education details of the mentee (optional).
        :param achievements: Achievements of the mentee (optional).
        :param dob: Date of birth of the mentee (optional).
        :param gender: Gender of the mentee (optional).
        :param nationality: Nationality of the mentee (optional).
        :param religion: Religion of the mentee (optional).
        :param community: Community of the mentee (optional).
        """
        mentor = self.find_node_by_name(mentor_name, self.admin)
        if mentor:
            mentee = MenteeNode(name, department, profile_picture, experience, skills, description, availability,
                                contact_info, education, achievements, dob, gender, nationality, religion, community)
            mentee.parent = mentor
            mentor.children.append(mentee)
            print(f"Added mentee {name} to mentor {mentor_name}")
        else:
            print(f"Mentor {mentor_name} not found. Cannot add mentee.")

    def remove_mentee(self, mentor_name, mentee_name):
        """
        Remove a mentee from a mentor in the tree.
        :param mentor_name: Name of the mentor.
        :param mentee_name: Name of the mentee to remove.
        """
        mentor = self.find_node_by_name(mentor_name, self.admin)
        if mentor:
            mentee = self.find_node_by_name(mentee_name, mentor)
            if mentee:
                mentor.children.remove(mentee)
                mentee.parent = None
                print(
                    f"Removed mentee: {mentee_name} from mentor: {mentor_name}")
            else:
                print(
                    f"Mentee {mentee_name} not found under mentor {mentor_name}.")
        else:
            print(f"Mentor {mentor_name} not found.")

    def get_mentor(self, node=None):
        """
        Get a list of mentors in the tree.
        :param node: Starting node for the search (optional).
        :return: List of mentor nodes.
        """
        if node is None:
            node = self.getroot()

        mentors = node.children
        return mentors

    def get_mentees(self, mentor_name):
        """
        Get a list of mentees under a mentor in the tree.
        :param mentor_name: Name of the mentor.
        :return: List of mentee names.
        """
        mentor = self.find_node_by_name(mentor_name, self.admin)
        if mentor:
            return [mentee.name for mentee in mentor.children]
        else:
            print(f"Mentor {mentor_name} not found.")
            return []

    def update_mentor_details(self, mentor_name, key, value):
        """
        Update details of a mentor in the tree.
        :param mentor_name: Name of the mentor.
        :param key: Attribute name to update.
        :param value: New value for the attribute.
        """
        mentor = self.find_node_by_name(mentor_name, self.admin)
        if mentor:
            setattr(mentor, key, value)
            print(f"Updated details for mentor: {mentor_name}")
        else:
            print(f"Mentor {mentor_name} not found.")

    def update_mentee_details(self, mentor_name, mentee_name, key, value):
        """
        Update details of a mentee under a mentor in the tree.
        :param mentor_name: Name of the mentor.
        :param mentee_name: Name of the mentee.
        :param key: Attribute name to update.
        :param value: New value for the attribute.
        """
        mentor = self.find_node_by_name(mentor_name, self.admin)
        if mentor:
            mentee = self.find_node_by_name(mentee_name, mentor)
            if mentee:
                setattr(mentee, key, value)
                print(
                    f"Updated details for mentee: {mentee_name} under mentor: {mentor_name}")
            else:
                print(
                    f"Mentee {mentee_name} not found under mentor {mentor_name}.")
        else:
            print(f"Mentor {mentor_name} not found.")

    def find_node_by_name(self, name, node=None):
        """
        Find a node in the tree by name.
        :param name: Name of the node to find.
        :param node: Starting node for the search (optional).
        :return: The node if found, None otherwise.
        """
        if node is None:
            node = self.getroot()

        if node.name == name:
            return node

        for child in node.children:
            result = self.find_node_by_name(name, child)
            if result:
                return result

        return None

    def __str__(self):
        """
        Get a string representation of the tree.
        :return: String representation of the tree.
        """
        return self.__get_tree_string(self.admin)

    def __get_tree_string(self, node, level=0):
        """
        Recursively generate a string representation of the tree.
        :param node: Current node in the recursion.
        :param level: Current level in the tree hierarchy.
        :return: String representation of the tree.
        """
        indent = "  " * level
        tree_string = f"{indent}- {node.name} ({node.department})\n"
        children = self.getchildren(node)
        if children:
            for child in children:
                tree_string += self.__get_tree_string(child, level + 1)
        return tree_string

    def inorder_traversal(self, node=None):
        """
        Perform an inorder traversal of the tree.
        :param node: Current node in the traversal.
        :return: List of nodes in the inorder traversal order.
        """
        if node is None:
            return []

        result = []

        for child in node.children:
            mentor_mentees = [child, self.inorder_traversal(child)]
            result.append(mentor_mentees)

        return result


def running_status():
    admin = AdminNode("ID1007", "Murugesan")
    tree = Tree(admin)
    # Adding mentors to the admin
    tree.add_mentor("Gopal", "IT")
    tree.add_mentor("Heisenberg", "Chemical")

    # Adding mentees to mentors
    tree.add_mentee("Gopal", "Ambi", "IT")
    tree.add_mentee("Gopal", "Remo", "IT")
    tree.add_mentee("Heisenberg", "Chinrasu", "CSE")
    tree.add_mentee("Heisenberg", "Chelladurai", "ECE")

    # Inorder traversal
    traversal_result = tree.inorder_traversal(tree.getroot())

    # Printing mentors and their associated mentees
    for mentor, mentees in traversal_result:
        mentor_name = mentor.get_name()
        mentor_department = mentor.get_department()

        print("Mentor:", mentor_name)
        print("Department:", mentor_department)

        if mentees:
            print("Mentees:")
            for mentee, _ in mentees:  # Ignore the empty sublist
                mentee_name = mentee.get_name()
                print("  -", mentee_name)

        print("---")
    print(tree)
    # Editing mentor details
    tree.update_mentor_details("Gopal", "experience", "10 years")
    tree.update_mentor_details("Heisenberg", "availability", "Part-time")

    # Editing mentee details
    tree.update_mentee_details("Gopal", "Ambi", "skills", "Python, Java")
    tree.update_mentee_details(
        "Heisenberg", "Chelladurai", "contact_info", "Chelladurai@example.com")

    # Removing mentor and mentee
    # tree.remove_mentor("Heisenberg")
    # tree.remove_mentee("Gopal", "Remo")

    # Inorder traversal after modifications
    traversal_result = tree.inorder_traversal(tree.getroot())

    # Printing mentors and their associated mentees
    for mentor, mentees in traversal_result:
        mentor_name = mentor.get_name()
        mentor_department = mentor.get_department()

        print("Mentor:", mentor_name)
        print("Department:", mentor_department)

        if mentees:
            print("Mentees:")
            for mentee, _ in mentees:  # Ignore the empty sublist
                mentee_name = mentee.get_name()
                print("  -", mentee_name)

        print("---")

    return tree
