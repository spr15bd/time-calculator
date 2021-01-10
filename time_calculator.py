def add_time(start, duration, dayOfWeek=""):
  start = start.split(":")
  hours = int(start[0])
  minutes = int(start[1].split()[0])
  amOrPm = start[1].split()[1]

  # convert start hours to 24-hour system
  if amOrPm == "PM":
    hours = hours +12

  total_start_minutes = hours * 60 + minutes 

  duration = duration.split(":")
  hours = int(duration[0])
  minutes = int(duration[1])
  #print(duration)
 

  total_minutes_to_add = hours * 60 + minutes 
  

  new_time_in_minutes = total_start_minutes + total_minutes_to_add
  
  if new_time_in_minutes % 60 <10:
    remainder_minutes = "0" + str(new_time_in_minutes % 60)
  else:
    remainder_minutes = str(new_time_in_minutes % 60)
  hours = int(new_time_in_minutes / 60)
  daysToAdd = int(hours / 24)
  
  if hours % 24 < 12:
    newAmOrPm = "AM"
  else:
    newAmOrPm = "PM"
  if hours > 12:
    hours = hours % 12
  new_time = str(hours) + ":" + remainder_minutes  + " " + newAmOrPm
  #if amOrPm == "PM" and newAmOrPm == "AM":
  #  daysToAdd = daysToAdd + 1
  if daysToAdd >=2 :
    
    new_time = new_time + " (" + str(daysToAdd) + " days later)"
  return new_time
