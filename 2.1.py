f = open("vb.txt", "w")
f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas tortor elit, hendrerit eu nibh ac, maximus scelerisque mi. Fusce elit ligula, ullamcorper quis tortor in, hendrerit vestibulum odio. Phasellus malesuada vel tellus ut sodales. In hac habitasse platea dictumst. Pellentesque a turpis feugiat, molestie ante quis, varius lorem. Fusce tristique diam odio, sed ultrices dolor iaculis at. Vestibulum auctor commodo quam, a posuere nisi mollis quis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;\nSuspendisse risus purus, malesuada eu placerat ut, malesuada in nulla. Nullam sollicitudin vestibulum nisi sit amet placerat. Sed ac posuere massa, congue tempor lectus. In hac habitasse platea dictumst. Donec suscipit mauris quis aliquam consequat. Sed ullamcorper facilisis sollicitudin. Duis sodales ligula quis eleifend vulputate. Aenean non commodo lacus, a efficitur dui. Sed eget lacus eget purus lacinia mollis. Sed posuere lacinia justo, non pretium dui scelerisque eget. Suspendisse bibendum mattis enim eget consectetur. Phasellus gravida malesuada mauris ultrices lacinia.\nDuis ut metus nec risus fringilla semper. Suspendisse potenti. Vivamus feugiat, odio sed dapibus commodo, sem massa fermentum purus, at porttitor orci nisi vitae magna. Ut fringilla nibh nisl, lobortis elementum dui feugiat in. In vel ligula feugiat, tristique turpis rutrum, mattis felis. Proin pharetra magna ac ex consectetur, eget placerat est bibendum. Suspendisse potenti.\nCurabitur vel sapien nec libero consectetur egestas. Mauris eu lacinia mi, et condimentum eros. Praesent dignissim nibh et quam finibus vulputate. Suspendisse pretium eros ut urna mattis, id tristique erat efficitur. Donec feugiat, turpis sit amet pharetra pulvinar, urna nulla condimentum turpis, vel maximus nibh lectus vitae arcu. Donec laoreet dolor bibendum, tincidunt mi ac, scelerisque elit. Nullam efficitur tincidunt nulla vitae facilisis. Quisque venenatis felis sit amet libero malesuada rhoncus. Donec lobortis suscipit ipsum eget fermentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Pellentesque efficitur dapibus nulla eget tincidunt. Donec vel diam at elit posuere sodales in vel diam. Ut mattis euismod elementum. Mauris vulputate fringilla mauris a ullamcorper.\nNulla condimentum magna sed ornare porttitor. Sed quam mauris, ultricies et quam eget, imperdiet finibus turpis. Vivamus arcu risus, scelerisque non justo sit amet, efficitur porta neque. Praesent pretium sit amet massa semper vestibulum. Vivamus facilisis porta diam, ac maximus dui. Quisque pellentesque posuere lectus nec mollis. Donec sapien odio, bibendum non sapien sed, aliquet ultrices felis. Nulla posuere nisl id tellus aliquet, et dictum odio iaculis. Cras dignissim risus lacus, cursus finibus lacus elementum nec. Sed vitae finibus mauris, sit amet varius mi. Vivamus aliquet tellus pharetra pharetra tincidunt.")
f.close()

f = open("vb.txt", "r")
def wordCount(s: str) -> int:
  return len(s.replace(';', ' ').replace(',', ' ').split())

def sentenceCount(s: str) -> int:
  return len(s.split('.'))

def find(i: str, s: str):
  return i.find(s)

def insert(path: str, s: str):
  f = open(str, 'a')
  f.write(s)
  f.close()
