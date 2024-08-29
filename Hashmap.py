from queue_meeting import MeetingRequest, MeetingRequestQueue
import matplotlib.pyplot as plt
import io
import base64


class HashMap:
    """
    Represents a hash map data structure.
    """

    def __init__(self):
        """
        Initializes an empty hash map.
        """
        self.hash_map = {}

    def put(self, key, value):
        """
        Adds a key-value pair to the hash map.

        Args:
            key: The key for the value.
            value: The value to be stored.
        """
        self.hash_map[key] = value

    def get(self, key):
        """
        Retrieves the value associated with the given key from the hash map.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if the key is not present in the hash map.
        """
        return self.hash_map.get(key)

    def contains_key(self, key):
        """
        Checks if the hash map contains the given key.

        Args:
            key: The key to check for.

        Returns:
            True if the key is present in the hash map, False otherwise.
        """
        return key in self.hash_map

    def remove(self, key):
        """
        Removes the key-value pair with the given key from the hash map.

        Args:
            key: The key to remove from the hash map.
        """
        if key in self.hash_map:
            del self.hash_map[key]

    def keys(self):
        """
        Returns a list of keys in the hash map.

        Returns:
            A list of keys in the hash map.
        """
        return self.hash_map.keys()

    def values(self):
        """
        Returns a list of values in the hash map.

        Returns:
            A list of values in the hash map.
        """
        return self.hash_map.values()

    def items(self):
        """
        Returns a list of key-value pairs in the hash map.

        Returns:
            A list of key-value pairs in the hash map.
        """
        return self.hash_map.items()

    def __str__(self) -> str:
        return str(self.hash_map)
    
class Meeting:
    """
    Represents a meeting with its details.
    """

    def __init__(self, date, link, details, participants):
        """
        Initializes a Meeting object.

        Args:
            date (str): The date of the meeting.
            link (str): The link or URL for the meeting.
            details (str): Additional details or description of the meeting.
            participants (list): A list of participants in the meeting.
        """
        self.date = date
        self.link = link
        self.details = details
        self.participants = participants

    def __str__(self):
        return (f"Event Details:\n"
                f"Date: {self.date}\n"
                f"Link: {self.link}\n"
                f"Details: {self.details}\n"
                f"Participants: {', '.join(self.participants)}")
    
    def __hash__(self):
        return hash((self.date, self.link, self.details, tuple(self.participants)))

    def __eq__(self, other):
        if isinstance(other, Meeting):
            return (self.date, self.link, self.details, tuple(self.participants)) == \
                   (other.date, other.link, other.details, tuple(other.participants))
        return False
    
class MentorMeetingHistory:
    """
    Represents the meeting history for a mentor.
    """

    def __init__(self):
        """
        Initializes an empty mentor meeting history.
        """
        self.meeting_history = HashMap()

    def add_meeting_record(self, mentor_name, meeting_record):
        """
        Adds a meeting record to the mentor's meeting history.

        Args:
            mentor_name (str): The name of the mentor.
            meeting_record (Meeting): The meeting record to add.
        """
        if self.meeting_history.contains_key(mentor_name):
            self.meeting_history.get(mentor_name).append(meeting_record)
        else:
            self.meeting_history.put(mentor_name, [meeting_record])

    def get_meeting_records(self, mentor_name):
        """
        Retrieves the meeting records for the given mentor.

        Args:
            mentor_name (str): The name of the mentor.

        Returns:
            A list of meeting records for the mentor. If the mentor has no meeting records, an empty list is returned.
        """
        if self.meeting_history.contains_key(mentor_name):
            return self.meeting_history.get(mentor_name)
        else:
            return []

    def generate_meeting_graph(self, mentor_name):
        """
        Generates a bar graph for the mentor's meeting history.

        Args:
            mentor_name (str): The name of the mentor.

        Returns:
            A base64-encoded image of the bar graph.
        """
        meetings = self.get_meeting_records(mentor_name)
        if not meetings:
            return None

        dates = [meeting.date for meeting in meetings]
        participants = [len(meeting.participants) for meeting in meetings]

        # Create a bar graph using matplotlib
        plt.figure(figsize=(10, 6))
        plt.bar(dates, participants, color='blue')
        plt.xlabel('Meeting Dates')
        plt.ylabel('Number of Participants')
        plt.title('Mentor Meeting History')
        plt.xticks(rotation=45)

        # Convert the plot to an image and encode it as base64
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        return image_base64


