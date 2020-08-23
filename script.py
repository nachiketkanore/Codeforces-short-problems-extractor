import requests
import json
import html2text

def generate_problem_links(api_link):
    
    response = requests.get(api_link)
    data = response.json()
    problems = data['result']['problems']
    
    pref = 'https://codeforces.com/problemset/problem/'
    problem_links = []
    
    for problem in problems:
        link = pref + str(problem['contestId']) + '/' + str(problem['index'])
        problem_links.append(link)
    return problem_links

def get_text_from_link(link): # give problem link
    res = requests.get(link)
    res = res.text
    h = html2text.HTML2Text()
    h.ignore_links = True
    res = h.handle(res)
    return res

def get_problem_statement(data):
#     data = get_text_from_link(link)
    data = data.split('standard output')
    data = data[1]
    data = data.split('Input')
    data = data[0]
    data = data.replace('$','')
    return data

tag = input('Enter the (VALID) tag to get problems:')
api_link = 'https://codeforces.com/api/problemset.problems?tags={}'.format(tag)
problem_links = generate_problem_links(api_link)

# print('Total problems = {}'.format(len(problem_links)))
# print('All the links of problems :')
# for link in problem_links:
#     print(link)
print('Total problems = {}'.format(len(problem_links)))

# exit(0)

lens = []
cnt = 1
for link in problem_links:
    print('Working on problem no : {}'.format(cnt))
    cnt += 1
    data = get_text_from_link(link)
    data = get_problem_statement(data)
    lens.append((len(data), link))

lens.sort()

for x in lens:
    print('Length of statement = {} , link = {}'.format(x[0], x[1]))
