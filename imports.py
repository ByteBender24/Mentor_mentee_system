from Tree import *
from queue_meeting import *
from Hashmap import *
announcements_list = []
tree = running_status()
all_meeting_requests, mentor_meeting_history = Hashmap_status()
queue = MeetingRequestQueue()


def check_tree_object(request):
    global tree
    if tree.getroot().children != []:
        tree = request.session.get("tree")