class AllMeetingRequests:
    """
    Represents all meeting requests made by mentees.
    """

    def __init__(self):
        """
        Initializes an empty collection of meeting requests.
        """
        self.meeting_requests = HashMap()

    def add_meeting_request(self, mentor_name, meeting_request):
        """
        Adds a meeting request to the collection.

        Args:
            mentor_name (str): The name of the mentor for whom the meeting request is made.
            meeting_request (MeetingRequest): The meeting request to add.
        """
        if self.meeting_requests.contains_key(mentor_name):
            queue = self.meeting_requests.get(mentor_name)
            queue.enqueue(meeting_request)
        else:
            queue = MeetingRequestQueue()
            queue.enqueue(meeting_request)
            self.meeting_requests.put(mentor_name, queue)

    def get_meeting_request_queue(self, mentor_name):
        """
        Retrieves the meeting request queue for the given mentor.

        Args:
            mentor_name (str): The name of the mentor.

        Returns:
            The meeting request queue for the mentor, or None if the mentor has no meeting requests.
        """
        if self.meeting_requests.contains_key(mentor_name):
            return self.meeting_requests.get(mentor_name)
        else:
            return None

    def remove_meeting_request_queue(self, mentor_name):
        """
        Removes the meeting request queue for the given mentor.

        Args:
            mentor_name (str): The name of the mentor.
        """
        if self.meeting_requests.contains_key(mentor_name):
            self.meeting_requests.remove(mentor_name)


class AllAnnouncements:
    """
    Represents all announcements made by mentors.
    """

    def __init__(self):
        """
        Initializes an empty collection of announcements.
        """
        self.announcement = HashMap()

    def add_announcement(self, mentor_name, announcement):
        """
        Adds an announcement to the collection.

        Args:
            mentor_name (str): The name of the mentor making the announcement.
            announcement (str): The announcement text.
        """
        if self.announcement.contains_key(mentor_name):
            announcement_list = self.announcement.get(mentor_name)
            announcement_list.append(announcement)
        else:
            announcement_list = []
            announcement_list.append(announcement)
            self.announcement.put(mentor_name, announcement_list)

    def get_announcement(self, mentor_name):
        """
        Retrieves the announcements made by the given mentor.

        Args:
            mentor_name (str): The name of the mentor.

        Returns:
            A list of announcements made by the mentor. If the mentor has made no announcements, None is returned.
        """
        if self.announcement.contains_key(mentor_name):
            return self.announcement.get(mentor_name)
        else:
            return None

    def remove_announcement(self, mentor_name):
        """
        Removes the announcements made by the given mentor.

        Args:
            mentor_name (str): The name of the mentor.
        """
        if self.announcement.contains_key(mentor_name):
            self.announcement.remove(mentor_name)


def Hashmap_status():
    all_meeting_requests = AllMeetingRequests()

    # Add meeting requests for mentors
    all_meeting_requests.add_meeting_request(
        "Heisenberg", MeetingRequest("Chinrasu", "2023-06-01", "Meeting request 1"))
    all_meeting_requests.add_meeting_request(
        "Heisenberg", MeetingRequest("Chelladurai", "2023-06-10", "Meeting request 2"))
    all_meeting_requests.add_meeting_request(
        "Gopal", MeetingRequest("Ambi", "2023-06-05", "Meeting request 3"))
    all_meeting_requests.add_meeting_request(
        "Gopal", MeetingRequest("Remo", "2023-06-15", "Meeting request 4"))

    # Get meeting request queues for mentors
    heisenberg_queue = all_meeting_requests.get_meeting_request_queue(
        "Heisenberg")
    Gopal_queue = all_meeting_requests.get_meeting_request_queue("Gopal")
    # Example usage:
    mentor_meeting_history = MentorMeetingHistory()

    # Add meeting records for mentors
    mentor_meeting_history.add_meeting_record("Heisenberg", Meeting(
        "2023-06-01", "https://example.com/meeting1", "Meeting 1 details", ["Chinrasu"]))
    mentor_meeting_history.add_meeting_record("Heisenberg", Meeting(
        "2023-06-10", "https://example.com/meeting2", "Meeting 2 details", ["Chinrasu", "Chelladurai"]))
    mentor_meeting_history.add_meeting_record("Gopal", Meeting(
        "2023-06-05", "https://example.com/meeting3", "Meeting 3 details", ["Ambi", "Remo"]))
    mentor_meeting_history.add_meeting_record("Gopal", Meeting(
        "2023-06-15", "https://example.com/meeting4", "Meeting 4 details", ["Ambi"]))

    # Retrieve meeting records for a mentor
    Heisenberg_meetings = mentor_meeting_history.get_meeting_records(
        "Heisenberg")
    Gopal_meetings = mentor_meeting_history.get_meeting_records("Gopal")

    # Print meeting records for John Doe
    print("Meeting records for John Doe:")
    for meeting in Heisenberg_meetings:
        print("Date:", meeting.date)
        print("Link:", meeting.link)
        print("Details:", meeting.details)
        print("Participants:", meeting.participants)
        print()

    # Print meeting records for Gopal
    print("Meeting records for Gopal:")
    for meeting in Gopal_meetings:
        print("Date:", meeting.date)
        print("Link:", meeting.link)
        print("Details:", meeting.details)
        print("Participants:", meeting.participants)
        print()
    print(heisenberg_queue)
    print(Gopal_queue)

    return all_meeting_requests, mentor_meeting_history
