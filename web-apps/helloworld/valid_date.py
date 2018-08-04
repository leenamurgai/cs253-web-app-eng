months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
month_abbvs = dict((m[:3].lower(), m) for m in months)
          
def valid_month1(month):
     for x in months:
          if x.lower() == month.lower():
               return x
     return None

def valid_month(month):
     return month_abbvs.get(month[:3].lower())

def valid_day1(day):
     try:
          if 0<int(day)<32:
               return int(day)
          else:
               return None
     except:
          None

def valid_day(day):
     if day and day.isdigit():
          day = int(day)
          if 0<day<32:
               return day

def valid_year(year):
     if year and year.isdigit():
          year = int(year)
          if 1899<year<2021:
               return year

