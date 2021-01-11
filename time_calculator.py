def add_time(start, duration, dayOfWeek=""):
  daysList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",  "Saturday", "Sunday"]

  # store the start time
  start = start.split(":")
  hours = int(start[0])
  minutes = int(start[1].split()[0])
  amOrPm = start[1].split()[1]

  # temporarily convert start hours to 24-hour system
  if amOrPm == "PM":
    hours = hours + 12

  # convert start time to total number of minutes
  total_start_minutes = hours * 60 + minutes 

  # store the time to be added
  duration = duration.split(":")
  hours = int(duration[0])
  minutes = int(duration[1])
 
  # comvert the time to be added to total number of minutes
  total_minutes_to_add = hours * 60 + minutes 
  
  new_time_in_minutes = total_start_minutes + total_minutes_to_add

  # add a zero to minutes if this is less than 10, eg 6:1 PM should be 6:01 PM
  if new_time_in_minutes % 60 <10:
    remainder_minutes = "0" + str(new_time_in_minutes % 60)
  else:
    remainder_minutes = str(new_time_in_minutes % 60)
  hours = int(new_time_in_minutes / 60)

  # divide total hours by 24 to find number of days added
  daysToAdd = int(hours / 24)
  
  # evaluate whether the new time is AM or PM
  if hours % 24 < 12:
    newAmOrPm = "AM"
  else:
    newAmOrPm = "PM"

  # convert hours back from 24 hour system to 12 hour system
  if hours > 12:
    hours = hours % 12
  if hours == 0:
    hours = 12

  new_time = str(hours) + ":" + remainder_minutes  + " " + newAmOrPm
  
  # if an optional day of week is specified as a parameter work out the new day of the week
  if len(dayOfWeek) > 0:
    dayOfWeek = dayOfWeek[0].upper() + dayOfWeek[1:len(dayOfWeek)].lower()
    daysIndex = daysList.index(dayOfWeek)
    daysIndex = daysIndex + daysToAdd
    daysIndex = daysIndex % 7

    new_time = new_time + ", " + daysList[daysIndex]

  # add the number of days later if greater than 1 day, 'next day' otherwise
  if daysToAdd >=2 :
    
    new_time = new_time + " (" + str(daysToAdd) + " days later)"
  elif daysToAdd == 1:
    new_time = new_time + " (next day)" 

  return new_time
