#!/usr/bin/env python

import requests
import datetime
from dateutil.parser import parse
from tzlocal import get_localzone
import pytz
from argparse import ArgumentParser

def parse_date(date):
    tzinfo = get_localzone()
    parsed_date = parse(date, dayfirst=True)
    local_date = tzinfo.localize(parsed_date)
    utc_date = local_date.astimezone(pytz.utc)
    return utc_date


def search_for_issues(user, repo):
    endpoint = 'https://api.github.com/search/issues?q=repo:{}/{}+type:issue+state:closed'.format(USER, REPO)
    r = requests.get(endpoint)
    return r.json()


def get_milestones_and_issues(data):
    milestones = {}
    issues = {}

    for i in json['items']:
        milestones[i['milestone']['title']] = {'url': i['milestone']['html_url'],
            'date': parse(i['milestone']['created_at'])
            }

        issues[i['title']] = {'url': i['html_url'],
            'milestone': i['milestone']['title'],
            'date': parse(i['closed_at'])
            }
    return milestones, issues


def filter_by_date(milestones, issues, date):
    actual_issues = {}
    actual_milestones = {}
    
    for i, v in issues.items():
        if v['date'] >= date:
            actual_issues[i] = v
    
    for i, v in actual_issues.items():
        m = v['milestone']
        actual_milestones[m] = milestones[m]

    return actual_milestones, actual_issues


def print_markdown(actual_milestones, actual_issues):
    for milestone in sorted(actual_milestones, key=lambda f: milestones[f]['date']):
        print('[{}]({})'.format(milestone, actual_milestones[milestone]['url']))
        for issue, data in actual_issues.items():
            if data['milestone'] == milestone:
                print('-    [{}]({})'.format(issue, data['url']))

if __name__ == '__main__':
    parser = ArgumentParser(description = 'Lists all closed issues for a given GitHub repository from a certain date until now')
    parser.add_argument('-u', '--user', required = True, help = 'Username owner of the GitHub repository')
    parser.add_argument('-r', '--repo', required = True, help = 'Repository from where we want to list the closed issues')
    parser.add_argument('-d', '--date', required = True, help = 'Issues will be taken from this date. Format %D-%M-%Y')

    args = parser.parse_args()

    USER = args.user
    REPO = args.repo
    DATE = args.date
    parsed_date = parse_date(DATE)

    json = search_for_issues(USER, REPO)
    milestones, issues = get_milestones_and_issues(json)
    actual_milestones, actual_issues = filter_by_date(milestones, issues, parsed_date)
    print_markdown(actual_milestones, actual_issues)
