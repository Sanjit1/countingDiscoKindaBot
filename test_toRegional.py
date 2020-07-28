import pyperclip

while True:
  text = raw_input("enter la text: ").lower()
  alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


  final_streeng = ""
  for latter in text:
    if latter in alfabet:
      final_streeng += ' :regional_indicator_' + latter + ': '
    elif latter == '1':
      final_streeng += ' :one: '
    elif latter == '2':
      final_streeng += ' :two: '
    elif latter == '3':
      final_streeng += ' :three: '
    elif latter == '4':
      final_streeng += ' :four: '
    elif latter == '5':
      final_streeng += ' :five: '
    elif latter == '6':
      final_streeng += ' :six: '
    elif latter == '7':
      final_streeng += ' :seven: '
    elif latter == '8':
      final_streeng += ' :eight: '
    elif latter == '9':
      final_streeng += ' :nine: '
    elif latter == ' ':
      final_streeng += '    '
    else:
      final_streeng += ' ' + latter + ' '

  print(final_streeng)
  pyperclip.copy(final_streeng)