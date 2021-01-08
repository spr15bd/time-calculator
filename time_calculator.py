def add_time(start, duration, dayOfWeek=""):
  start = start.split(":")
  hours = int(start[0])
  minutes = int(start[1].split()[0])
  amOrPm = start[1].split()[1] 

  total_start_minutes = hours * 60 + minutes 

  duration = duration.split(":")
  hours = int(duration[0])
  minutes = int(duration[1])
  print(duration)
 

  total_minutes_to_add = hours * 60 + minutes 
  

  new_time_in_minutes = total_start_minutes + total_minutes_to_add
  new_time = str(new_time_in_minutes / 60) + ":" + str(new_time_in_minutes % 60)
  return new_time
