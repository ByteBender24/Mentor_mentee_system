class AdminNode:
    def __init__(self, ID, name):
        self.id = ID
        self.name = name
        self.parent = None
        self.children = []


class MentorNode:
    def __init__(self, name, department, profile_picture=None, experience=None, skills=None, description=None,
                 availability=None, contact_info=None, education=None, achievements=None):
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
        self.name = name

    def update_profile_image(self, img):
        self.profile_picture = img

    def update_experience(self, info):
        self.experience = info

    def update_skills(self, skills):
        self.skills = skills

    def update_description(self, description):
        self.description = description

    def update_availability(self, availability):
        self.availability = availability

    def update_contact_info(self, contact_info):
        self.contact_info = contact_info

    def update_education(self, education):
        self.education = education

    def update_achievements(self, achievements):
        self.achievements = achievements

    def get_name(self):
        return self.name

    def get_department(self):
        return self.department

    def get_profile_picture(self):
        return self.profile_picture

    def get_experience(self):
        return self.experience

    def get_skills(self):
        return self.skills

    def get_description(self):
        return self.description

    def get_availability(self):
        return self.availability

    def get_contact_info(self):
        return self.contact_info

    def get_education(self):
        return self.education

    def get_achievements(self):
        return self.achievements


class MenteeNode:
    def __init__(self, name, department, profile_picture=None, experience=None, skills=None, description=None,
                 availability=None, contact_info=None, education=None, achievements=None, dob=None, gender=None,
                 nationality=None, religion=None, community=None):
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
        self.parent = None
        self.children = []

    def update_name(self, name):
        self.name = name

    def update_profile_image(self, img):
        self.profile_picture = img

    def update_skills(self, skills):
        self.skills = skills

    def update_contact_info(self, contact_info):
        self.contact_info = contact_info

    def update_education(self, education):
        self.education = education

    def update_achievements(self, achievements):
        self.achievements = achievements

    def update_details(self, key, value):
        setattr(self, key, value)

    def get_name(self):
        return self.name

    def get_department(self):
        return self.department

    def get_profile_picture(self):
        return self.profile_picture

    def get_skills(self):
        return self.skills

    def get_contact_info(self):
        return self.contact_info

    def get_education(self):
        return self.education

    def get_achievements(self):
        return self.achievements

    def get_dob(self):
        return self.dob

    def get_gender(self):
        return self.gender

    def get_nationality(self):
        return self.nationality

    def get_religion(self):
        return self.religion

    def get_community(self):
        return self.community


class Tree:
    def __init__(self, admin):
        self.admin = admin

    def getroot(self):
        return self.admin

    def getchildren(self, person):
        if person.children:
            return person.children
        return None

    def add_mentor(self, name, department, profile_picture=None, experience=None, skills=None, description=None,
                   availability=None, contact_info=None, education=None, achievements=None):
        mentor = MentorNode(name, department, profile_picture, experience, skills, description, availability,
                            contact_info, education, achievements)
        mentor.parent = self.admin
        self.admin.children.append(mentor)

    def remove_mentor(self, mentor_name):
        mentor = self.find_node_by_name(mentor_name, self.admin)
        if mentor:
            self.admin.children.remove(mentor)
            mentor.parent = None
            print(f"Removed mentor: {mentor_name}")
        else:
            print(f"Mentor {mentor_name} not found.")

    def add_mentee(self, mentor_name, name, department, profile_picture=None, experience=None, skills=None,
                   description=None, availability=None, contact_info=None, education=None, achievements=None,
                   dob=None, gender=None, nationality=None, religion=None, community=None):
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
        admin = self.getroot()
        mentors = admin.children
        return mentors

    # if mentor nodes are present, as below mentees...but in this structure, it is given as admin - mentor - mentee.
    # def get_mentors(self):
    #     mentors = []
    #     for child in self.admin.children:
    #         mentors.append(child)
    #         mentors.extend(self.get_mentors_recursive(child))
    #     return mentors

    # def get_mentors_recursive(self, node):
    #     mentors = []
    #     for child in node.children:
    #         mentors.append(child)
    #         mentors.extend(self.get_mentors_recursive(child))
    #     return mentors

    def get_mentees(self, mentor_name):
        mentor = self.find_node_by_name(mentor_name, self.admin)
        if mentor:
            return mentor.children
        else:
            print(f"Mentor {mentor_name} not found.")
            return []

    def update_mentor_details(self, mentor_name, key, value):
        mentor = self.find_node_by_name(mentor_name, self.admin)
        if mentor:
            setattr(mentor, key, value)
            print(f"Updated details for mentor: {mentor_name}")
        else:
            print(f"Mentor {mentor_name} not found.")

    def update_mentee_details(self, mentor_name, mentee_name, key, value):
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
        return self.__get_tree_string(self.admin)

    def __get_tree_string(self, node, level=0):
        indent = "  " * level
        tree_string = f"{indent}- {node.name}\n"
        children = self.getchildren(node)
        if children:
            for child in children:
                tree_string += self.__get_tree_string(child, level + 1)
        return tree_string

    def inorder_traversal(self,node):
        if node is None:
            return []

        result = []

        for child in node.children:
            mentor_mentees = [child, self.inorder_traversal(child)]
            result.append(mentor_mentees)

        return result

admin = AdminNode("ID1007", "Murugesan")
tree = Tree(admin)
# Adding mentors to the admin
tree.add_mentor("John Doe", "IT")
tree.add_mentor("Jane Smith", "CSE")
tree.add_mentor("David Johnson", "ECE")

# Adding mentees to mentors
tree.add_mentee("John Doe", "Alice", "IT")
tree.add_mentee("John Doe", "Eva", "IT")
tree.add_mentee("Jane Smith", "Bob", "CSE")
tree.add_mentee("David Johnson", "Charlie", "ECE")

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

# Editing mentor details
tree.update_mentor_details("John Doe", "experience", "10 years")
tree.update_mentor_details("Jane Smith", "availability", "Part-time")

# Editing mentee details
tree.update_mentee_details("John Doe", "Alice", "skills", "Python, Java")
tree.update_mentee_details("David Johnson", "Charlie", "contact_info", "charlie@example.com")

# Removing mentor and mentee
tree.remove_mentor("Jane Smith")
tree.remove_mentee("John Doe", "Eva")

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
