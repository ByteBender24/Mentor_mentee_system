class MeetingRequestQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, request):
        """
        Add a meeting request to the queue.
        """
        self.queue.append(request)

    def dequeue(self):
        """
        Remove and return the next meeting request from the queue.
        """
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Get the number of meeting requests in the queue.
        """
        return len(self.queue)

    def get_next_request(self):
        """
        Get the next meeting request in the queue without removing it.
        """
        if not self.is_empty():
            return self.queue[0]
        return None

    def list(self):
        """
        Return a list of elements in the queue.
        """
        return self.queue

    def __str__(self):
        """
        Returns a string representation of the MeetingRequestQueue object.

        Returns:
            str: The string representation of the MeetingRequestQueue object.
        """
        queue_str = "\n".join(str(request) for request in self.queue)
        return f"Meeting Request Queue:\n{queue_str}"


class MeetingRequest:
    """
    Represents a meeting request from a mentee.
    """

    def __init__(self, mentee_name, date, text):
        """
        Initializes a MeetingRequest object.

        Args:
            mentee_name (str): The name of the mentee making the request.
            date (str): The date of the meeting request.
            text (str): The text or details of the meeting request.
        """
        self.mentee_name = mentee_name
        self.date = date
        self.text = text

    def __str__(self):
        """
        Returns a string representation of the MeetingRequest object.

        Returns:
            str: The string representation of the MeetingRequest object.
        """
        return f"Mentee: {self.mentee_name} | Date: {self.date} | Text: {self.text}"
