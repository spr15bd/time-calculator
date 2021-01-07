def add_time(start, duration, dayOfWeek=""):
  start = start.split(":")
  hours = int(start[0])
  minutes = int(start[1].split()[0])
  amOrPm = start[1].split()[1] 

  total_minutes = hours * 60 + minutes 
  new_time = total_minutes


  return new_time
