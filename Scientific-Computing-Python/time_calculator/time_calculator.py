def add_time(start, duration, start_day=""):
  new_time = ""
  hour = 0
  extra_hour = 0
  day_index = -1
  am_pm = ""
  day = ""

  # Week tuple
  week = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")

  # Split the start time data
  mod_start = start.replace(" ",":").split(":")
  s_hour      = int(mod_start[0])
  s_min       = int(mod_start[1])
  s_am_pm     = mod_start[2]

  # Split the duration time data
  mod_duration = duration.split(":")
  d_hour    = int(mod_duration[0])  
  d_min     = int(mod_duration[1])

  # Add up all of the minutes
  sub_total_min = s_min + d_min
  if sub_total_min > 59:
    extra_hour += 1
    total_min = sub_total_min - 60
  else:
    total_min = sub_total_min

  # Format the minute sum by adding 0 in front of minutes 1-9.
  if total_min < 10:
    minutes = "0{}".format(total_min)
  else:
    minutes = str(total_min)

  # Get ready to loop!
  total_duration_hours = d_hour + extra_hour
  am_pm = s_am_pm
  loop_hour = 1
  days_later = 0
  hour = s_hour
  
  if not start_day == "":
    day_index = week.index(start_day.title())
    day = week[day_index]

  # Add it all up!
  while loop_hour <= total_duration_hours:
    hour += 1
    if hour % 13 == 0:
      hour = 1
      
    # Switch am_pm
    if hour % 12 == 0:
      if am_pm == "PM":
        am_pm = "AM"
        days_later += 1

        # calc the day of the week
        if not day_index == -1:
          day_index += 1
          if day_index == 7:
            day_index = 0          
          day = week[day_index]
      else:
        am_pm = "PM"
      
    # print("{} {} {}".format(hour,am_pm,day))
    loop_hour += 1

  # Return Same Day
  if days_later == 0:
    if start_day == "":
      new_time = "{}:{} {}".format(hour,minutes,am_pm)      
      return new_time
    else:
      new_time = "{}:{} {}, {}".format(hour,minutes,am_pm,day)
      return new_time
  # Return Next Day
  elif days_later == 1:
    if start_day == "":
      new_time = "{}:{} {} (next day)".format(hour,minutes,am_pm)
      return new_time
    else:
      new_time = "{}:{} {}, {} (next day)".format(hour,minutes,am_pm,day)
      return new_time
  # Return n Days Later
  elif days_later > 1:
    if start_day == "":
      new_time = "{}:{} {} ({} days later)".format(hour,minutes,am_pm,days_later)
      return new_time
    else:
      new_time = "{}:{} {}, {} ({} days later)".format(hour,minutes,am_pm,day,days_later)
      return new_time