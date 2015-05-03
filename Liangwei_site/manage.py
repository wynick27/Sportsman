#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Liangwei_site.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


    # from search.models import State
    # with open('List_Of_States.txt','r') as f:
    #     for line in f:
    #         temp = line.split('|')
    #         s = temp[0]
    #         q = State(name=s)
    #         q.save()

