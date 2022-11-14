#!/usr/bin/env python
# -*- coding:utf-8 -*-

from time import sleep
import pywhatkit as pwk
from datetime import datetime as dt
from datetime import timedelta, date

import os.path
import webbrowser

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = dt.utcnow()# + 'Z'  # 'Z' indicates UTC time
        today = str(date.today())
        #print(today)
        timeMin = dt.fromisoformat(today)
        delta = timedelta(hours = 5)
        timeMin = timeMin +delta
        delta = timedelta(hours = 23)
        timeMax = timeMin +delta
        timeMin = timeMin.isoformat()+'Z'
        timeMax = timeMax.isoformat()+'Z'
        # timeMin = timeMin+'-07:00'
        # timeMax = timeMax.isoformat()+'-07:00'
        #print(timeMin)
        #print(timeMax)
        events_result = service.events().list(calendarId='4c03868c4f5e2ff2954600304e50f2b71e216a458456180b33790d0d92c34c4d@group.calendar.google.com', 
                                                timeMin=timeMin,
                                                timeMax = timeMax, 
                                                singleEvents=True,
                                              ).execute()
        events = events_result.get('items', [])
        
        creation_date = date.fromisoformat('2022-11-14')
        current_date = date.today()
        expiration = current_date-creation_date
        expiration = 100-expiration.days    
        
        if not events:
            if expiration <= 0:
                exp_message = "No upcoming events found.\n. Renew token."
            else:
                exp_message ="No upcoming events found.\n" + str(expiration) + " days until token expires"
            pwk.sendwhatmsg_to_group_instantly(group_id="HVTkMePvgYF9Q4TPQypOS2", message = exp_message, tab_close=True)
            return
        else:
            message = ""
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
                text = event['summary']
                nameEnd = text.index('\'')
                name = text[:nameEnd]
                if "Anniversary" in text or "anniversary" in text:
                    message += "Happy Anniversary " + name + " :ring\t" + " :confetti\t" + "\n"
                if name != "Jessie":
                    if "Bday" in text or "bday" in text:
                        message += "Happy Birthday " + name + " :cake\t" + " :hat\t" + "\n"
                #print(message)
            pwk.sendwhatmsg_to_group_instantly(group_id="1DocDGrVE671sOh1MrdFfS", message = message, tab_close=True)
            if expiration <= 0:
                exp_message = "Renew token"
            else:
                exp_message ="Events found.\n" + str(expiration) + " days until token expires"
            pwk.sendwhatmsg_to_group_instantly(group_id="HVTkMePvgYF9Q4TPQypOS2", message = exp_message, tab_close=True)
		    #MarlinNeighbors GroupId = "1DocDGrVE671sOh1MrdFfS"	
		    #DevTesting GroupId = "HVTkMePvgYF9Q4TPQypOS2"

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
