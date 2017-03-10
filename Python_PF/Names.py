students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def pOne():
    for x in students:
        print x['first_name'], x['last_name']

# pOne()


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def pTwo():
 for key, data in users.items():
     print key
     for index, name in enumerate(data):
        #  print name['first_name'], name['last_name'], "-", len(name['first_name']+name['last_name'])
        print index+1,"-", name['first_name'],name['last_name'],"-",len(name['first_name']+name['last_name'])

pTwo()
