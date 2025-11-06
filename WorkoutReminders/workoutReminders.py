# import pygetwindow as gw
import pyautogui
import time
import os
import emoji

import datetime
from datetime import datetime as dt
import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

CLIENT_DIR_PATH = str(Path(__file__).resolve().parents[2]) + "\\GoogleAPICredentials"
# dir_path = os.path.dirname(os.path.realpath(__file__))

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  path = CLIENT_DIR_PATH + "\\token.json"
  if os.path.exists(path):
    creds = Credentials.from_authorized_user_file(path, SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          CLIENT_DIR_PATH + "\\calendar_credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(path, "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="875835bd9794a5187c651c980a08ef3f73593016803d682a816d8d0eae683e62@group.calendar.google.com",
            timeMin=now,
            maxResults=100,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    substring = "woodmont"
    workouts = []
    for event in events:
    #   print(event["start"])
      if substring in event["summary"].lower():
        googletime = event["start"].get("dateTime", event["start"].get("date"))
        # parse ISO 8601 string 
        parsedtime = dt.fromisoformat(googletime)
        workouts.append(parsedtime.strftime("%B %d, %Y, %I:%M %p"))
    return workouts
  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
    workouts = main()
    os.startfile("whatsapp://send?phone=19176126688")
    time.sleep(2)

    pyautogui.keyDown("ctrl")
    pyautogui.press('f')
    pyautogui.keyUp("ctrl")
    # clears textbox
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')

    # search for workout class
    pyautogui.write("Woodmont Workouts")

    # click into appropriate chat
    pyautogui.press('tab')
    pyautogui.press('enter')

    # write message
    time.sleep(2)
    # clears textbox
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.write("Weekly Upcoming Woodmont Workout Bot Reminder :robot")
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(". Be there or be destroyed:")
    # time.sleep(1)
    for workout in workouts:
        pyautogui.hotkey('shift', 'enter')
        pyautogui.write(workout)
    pyautogui.press('enter')