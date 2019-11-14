import requests

# print(requests.get('https://api.github.com/events'))
# print(requests.get('https://api.github.com/eventsblargh'))

r = requests.get('http://localhost:9999/secret')
print(r.status_code)
print(r.text)


# with open("number.txt", 'w') as writer:
#     for n in range(30):
#         if n % 2 == 0:
#             writer.write(f'{n}\n')

# with open('read.txt') as read:
#     with open('copy.txt', 'w') as copy:
#         copy.write(read.read())


# with open("wechat_friends.csv") as my_csv:
#     print(my_csv.read())

# Create a string with 99 a's and one b.
# There will always be one b, but it will be at a random position from 0 to 99.
# import random
# letters = ['a'] * 100
# b = random.randint(0, 99)
# letters[b] = 'b'
# letters = "".join(letters)

# # Search for the letter b in the string.
# # How many times will this print "Not yet" ?
# print("Looking for 'b' ...")
# pos = 0
# while letters[pos] != 'b':
#     pos += 1
#     print("Not yet")
# print(f"Found it!{pos}")

# def extract_place(file_str):
#     # first = file_str.find('_')
#     # tem_str = file_str[first + 1:]
#     # second = tem_str.find('_')
#     # return tem_str[:second]

#     return file_str.split('_')[1]


# print(extract_place("2018-06-06_MountainView_16:20:00.jpg"))




# import random
# import words


# def silly_string(nouns, verbs, templates):
#     # Choose a random template.
#     template = random.choice(templates)

#     # We'll append strings into this list for output.
#     output = []

#     # Keep track of where in the template string we are.
#     pos = 0

#     while pos < len(template):
#         if template[pos:pos+8] == '{{noun}}':
#             # Add a random noun to the output.
#             output.append(random.choice(nouns))
#             pos += 8
#         elif template[pos:pos+8] == '{{verb}}':
#             # Add a random verb to the output.
#             output.append(random.choice(verbs))
#             pos += 8
#         else:
#             # Copy a character to the output.
#             output.append(template[pos])
#             pos += 1

#     # Join the output into a single string.
#     output = ''.join(output)

#     return output


# if __name__ == '__main__':
#     print(silly_string(words.nouns, words.verbs,
#         words.templates))
    
    


# def  breakify(lines):
#     return '<br>'.join(lines)

# lines = ["Haiku frogs in snow",
#          "A limerick came from Nantucket",
#          "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]
# print(breakify(lines))





# def locate_all(whole, sub):
#     index = 0
#     list_ = []
#     while index < len(whole) - len(sub) + 1:
#         if whole[index:index + len(sub)] == sub:
#             list_.append(index)
#             index += len(sub)
           
#         else:
#             index +=1
#     return list_

# print(locate_all('cookbook', 'ook'))
# print(locate_all('yesyesyes', 'yes'))
# print(locate_all('the upside down', 'barb'))






# def locate_first(sub, whole):
#     index = 0
#     while index < len(whole) - len(sub) + 1:
#         if whole[index:index + len(sub)] == sub:
#             return index
#         index += 1
#     return -1

# print(locate_first('ook', 'cookbook'))
# print( locate_first('base', 'all your bass are belong to us'))







# def count_substring_v1(string, target):
#     count = 0
#     index = 0
#     while index < len(string) - len(target) + 1:
#         if string[index : index + len(target)] == target:
#             count += 1
#         index += 1    # <- look here
#     return count

# def count_substring_v2(string, target):
#     count = 0
#     index = 0
#     while index < len(string) - len(target) + 1:
#         if string[index : index + len(target)] == target:
#             count += 1
#             index += len(target)   # <- look here
#         else:
#             index += 1
#     return count

# print(count_substring_v1('AAAA', 'AA'))
# print(count_substring_v2('AAAA', 'AA'))




# def count_string(whole, sub):
#     count = 0
#     if len(sub) >= len(whole):
#         return sub == whole
#     index = 0
#     while index <= len(whole) - len(sub) + 1:
#         if whole[index:index+len(sub)] == sub:
#             count  += 1
#         index +=1
#     return count

# print(count_string('hello world hello world h world hell hello ', 'hello'))







# def is_substring(sub, whole):
#     result = False
#     if len(whole) < len(sub):
#         return result
#     for n in range(len(whole) - len(sub)):
#         if whole[n:n + len(sub)] == sub:
#             return True
#     return False

# print(is_substring('jkl', 'asdfasdfadsfjklasdfasdfasdf'))
# print(is_substring('asdfdsfasdfasdfasdf', 'dfasdfd1fas1dfasdf1asdf'))






# def starts_with_v1(long, short):
#     for position in range(len(short)):
#         if long[position] != short[position]:
#             return False
#     return True

# def starts_with_v2(long, short):
#     length = len(short)
#     beginning = long[0 : length]
#     if beginning == short:
#         return True
#     else:
#         return False


# def starts_with_v3(long, short):
#     return long[0:len(short)] == short

# # print(starts_with_v1("tin", "tinkerbell"))
# # print(starts_with_v2("tin", "tinkerbell"))
# print(starts_with_v3("tin", "tinkerbell"))

# def no_reapting():
#     words = []
#     while True:
#         word = input('give me a word')
#         if word in words:
#             print(f'{word} already exist!')
#             break
#         words.append(word)
#     return words
# no_reapting()



# while True:
#     print('hello, i\'m a infinity loop' )



# def until_dot(s):
#     index = 0
#     while index < len(s) and s[index] != '.':
#         # No dots yet, keep going.
#         index += 1
#     # We either found a dot or ran out of string.
#     return s[:index]

# print(until_dot('hello.world'))


# def count_ch(str, chr):
#     sum_ = 0
#     for x in str:
#         if chr == x:
#             sum_ += 1
#     return sum_

# print(count_ch("the goofy doom of the balloon goons", "o"))
# print(count_ch("papa pony and the parcel post problem", "p"))
# print(count_ch("this bunch of words has no", "e"))




# def total_length(word):
#     total = 0
#     for n in word:
#         total = total + len(n)
#     return total

# print(total_length(['123412', 'aadfadf', 'adfadsf']))

# def good_len(str):
#     return len(str) >= 8 and len(str) <= 64

# print(good_len('ashort'))
# print(good_len('123456normal'))
# print(good_len('helloworld1234567!@#$%^&^%$#@#$%^$#@#$%^1234567890987654312qwerqweqweqwerqwerqwerqwerty'))

# print('nana'.isdigit())
# print('1234567'.isdigit())
# print('    '.isspace())
# print('aAbcdefG'.islower())
# print('abcdefg'.islower())

# def start_with(long_str, short_str):
#     return long_str[0 : len(short_str)] == short_str

# print(start_with("banana", "ba"))
# print(start_with('apple', 'appver'))
# print(start_with('watermelon', 'water'))


# def total_of_three():
#     one = input("Enter a number:")
#     two = input("Enter another number:")
#     three = input("Enter a third number:")
#     result = int(one) + int(two) + int(three)
#     print(f"{one} + {two} + {three} = {result}")
# total_of_three()


# import math
# print(math.pi)

# print(f"pi.value.is:{math.pi:.6}")

# print(ord('A'))
# print(ord('a'))

# def world_triangle(world):
#     length = len(world)
#     for n in range(length):
#         print(world[:length - n])

# world_triangle('kitten')


