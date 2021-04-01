def count_time(date_created, current_time):
    year_to_min = date_created.year * 365 * 24 * 60
    mon_to_min = date_created.month * 30 * 24 * 60
    day_to_min = date_created.day * 24 * 60
    hour_to_min = date_created.hour * 60
    minutes = date_created.minute
    document_time = year_to_min + mon_to_min + day_to_min + hour_to_min + minutes
    current_year_to_min = current_time.year * 365 * 24 * 60
    current_mon_to_min = current_time.month * 30 * 24 * 60
    current_day_to_min = current_time.day * 24 * 60
    current_hour_to_min = current_time.hour * 60
    current_minute = current_time.minute
    current_total_time = current_year_to_min + current_mon_to_min + current_day_to_min + current_hour_to_min + current_minute
    return current_total_time - document_time
