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

# Change this according to the requirement from https://codeforces.com/apiHelp
api_link = 'https://codeforces.com/api/problemset.problems?tags=fft'
problem_links = generate_problem_links(api_link)

print('All the links of problems :')
for link in problem_links:
    print(link)

lens = []
for link in problem_links:
    data = get_text_from_link(link)
    data = get_problem_statement(data)
    lens.append((len(data), link))

lens.sort()

for x in lens:
    print(x[0], x[1])
