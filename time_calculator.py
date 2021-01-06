def add_time(start, duration, dayOfWeek=""):
  start = start.split(":")
  hours = start[0]
  minutes = start[1].split()[0]
  amOrPm = start[1].split()[1] 
  new_time = hours+ " " + minutes + " " + amOrPm


  return new_time
