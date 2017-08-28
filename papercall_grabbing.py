"""
Functions to grab info from papercall.io
"""

import os
import time
import requests

token = 'your_papercall_token'  # ,<-- fill this in

THIS_DIR = os.path.abspath(os.path.dirname(__file__))

des_template = """
Title: {title}
URL: 2017/descriptions/{id}.html
save_as: 2017/descriptions/{id}.html

{description}
""".lstrip()


def get_submission_ids():
    # Query all submission ids
    all_ids = []
    for state in ('submitted', 'accepted', 'rejected', 'waitlist'):
        url = 'https://www.papercall.io/api/v1/submissions?_token=%s&per_page=999&state=%s'
        all = requests.get(url % (token, state)).json()
        all_ids.extend([x['id'] for x in all])
    return all_ids


def get_reviewer_list():
    """ Print out the names of all people who did reviews.
    """
    # Collect submission ids
    all_ids = get_submission_ids()
    
    # Collect all reviewers
    reviewers = set()
    for id in all_ids:
        url = 'https://www.papercall.io/api/v1/submissions/%s/ratings?_token=%s'
        ratings = requests.get(url % (id, token)).json()
        for rating in ratings:
            reviewers.add(rating['user']['name'])
    
    # Print a list
    for reviewer in sorted(reviewers):
        print(reviewer)


def get_talk_descriptions():
    """ Get talk descriptions and store each in a markdown file.
    """
    # Collect submission ids
    all_ids = get_submission_ids()
    
    # Collect descriptions
    index = {}
    for id in all_ids:
        url = 'https://www.papercall.io/api/v1/submissions/%s?_token=%s'
        submission = requests.get(url % (id, token)).json()
        id = str(submission['id'])
        title = submission['talk']['title']
        page = des_template.format(description=submission['talk']['description'],
                                   title=title, id=id)
        fname = os.path.join(THIS_DIR, 'content', 'pages', '2017', 'descriptions', id + '.md')
        with open(fname, 'wb') as f:
            f.write(page.encode())
        index[id] = title
        time.sleep(0.1)
    
    fname = os.path.join(THIS_DIR, 'content', 'pages', '2017', 'descriptions', 'index.md')
    with open(fname, 'wb') as f:
        for id in sorted(index):
            line = id + ' - ' + index[id] + '\n'
            f.write(line.encode())


def make_links_in_program():
    """ Make the talk titles in the program link to description pages,
    as far as we can, anyway. The rest should be done by hand by making use of
    the descriptions.index.md.
    """
    raise NotImplementedError()


if __name__ == '__main__':
    pass
    # get_reviewer_list()
    # get_talk_descriptions()
    # make_links_in_program()
    